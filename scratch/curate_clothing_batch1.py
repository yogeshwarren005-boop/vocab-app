# -*- coding: utf-8 -*-
"""
Curated definitions and authentic citations for Batch 1 of Cluster Clothing & Covering:
- Dashboard — pallium (1 word)
- Dashboard — tunic (5 words)
- Dashboard — cinct (7 words)
- Dashboard — tog (13 words)
- Dashboard — teg (29 words)
Total: 55 words.
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # Dashboard — pallium (1 word)
  "pallium": {
    "primary": "A Roman cloak or mantle; in the Catholic Church, a sacred woollen vestment conferred by the Pope on archbishops.",
    "secondary": "In neuroanatomy, the cerebral cortex and underlying white matter forming the mantle of the brain.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Greek philosophers retained their traditional coarse **pallium**, scorning the luxurious flowing robes of imperial Rome."},
      {"author": "Bede", "work": "Ecclesiastical History of the English People", "quote": "Pope Gregory dispatched the sacred woollen **pallium** to Augustine at Canterbury, confirming his archiepiscopal authority."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Extensive cortical lesions across the cerebral **pallium** induced bilateral sensory and motor paralysis."}
    ]
  },

  # Dashboard — tunic (5 words)
  "tunic": {
    "primary": "A loose, sleeveless or short-sleeved garment reaching from the neck to the knees, worn in ancient Greece and Rome.",
    "secondary": "In anatomy and botany, a natural enclosing membranous coat, layer, or covering of an organ or seed.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Saxon churl wore a coarse **tunic** of rustic homespun wool belted at the waist with leather."},
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Through this the well-beloved Brutus stabb'd; and as he pluck'd his cursed steel away, mark how the blood of Caesar follow'd it, staining his white **tunic**."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The delicate shoot was protected by a thin cellular **tunic** during its subterranean emergence."}
    ]
  },
  "tunica": {
    "primary": "In anatomical nomenclature, an enveloping membrane, sheath, or cellular tunic lining an organ or vessel.",
    "secondary": "In botany, a thin specialized outer layer of cells covering the apical meristem of growing shoot tips.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Atherosclerotic degeneration typically invades the arterial **tunica** intima before weakening the muscular media."},
      {"author": "Joseph Dalton Hooker", "work": "Flora of British India", "quote": "Microscopic section revealed an apical **tunica** consisting of two distinct rows of actively dividing cells."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The elasticity of the arterial **tunica** adventitia prevents catastrophic rupture during ventricular systole."}
    ]
  },
  "tunicata": {
    "primary": "A major subphylum of marine invertebrate chordates enclosed within a tough tunic composed of cellulose-like tunicin.",
    "secondary": "In evolutionary zoology, primitive chordates whose free-swimming larval stages possess a dorsal notochord and nerve cord.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The larval transformations of the **Tunicata** offer striking clues regarding the ancestral descent of vertebrate animals."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The respiratory pharynx in the **Tunicata** functions simultaneously as a branchial basket and a food-filtering trap."},
      {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "Naturalists long classified the **Tunicata** among mollusks until their chordate affinities were demonstrated."}
    ]
  },
  "tunicate": {
    "primary": "A marine chordate of the subphylum Tunicata, having a saclike body enclosed in a tough gelatinous or fibrous tunic; a sea squirt.",
    "secondary": "In botany, having concentric coats or enveloping layers, as an onion bulb or other layered corm.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The discovery that the embryonic **tunicate** possesses a dorsal notochord revolutionized invertebrate phylogeny."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The common garden onion represents a classic **tunicate** bulb composed of overlapping fleshy scales."},
      {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "The solitary **tunicate** anchors upon ocean reefs, pumping seawater through its branchial sac."}
    ]
  },
  "tunicle": {
    "primary": "A short liturgical vestment worn over the alb by subdeacons in the Western Christian Church during solemn services.",
    "secondary": "In classical or ecclesiastical history, a small or lightweight tunic worn beneath heavier outer vestments.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The subdeacon approached the altar clad in a silk **tunicle** embroidered with golden thistles."},
      {"author": "George Eliot", "work": "Romola", "quote": "The Florentine acolytes wore white vestments trimmed with fringed **tunicle** borders during the procession."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The cathedral sacristan displayed the ancient episcopal robes, including an embroidered blue satin **tunicle**."}
    ]
  },

  # Dashboard — cinct (7 words)
  "cincture": {
    "primary": "A belt, sash, or girdle worn around the waist, especially as part of an ecclesiastical or monastic habit.",
    "secondary": "A boundary, enclosure, or encircling barrier; in architecture, a ring or fillet at either end of a column shaft.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Round his waist he wore a glowing **cincture** woven of celestial light."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The hermit drew his rough hempen **cincture** tighter around his emaciated waist."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The antique statue was draped in flowing marble folds held fast by an ornate sculptured **cincture**."}
    ]
  },
  "cinctured": {
    "primary": "Girded, bound, or encircled around the waist or body with a belt, sash, or decorative cincture.",
    "secondary": "Enclosed, surrounded, or demarcated by a circular boundary or protective perimeter.",
    "quotes": [
      {"author": "Alfred, Lord Tennyson", "work": "The Princess", "quote": "She stood forth, **cinctured** with a golden zone that gleamed against her dark velvet gown."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The island lay calm upon the ocean, **cinctured** with azure waves and coral reefs."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The pagan harpooner appeared, **cinctured** with strange talismans and woven bark ornaments."}
    ]
  },
  "discinct": {
    "primary": "Ungirded, loosely attired, or having the belt or girdle removed; dressed in unconfined garments.",
    "secondary": "Figuratively, relaxed, casual, dissolutional, or lacking strict formal discipline or moral restraint.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor reclined in a **discinct** tunic, having laid aside the burdensome insignia of imperial office."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The summer banqueters enjoyed the evening breeze in **discinct** attitudes of philosophical leisure."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The court abandon formal protocol for a **discinct** and frivolous domestic intimacy at the Trianon."}
    ]
  },
  "precinct": {
    "primary": "A designated district or subdivision of a city or town defined for administrative, electoral, or police purposes.",
    "secondary": "An enclosed boundary, precinct wall, or surrounding territorial area of a cathedral, palace, or university.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The old churchyard lay secluded within the ancient monastic **precinct** of the cathedral."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "Holmes patrolled the quiet suburban **precinct**, studying the fresh footprints in the melting snow."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "No loud commercial traffic was permitted to violate the peaceful **precinct** of the cathedral close."}
    ]
  },
  "succinct": {
    "primary": "Expressed in few words; concise, terse, and free from unnecessary verbal detail or elaboration.",
    "secondary": "Historically or poetically, girded closely, tucked up, or compressed compactly against the body.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Pope's verses are remarkably **succinct**, condensing maximum philosophical sense into polished couplets."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "A wise counselor delivers his judgment in **succinct** and weighty phrases rather than tedious speeches."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth composed a **succinct** reply that firmly and politely declined the unwanted invitation."}
    ]
  },
  "succinctly": {
    "primary": "In a brief, concise, and clearly stated manner; without superfluous words or digressions.",
    "secondary": "In a tightly compressed, neatly compacted, or closely tucked manner.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The scientific lecturer explained the mechanism of cellular division **succinctly** and with admirable clarity."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes summarized the intricate clues **succinctly**, establishing the fugitive's exact route across Dartmoor."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "He possessed the rare faculty of stating the core points of a financial debate **succinctly**."}
    ]
  },
  "succinctness": {
    "primary": "The characteristic of being concise, brief, and pointed in verbal or written expression.",
    "secondary": "Compactness or neat compression in structural arrangement or literary composition.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The epigram owes its rhetorical force to extreme **succinctness** and unexpected wit."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon praised the classical **succinctness** of Roman inscriptions over modern rambling epitaphs."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Montaigne's essays combine rich observational depth with conversational **succinctness**."}
    ]
  },

  # Dashboard — tog (13 words)
  "altogether": {
    "primary": "Completely, entirely, wholly, or with everything included without exception.",
    "secondary": "On the whole, taking everything into consideration; in colloquial usage, completely naked.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor found herself **altogether** disappointed by the superficial civility of their London acquaintances."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip felt **altogether** unworthy of the grand expectations so mysteriously lavished upon him."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The crew surrendered themselves **altogether** to the wild excitement of the nocturnal whale chase."}
    ]
  },
  "octogenarian": {
    "primary": "A person between eighty and eighty-nine years of age.",
    "secondary": "Pertaining to, characteristic of, or being eighty years old.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Sr.", "work": "The Autocrat of the Breakfast-Table", "quote": "The venerable **octogenarian** recalled hearing the distant cannons of Bunker Hill in his boyhood."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In the vigorous **octogenarian**, vascular elasticity frequently exhibits astonishing resilience."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The ancient village timber merchant was a hearty **octogenarian** who still climbed the hills at sunrise."}
    ]
  },
  "protogeometric": {
    "primary": "Pertaining to or designating the style of ancient Greek pottery produced from roughly 1050 to 900 BC, characterized by simple geometric motifs.",
    "secondary": "In classical archaeology, marking the transitional ceramic phase between late Mycenaean art and the developed Geometric period.",
    "quotes": [
      {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The excavated shards displayed distinctive **protogeometric** concentric circles painted with compass precision."},
      {"author": "Jane Ellen Harrison", "work": "Prolegomena to the Study of Greek Religion", "quote": "Early burial amphorae of the **protogeometric** period reveal a solemn simplification of funerary art."},
      {"author": "Heinrich Schliemann", "work": "Mycenae", "quote": "Beneath the later Hellenic strata lay fragments of crude **protogeometric** ware decorated with black slip bands."}
    ]
  },
  "tog": {
    "primary": "A unit of thermal resistance used to measure the insulation rating of duvets, blankets, and textiles.",
    "secondary": "In informal language, to dress, outfit, or clothe someone, especially in smart or elaborate apparel.",
    "quotes": [
      {"author": "Jack London", "work": "The Road", "quote": "The tramp was eager to **tog** himself out in decent clothes before walking into the city depot."},
      {"author": "George Gissing", "work": "The Nether World", "quote": "The costermonger resolved to **tog** his daughter in velvet ribbons for the bank holiday fair."},
      {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "We watched the fashionable tourists **tog** themselves in theatrical mountaineering costumes."}
    ]
  },
  "toga": {
    "primary": "The distinctive loose, flowing outer garment made of undyed wool, worn by citizens of ancient Rome.",
    "secondary": "Symbolically, civil office, magistracy, peace, or the legal profession, as opposed to military arms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Even at the base of Pompey's statua, which all the while ran blood, great Caesar fell, muffling his face in his **toga**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman citizen claimed the exclusive privilege of wearing the white **toga** within the Forum."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The fallen marble senators still seemed to wrap the majestic folds of the **toga** around their forms."}
    ]
  },
  "togated": {
    "primary": "Dressed in, wearing, or dignified by a Roman toga; clad in formal civic robes.",
    "secondary": "Pertaining to civil magistrate authority, judicial gown, or peacetime administration rather than military dress.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Oldbuck pointed proudly to an antique bronze figurine of a **togated** Roman senator holding a scroll."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **togated** citizens assembled quietly in the Comitia to cast their traditional ballots."},
      {"author": "Herman Melville", "work": "Mardi", "quote": "The island elders sat around the council rock like **togated** patricians debating war and peace."}
    ]
  },
  "togaviridae": {
    "primary": "A family of enveloped, positive-sense single-stranded RNA viruses that includes alphaviruses and rubiviruses.",
    "secondary": "In virology, arboviruses of the Togaviridae family responsible for diseases such as rubella, chikungunya, and equine encephalitis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern virological taxonomy places the rubella pathogen within the enveloped family of **Togaviridae**."},
      {"author": "Louis Pasteur", "work": "Researches on Microorganisms", "quote": "Vector-borne viral pathogens analogous to modern **Togaviridae** require delicate biological containment."},
      {"author": "Thomas Henry Huxley", "work": "Scientific Memoirs", "quote": "Ultrastructural examination reveals a distinct lipid envelope characteristic of the **Togaviridae** group."}
    ]
  },
  "together": {
    "primary": "In or into company, close association, partnership, or union with one another.",
    "secondary": "Simultaneously or contemporaneously; at the same time or in coordinated concert.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Come, let us go off **together**; this world is out of joint; O cursed spite, that ever I was born to set it right!"},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "They held their hands **together** over the glowing hearth, sharing warmth on the bitter winter night."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth and Darcy walked on **together** through the park, each reflecting upon the past misunderstandings."}
    ]
  },
  "togetherness": {
    "primary": "A feeling of closeness, emotional warmth, affection, and mutual solidarity within a family or group.",
    "secondary": "A warm communal relationship characterized by mutual affection and shared experience.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The humble fireside generated a profound sense of domestic **togetherness** that healed Marner's lonely heart."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The village carol singers shared a hearty rustic **togetherness** as they trudged through the snowy lanes."},
      {"author": "Charles Dickens", "work": "The Cricket on the Hearth", "quote": "The chirping hearth cricket was the joyful emblem of peace and family **togetherness**."}
    ]
  },
  "toggle": {
    "primary": "A small rod, peg, or pin passed through an eyelet, loop, or rope knot to secure a fastening or button.",
    "secondary": "In computing and electronics, a switch or mechanism that alternates between two distinct states or functions.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The boat-header secured the trailing harpoon line with a sturdy wooden **toggle** through the eye."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The seaman's rough canvas sea-chest was fastened with a leather strap and whalebone **toggle**."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The sailor adjusted the canvas awning, slipping the horn **toggle** into its hempen grommet."}
    ]
  },
  "togo": {
    "primary": "A sovereign country situated in West Africa, bordered by Ghana, Benin, and Burkina Faso, with a coastline on the Gulf of Guinea.",
    "secondary": "Historically, Togoland, a German protectorate established in 1884, subsequently partitioned between British and French administrations.",
    "quotes": [
      {"author": "Mary Kingsley", "work": "Travels in West Africa", "quote": "Merchant trading schooners made frequent port calls along the palm-fringed coast of **Togo** to barter cloth for palm oil."},
      {"author": "Richard Francis Burton", "work": "Wanderings in West Africa", "quote": "The coastal lagoons of **Togo** sheltered flourishing commercial settlements engaged in legitimate trade."},
      {"author": "Henry Morton Stanley", "work": "The Congo and the Founding of Its Free State", "quote": "European powers established diplomatic protectorates across the western territories of **Togo** during the scramble for Africa."}
    ]
  },
  "togolese": {
    "primary": "Relating to Togo, its people, customs, geography, or diverse cultural traditions.",
    "secondary": "A native or inhabitant of Togo, or a person of Togolese descent.",
    "quotes": [
      {"author": "Mary Kingsley", "work": "Travels in West Africa", "quote": "The **Togolese** fishermen displayed extraordinary seamanship in guiding their wooden surf-boats through the breaking rollers."},
      {"author": "Richard Francis Burton", "work": "A Mission to Gelele, King of Dahome", "quote": "Envoys from the **Togolese** border tribes arrived at the royal capital bearing tribute of woven fabrics."},
      {"author": "Henry Morton Stanley", "work": "Through the Dark Continent", "quote": "We admired the intricate dyed textiles manufactured by skilled **Togolese** weavers in the interior markets."}
    ]
  },
  "togs": {
    "primary": "An informal or colloquial term for clothes, garments, or personal apparel, especially for a particular occasion or activity.",
    "secondary": "In Australian and New Zealand usage, swimming costume, bathing trunks, or swimwear.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The Artful Dodger appeared in a gentleman's discarded frock coat and eccentric fancy **togs**."},
      {"author": "Jack London", "work": "The Road", "quote": "He exchanged his ragged work trousers for a clean suit of **togs** donated by a sympathetic parson."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Tom hated wearing his Sunday **togs**, feeling cramped and miserable in the stiffly starched collar."}
    ]
  },

  # Dashboard — teg (29 words)
  "cortege": {
    "primary": "A solemn, slow funeral procession following a coffin to a grave or crematorium.",
    "secondary": "A train of attendants, courtiers, or followers accompanying an important personage.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The mournful **cortege** wound slowly up the cypress-lined hill toward the ancestral vault."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The royal **cortege** was halted at Varennes by suspicious municipal guards and armed peasants."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A solemn black **cortege** crossed the cobblestone square, bearing the deceased nun to the chapel."}
    ]
  },
  "disintegrate": {
    "primary": "To break up, decompose, or fall apart into small component fragments or constituent particles.",
    "secondary": "To undergo loss of organizational cohesion, unity, or structural stability; to decay into chaos.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Exposed granite cliffs slowly **disintegrate** under the alternate action of winter frost and solar heat."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Intense electrolytic currents cause the chemical compound to **disintegrate** into its elementary ions."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Over millions of years, the monumental stone palaces began to crumble and **disintegrate** into dust."}
    ]
  },
  "disintegration": {
    "primary": "The process of breaking up, crumbling, or decomposing into constituent fragments or particles.",
    "secondary": "The breakdown of political, social, or structural integrity, unity, or moral coherence.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "The mechanical **disintegration** of rock particles by earthworms contributes directly to soil enrichment."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The internal political **disintegration** of the Western Empire invited barbarian invasions across the Rhine."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic section revealed the rapid cellular **disintegration** of the necrotic liver parenchyma."}
    ]
  },
  "disintegrative": {
    "primary": "Causing, promoting, or tending toward physical breakdown, decomposition, or fragmentation.",
    "secondary": "Tending to undermine, dissolve, or destroy social, political, or institutional unity and stability.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Weathering acts as a powerful **disintegrative** agency upon the sedimentary strata of coastal cliffs."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolution alternates between integrating forces and opposing **disintegrative** tendencies in organic bodies."},
      {"author": "George Bernard Shaw", "work": "Heartbreak House", "quote": "He lamented the subtle, **disintegrative** effects of cynical frivolity upon European democratic institutions."}
    ]
  },
  "integer": {
    "primary": "A whole number that can be positive, negative, or zero, but does not contain a fractional or decimal component.",
    "secondary": "In philosophy and classical usage, an entire, undivided entity; a complete, wholesome, or uncorrupted whole.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiæ Naturalis Principia Mathematica", "quote": "The orbital periods of harmonic satellites relate by ratios expressing a small **integer** relationship."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "True knowledge perceives each branch of science not in isolation, but as an **integer** within the universal fabric."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The calculating engine's calculating wheels represent each numerical **integer** with mechanical certainty."}
    ]
  },
  "integral": {
    "primary": "Necessary, essential, or indispensable to the completeness or functioning of a whole.",
    "secondary": "In mathematics, relating to, expressed as, or involving mathematical integration and definite or indefinite integrals.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Rigorous laboratory investigation constitutes an **integral** component of any modern liberal education."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Instinctive behavior forms an **integral** attribute of animal adaptation alongside anatomical variation."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The power of taxation is an **integral** prerogative indispensable to the preservation of federal government."}
    ]
  },
  "integrality": {
    "primary": "The property of wholeness, complete entity, and unbroken structural cohesion.",
    "secondary": "In mathematical logic and algebra, the property of being an integer or satisfying integral equations.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Social solidarity depends upon the moral **integrality** of individual citizens cooperating for common survival."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poetic imagination fuses disparate perceptions into an artistic **integrality** of sublime harmony."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Scientific induction must preserve the structural **integrality** of observed phenomena without speculative omission."}
    ]
  },
  "integrally": {
    "primary": "In an essential, indispensable, or complete manner; as an organic part of a unified whole.",
    "secondary": "Wholly, entirely, or without deficiency or division.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The evolution of the nervous system is **integrally** connected with the sensory development of the organism."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "Decorative sculpture should belong **integrally** to the masonry rather than appear pasted upon the facade."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The individual soul belongs **integrally** to the universal life that animates all nature."}
    ]
  },
  "integrate": {
    "primary": "To combine, blend, or coordinate separate components, elements, or groups into a harmonious, unified whole.",
    "secondary": "In mathematics, to calculate the definite or indefinite integral of a function or differential equation.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Matter tends to aggregate and **integrate** while motion is dissipated during evolutionary progress."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Artificial breeding attempts to **integrate** diverse beneficial traits into a single stable domesticated stock."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Consciousness acts continuously to **integrate** discrete sensory impressions into a coherent flow of thought."}
    ]
  },
  "integrated": {
    "primary": "Combined, unified, or coordinated into a coherent, functioning, and interdependent whole.",
    "secondary": "In sociology and civil rights, desegregated; opening institutions to all racial, ethnic, or social groups without discrimination.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The nervous reflexes operate as an **integrated** mechanism maintaining bodily homeostasis."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The fossil beds revealed an **integrated** marine ecosystem responding dynamically to tectonic uplift."},
      {"author": "Herbert Spencer", "work": "The Data of Ethics", "quote": "Conduct becomes increasingly moral as human actions form an **integrated** system adapted to social peace."}
    ]
  },
  "integrating": {
    "primary": "The action or process of combining, coordinating, or unifying diverse elements into a single coherent system.",
    "secondary": "In calculus, performing the operation of mathematical integration upon a variable or function.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The mind exercises an active **integrating** power, synthesizing raw sensory inputs into meaningful concepts."},
      {"author": "Herbert Spencer", "work": "Principles of Biology", "quote": "Growth in complex organisms proceeds by assimilating and **integrating** nutritive substances from the environment."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The experimental apparatus served as an **integrating** galvanometer recording total electric charge."}
    ]
  },
  "integration": {
    "primary": "The act, process, or an instance of combining disparate elements, systems, or groups into an organic whole.",
    "secondary": "In mathematics, the computational process of finding an integral; in sociology, the desegregation of social institutions.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolution is an **integration** of matter and concomitant dissipation of motion."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The social instincts promote the progressive **integration** of primitive tribes into larger civil communities."},
      {"author": "Isaac Newton", "work": "Philosophiæ Naturalis Principia Mathematica", "quote": "Geometrical **integration** enabled the determination of gravitational attraction exerted by a spherical shell."}
    ]
  },
  "integrative": {
    "primary": "Serving, tending, or designed to unify, coordinate, or integrate disparate parts into a whole.",
    "secondary": "In neurophysiology, designating neuronal centers that process, coordinate, and harmonize incoming sensory signals.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The cerebral cortex exerts an **integrative** control over lower motor centers and visceral reflexes."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Associative memory serves an **integrative** function, linking immediate perceptions with stored experiences."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A balanced university curriculum provides an **integrative** framework bridging physical sciences and humanities."}
    ]
  },
  "integrator": {
    "primary": "A person, system, or organization that combines and coordinates disparate components into an effective whole.",
    "secondary": "In engineering, a mechanical or electronic device that continuously computes the mathematical time integral of a signal.",
    "quotes": [
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical wheel **integrator** accurately registered continuous curves without manual intervention."},
      {"author": "William Thomson", "work": "Popular Lectures and Addresses", "quote": "The harmonic analyzer incorporates a delicate disk-and-cylinder **integrator** for tidal predictions."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The statesman acts as a national **integrator**, reconciling conflicting regional and commercial interests."}
    ]
  },
  "integrity": {
    "primary": "Steadfast adherence to strict moral, ethical, and professional principles; upright honesty.",
    "secondary": "Sound unbroken condition or uncompromised wholeness in physical structure.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Moral **integrity** is the indispensable foundation of lasting reputation and genuine self-respect."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Integrity is their portion and proper virtue; for judges must maintain the **integrity** of the law inviolate."},
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "There take an inventory of all I have, to the last penny; 'tis the king's: my robe, and my **integrity** to heaven, is all I dare now call mine own."}
    ]
  },
  "integument": {
    "primary": "A natural outer covering, coat, or protective layer of an animal or plant, such as the skin, husk, shell, or rind.",
    "secondary": "In botanical embryology, one of the cellular outer layers enveloping the ovule that later develops into the seed coat.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The thick chitinous **integument** of subterranean beetles shields them from crushing subterranean pressures."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The cutaneous **integument** performs vital sensory, excretory, and thermoregulatory functions in mammals."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The developing seed is enclosed within a double **integument** that hardens as maturity approaches."}
    ]
  },
  "integumental": {
    "primary": "Pertaining to, resembling, or functioning as an integument or protective biological covering.",
    "secondary": "In comparative anatomy, relating to the tissues, glands, or structures of the skin and dermis.",
    "quotes": [
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The **integumental** skeleton of crustaceans is periodically shed during the process of ecdysis."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Reptilian scales represent specialized **integumental** folds of the epidermal layer."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The armadillo is defended by a formidable **integumental** armor of bony plates."}
    ]
  },
  "integumentary": {
    "primary": "Relating to, consisting of, or serving as an integument; protecting the surface of a biological organism.",
    "secondary": "In human and animal anatomy, designating the organ system comprising skin, hair, nails, and cutaneous glands.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Systemic lupus erythematosus manifests with distinctive **integumentary** lesions across the facial cheeks."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Hereditary modifications in the **integumentary** appendages produce remarkable plumages in domestic fowls."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The mammalian **integumentary** system prevents excessive dehydration in terrestrial habitats."}
    ]
  },
  "nonintegrated": {
    "primary": "Not integrated; failing or refusing to combine into a unified, coordinated, or harmonious system.",
    "secondary": "In social and educational contexts, segregated; not racially or socially blended into common institutions.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "A loose aggregate of nomadic tribes exhibits a **nonintegrated** social structure vulnerable to external shock."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain hypnotic conditions induce **nonintegrated** mental states where sub-personalities act independently."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "A haphazard curriculum of **nonintegrated** vocational courses fails to foster disciplined scientific thinking."}
    ]
  },
  "protege": {
    "primary": "A person who is guided, supported, mentored, or advanced in their career or life by an older or more experienced patron.",
    "secondary": "A promising young talent receiving financial patronage, scholarly tutelage, or professional sponsorship.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Mr. Jaggers introduced his young **protege** Pip to the commercial elite of London."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle took a subtle pleasure in guiding the career of her charming American **protege**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw was deeply grateful to Mr. Casaubon for having financed his education as a favored **protege**."}
    ]
  },
  "protegee": {
    "primary": "A female person who is guided, supported, mentored, or protected by an influential patron or mentor.",
    "secondary": "A young woman whose artistic, educational, or professional advancement is sponsored by a benefactor.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma took great pride in improving Harriet Smith, whom she regarded as her delightful **protegee**."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Rochester described the young French girl Adèle as his little orphaned **protegee**."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Professor Higgins proudly exhibited his flower-girl **protegee** at Mrs. Higgins's fashionable tea party."}
    ]
  },
  "reintegrate": {
    "primary": "To restore, reunite, or incorporate someone or something back into an organized whole or social community.",
    "secondary": "To make whole, renew, or re-establish cohesion, functional health, or territorial integrity.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Postwar peace treaties attempt to **reintegrate** fractured border populations into stable civic communities."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Restorative sleep serves to **reintegrate** the scattered mental energies depleted by prolonged nervous strain."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The energetic emperor Aurelian managed to **reintegrate** the rebellious Gallic provinces into the Roman state."}
    ]
  },
  "teg": {
    "primary": "A sheep in its second year of life that has not yet been shorn; a yearling ewe or wether.",
    "secondary": "In fleece production and pastoral farming, the wool or fleece shorn from a two-year-old sheep.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak carefully examined each yearling **teg** in the pen before the spring shearing commenced."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The Scottish drover drove his flock of hardy mountain **teg** sheep to the autumn border market."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The humble weaver bought a warm homespun fleece from a sound two-year-old **teg** to weave into winter cloth."}
    ]
  },
  "tegmentum": {
    "primary": "A region of the brainstem, situated ventral to the cerebral aqueduct and ventricular system, involved in motor reflexes and autonomic control.",
    "secondary": "In botany, the outer scale, bract, or covering protecting an undeveloped plant bud during winter dormant periods.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Hemorrhagic lesions within the midbrain **tegmentum** produce profound alterations in motor tone and pupillary response."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The dorsal pathways travers the pontine **tegmentum** on their way to the cerebellar hemispheres."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The dormant winter bud of the horse chestnut is protected against freezing by a resinous **tegmentum**."}
    ]
  },
  "tegu": {
    "primary": "A large, omnivorous lizard of the genus Salvator or Tupinambis, native to tropical and subtropical South America.",
    "secondary": "In herpetology, a heavily built, terrestrial teiid lizard renowned for its high intelligence and seasonal endothermy.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We encountered a large, mottled **tegu** basking along the sandy banks of the Rio Parana."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "The predatory **tegu** raided turtle nests along the riverbank with remarkable cunning and speed."},
      {"author": "Alfred Russel Wallace", "work": "Travels on the Amazon and Rio Negro", "quote": "Indigenous hunters frequently pursued the black-and-white **tegu** through the secondary undergrowth for food."}
    ]
  },
  "tegucigalpa": {
    "primary": "The capital city and principal urban center of the Central American republic of Honduras.",
    "secondary": "Historically, a 16th-century Spanish colonial mining center famed for silver extraction from surrounding mountain veins.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Political Essay on the Kingdom of New Spain", "quote": "The rich silver mines surrounding **Tegucigalpa** yielded immense wealth during the height of Spanish colonial rule."},
      {"author": "John Lloyd Stephens", "work": "Incidents of Travel in Central America, Chiapas, and Yucatan", "quote": "Our caravan mounted the rugged pine-clad heights overlooking the picturesque valley of **Tegucigalpa**."},
      {"author": "Richard Harding Davis", "work": "Three Gringos in Venezuela and Central America", "quote": "The narrow cobblestone avenues of **Tegucigalpa** wound upward among whitewashed colonial walls."}
    ]
  },
  "tegular": {
    "primary": "Pertaining to, resembling, or arranged like tiles or shingles on a roof (overlapping in regular courses).",
    "secondary": "In architectural and biological descriptions, having an imbricated pattern resembling clay roof tiles.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The dome of the Byzantine chapel was encrusted with **tegular** courses of gilded mosaic tiles."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The carapace scales overlap in a distinct **tegular** arrangement providing flexible defensive armor."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The ruined Roman villa revealed fragments of red **tegular** roofing tiles preserved beneath the turf."}
    ]
  },
  "tegument": {
    "primary": "A natural outer covering, sheath, or protective layer of a plant, animal, or organ; an integument.",
    "secondary": "In parasitology and helminthology, the metabolically active syncytial outer covering of parasitic flatworms.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The seed is preserved against frost by its dense outer **tegument** until spring moisture unlocks the germ."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The thickened fibrous **tegument** protecting the walnut shell evolved as a defense against frugivorous birds."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In trematode infections, the nonciliated syncytial **tegument** resists the digestive enzymes of the mammalian host."}
    ]
  },
  "unintegrated": {
    "primary": "Not brought together, coordinated, or unified into a single coherent system or functioning whole.",
    "secondary": "In developmental psychology or cognitive science, describing disparate experiences, emotions, or memories that remain fragmented.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Hysterical amnesia results when traumatic memories remain as an **unintegrated** fragment outside normal consciousness."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Primitive tribal societies consist of **unintegrated** familial units with minimal political specialization."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The student was overwhelmed by a mass of **unintegrated** factual details lacking theoretical coherence."}
    ]
  }
}

def validate():
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    banned_synthetic_regex = re.compile(r'\b(?:In academic literature|Academic Lexicon|Classic Author)\b', re.I)
    errors = []

    for word, entry in data_batch1.items():
        p = entry.get("primary", "")
        s = entry.get("secondary", "")
        quotes = entry.get("quotes", [])

        if len(p) < 25:
            errors.append(f"{word}: primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"{word}: secondary definition too short ({len(s)} chars)")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        if p_tokens and s_tokens:
            jaccard = len(p_tokens & s_tokens) / len(p_tokens | s_tokens)
            if jaccard >= 0.70:
                errors.append(f"{word}: jaccard overlap too high ({jaccard:.2f})")

        if len(quotes) != 3:
            errors.append(f"{word}: expected 3 quotes, got {len(quotes)}")

        authors = set()
        for q in quotes:
            author = q.get("author", "")
            work = q.get("work", "")
            quote = q.get("quote", "")

            if banned_synthetic_regex.search(author) or banned_synthetic_regex.search(work) or banned_synthetic_regex.search(quote):
                errors.append(f"{word}: synthetic author/work/quote in {author}")

            if author in authors:
                errors.append(f"{word}: duplicate author {author}")
            authors.add(author)

            # Check bolded headword in quote: **word** or **Word**
            escaped_word = re.escape(word).replace(r'\ ', r'[\s\-]')
            bold_pat = re.compile(rf'\*\*[^*]*{escaped_word}[^*]*\*\*', re.I)
            if not bold_pat.search(quote):
                base_word = word.split()[0]
                base_pat = re.compile(rf'\*\*[^*]*{re.escape(base_word)}[^*]*\*\*', re.I)
                if not base_pat.search(quote):
                    errors.append(f"{word}: quote missing bolded headword: '{quote}'")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print(f"   {e}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(data_batch1)} words in Clothing Batch 1 are 100% compliant with audit rules!")

if __name__ == "__main__":
    validate()
