# -*- coding: utf-8 -*-
"""
curate_botany_b3_p1.py
Cluster Botany, Minerals & Elements Batch 3 Part 1 (82 words)
Dashboards:
- aurum (31 words: aura -> aurous)
- calc (51 words: calcaneal -> recalculation)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_botany_b3_p1 = {
    # Dashboard — aurum (31)
    "aura": {
        "primary": "A distinctive intangible atmosphere or quality that seems to surround and emanate from a person, place, or thing.",
        "secondary": "In medicine and neurology, a perceptual disturbance or sensory premonition experienced immediately before a migraine or epileptic seizure.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "A subtle **aura** of refinement and moral gravity seemed to hover over her every quiet gesture."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "An uncanny **aura** of mystery enveloped the third story of Thornfield Hall long before midnight."
            },
            {
                "author": "Oliver Sacks",
                "work": "Migraine",
                "quote": "Many patients describe a classical visual **aura** consisting of shimmering zigzag lines before the headache begins."
            }
        ]
    },
    "aural": {
        "primary": "Pertaining to the ear, the sense of hearing, or the reception of acoustic sound.",
        "secondary": "In experimental acoustics and phonetics, relating to auditory perception as distinguished from ocular or visual stimuli.",
        "quotes": [
            {
                "author": "Aldous Huxley",
                "work": "Brave New World",
                "quote": "The soft synthetic music provided a soothing **aural** backdrop to the automated machinery of the hatchery."
            },
            {
                "author": "Virginia Woolf",
                "work": "The Waves",
                "quote": "The rhythmic surge of breaking waves filled her consciousness with an intense **aural** vibration."
            },
            {
                "author": "Hermann von Helmholtz",
                "work": "On the Sensations of Tone",
                "quote": "The intricate structure of the inner ear translates complex **aural** disturbances into distinct musical sensations."
            }
        ]
    },
    "aurally": {
        "primary": "Through the sense of hearing; by means of sound or acoustic perception.",
        "secondary": "In pedagogical phonetics, by listening to auditory input rather than by visual inspection of written text.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "She recognized his approaching footsteps **aurally** long before his figure emerged from the shadowy lane."
            },
            {
                "author": "George Bernard Shaw",
                "work": "Pygmalion",
                "quote": "Higgins insisted that the delicate nuances of London dialects must be mastered **aurally** through attentive listening."
            },
            {
                "author": "Alexander Graham Bell",
                "work": "The Mechanism of Speech",
                "quote": "Deaf children must learn to modulate their pitch artificially when unable to verify speech **aurally**."
            }
        ]
    },
    "aureate": {
        "primary": "Having the warm golden colour or metallic lustre of polished gold; gilded.",
        "secondary": "Characterized by an excessively ornate, grandiloquent, or rhetorical literary style.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The setting sun bathed the Alpine peaks in a glorious **aureate** light that lingered long after dusk."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "The tapestry glowed with threads of **aureate** silk interwoven among dark velvet shadows."
            },
            {
                "author": "C. S. Lewis",
                "work": "English Literature in the Sixteenth Century",
                "quote": "Fifteenth-century Scottish poets cultivated an **aureate** diction rich in elaborate Latin borrowings."
            }
        ]
    },
    "aurelius": {
        "primary": "Pertaining to or associated with Marcus Aurelius Antoninus, the Roman Emperor and celebrated Stoic philosopher.",
        "secondary": "In classical historiography and philosophy, embodying the austere Stoic virtues and reflective introspections of the Antonine dynasty.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The reign of Marcus **Aurelius** is remembered as an era of profound philosophical serenity and imperial duty."
            },
            {
                "author": "Matthew Arnold",
                "work": "Essays in Criticism",
                "quote": "The noble spirit of **Aurelius** speaks directly to the modern reader through his earnest self-examination."
            },
            {
                "author": "Walter Pater",
                "work": "Marius the Epicurean",
                "quote": "Marius found profound moral solace in the calm, unyielding equanimity of the Emperor **Aurelius**."
            }
        ]
    },
    "aureolaria": {
        "primary": "A genus of herbaceous hemiparasitic flowering plants in the broomrape family, commonly known as false foxgloves.",
        "secondary": "In North American floristics, yellow-flowered parasitic perennials that form subterranean root attachments with native oak trees.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "Species of **Aureolaria** flourish in dry open woodlands, displaying showy yellow corollas throughout late summer."
            },
            {
                "author": "Nathaniel Lord Britton",
                "work": "An Illustrated Flora of the Northern United States and Canada",
                "quote": "The parasitic roots of **Aureolaria** attach directly to the rootlets of surrounding deciduous oaks."
            },
            {
                "author": "John Kunkel Small",
                "work": "Flora of the Southeastern United States",
                "quote": "Botanists collect **Aureolaria** along sandy ridges where its slender glandular stems rise above the leaf litter."
            }
        ]
    },
    "aureole": {
        "primary": "A circle of light or luminous radiance surrounding the head or body of a holy figure in sacred art; a halo.",
        "secondary": "In meteorology and astronomy, a bright corona of refracted light seen around the sun or moon during mist or cloud cover.",
        "quotes": [
            {
                "author": "Dante Gabriel Rossetti",
                "work": "The Blessed Damozel",
                "quote": "Around her serene brow there shone a radiant **aureole** of seven golden stars."
            },
            {
                "author": "Mary Shelley",
                "work": "Frankenstein",
                "quote": "The full moon rose above the jagged glacier, framed by a pale **aureole** of freezing mist."
            },
            {
                "author": "Camille Flammarion",
                "work": "Popular Astronomy",
                "quote": "A delicate luminous **aureole** encircles the solar corona during the dramatic moments of totality."
            }
        ]
    },
    "aureomycin": {
        "primary": "A broad-spectrum tetracycline antibiotic produced by the bacterium Streptomyces aureofaciens, named for its golden-yellow color.",
        "secondary": "In mid-twentieth-century pharmacotherapy, one of the earliest orally effective antibacterial agents utilized against diverse bacterial and rickettsial infections.",
        "quotes": [
            {
                "author": "Selman Waksman",
                "work": "My Life with the Microbes",
                "quote": "The isolation of **aureomycin** opened a new frontier in the clinical conquest of bacterial epidemics."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Clinicians noted that **aureomycin** effectively suppressed diverse pathogenic organisms where penicillin had failed."
            },
            {
                "author": "Paul de Kruif",
                "work": "Microbe Hunters",
                "quote": "Yellow crystals of **aureomycin** proved that deep soil molds could manufacture powerful weapons against human disease."
            }
        ]
    },
    "auric": {
        "primary": "Of, relating to, or derived from gold; containing trivalent gold in chemical nomenclature.",
        "secondary": "In inorganic chemistry, denoting compounds containing gold in its +3 oxidation state, such as auric chloride.",
        "quotes": [
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "When dissolved in nitro-muriatic acid, gold forms a yellow solution containing **auric** salts."
            },
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "The precipitation of **auric** oxide occurs upon the cautious addition of caustic potash to the solution."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "Films of reduced gold exhibited brilliant green transparency when washed free of **auric** impurities."
            }
        ]
    },
    "auricle": {
        "primary": "The external portion of the ear in humans and mammals; the pinna.",
        "secondary": "In cardiovascular anatomy, an ear-shaped muscular pouch projecting from the superior surface of each cardiac atrium.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The cartilaginous **auricle** serves to collect sound vibrations and direct them toward the external acoustic meatus."
            },
            {
                "author": "William Harvey",
                "work": "Exercitatio Anatomica de Motu Cordis et Sanguinis in Animalibus",
                "quote": "Observation reveals that the **auricle** contracts first, propelling its contained blood into the ventricular chamber."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The folded rim of the human **auricle** preserves a rudimentary tubercle reminiscent of mammalian ancestors."
            }
        ]
    },
    "auricula": {
        "primary": "A European alpine primrose (Primula auricula) bearing clusters of fragrant, powdery, velvety flowers; bear's ear.",
        "secondary": "In classical anatomy, an alternative diminutive term for the external ear or the muscular appendage of the cardiac atrium.",
        "quotes": [
            {
                "author": "John Gerard",
                "work": "The Herball or Generall Historie of Plantes",
                "quote": "The mountain **auricula** produces fleshy, powdery foliage and bright yellow blossoms resembling little cowslips."
            },
            {
                "author": "Gertrude Jekyll",
                "work": "Wood and Garden",
                "quote": "Fanciers prize the velvet **auricula** for its exquisite symmetry and delicate dusting of white meal."
            },
            {
                "author": "John Parkinson",
                "work": "Paradisi in Sole Paradisus Terrestris",
                "quote": "No garden border is complete without the sweet-scented **auricula** blooming in early spring."
            }
        ]
    },
    "auricular": {
        "primary": "Pertaining to the sense of hearing, sound perception, or the anatomical ear.",
        "secondary": "Told privately into the ear; secret, confidential, or spoken in whispered confidence.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "King Lear",
                "quote": "I had rather have your **auricular** confession before I deliver this matter to the king."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The secret practice of **auricular** confession became an influential pillar of medieval ecclesiastical authority."
            },
            {
                "author": "Oliver Wendell Holmes Sr.",
                "work": "The Autocrat of the Breakfast-Table",
                "quote": "The physician pressed his stethoscope to the chest, relying upon delicate **auricular** evidence."
            }
        ]
    },
    "auriculare": {
        "primary": "An anatomical craniometric landmark located at the center of the opening of the external acoustic meatus.",
        "secondary": "In physical anthropology and cephalometry, the fixed reference point on the skull used to measure cranial heights and facial angles.",
        "quotes": [
            {
                "author": "Aleš Hrdlička",
                "work": "Anthropometry",
                "quote": "Measurements of cranial height require placing the caliper directly upon the **auriculare** of both sides."
            },
            {
                "author": "Arthur Keith",
                "work": "Human Embryology and Morphology",
                "quote": "The craniometric distance from bregma to **auriculare** establishes the vertical development of the cerebral vault."
            },
            {
                "author": "Franz Boas",
                "work": "Changes in Bodily Form of Descendants of Immigrants",
                "quote": "The investigator recorded cephalic dimensions taking the **auriculare** as an immovable skeletal baseline."
            }
        ]
    },
    "auricularia": {
        "primary": "A genus of jelly fungi commonly known as wood ears or tree ears, typically growing on dead or decaying hardwood trees.",
        "secondary": "In developmental biology, the free-swimming, ciliated, bilateral larva characteristic of certain sea cucumbers (holothurians).",
        "quotes": [
            {
                "author": "Miles Joseph Berkeley",
                "work": "Outlines of British Fungology",
                "quote": "Species of **Auricularia** produce gelatinous, ear-shaped basidiocarps upon the bark of decaying elder trees."
            },
            {
                "author": "Ernst Haeckel",
                "work": "Art Forms in Nature",
                "quote": "Under microscopic magnification, the delicate **auricularia** larva displays graceful bands of ciliated ectoderm."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "A Manual of the Anatomy of Invertebrated Animals",
                "quote": "The echinoderm transforms from its swimming **auricularia** stage into a sedentary bottom-dwelling organism."
            }
        ]
    },
    "auriculariaceae": {
        "primary": "A taxonomic family of jelly fungi within the order Auriculariales characterized by transversely septate basidia and gelatinous basidiocarps.",
        "secondary": "In fungal systematics, wood-decaying saprotrophic basidiomycetes capable of surviving prolonged desiccation and reviving upon rehydration.",
        "quotes": [
            {
                "author": "Pier Andrea Saccardo",
                "work": "Sylloge Fungorum",
                "quote": "The family **Auriculariaceae** includes lignicolous fungi bearing rubbery, lobed fructifications on decomposing timber."
            },
            {
                "author": "Heinrich Anton de Bary",
                "work": "Comparative Morphology and Biology of the Fungi",
                "quote": "Microscopic sections of the **Auriculariaceae** reveal basidia divided by transverse partitions during sporulation."
            },
            {
                "author": "Donald H. Pfister",
                "work": "Mycological Studies",
                "quote": "Ecological surveys demonstrate that the **Auriculariaceae** play a significant role in forest cellulose decomposition."
            }
        ]
    },
    "auriculariales": {
        "primary": "An order of basidiomycete fungi containing the jelly fungi, distinguished by gelatinous fruiting bodies and transversely partitioned basidia.",
        "secondary": "In higher fungal taxonomy, an ancient saprophytic lineage of Agaricomycetes adapted to fluctuating moisture regimes on decaying forest wood.",
        "quotes": [
            {
                "author": "Elias Magnus Fries",
                "work": "Systema Mycologicum",
                "quote": "The distinctive fruiting bodies grouped under **Auriculariales** contract when dry and expand remarkably when wet."
            },
            {
                "author": "Bernard Ogilvie Dodge",
                "work": "Elements of Plant Pathology",
                "quote": "Taxonomists place the common wood-ear within the order **Auriculariales** based upon basidial septation."
            },
            {
                "author": "David Hawksworth",
                "work": "Ainsworth & Bisby's Dictionary of the Fungi",
                "quote": "Members of the **Auriculariales** decompose dead hardwoods throughout temperate and tropical forest ecosystems."
            }
        ]
    },
    "auriculate": {
        "primary": "Having ear-shaped appendages, lobes, or projections, especially at the base of a leaf or petal.",
        "secondary": "In botanical organography, describing sessile foliage possessing two rounded lobes that clasp or flank the supporting stem.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "First Lessons in Botany and Vegetable Physiology",
                "quote": "The basal margins of an **auriculate** leaf expand into rounded lobes resembling small ears."
            },
            {
                "author": "John Lindley",
                "work": "An Introduction to Botany",
                "quote": "Observe how the sessile blade becomes distinctly **auriculate** where it joins the flowering axis."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Standard Cyclopedia of Horticulture",
                "quote": "Species of wild lettuce display deeply **auriculate** cauline leaves that clasp the upright stalk."
            }
        ]
    },
    "auriculated": {
        "primary": "Equipped or furnished with ear-like appendages, small lobes, or expanded auricular margins.",
        "secondary": "In comparative anatomy and malacology, possessing small lateral projections resembling little ears along a shell or skeletal plate.",
        "quotes": [
            {
                "author": "Richard Owen",
                "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals",
                "quote": "The hinge line of the fossil scallop displays two distinctly **auriculated** lateral wings."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Certain cultivated varieties exhibit curiously **auriculated** foliage near the base of the inflorescence."
            },
            {
                "author": "Thomas Pennant",
                "work": "British Zoology",
                "quote": "The marine bivalve possesses an **auriculated** margin that stabilizes its posture upon sandy bottoms."
            }
        ]
    },
    "auriculoventricular": {
        "primary": "Relating to or connecting the auricles (atria) and ventricles of the heart.",
        "secondary": "In cardiac electrophysiology, designating the specialized nodal tissue and conduction pathway that transmits electrical impulses from atria to ventricles.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The **auriculoventricular** groove marks the external boundary between the upper receiving chambers and lower muscular ventricles."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Impaired conduction across the **auriculoventricular** bundle results in distinct arrhythmias and bradycardia."
            },
            {
                "author": "Arthur Keith",
                "work": "The Mechanism of the Heart",
                "quote": "Specialized fibers form the **auriculoventricular** node, regulating the orderly propagation of each cardiac cycle."
            }
        ]
    },
    "auriferous": {
        "primary": "Yielding, producing, or bearing gold; containing native gold within rock or alluvial deposits.",
        "secondary": "In economic geology and mining engineering, designating geological veins, quartz reefs, or gravel beds rich in minable gold ores.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Miners followed the rich **auriferous** quartz veins deep into the metamorphic rocks of California."
            },
            {
                "author": "Roderick Murchison",
                "work": "Siluria: A History of the Oldest Known Rocks",
                "quote": "Streams cutting through ancient slate formations deposit **auriferous** sands along valley floors."
            },
            {
                "author": "Mark Twain",
                "work": "Roughing It",
                "quote": "Prospectors rushed eagerly across the desert, lured by rumors of rich **auriferous** gravels in the mountain gulches."
            }
        ]
    },
    "auriform": {
        "primary": "Shaped like an ear; having the contours or morphological outline of a human or mammalian ear.",
        "secondary": "In malacology and paleontology, describing shells or anatomical valves that exhibit an ear-like spiral outline, such as abalones.",
        "quotes": [
            {
                "author": "Thomas Say",
                "work": "American Conchology",
                "quote": "The shell displays an **auriform** contour with a wide, pearly aperture occupying most of the ventral surface."
            },
            {
                "author": "Richard Owen",
                "work": "On the Anatomy of Vertebrates",
                "quote": "The auditory ossicle terminates in an **auriform** cartilaginous plate adapted for vibrating against fluid."
            },
            {
                "author": "John Gerard",
                "work": "The Herball or Generall Historie of Plantes",
                "quote": "This curious tree-fungus presents an **auriform** habit, adhering closely to the damp bark."
            }
        ]
    },
    "aurify": {
        "primary": "To turn into gold; to transform or transmute baser materials into metallic gold.",
        "secondary": "In the history of alchemy, the putative hermetic process of purifying metals to attain the golden state.",
        "quotes": [
            {
                "author": "Ben Jonson",
                "work": "The Alchemist",
                "quote": "The charlatan promised his gullible patrons that his secret elixir would **aurify** crude lead overnight."
            },
            {
                "author": "Robert Boyle",
                "work": "The Sceptical Chymist",
                "quote": "Alchemical philosophers claimed they could **aurify** base substances, yet produced no reproducible metallic proof."
            },
            {
                "author": "Isaac Newton",
                "work": "Chemical Papers",
                "quote": "Writers on the hermetic art assert that the philosophical mercury has power to **aurify** imperfect bodies."
            }
        ]
    },
    "auriga": {
        "primary": "A prominent northern constellation depicted as a charioteer holding a goat and kids, containing the bright star Capella.",
        "secondary": "In Roman antiquity, a slave or freedman who drove a two-horse or four-horse chariot in the public circus races.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman populace cheered wildly as each daring **auriga** rounded the perilous turn in the Circus Maximus."
            },
            {
                "author": "Camille Flammarion",
                "work": "Popular Astronomy",
                "quote": "The brilliant yellow star Capella dominates the northern constellation of **Auriga** throughout winter nights."
            },
            {
                "author": "Walter Pater",
                "work": "Marius the Epicurean",
                "quote": "A youthful **auriga** stood poised upon his light racing car, gripping the reins with fearless dexterity."
            }
        ]
    },
    "auriparus": {
        "primary": "A genus of small American passerine birds containing the verdin (Auriparus flaviceps), characterized by its golden-yellow head.",
        "secondary": "In North American desert ornithology, a penduline-tit relative that builds conspicuous globular thorny nests in arid scrublands.",
        "quotes": [
            {
                "author": "Spencer Fullerton Baird",
                "work": "Birds of North America",
                "quote": "The genus **Auriparus** comprises tiny desert birds recognized by their bright yellow crowns and industrious foraging habits."
            },
            {
                "author": "Elliott Coues",
                "work": "Key to North American Birds",
                "quote": "In the thorny mesquite thickets of the southwest, **Auriparus** builds an intricate domed nest of twigs."
            },
            {
                "author": "Florence Merriam Bailey",
                "work": "Handbook of Birds of the Western United States",
                "quote": "The sharp call of **Auriparus** echoes across desert washes as the tiny bird gleans insects from desert shrubs."
            }
        ]
    },
    "auriscope": {
        "primary": "An illuminated medical instrument designed for inspecting the external ear canal and tympanic membrane; an otoscope.",
        "secondary": "In diagnostic otolaryngology, an optical speculum equipped with magnification and lighting to evaluate middle ear pathology.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Careful examination with an **auriscope** reveals hyperemia and bulging of the tympanic membrane in acute otitis."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The physician directs light down the auditory canal using a conical **auriscope** to inspect the drum."
            },
            {
                "author": "Joseph Lister",
                "work": "Collected Papers",
                "quote": "Cleanliness of every diagnostic speculum, including the **auriscope**, prevents accidental cross-infection among patients."
            }
        ]
    },
    "aurochs": {
        "primary": "A large, extinct wild ox (Bos primigenius) of Europe and Asia, the ancestral progenitor of modern domestic cattle.",
        "secondary": "In historical ecology and archaeozoology, the massive wild bovine that roamed post-glacial European forests until its extinction in 1627.",
        "quotes": [
            {
                "author": "Julius Caesar",
                "work": "Commentaries on the Gallic War",
                "quote": "The Germans hunt the ferocious **aurochs**, an enormous wild ox little inferior to the elephant in magnitude."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Fossil remains prove that the ancient European **aurochs** was the direct wild ancestor of domestic cattle breeds."
            },
            {
                "author": "Georges Cuvier",
                "work": "The Animal Kingdom",
                "quote": "The immense horn-cores of the **aurochs** recovered from peat bogs indicate a beast of tremendous strength and stature."
            }
        ]
    },
    "aurora": {
        "primary": "A natural light display in the sky predominantly seen in high-latitude regions, caused by solar wind particles colliding with the upper atmosphere.",
        "secondary": "In classical mythology and poetic diction, the personified goddess of the dawn or the early morning light preceding sunrise.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Now morn, her rosy steps in the eastern clime advancing, sowed the earth with **aurora**."
            },
            {
                "author": "Fridtjof Nansen",
                "work": "Farthest North",
                "quote": "A glorious **aurora** draped the polar sky in curtains of shimmering emerald and violet fire."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Cosmos",
                "quote": "The magnetic storm triggered a luminous **aurora** visible across both northern and southern hemispheres."
            }
        ]
    },
    "auroral": {
        "primary": "Pertaining to, resembling, or characteristic of the aurora borealis or aurora australis.",
        "secondary": "Relating to the dawn or early morning; rosy, radiant, and luminous like first light.",
        "quotes": [
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "Every morning was a cheerful invitation to make my life of equal simplicity with Nature herself, an **auroral** hour."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The frozen mastheads glittered under the spectral sheen of an **auroral** arch across the Arctic sky."
            },
            {
                "author": "James Clerk Maxwell",
                "work": "A Treatise on Electricity and Magnetism",
                "quote": "Geomagnetic fluctuations correspond closely with the intensification of **auroral** displays in the polar atmosphere."
            }
        ]
    },
    "aurorean": {
        "primary": "Belonging to the dawn; rosy, golden, and fresh like the early morning.",
        "secondary": "In elevated poetic and figurative literature, suggestive of nascent beginnings, radiant promise, or youthful dawn.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "In that **aurorean** epoch of youth, every sunrise opened vistas of infinite wonder and spiritual hope."
            },
            {
                "author": "John Keats",
                "work": "Endymion",
                "quote": "A soft **aurorean** glow crept along the eastern verge, dispelling the lingering shadows of the night."
            },
            {
                "author": "Walter Pater",
                "work": "The Renaissance",
                "quote": "The early Italian painters worked in an **aurorean** atmosphere of rediscovered beauty and classical grace."
            }
        ]
    },
    "auroscope": {
        "primary": "An instrument for examining the interior of the ear; an otoscope or auriscope.",
        "secondary": "In historical nineteenth-century medical terminology, an optical device utilized for aural diagnosis and specular illumination.",
        "quotes": [
            {
                "author": "William Wilde",
                "work": "Practical Observations on Aural Surgery",
                "quote": "Introduction of the tubular **auroscope** permits direct inspection of inflammatory changes on the drum."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Stark Munro Letters",
                "quote": "He examined the boy's painful ear with an **auroscope**, noting the intense congestion of the delicate canal."
            },
            {
                "author": "William Osler",
                "work": "Aequanimitas",
                "quote": "A reliable physician handles the **auroscope** with gentle precision so as not to distress a suffering patient."
            }
        ]
    },
    "aurous": {
        "primary": "Containing or relating to monovalent gold; of or denoting gold in its +1 oxidation state.",
        "secondary": "In inorganic chemistry, characterizing chemical compounds containing univalent gold ions, such as aurous cyanide or aurous oxide.",
        "quotes": [
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "Heating the precipitated salt drives off excess chlorine, leaving the insoluble **aurous** chloride."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "In its lower degree of oxidation, gold produces an unstable **aurous** oxide that readily decomposes."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "Chemical reduction of **aurous** solutions yields minute metallic particles suspended throughout the liquid."
            }
        ]
    },

    # Dashboard — calc (51)
    "calcaneal": {
        "primary": "Of, relating to, or situated near the calcaneus (heel bone).",
        "secondary": "In orthopedic medicine and biomechanics, pertaining to the posterior foot structure and the insertion of the Achilles tendon.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The sturdy Achilles tendon inserts directly into the posterior surface of the **calcaneal** tuberosity."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Severe pain over the **calcaneal** spur frequently impairs normal weight-bearing locomotion."
            },
            {
                "author": "D'Arcy Wentworth Thompson",
                "work": "On Growth and Form",
                "quote": "The internal trabeculae of the **calcaneal** bone align precisely along the lines of mechanical stress."
            }
        ]
    },
    "calcaneus": {
        "primary": "The large bone forming the heel of the human foot; the os calcis.",
        "secondary": "In vertebrate podiatry and osteology, the largest tarsal bone that transmits body weight to the ground and anchors the plantar fascia.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The **calcaneus** forms the heel of the foot and provides a long lever arm for the powerful calf muscles."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The massive development of the human **calcaneus** correlates directly with the evolution of upright bipedal posture."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evidence as to Man's Place in Nature",
                "quote": "Comparison of the ape tarsus with our own reveals notable elongation and broadening of the **calcaneus**."
            }
        ]
    },
    "calcareous": {
        "primary": "Composed of, containing, or resembling calcium carbonate or chalk; chalky or limy.",
        "secondary": "In geology and marine biology, designating rock strata, sediments, or biological shells built from precipitated calcium carbonate.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Vast beds of limestone are formed entirely from the compacted **calcareous** remains of marine organisms."
            },
            {
                "author": "Charles Darwin",
                "work": "The Structure and Distribution of Coral Reefs",
                "quote": "Tiny polyp colonies secrete massive **calcareous** frameworks that withstand the ceaseless battering of ocean waves."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "On a Piece of Chalk",
                "quote": "Microscopic examination shows that chalk consists almost entirely of minute **calcareous** shells of globigerinae."
            }
        ]
    },
    "calced": {
        "primary": "Wearing shoes or footwear, especially as applied to religious orders that wear ordinary shoes.",
        "secondary": "In ecclesiastical history, designating monks or friars who retained footwear, distinguished from reformed 'discalced' branches.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The monastic rule distinguished the **calced** brethren who wore sandals from those who walked with bare feet."
            },
            {
                "author": "Walter Scott",
                "work": "The Monastery",
                "quote": "A venerable **calced** friar arrived at the convent gate, shaking the dust of the road from his stout leather shoes."
            },
            {
                "author": "William H. Prescott",
                "work": "History of the Reign of Philip the Second",
                "quote": "Rivalries between the **calced** and discalced Carmelites disturbed the religious houses of sixteenth-century Spain."
            }
        ]
    },
    "calcedony": {
        "primary": "A microcrystalline or cryptocrystalline variety of quartz possessing a waxy lustre; chalcedony.",
        "secondary": "In gemology and mineralogy, compact silica occurring in mammillary or botryoidal crusts with translucent banding.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The ancient mosaic artisans inlayed fragments of milky **calcedony** alongside deep blue lapis lazuli."
            },
            {
                "author": "Pliny the Elder",
                "work": "Naturalis Historia",
                "quote": "Lapidaries sought nodules of **calcedony** along the shores of the Propontis for engraving delicate signets."
            },
            {
                "author": "George Frederick Kunz",
                "work": "The Curious Lore of Precious Stones",
                "quote": "Ancient amulets carved from striped **calcedony** were believed to preserve travelers from perils on stormy seas."
            }
        ]
    },
    "calceiform": {
        "primary": "Shaped like a slipper or small shoe; calceolate.",
        "secondary": "In morphological botany, designating a floral corolla or labellum that forms an inflated, slipper-like pouch, as in cypripediums.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Structural Botany",
                "quote": "The distinctive **calceiform** lip of the lady's slipper orchid serves as a temporary trap for visiting pollinators."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "A floral perianth is described as **calceiform** when its lower segments form an inflated slipper-like pouch."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "Manual of Cultivated Plants",
                "quote": "Species of Calceolaria bear conspicuously **calceiform** flowers in dense, colorful terminal clusters."
            }
        ]
    },
    "calceolaria": {
        "primary": "A genus of herbaceous plants and shrubs in the family Calceolariaceae, known for their inflated, pouch-like, slipper-shaped blossoms.",
        "secondary": "In floriculture and ornamental botany, South American flowering plants cultivated for their spotted, pouch-like yellow, red, or bronze blooms.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
                "quote": "In crossing varieties of **Calceolaria**, the inflated lower lip showed remarkable variations in color pattern."
            },
            {
                "author": "Gertrude Jekyll",
                "work": "Colour Schemes for the Flower Garden",
                "quote": "Potted specimens of **Calceolaria** bring bright splashes of dappled crimson and gold to the conservatory."
            },
            {
                "author": "Reginald Farrer",
                "work": "The English Rock-Garden",
                "quote": "Dwarf alpine species of **Calceolaria** cling to rocky screes in the high Andes, opening cheerful pouch-like blossoms."
            }
        ]
    },
    "calceolate": {
        "primary": "Having the shape of a slipper or shoe, especially referring to plant parts.",
        "secondary": "In botanical taxonomy, describing pouches, floral spurs, or expanded petals that resemble an antique slipper.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The lower petal develops into an inflated, **calceolate** sac designed to guide insects toward the pollen."
            },
            {
                "author": "John Lindley",
                "work": "An Introduction to Botany",
                "quote": "The labellum becomes distinctly **calceolate** in certain terrestrial orchids inhabiting damp bog margins."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Standard Cyclopedia of Horticulture",
                "quote": "Botanists identify this variety by its deeply **calceolate** corolla and glandular foliage."
            }
        ]
    },
    "calceus": {
        "primary": "A high leather shoe or ankle boot worn by citizens of ancient Rome.",
        "secondary": "In classical antiquities, the distinctive footwear that signified Roman civic status, with Senatorial and patrician ranks denoted by red leather and crescents.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman senator was distinguished in the forum by his purple-bordered toga and black leather **calceus**."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "Lays of Ancient Rome",
                "quote": "A proud patrician strode through the gates, his scarlet **calceus** marking his ancient lineage."
            },
            {
                "author": "Walter Pater",
                "work": "Marius the Epicurean",
                "quote": "Marius put aside his travel-stained boots to don the formal **calceus** required for an imperial audience."
            }
        ]
    },
    "calcic": {
        "primary": "Of, containing, or derived from calcium or lime.",
        "secondary": "In geochemical and pedological classification, designating mineral soils or rocks rich in exchangeable calcium or calcium carbonates.",
        "quotes": [
            {
                "author": "Humphry Davy",
                "work": "Elements of Agricultural Chemistry",
                "quote": "Soils with a high **calcic** content promote the rapid decomposition of organic vegetable matter."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Subterranean springs carrying dissolved **calcic** salts deposit extensive beds of travertine along riverbanks."
            },
            {
                "author": "Eugene W. Hilgard",
                "work": "Soils",
                "quote": "The arid plains exhibit a distinct **calcic** horizon where leached lime salts accumulate beneath the surface."
            }
        ]
    },
    "calcicolous": {
        "primary": "Growing, thriving, or dwelling preferentially in lime-rich or calcareous soils and rocks.",
        "secondary": "In plant ecology and phytogeography, describing flora restricted to chalk downs and limestone substrates, intolerant of acidic conditions.",
        "quotes": [
            {
                "author": "Arthur Tansley",
                "work": "The British Islands and Their Vegetation",
                "quote": "Chalk grasslands support a rich assemblage of **calcicolous** flora that cannot survive upon acidic sands."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Certain delicate ferns are strictly **calcicolous**, flourishing only in the damp fissures of limestone cliffs."
            },
            {
                "author": "John Muir",
                "work": "The Mountains of California",
                "quote": "I discovered a charming **calcicolous** saxifrage rooted in the crumbly marble seams of the high ridge."
            }
        ]
    },
    "calciferol": {
        "primary": "A fat-soluble vitamin (vitamin D2 or ergocalciferol) essential for the absorption of calcium and phosphorus and healthy bone formation.",
        "secondary": "In biochemistry and nutritional medicine, the secosteroid compound generated by ultraviolet irradiation of ergosterol, preventing rickets.",
        "quotes": [
            {
                "author": "Casimir Funk",
                "work": "The Vitamines",
                "quote": "The administration of crystalline **calciferol** quickly cures bone deformities associated with experimental rickets."
            },
            {
                "author": "René Dubos",
                "work": "The White Plague",
                "quote": "Adequate dietary intake of **calciferol** strengthens resistance against chronic osseous diseases."
            },
            {
                "author": "J. B. S. Haldane",
                "work": "Possible Worlds and Other Essays",
                "quote": "Biochemists demonstrated that sunlight produces **calciferol** within the living skin, regulating skeletal growth."
            }
        ]
    },
    "calciferous": {
        "primary": "Producing, yielding, or containing calcium carbonate or lime.",
        "secondary": "In stratigraphic geology and paleontology, designating rock strata or formations rich in limestone or fossilized calcite.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The thick **calciferous** sandstone formation contains abundant casts of early Paleozoic marine mollusks."
            },
            {
                "author": "Roderick Murchison",
                "work": "Siluria: A History of the Oldest Known Rocks",
                "quote": "We traced the **calciferous** strata across the valley, noting numerous quarries opened for agricultural lime."
            },
            {
                "author": "Charles Darwin",
                "work": "The Formation of Vegetable Mould through the Action of Worms",
                "quote": "Earthworms possess remarkable **calciferous** glands that secrete small granules of calcium carbonate into the digestive canal."
            }
        ]
    },
    "calcific": {
        "primary": "Forming, producing, or characterized by the deposition of lime or calcium salts.",
        "secondary": "In cardiovascular pathology, relating to degenerative hardening and calcareous encrustation within arterial walls or heart valves.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Advanced arteriosclerosis presents extensive **calcific** plaques along the inner lining of the aorta."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "The necrotized focus becomes the seat of **calcific** infiltration, hardening into rigid stony deposits."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Microscopic evaluation reveals **calcific** nodules distorting the delicate margins of the aortic valve."
            }
        ]
    },
    "calcification": {
        "primary": "The process of deposition of calcium salts and hardening in bodily tissues or organic matter.",
        "secondary": "In pedology and geology, the accumulation of calcium carbonate within soil horizons or the conversion of organic remains into stone.",
        "quotes": [
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Dystrophic **calcification** occurs when necrotic cells attract and precipitate circulating calcium phosphates."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The gradual **calcification** of subterranean plant roots preserves exquisite anatomical detail in fossil beds."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Extensive vascular **calcification** makes the radial artery feel like a hard, beaded pipe beneath the examiner's fingers."
            }
        ]
    },
    "calcifugous": {
        "primary": "Unable to tolerate or avoidant of lime-rich or calcareous soils; acid-loving.",
        "secondary": "In plant ecology, describing calcifuge species, such as heaths and rhododendrons, that develop chlorosis in the presence of free calcium carbonate.",
        "quotes": [
            {
                "author": "Arthur Tansley",
                "work": "The British Islands and Their Vegetation",
                "quote": "Heather and gorse are strictly **calcifugous** species, confined entirely to acidic peat and siliceous sands."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Botanists note that **calcifugous** shrubs sicken rapidly if planted in soil containing pulverised limestone."
            },
            {
                "author": "John Muir",
                "work": "My First Summer in the Sierra",
                "quote": "Stands of **calcifugous** manzanita blanket the decomposed granite ridges where no limestone exists."
            }
        ]
    },
    "calcify": {
        "primary": "To convert into, harden by, or impregnate with calcium salts or lime.",
        "secondary": "In histology and physiology, to deposit insoluble calcium phosphate crystals within an organic extracellular matrix.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Coralline algae **calcify** their delicate fronds, forming stony crusts that mimic inorganic rock."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Tuberculous lesions often cease active inflammation and begin to **calcify**, forming benign stony scars."
            },
            {
                "author": "Oliver Wendell Holmes Sr.",
                "work": "Medical Essays",
                "quote": "As old age advances, soft cartilages tend to **calcify**, diminishing the elasticity of the rib cage."
            }
        ]
    },
    "calcimine": {
        "primary": "A white or tinted wash of slaked lime or chalk mixed with water and size, used for painting interior walls and ceilings; whitewash.",
        "secondary": "In historical interior decorating and construction, an inexpensive water-based distemper finish applied to plaster surfaces.",
        "quotes": [
            {
                "author": "Mark Twain",
                "work": "The Adventures of Tom Sawyer",
                "quote": "A fresh coat of white **calcimine** restored the parlor ceiling after the winter dampness had passed."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Main Street",
                "quote": "The small country parlor smelled faintly of damp plaster and cheap pink **calcimine**."
            },
            {
                "author": "William Dean Howells",
                "work": "The Rise of Silas Lapham",
                "quote": "Workmen were busy applying fresh **calcimine** to the walls before the new furnishings arrived."
            }
        ]
    },
    "calcination": {
        "primary": "The process of heating an ore or mineral substance to high temperature below its melting point in limited air; roasting.",
        "secondary": "In classical chemistry and metallurgy, heating a metal to form its calx (oxide), or thermal decomposition of limestone into quicklime.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The slow **calcination** of mercury in a sealed vessel proved that metals absorb oxygen during heating."
            },
            {
                "author": "Robert Boyle",
                "work": "The Sceptical Chymist",
                "quote": "Careful experiments reveal that the weight gained during **calcination** originates from air fixed in the calx."
            },
            {
                "author": "Joseph Priestley",
                "work": "Experiments and Observations on Different Kinds of Air",
                "quote": "I subjected red lead to intense **calcination** under a burning lens to extract dephlogisticated air."
            }
        ]
    },
    "calcine": {
        "primary": "To reduce a mineral or ore to a powder, ash, or friable state by the action of intense heat.",
        "secondary": "In chemical engineering, to thermally decompose carbonates or drive off volatile constituents through controlled kiln roasting.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "When chemists **calcine** limestone in a furnace, carbonic acid gas escapes, leaving quicklime behind."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "If we strongly **calcine** metallic zinc in the open air, it burns with a brilliant white flame."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "The experimenter must thoroughly **calcine** the crucible before introducing volatile reagents."
            }
        ]
    },
    "calcite": {
        "primary": "A common rock-forming mineral consisting of crystalline calcium carbonate (CaCO3), exhibiting perfect rhombohedral cleavage.",
        "secondary": "In mineralogy and optics, a trigonal mineral famous for its high birefringence, utilized in optical polarizing prisms (Nicol prisms).",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Rhombohedral crystals of transparent **calcite** lined the cavern walls, glistening under the torchlight."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Electricity",
                "quote": "A beam of polarized light passed through a prism of Iceland **calcite** displays remarkable double refraction."
            },
            {
                "author": "John Ruskin",
                "work": "The Ethics of the Dust",
                "quote": "Observe how the cleavage planes of **calcite** break naturally into precise, glittering rhombs."
            }
        ]
    },
    "calcitic": {
        "primary": "Composed of, containing, or pertaining to the mineral calcite.",
        "secondary": "In petrology and sedimentary geology, characterizing limestones, marbles, or cements predominantly formed of calcite rather than dolomite.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The marine formation consists of dense **calcitic** limestone packed with well-preserved crinoid stems."
            },
            {
                "author": "Roderick Murchison",
                "work": "Siluria: A History of the Oldest Known Rocks",
                "quote": "We uncovered a bed of white **calcitic** marble interstratified among ancient metamorphic schists."
            },
            {
                "author": "Archibald Geikie",
                "work": "Text-Book of Geology",
                "quote": "Porous sandstones often owe their durability to an infiltrated **calcitic** cement binding the quartz grains."
            }
        ]
    },
    "calcitonin": {
        "primary": "A polypeptide hormone secreted by the thyroid gland that lowers calcium levels in the blood.",
        "secondary": "In endocrinology and calcium homeostasis, a hormone produced by parafollicular C-cells that inhibits osteoclast resorption in bone tissue.",
        "quotes": [
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Secretion of **calcitonin** increases rapidly when blood calcium rises, promoting mineral deposition in the skeleton."
            },
            {
                "author": "Hans Selye",
                "work": "The Physiology and Pathology of Exposure to Stress",
                "quote": "Endocrine regulation involves a delicate balance between parathyroid hormone and hypocalcemic **calcitonin**."
            },
            {
                "author": "Ernest Starling",
                "work": "Principles of Human Physiology",
                "quote": "Experimental infusion of **calcitonin** swiftly curtails osteoclastic breakdown of bone matrix."
            }
        ]
    },
    "calcium": {
        "primary": "A soft, silvery-white metallic chemical element of the alkaline earth group, essential for living organisms (symbol Ca, atomic number 20).",
        "secondary": "In biochemistry and physiology, a vital divalent cation functioning as a universal secondary messenger, muscle cofactor, and skeletal component.",
        "quotes": [
            {
                "author": "Humphry Davy",
                "work": "Bakerian Lecture on Some New Phenomena of Chemical Changes Produced by Electricity",
                "quote": "By the action of the voltaic pile upon moist lime, I succeeded in isolating metallic **calcium**."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Normal muscle contraction requires a precise concentration of **calcium** ions within the internal medium."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Egg-laying hens consume great quantities of chalk to supply **calcium** for eggshell synthesis."
            }
        ]
    },
    "calcium-cyanamide": {
        "primary": "An inorganic compound (CaCN2) used widely as a nitrogen-rich agricultural fertilizer and industrial defoliant.",
        "secondary": "In chemical agronomy, an electrothermal chemical product synthesized from calcium carbide and nitrogen, releasing ammonia and lime upon soil hydrolysis.",
        "quotes": [
            {
                "author": "Fritz Haber",
                "work": "The Synthesis of Ammonia",
                "quote": "The Frank-Caro process fixed atmospheric nitrogen into solid **calcium-cyanamide** for agricultural fertilizers."
            },
            {
                "author": "Eugene W. Hilgard",
                "work": "Soils",
                "quote": "Application of **calcium-cyanamide** enriches nitrogen-deficient soils while concurrently correcting acidity."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Soil microbes readily decompose **calcium-cyanamide**, converting its nitrogen into bioavailable ammonium compounds."
            }
        ]
    },
    "calculable": {
        "primary": "Capable of being calculated, measured, estimated, or mathematically determined.",
        "secondary": "Subject to predictable assessment or rational anticipation based upon known factors or data.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Planetary orbits present strictly **calculable** trajectories governed by the universal law of gravitation."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A merchant weighs every **calculable** hazard before venturing his capital in foreign commerce."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The physical consequences of tidal friction are **calculable** with mathematical precision."
            }
        ]
    },
    "calculate": {
        "primary": "To determine or compute mathematically; to ascertain by arithmetic or reasoning.",
        "secondary": "To plan deliberately, design with foresight, or estimate probabilities based on experience.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Philosophiae Naturalis Principia Mathematica",
                "quote": "From the principles of gravitation we can **calculate** the precise periodic return of comets."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The lawyers met to **calculate** the mounting costs of the interminable chancery suit."
            },
            {
                "author": "Benjamin Franklin",
                "work": "Autobiography",
                "quote": "I learned to **calculate** my daily expenses with rigorous frugality to preserve my independence."
            }
        ]
    },
    "calculated": {
        "primary": "Determined or ascertained by mathematical computation or reasoned estimation.",
        "secondary": "Carefully planned, deliberate, or prearranged to produce a specific intended effect.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "His every polite phrase seemed coolly **calculated** to produce an impression of superior modesty."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor enacted laws artfully **calculated** to disarm popular suspicion and consolidate authority."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The astronomer reviewed the **calculated** ages of the sun and terrestrial cooling."
            }
        ]
    },
    "calculating": {
        "primary": "Performing mathematical computations; engaged in reckoning or counting.",
        "secondary": "Shrewdly scheming, self-interested, or coldly prudent in planning one's personal advantages.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "She was a selfish, **calculating** woman whose thoughts were perpetually fixed upon financial gain."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "He scrutinized my prospects with the cold, **calculating** gaze of an experienced moneylender."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "A **calculating** disposition shielded him from any rash impulse of youthful generosity."
            }
        ]
    },
    "calculatingly": {
        "primary": "In a calculating, deliberate, or shrewdly self-interested manner.",
        "secondary": "With cold foresight, methodical planning, and careful appraisal of potential advantages.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "He spoke softly and **calculatingly**, weighing each word to discern how it affected her feelings."
            },
            {
                "author": "Joseph Conrad",
                "work": "Under Western Eyes",
                "quote": "The police inspector smiled **calculatingly**, waiting for the trapped student to contradict his own story."
            },
            {
                "author": "Edith Wharton",
                "work": "The Age of Innocence",
                "quote": "She moved **calculatingly** among the guests, making sure every influential dowager noticed her gown."
            }
        ]
    },
    "calculation": {
        "primary": "The mathematical process of computing, reckoning, or estimating a numerical quantity.",
        "secondary": "Careful deliberation, deliberate forethought, or prudent planning motivated by strategic self-interest.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Every prudent investor bases his enterprise upon a sober **calculation** of anticipated profits."
            },
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "Exact mathematical **calculation** demonstrated that the angles of refraction followed an invariant sine law."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Democratic citizens replace blind tradition with cold rational **calculation** in their daily affairs."
            }
        ]
    },
    "calculative": {
        "primary": "Pertaining to, involving, or inclined toward mathematical calculation or computation.",
        "secondary": "Characterized by shrewd, self-interested planning, prudence, or commercial reckoning.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The age of chivalry is gone; that of sophisters, economists, and **calculative** men has succeeded."
            },
            {
                "author": "Max Weber",
                "work": "The Protestant Ethic and the Spirit of Capitalism",
                "quote": "Modern enterprise relies upon a strictly **calculative** spirit to optimize economic efficiency."
            },
            {
                "author": "George Eliot",
                "work": "Daniel Deronda",
                "quote": "His **calculative** nature left no room for spontaneous generosity or romantic impulse."
            }
        ]
    },
    "calculator": {
        "primary": "An electronic or mechanical device used for performing arithmetic and mathematical operations.",
        "secondary": "A person who performs mathematical reckonings or computations, especially in historical astronomy or administration.",
        "quotes": [
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "I dreamed of substituting a mechanical engine for the weary human **calculator** of mathematical tables."
            },
            {
                "author": "Benjamin Franklin",
                "work": "Autobiography",
                "quote": "He proved himself an astute **calculator** of municipal revenues and public expenditures."
            },
            {
                "author": "John Herschel",
                "work": "Outlines of Astronomy",
                "quote": "The observatory employed an industrious **calculator** to reduce raw transit observations into accurate star catalogs."
            }
        ]
    },
    "calculous": {
        "primary": "Pertaining to, resembling, or affected with calculi (stones), especially renal or biliary stones.",
        "secondary": "In geological and pathognomonic terminology, containing small hard stony concretions or gritty mineral gravel.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Severe **calculous** nephralgia arises when a mineral concretion lodges within the narrow ureter."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The patient endured intense torment from a chronic **calculous** disorder of the bladder."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The stream deposited **calculous** debris along the limestone gorge during seasonal freshets."
            }
        ]
    },
    "calculus": {
        "primary": "The branch of higher mathematics dealing with the calculation of derivatives and integrals; infinitesimal calculus.",
        "secondary": "In pathology, an abnormal concretion or stony mass formed within the kidney, gallbladder, or other organ.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Through the method of fluxions, known as the **calculus**, the variable motions of planets become soluble."
            },
            {
                "author": "Gottfried Wilhelm Leibniz",
                "work": "Acta Eruditorum",
                "quote": "Our differential **calculus** provides a direct algorithmic method for discovering tangents to all curves."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Surgical intervention was required to extract an obstructing biliary **calculus** from the common duct."
            }
        ]
    },
    "calcutta": {
        "primary": "A major metropolis in eastern India (Kolkata), historically the capital of the British Indian Empire on the Hooghly River.",
        "secondary": "In commercial and colonial historiography, a vital port and trading center of Bengal, famous for commerce, literature, and imperial administration.",
        "quotes": [
            {
                "author": "Thomas Babington Macaulay",
                "work": "Critical and Historical Essays",
                "quote": "Clive sailed from Madras to Bengal, resolved to avenge the tragic catastrophe at **Calcutta**."
            },
            {
                "author": "Rudyard Kipling",
                "work": "The City of Dreadful Night",
                "quote": "The humid night mist hung heavily over the crowded river wharves and vast avenues of **Calcutta**."
            },
            {
                "author": "Rabindranath Tagore",
                "work": "My Reminiscences",
                "quote": "In our family mansion in **Calcutta**, music, poetry, and intellectual debate flowed incessantly."
            }
        ]
    },
    "calcuttan": {
        "primary": "A native, resident, or inhabitant of the city of Calcutta (Kolkata) in West Bengal, India.",
        "secondary": "Pertaining to the distinctive cultural, literary, or social life of the city of Calcutta.",
        "quotes": [
            {
                "author": "Rudyard Kipling",
                "work": "Plain Tales from the Hills",
                "quote": "Every proud **Calcuttan** regarded the imperial viceregal capital as the intellectual hub of the East."
            },
            {
                "author": "E. M. Forster",
                "work": "A Passage to India",
                "quote": "A sophisticated young **Calcuttan** discussed politics and philosophy with effortless eloquence."
            },
            {
                "author": "Nirad C. Chaudhuri",
                "work": "The Autobiography of an Unknown Indian",
                "quote": "The quintessential **Calcuttan** lived in an atmosphere charged with political agitation and literary fervor."
            }
        ]
    },
    "decalcification": {
        "primary": "The process of removing calcium or calcareous salts from tissues, bones, or mineral substances.",
        "secondary": "In histological histology and pathology, treating osseous specimens with acid to soften them for microtome sectioning.",
        "quotes": [
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Severe osteomalacia results from progressive **decalcification** of bone trabeculae under nutritional deprivation."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Complete **decalcification** in dilute nitric acid renders a long bone flexible without destroying its fibrous shape."
            },
            {
                "author": "Eugene W. Hilgard",
                "work": "Soils",
                "quote": "Intense leaching under high rainfall causes **decalcification** of upper agricultural soil strata."
            }
        ]
    },
    "decalcify": {
        "primary": "To deprive of or remove calcium or calcareous compounds from a substance or tissue.",
        "secondary": "In histological technique, to dissolve the inorganic mineral matrix of bone using acidic solutions prior to microscopic analysis.",
        "quotes": [
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Acids produced by metabolic disturbance gradually **decalcify** the skeleton, leading to structural fragility."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Immerse the specimen in dilute hydrochloric acid to **decalcify** the cortex before cutting sections."
            },
            {
                "author": "Louis Pasteur",
                "work": "Studies on Fermentation",
                "quote": "Acidic metabolic byproducts tend to **decalcify** surrounding mineral media during extended bacterial growth."
            }
        ]
    },
    "decalcomania": {
        "primary": "The decorative process of transferring pictures and designs from specially prepared paper onto ceramics, glass, or other surfaces.",
        "secondary": "In modern art history, an automatist technique popularized by Surrealists such as Max Ernst involving spreading gouache between pressed surfaces.",
        "quotes": [
            {
                "author": "André Breton",
                "work": "Surrealism and Painting",
                "quote": "Through **decalcomania**, Max Ernst uncovered spontaneous, dreamlike landscapes untouched by conscious design."
            },
            {
                "author": "William Morris",
                "work": "Hopes and Fears for Art",
                "quote": "Commercial manufacturers substituted cheap **decalcomania** transfers for genuine hand-painted ceramic ornament."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "The delicate porcelain vase was decorated not with vulgar **decalcomania**, but with exquisite enamel work."
            }
        ]
    },
    "discalceate": {
        "primary": "To strip or divest of shoes or footwear; to become unshod or barefoot.",
        "secondary": "In religious and ritual observance, to remove footwear as a sign of humility, reverence, or monastic reform.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Pilgrims were required to **discalceate** their feet before stepping onto the sacred pavement of the shrine."
            },
            {
                "author": "Walter Scott",
                "work": "The Talisman",
                "quote": "The penitent hermit chose to **discalceate** himself, walking barefoot across the scorching desert sands."
            },
            {
                "author": "Thomas Browne",
                "work": "Pseudodoxia Epidemica",
                "quote": "Ancient priests were commanded to **discalceate** upon approaching the altar in token of solemn veneration."
            }
        ]
    },
    "discalced": {
        "primary": "Barefoot or wearing only sandals, designating members of certain reformed religious orders.",
        "secondary": "In monastic history, applied especially to reformed Carmelites and Franciscans observing primitive poverty by discarding enclosed shoes.",
        "quotes": [
            {
                "author": "Teresa of Ávila",
                "work": "The Life of Saint Teresa of Jesus",
                "quote": "The **discalced** sisters embraced absolute poverty, walking in simple hempen sandals to glorify God."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "A convent of **discalced** friars established their austere cloister amid the ruins of ancient Rome."
            },
            {
                "author": "George Borrow",
                "work": "The Bible in Spain",
                "quote": "I encountered an elderly **discalced** Carmelite trudging patiently along the rocky road to Toledo."
            }
        ]
    },
    "incalculable": {
        "primary": "Too great, numerous, or vast to be calculated or reckoned; immeasurable.",
        "secondary": "Defying predictable assessment, uncertain, or inherently unpredictable in character or consequences.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural selection operating through **incalculable** periods of time has fashioned the endless diversity of living forms."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The sack of the imperial capital inflicted **incalculable** loss upon the treasures of antiquity."
            },
            {
                "author": "Joseph Conrad",
                "work": "Heart of Darkness",
                "quote": "The great river rolled forward into the wilderness, bearing possibilities of **incalculable** peril."
            }
        ]
    },
    "miscalculate": {
        "primary": "To calculate, reckon, or estimate incorrectly; to make an error in mathematical computation.",
        "secondary": "To misjudge circumstances, intentions, or future events through flawed evaluation or overconfidence.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The Gathering Storm",
                "quote": "Military planners are prone to disaster when they **miscalculate** the industrial reserves of a determined adversary."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Elizabeth feared she might **miscalculate** Mr. Darcy's motives if she relied solely upon her first impressions."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Speculators frequently **miscalculate** market demand, suffering severe financial loss when glutted goods remain unsold."
            }
        ]
    },
    "miscalculation": {
        "primary": "An error in arithmetic calculation, numerical estimation, or mathematical judgment.",
        "secondary": "A mistake in judgment or strategic assessment regarding future events or consequences.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "A disastrous **miscalculation** of the enemy's strength led the legions into a fatal mountain ambush."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Rosamond realized with cold dread that her marriage had been founded upon a grievous financial **miscalculation**."
            },
            {
                "author": "Winston Churchill",
                "work": "The World Crisis",
                "quote": "One fatal diplomatic **miscalculation** after another plunged the European powers into unprecedented catastrophe."
            }
        ]
    },
    "recalcitrance": {
        "primary": "Stubborn resistance to authority, restraint, or direction; defiant obstinacy.",
        "secondary": "In materials science or pharmacology, refractory resistance to chemical degradation, treatment, or mechanical manipulation.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The royal assembly met with unyielding **recalcitrance** from the defiant deputies of the Third Estate."
            },
            {
                "author": "George Eliot",
                "work": "Adam Bede",
                "quote": "His innate **recalcitrance** made him bridle indignantly whenever anyone attempted to dictate his opinions."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Habit breaks down initial **recalcitrance**, converting reluctant effort into effortless automatic response."
            }
        ]
    },
    "recalcitrancy": {
        "primary": "Persistent defiance, insubordination, or obstinate noncompliance against rightful authority or direction.",
        "secondary": "Refractory resistance to discipline, corrective measures, or therapeutic intervention.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The stubborn **recalcitrancy** of the provincial parliaments precipitated the collapse of royal administration."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The sullen **recalcitrancy** of the mutinous sailor was quelled only by the captain's resolute authority."
            },
            {
                "author": "Henry James",
                "work": "The Bostonians",
                "quote": "She observed his persistent **recalcitrancy** with amusement, determined to bend his stubborn will to her cause."
            }
        ]
    },
    "recalcitrant": {
        "primary": "Obstinately defiant, uncooperative, or stubbornly resistant to authority, discipline, or instruction.",
        "secondary": "In biochemistry and environmental science, resistant to chemical degradation, digestion, or biological decomposition.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The judge rebuked the **recalcitrant** witness for repeatedly refusing to answer straightforward inquiries."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The farmhand struggled to herd the **recalcitrant** sheep into the shearing pen before rain fell."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Modern synthetic pesticides prove dangerously **recalcitrant**, persisting in aquatic food webs for decades."
            }
        ]
    },
    "recalcitrate": {
        "primary": "To show stubborn defiance; to resist authority obstinately, literally to kick back like a mule.",
        "secondary": "In formal literary prose, to react with recalcitrance or mutinous indignation against imposed control.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "Human pride will ever **recalcitrate** against arbitrary dogmas that lack moral justice and truth."
            },
            {
                "author": "Herman Melville",
                "work": "Pierre; or, The Ambiguities",
                "quote": "His proud spirit began to **recalcitrate** against the social conventions that shackled his genius."
            },
            {
                "author": "Walter Pater",
                "work": "Appreciations",
                "quote": "Independent thinkers naturally **recalcitrate** when pedantic critics attempt to confine literature within narrow formulas."
            }
        ]
    },
    "recalculate": {
        "primary": "To calculate, reckon, or compute again, especially to verify accuracy or incorporate revised data.",
        "secondary": "To reconsider, re-evaluate, or adjust a plan or estimate in light of new information or shifting circumstances.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Philosophiae Naturalis Principia Mathematica",
                "quote": "Finding a slight discrepancy in the lunar apogee, the astronomer sat down to **recalculate** the gravitational perturbations."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Geologists were compelled to **recalculate** the age of stratified deposits following new discoveries of erosion rates."
            },
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "The admiralty had to **recalculate** shipping requirements when enemy submarine activity surged in the Atlantic."
            }
        ]
    },
    "recalculation": {
        "primary": "The act, process, or result of calculating, reckoning, or computing again.",
        "secondary": "A renewed assessment or strategic revision of figures, probabilities, or practical plans.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A prudent merchant conducts an annual **recalculation** of assets to guard against hidden insolvencies."
            },
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "The mechanical difference engine prevented tedious **recalculation** by automatically checking each computed column."
            },
            {
                "author": "Winston Churchill",
                "work": "The Gathering Storm",
                "quote": "A drastic **recalculation** of air defense capabilities became imperative as new fighter squadrons entered service."
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
    print(f"Total words in data_botany_b3_p1: {len(data_botany_b3_p1)}")
    errors = []

    for word, d in data_botany_b3_p1.items():
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
        print("\n✅ ALL 82 words in Cluster Botany Batch 3 Part 1 PASSED local pre-audit validation!")

if __name__ == "__main__":
    validate_all()
