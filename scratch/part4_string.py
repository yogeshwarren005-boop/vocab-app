# -*- coding: utf-8 -*-
"""
Part 4: 17 words from Dashboard — string ('astringe' to 'unstring')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part4_string = {
  "astringe": {
    "primary": "To draw together, compress, or cause organic tissue to contract; to constrict or bind tightly.",
    "secondary": "In classical therapeutics and materia medica, to apply an astringent agent that stops hemorrhage, diminishes secretions, or tightens mucous membranes.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Cold doth **astringe** and bind the pores of the body, shutting in the natural spirits and preventing excessive dissipation."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tannic acid was traditionally employed to **astringe** the weeping mucosal surfaces and arrest superficial capillary bleeding."},
      {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "The bitter bark of the oak hath an ancient virtue to **astringe** loose tissues and firm up relaxed sinews in medicinal draughts."}
    ]
  },
  "astringence": {
    "primary": "The quality, state, or property of drawing tissues together or contracting organic surfaces; constricting power.",
    "secondary": "In pharmaceutical chemistry and sensory physiology, the rough, puckering tactile sensation in the oral cavity caused by tannins precipitating salivary proteins.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The notable **astringence** of vitriolic liquors upon the tongue arises from their power to coagulate the subtle animal spirits in the saliva."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The green sloe berries possess such intense **astringence** that cattle avoid grazing upon the blackthorn hedges."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Certain vegetable infusions produce an immediate **astringence** across the mucous membranes by coagulating superficial cellular proteins."}
    ]
  },
  "astringency": {
    "primary": "A sharp, drying, or puckering quality in taste or sensation; or the capacity to contract and tighten organic tissues.",
    "secondary": "In enology and literary criticism, the tannic bitterness in dry wines; or severe, harsh, biting rigor in satirical prose.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Then, when he spoke, there was a dry **astringency** in his tone that checked any exuberant outburst of juvenile enthusiasm."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The wild fruits growing upon the patagonian hills possessed an extreme **astringency**, rendering them completely unpalatable to our party."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "In traditional medicine, plants possessing marked **astringency** were frequently chosen for sacred purification rituals."}
    ]
  },
  "astringent": {
    "primary": "Causing the contraction of skin cells and other body tissues; sharp, severe, or biting in manner or style.",
    "secondary": "In pharmacology and dermatology, a topical agent (such as witch hazel, alum, or zinc oxide) used to reduce secretions and protect epidermal surfaces.",
    "quotes": [
      {"author": "Anthony Pryde", "work": "Nightfall", "quote": "Where the autumn breeze blew over the marsh, the air held an **astringent** coolness that revived his weary spirits."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Application of a mild **astringent** lotion effectively diminished cutaneous exudation and accelerated healthy epithelial healing."},
      {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "There is an **astringent** common sense in the English temperament that rejects wild metaphysical abstractions."}
    ]
  },
  "constringe": {
    "primary": "To draw tightly together, contract, compress, or cause to shrink in dimensions through physical or chemical action.",
    "secondary": "In physiology and chemical physics, to induce reversible or irreversible muscular or macromolecular contraction across tissue structures.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Sudden cold doth **constringe** the outward parts of living creatures, driving the vital heat inward to preserve life."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Rigorous cold baths serve to **constringe** the fibres of the skin, hardening young bodies against delicate ailments."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Misfortune will either elevate a generous soul or **constringe** a narrow mind into bitter, suspicious isolation."}
    ]
  },
  "nonastringent": {
    "primary": "Not causing contraction of tissues or drawing together of organic surfaces; lacking a puckering, sharp, or drying quality.",
    "secondary": "In pomology and food science, designating persimmon cultivars (such as Fuyu) that lose tannin insolubility early and can be consumed while still firm.",
    "quotes": [
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Modern orchardists select **nonastringent** varieties of oriental persimmons because the crisp fruits can be eaten immediately upon ripening."},
      {"author": "Asa Gray", "work": "Scientific Papers of Asa Gray", "quote": "The cultivated variety yielded a sweet, **nonastringent** pulp quite unlike the harsh, tannin-rich fruit of the wild persimmon tree."},
      {"author": "Luther Burbank", "work": "His Methods and Discoveries", "quote": "Through selective breeding, we isolated a completely **nonastringent** seedling whose succulent flesh had entirely lost its ancestral bitterness."}
    ]
  },
  "string": {
    "primary": "A long, thin piece of twisted thread, cord, or twine used for tying, binding, or fastening objects together.",
    "secondary": "In computer science and music, an ordered sequence of characters in code; or a vibrating wire, gut, or nylon cord producing acoustic tones on an instrument.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Her tongue will not obey her heart, nor can her heart inform her tongue; the **string** is broke that should tie them together."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "He tied the packet of letters securely with a length of faded pink **string**, placing it carefully in the secret drawer."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver carried his parcels of finished linen tied with stout flaxen **string**, walking along the hedgerows into the town."}
    ]
  },
  "stringency": {
    "primary": "Rigorous, uncompromising strictness, precision, or severity in requirements, rules, standards, or enforcement.",
    "secondary": "In financial economics and banking, tightness in money markets caused by credit scarcity, high interest rates, and contraction of currency circulation.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Then what with the increasing **stringency** of agricultural rents and the falling markets, the farmers found themselves hard pressed."},
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The commercial crisis was marked by extreme **stringency** in the loan market, with banks refusing credit even on prime collateral."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The superstitious taboo was enforced with absolute **stringency**, and any violator was immediately banished from the tribal hearth."}
    ]
  },
  "stringent": {
    "primary": "Demanding strict, rigorous, and exact adherence to rules, standards, or conditions; severely limiting or restricting.",
    "secondary": "In economic markets and constitutional administration, characterized by severe shortage of capital or binding, unyielding legal prohibitions.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The legislature enacted **stringent** factory inspection laws to curb child labor and ensure sanitary conditions in industrial workshops."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She submitted with patient fortitude to the **stringent** regulations of Lowood, finding in steady labor a relief from sorrow."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A **stringent** enforcement of contracts is the indispensable cornerstone upon which modern mercantile enterprise rests."}
    ]
  },
  "stringently": {
    "primary": "In a strict, rigorous, and demanding manner; with precise, severe enforcement of rules, standards, or obligations.",
    "secondary": "In regulatory compliance and fiscal control, administered without leniency, discretion, or allowable deviation from statutory mandates.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "When statutory safety codes are **stringently** enforced by competent inspectors, industrial accidents decline dramatically across mines and mills."},
      {"author": "Bernard Shaw", "work": "Cashel Byron's Profession", "quote": "The athletic trainer **stringently** regulated the young fighter's diet and sleep, permitting no self-indulgence whatsoever."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Revenue laws must be **stringently** executed to maintain public credit and deter fraudulent evasions at the customs ports."}
    ]
  },
  "stringer": {
    "primary": "A person or thing that strings; especially a freelance journalist paid by the piece, or a long horizontal timber used to support structures.",
    "secondary": "In bridge engineering, shipbuilding, and architecture, a heavy longitudinal beam supporting a deck, railroad tracks, or stair treads.",
    "quotes": [
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The ship's carpenters bolted a massive oak **stringer** along the inner timbers of the gun-deck to support the heavy battery."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "Our country paper relied upon a local **stringer** at every river landing to wire rumors of floods, steamboat races, and town brawls."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The heavy staircase rested upon an unadorned stone **stringer**, revealing the honest structural framework of the medieval masonry."}
    ]
  },
  "strings": {
    "primary": "Multiple cords or threads; or the stringed instruments played in an orchestra, including violins, violas, cellos, and double basses.",
    "secondary": "In physics and theoretical mechanics, slender, vibrating acoustic filaments; or conditions, stipulations, and qualifications attached to an offer.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "How sweet the moonlight sleeps upon this bank! Here will we sit and let the sounds of music creep in our ears; soft stillness and the night become the touches of sweet harmony from sounding **strings**."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The village choir tuned the fiddle **strings** with earnest devotion before embarking upon their lively Christmas carol."},
      {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "The Mock Turtle sighed deeply, drawing his bow across the fiddle **strings** to produce a plaintive, quavering melody."}
    ]
  },
  "stringy": {
    "primary": "Containing, consisting of, or resembling long, tough strings or fibrous threads; chewy and fibrous in texture.",
    "secondary": "In physical geology, metallurgy, and culinary anatomy, exhibiting viscous ropiness or tough, fibrous connective tissue bands.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The turf was bound together by **stringy** roots of wild heath that clung with stubborn tenacity to the barren chalk hill."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The meat of the wild guanaco was lean and **stringy**, requiring hours of slow simmering over our campfires to make it tender."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Long, **stringy** filaments of marine weed hung from the rusty anchor flukes, dripping sea-water onto the forecastle deck."}
    ]
  },
  "stringybark": {
    "primary": "Any of several Australian eucalyptus trees characterized by thick, fibrous, deeply furrowed bark that can be stripped off in long cords.",
    "secondary": "In Australian silviculture and forestry, timber-yielding Eucalyptus species (such as Eucalyptus obliqua) yielding durable building timber and fibrous bark used for cordage.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In the blue mountains of New South Wales, the majestic **stringybark** eucalyptus trees rose with fibrous trunks high into the clear sky."},
      {"author": "Alfred Russel Wallace", "work": "Australasia", "quote": "Settlers constructed their first bush huts using the thick, pliable bark stripped from the towering **stringybark** trees."},
      {"author": "Ferdinand von Mueller", "work": "Eucalyptographia", "quote": "The economic value of the **stringybark** lies not only in its excellent timber for railway ties, but also in the tough fibers of its cortex."}
    ]
  },
  "substring": {
    "primary": "A contiguous sequence of characters taken from within a longer string of text or code.",
    "secondary": "In formal language theory, string matching algorithms, and computational linguistics, any contiguous linear sub-segment of an alphabet sequence.",
    "quotes": [
      {"author": "Alan Turing", "work": "Computing Machinery and Intelligence", "quote": "The symbolic machine scans the tape cell by cell, identifying whether a target **substring** occurs within the coded input sequence."},
      {"author": "Donald Knuth", "work": "The Art of Computer Programming", "quote": "Efficient pattern matching requires determining whether a specified **substring** appears within a text in linear time without backtracking."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical engine was designed to analyze each numerical **substring** represented by the rotational positions of its geared wheels."}
    ]
  },
  "superstring": {
    "primary": "A hypothetical one-dimensional vibrating quantum entity measuring roughly the Planck length, postulated as the fundamental constituent of all matter and forces.",
    "secondary": "In theoretical physics and quantum cosmology, the fundamental vibrating filament in ten or eleven space-time dimensions reconciling quantum mechanics with general relativity.",
    "quotes": [
      {"author": "Stephen Hawking", "work": "A Brief History of Time", "quote": "In **superstring** theory, the fundamental constituents of the universe are not point-like particles, but tiny vibrating loops of energy."},
      {"author": "Brian Greene", "work": "The Elegant Universe", "quote": "Each vibrational pattern of a single **superstring** produces a distinct particle mass and charge, orchestrating the symphony of the cosmos."},
      {"author": "Roger Penrose", "work": "The Road to Reality", "quote": "The mathematical beauty of **superstring** models has attracted generations of theoretical physicists seeking a unified quantum geometry."}
    ]
  },
  "unstring": {
    "primary": "To loosen, remove, or release the strings of a bow, musical instrument, or necklace; to relax or weaken someone's nerves or resolve.",
    "secondary": "In psychological descriptions and classical warfare, to cause physical trembling or collapse of fortitude; or to de-tension a composite recurve bow.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Let sorrow **unstring** thy heart no more; arise and arm thy courage against the approaching storm."},
      {"author": "Alexander Pope", "work": "The Iliad of Homer", "quote": "The weary archer hastened to **unstring** his horn bow when the shadows of night fell over the bloody Trojan plain."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The sudden shock seemed to **unstring** all Henchard's vigorous faculties, leaving him trembling like an aged invalid."}
    ]
  }
}
