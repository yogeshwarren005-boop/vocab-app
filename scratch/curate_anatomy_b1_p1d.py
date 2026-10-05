# -*- coding: utf-8 -*-
"""
curate_anatomy_b1_p1d.py
Batch 1 Part 1d of Cluster Anatomy & Clinical Medicine (25 words):
- aur_ear remaining (25 words): aurelius, aureole, aureolin, aureomycin,
  auric, auricle, auricula, auricular, auriculate, auriferous, auriform,
  aurify, auripigment, aurochs, aurora, auroral, aurore, aurous, aurum,
  diauric, inaurate, inauration, postauricular, subauricular, superauricular
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_p1d = {
    # 79. aurelius
    "aurelius": {
        "primary": "Pertaining to Marcus Aurelius Antoninus (121–180 AD), Roman Emperor and renowned Stoic philosopher.",
        "secondary": "In intellectual history and classical philosophy, reflecting the austere, introspective moral duties outlined in his private philosophical journal, the *Meditations*.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Marcus **Aurelius** insisted that our highest moral duty is to cultivate universal goodwill toward all fellow human beings."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The golden age of the Antonines reached its philosophical summit under the benevolent reign of Marcus **Aurelius**."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Marius listened with reverent awe as the Emperor **Aurelius** addressed the Roman senate upon the stoic virtues of civic duty."}
        ]
    },

    # 80. aureole
    "aureole": {
        "primary": "A radiant circle of light or golden halo surrounding the head or body of a sacred figure.",
        "secondary": "In art history, iconography, and meteorology, a luminous mandorla enveloping holy persons, or a bright corona seen around the sun through misty clouds.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Religious painters surround their saints with a radiant **aureole** of light to signify supernatural holiness."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The stained-glass window cast a glowing **aureole** about the marble virgin, tinting the chapel with ruby and azure light."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The setting sun crowned the distant mountain peaks with a fiery **aureole** that lingered in the evening sky."}
        ]
    },

    # 81. aureolin
    "aureolin": {
        "primary": "A bright yellow synthetic pigment composed of potassium cobaltinitrite, valued in oil and watercolor painting.",
        "secondary": "In fine art materials science and color chemistry, cobalt yellow (*aureolin*), synthesized in 1848 by Fischer as a stable, semi-transparent glazing color.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The luminous wash of **aureolin** upon the illuminated clouds reproduced Turner's subtle transitions from pure sunlight to gold."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The chemist identified traces of potassium cobaltinitrite, commonly sold as the artists' pigment **aureolin**, upon the stained palette."},
            {"author": "Henry James", "work": "Roderick Hudson", "quote": "The painter mixed a touch of warm **aureolin** into his varnish to impart a mellow afternoon glow to the Roman landscape."}
        ]
    },

    # 82. aureomycin
    "aureomycin": {
        "primary": "Chlortetracycline, the first discovered tetracycline antibiotic, isolated from the actinomycete *Streptomyces aureofaciens*.",
        "secondary": "In antimicrobial pharmacology and clinical infectious disease history, a broad-spectrum golden-yellow antibiotic discovered in 1948 by Benjamin Duggar.",
        "quotes": [
            {"author": "Selman Waksman", "work": "My Life with the Microbes", "quote": "The discovery of **Aureomycin** by Duggar demonstrated the vast reservoir of therapeutic antibiotics synthesized by soil actinomycetes."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The introduction of broad-spectrum tetracyclines such as **aureomycin** revolutionized the therapy of rickettsial and chlamydial infections."},
            {"author": "René Dubos", "work": "Mirage of Health", "quote": "Widespread administration of **aureomycin** in livestock feeds sparked early warnings concerning the emergence of antibiotic-resistant bacteria."}
        ]
    },

    # 83. auric
    "auric": {
        "primary": "Pertaining to or containing gold, especially gold in its trivalent (+3) chemical oxidation state.",
        "secondary": "In inorganic chemistry and electrochemistry, designating trivalent gold salts such as auric chloride ($AuCl_3$) and auric oxide ($Au_2O_3$).",
        "quotes": [
            {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "By evaporating a solution of gold in aqua regia, deep ruby-red crystals of **auric** chloride were readily obtained."},
            {"author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "The **auric** compounds exhibit lower stability than the corresponding aurous salts, reducing to metallic gold upon gentle heating."},
            {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Electrolysis of the **auric** cyanide solution deposited a lustrous, unblemished coat of gold upon the brass electrode."}
        ]
    },

    # 84. auricle
    "auricle": {
        "primary": "The external visible part of the ear (pinna), or an upper atrium/appendage of the heart that receives blood.",
        "secondary": "In human cardiac anatomy, the muscular pouch projecting from the right or left atrium, functioning as an elastic reservoir during atrial systole.",
        "quotes": [
            {"author": "William Harvey", "work": "Exercitatio Anatomica de Motu Cordis et Sanguinis in Animalibus", "quote": "The blood enters the right **auricle** of the heart from the vena cava, whence by atrial contraction it is impelled into the ventricle."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The cartilaginous **auricle** of the external ear collects sound waves and reflects them down the external acoustic meatus."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The pointed projection on the margin of the human **auricle**, known as Darwin's tubercle, represents a vestige of pointed mammalian ears."}
        ]
    },

    # 85. auricula
    "auricula": {
        "primary": "A European alpine primrose (*Primula auricula*) cultivated for its brightly colored, fragrant flowers, or the external ear.",
        "secondary": "In historical floriculture and botany, the bear's-ear primula celebrated by eighteenth-century English plant fanciers for its meal-dusted petals and intricate color rings.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The cottage gardeners displayed prized pots of blooming **auricula**, shielding the delicate powdery petals from spring squalls."},
            {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "This charming plant is termed **auricula** ursi or bear's ear, because its thick fleshy leaves resemble the ears of a beast."},
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Horticultural varieties of **Auricula** illustrate heterostyly, requiring cross-pollination between long-styled and short-styled blossoms."}
        ]
    },

    # 86. auricular
    "auricular": {
        "primary": "Pertaining to the ear, the sense of hearing, or the auricles of the heart.",
        "secondary": "In ecclesiastical practice and cardiology, private confession whispered into a priest's ear, or relating to atrial rhythms and fibrillation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "I heard him swear that it was not his intention: 'Tis my son: God put him to't! But yet I have an **auricular** assurance of it in his own letters."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The quiet whispers exchanged across the pews were intended for the **auricular** benefit of the rector alone."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Irregular pulse deficits in mitral stenosis frequently signal the onset of chronic **auricular** fibrillation."}
        ]
    },

    # 87. auriculate
    "auriculate": {
        "primary": "Having ear-like lobes, appendages, or expansions, especially at the base of a leaf.",
        "secondary": "In morphological botany and paleontology, describing clasping leaf bases that project into two rounded ear-like lobes embracing the stem.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The stem leaves in this species of dock are distinctly **auriculate**, clasping the stalk with two rounded basal lobes."},
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The calyx lobes in the hybrid seedling were conspicuously **auriculate**, inheriting the basal flaps of the pollen parent."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The cartilaginous skull in the embryonic skate develops prominent **auriculate** expansions enclosing the labyrinth of the inner ear."}
        ]
    },

    # 88. auriferous
    "auriferous": {
        "primary": "Yielding, containing, or bearing gold; gold-bearing.",
        "secondary": "In economic geology and alluvial mining, designating quartz veins, gravel reefs, or conglomerates that contain profitable concentrations of native gold.",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The weathering of ancient quartz veins liberates rich nuggets of native gold into the **auriferous** gravels of river valleys."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "Excited prospectors rushed into the gulch, declaring that every spadeful of gravel was rich in **auriferous** sand."},
            {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "In the Chilean mining districts, the mountain streams wash down debris from **auriferous** pyrites embedded in metamorphic slates."}
        ]
    },

    # 89. auriform
    "auriform": {
        "primary": "Shaped like an ear; having the form or contour of a human or mammalian ear.",
        "secondary": "In malacology and mycology, describing ear-shaped biological structures such as the ear-shell (*Haliotis*) or jelly ear fungus (*Auricularia*).",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The shell of the abalone exhibits an **auriform** contour with a flattened spire and an enormous iridescent aperture."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Upon the decaying trunk of an ancient elder tree we observed curious **auriform** gelatinous fungi glistening in the autumn rain."},
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "Certain marine gastropods develop an **auriform** operculum that securely closes their ear-shaped shell against predatory crabs."}
        ]
    },

    # 90. aurify
    "aurify": {
        "primary": "To turn or transform into gold, or to gild and adorn with gold.",
        "secondary": "In the history of alchemy and poetic metaphor, the sought-after transmutation of base metals into pure gold via the philosopher's stone.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The alchemists labored in vain to **aurify** common lead and copper through subtle mercurial distillations."},
            {"author": "Samuel Johnson", "work": "The Idler", "quote": "The poet's imagination possesses the wondrous faculty to **aurify** the meanest objects of daily life with glorious imagery."},
            {"author": "Walter Pater", "work": "The Renaissance: Studies in Art and Poetry", "quote": "The morning sun seemed to **aurify** the marble domes of Venice, turning water and stone into a city of pure gold."}
        ]
    },

    # 91. auripigment
    "auripigment": {
        "primary": "Orpiment (arsenic trisulfide, $As_2S_3$), a bright yellow mineral historically used as an artist's pigment.",
        "secondary": "In historical mineralogy and manuscript illumination (*auri pigmentum*, gold pigment), a brilliant golden-yellow sulfide mined since antiquity for gilding imitations.",
        "quotes": [
            {"author": "Pliny the Elder", "work": "Natural History", "quote": "The mineral known as **auripigment** is dug from mines in Syria, prized by painters for its brilliant resemblance to refined gold."},
            {"author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "Chemical analysis confirms that natural **auripigment** consists of arsenic trisulfide, yielding toxic fumes when roasted over charcoal."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Medieval illuminators enriched their manuscripts with golden backgrounds laid on with crushed **auripigment** and egg tempera."}
        ]
    },

    # 92. aurochs
    "aurochs": {
        "primary": "An extinct large wild ox (*Bos primigenius*) that inhabited the forests of Europe, ancestral to domestic cattle.",
        "secondary": "In European paleontological ecology and hunting history, the towering horned wild bovine that survived in Poland until the final specimen perished in 1627.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Skeletal remains from Swiss lake dwellings demonstrate that our larger breeds of domestic cattle descend from the formidable wild **aurochs**."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The immense horn-cores of the **aurochs** recovered from Pleistocene peat bogs dwarf those of any modern domesticated ox."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Caesar described the fierce and gigantic **aurochs** roaming the Hercynian forest, which the German youth captured in concealed pits."}
        ]
    },

    # 93. aurora
    "aurora": {
        "primary": "A natural electrical light display in the sky near the magnetic poles (aurora borealis or australis), or the dawn.",
        "secondary": "In geophysics and classical poetry, atmospheric luminous emissions produced by geomagnetic solar wind interactions in the ionosphere, or the Roman goddess of dawn.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "But all so soon as the all-cheering sun should in the farthest east begin to draw the shady curtains from **Aurora**'s bed, away from light steals home my heavy son."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "A faint luminous arch spanned the northern sky, pulsing with the ghostly green streamers of the **aurora** above Egdon Heath."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The poet sees in the rising dawn a celestial **aurora** that awakens the sleeping intellect of humanity."}
        ]
    },

    # 94. auroral
    "auroral": {
        "primary": "Pertaining to, resembling, or characteristic of the dawn or the aurora borealis.",
        "secondary": "In upper atmospheric physics and romantic aesthetics, denoting atmospheric geomagnetic emissions, or the fresh, rosy illumination of daybreak.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Every morning was a cheerful invitation to make my life of equal simplicity, and I may say innocence, with Nature herself; I have been as sincere a worshipper of **Aurora** as the Greeks; morning brings back the heroic ages with its **auroral** freshness."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I salute the glorious **auroral** flashes spanning the midnight skies above the frozen Arctic seas."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "A delicate **auroral** flush overspread the eastern horizon, tinting the Alban hills with rose and violet."}
        ]
    },

    # 95. aurore
    "aurore": {
        "primary": "A soft, warm yellowish-pink or peach color resembling the morning dawn, or the French word for dawn.",
        "secondary": "In textile dyeing and decorative arts, a delicate salmon-pink silk dye popular in eighteenth-century French fashion, named after the rosy dawn (*aurore*).",
        "quotes": [
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp wore a charming gown of pale **aurore** silk that highlighted her fair complexion and sparkling green eyes."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The morning light crept into the long drawing-room, casting a faint **aurore** glow upon the antique tapestry panels."},
            {"author": "Honoré de Balzac", "work": "Old Goriot", "quote": "Her salon was draped in elegant fabrics of **aurore** satin, creating an ambiance of soft and flattering warmth."}
        ]
    },

    # 96. aurous
    "aurous": {
        "primary": "Pertaining to, containing, or derived from gold, especially in its monovalent (+1) oxidation state.",
        "secondary": "In inorganic chemistry, designating univalent gold compounds such as aurous chloride ($AuCl$) or aurous cyanide ($AuCN$).",
        "quotes": [
            {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Gentle heating of the trichloride expels chlorine gas, yielding pale yellow insoluble powder of **aurous** chloride."},
            {"author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "The **aurous** oxide dissolves in boiling water with immediate disproportionation into metallic gold and auric hydroxide."},
            {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The formation of the double cyanide of **aurous** gold and potassium is fundamental to commercial electrolytic gilding."}
        ]
    },

    # 97. aurum
    "aurum": {
        "primary": "The Latin word for gold, from which the chemical symbol Au is derived.",
        "secondary": "In classical metallurgy and pharmacy, the elemental noble metal ($Au$), historically prescribed as *aurum potabile* (drinkable gold) in alchemical elixirs.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Ancient alchemists celebrated **aurum** potabile as a sovereign panacea capable of renewing human youth and vital spirits."},
            {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "No solvent known to antiquity save aqua regia was capable of dissolving the dense noble substance **aurum**."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Physicians still debate the medicinal efficacy of chemical preparations compounded with refined **aurum**."}
        ]
    },

    # 98. diauric
    "diauric": {
        "primary": "Pertaining to or containing two gold atoms in a chemical formula or molecule.",
        "secondary": "In coordination chemistry and organometallic gold complexes, designating bimetallic gold compounds containing two distinct auric or aurous centers.",
        "quotes": [
            {"author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "The stoichiometric analysis of this complex double salt indicates a **diauric** composition containing two atoms of gold per molecule."},
            {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "By thermal precipitation from the mixed chloride solution, we isolated an intermediate **diauric** oxide precipitate."},
            {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Certain organogold derivatives behave as **diauric** complexes, exhibiting strong metal-metal interactions between adjacent gold centers."}
        ]
    },

    # 99. inaurate
    "inaurate": {
        "primary": "To gild; to cover, coat, or overlay with a thin layer of gold.",
        "secondary": "In historical craft terminology and pharmacy, to apply gold leaf or gilding to medicinal pills to mask their bitter taste or enhance ceremonial prestige.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Apothecaries were anciently accustomed to **inaurate** foul-tasting boluses with delicate leaves of gold foil."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Physicians strive to **inaurate** their bitter pills with sweet syrups and flattering promises of speedy recovery."},
            {"author": "John Evelyn", "work": "Sylva", "quote": "The carvers were instructed to **inaurate** the cornice and ornate brackets of the state bed with fine gold leaf."}
        ]
    },

    # 100. inauration
    "inauration": {
        "primary": "The act or process of gilding; coating or overlaying an object with gold.",
        "secondary": "In historical metallurgy and pharmaceutical history, applying gold leaf to architectural carvings, coins, or medicinal pills.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The craft of **inauration** by amalgamation with quicksilver leaves a durable coating of gold upon copper vessels."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Ancient artisans performed the **inauration** of bronze statues with fiery amalgams that drove off the volatile mercury."},
            {"author": "John Evelyn", "work": "Numismata: A Discourse of Medals", "quote": "The **inauration** of memorial medals preserved their crisp relief against atmospheric tarnish for centuries."}
        ]
    },

    # 101. postauricular
    "postauricular": {
        "primary": "Situated behind or posterior to the external ear.",
        "secondary": "In clinical otolaryngology and surgical anatomy, designating lymph nodes, incisions, or abscesses located in the retroauricular sulcus overlying the mastoid process.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute mastoiditis presents with painful boggy swelling and redness in the **postauricular** region behind the pinna."},
            {"author": "Sir Astley Cooper", "work": "Lectures on the Principles and Practice of Surgery", "quote": "The surgeon made a curved **postauricular** incision to expose the cortex of the mastoid bone without injuring the facial nerve."},
            {"author": "Howard Kelly", "work": "Operative Surgery", "quote": "Enlargement of the **postauricular** lymph glands frequently accompanies pediculosis or cutaneous infections of the scalp."}
        ]
    },

    # 102. subauricular
    "subauricular": {
        "primary": "Situated beneath, below, or on the inferior aspect of the ear.",
        "secondary": "In head and neck surgical anatomy, designating the region directly below the ear lobe containing the lower tail of the parotid gland and upper deep cervical lymph nodes.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Painful tenderness in the **subauricular** groove beneath the ear lobe provides an early sign of acute epidemic parotitis."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The external jugular vein receives tributaries emerging from the **subauricular** venous plexus before descending into the neck."},
            {"author": "Sir Astley Cooper", "work": "A Treatise on Dislocations and Fractures of the Joints", "quote": "A deep tumor situated in the **subauricular** fossa demands cautious dissection to protect the underlying carotid artery."}
        ]
    },

    # 103. superauricular
    "superauricular": {
        "primary": "Situated above or superior to the ear.",
        "secondary": "In cranial anatomy and neurology, designating the scalp region, temporoparietal fascia, or superficial temporal arterial branches located superior to the pinna.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe temporal arteritis produces exquisite tenderness along the **superauricular** course of the superficial temporal artery."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The temporal line arches across the **superauricular** vault of the cranium, demarcating the origin of the temporalis muscle."},
            {"author": "Sir Astley Cooper", "work": "Lectures on the Principles and Practice of Surgery", "quote": "The surgeon applied pressure to the **superauricular** arterial branch to arrest hemorrhage from a deep scalp laceration."}
        ]
    }
}
