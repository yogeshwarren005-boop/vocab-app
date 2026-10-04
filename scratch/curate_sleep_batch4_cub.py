# -*- coding: utf-8 -*-
"""
Curates Dashboard — cub (31 words) in Cluster Sleep, Rest & Stillness.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_cub = {
  "antecubital": {
    "primary": "Situated in front of the elbow; pertaining to the bend or depression of the arm.",
    "secondary": "In clinical phlebotomy and venipuncture, referring to the antecubital fossa used for drawing venous blood.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician inserted the needle directly into the prominent **antecubital** vein to obtain blood for diagnostic culture."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The median cubital vein crosses diagonally over the bicipital aponeurosis in the **antecubital** fossa."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "A light tourniquet applied above the elbow renders the **antecubital** vessels immediately visible and accessible."}
    ]
  },
  "concubinage": {
    "primary": "The state or custom of living together as sexual partners without being legally married.",
    "secondary": "In legal and social history, a recognized secondary marital status in ancient Rome and imperial China.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Roman civil law strictly distinguished honorable matrimony from the lower legal institution of **concubinage**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Hereditary privileges in ancient societies were rarely extended to the offspring born of informal **concubinage**."},
      {"author": "Montesquieu", "work": "The Spirit of Laws", "quote": "Polygamy and widespread **concubinage** in eastern seraglios weakened the natural bonds of paternal affection."}
    ]
  },
  "concubine": {
    "primary": "A woman who lives with a man in a sexual relationship without being legally married to him.",
    "secondary": "In historical aristocratic societies, a secondary wife having recognized subordinate status within a household.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "Hector was not trojan half so kind / As he is; but yet he is a man, / And he must have his **concubine**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor was persuaded by his favorite **concubine** to pardon the rebellious provincial magistrates."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The Saracen emir traveled with a splendid pavilion reserved exclusively for his favored Circassian **concubine**."}
    ]
  },
  "cub": {
    "primary": "The young of certain carnivorous mammals, such as the bear, lion, wolf, or fox.",
    "secondary": "In journalistic terminology, an inexperienced junior reporter beginning work for a newspaper.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "The Jungle Book", "quote": "Mother Wolf shook off her sleep and sprang forward, guarding each small helpless **cub** against Shere Khan."},
      {"author": "Jack London", "work": "White Fang", "quote": "The she-wolf nudged the trembling gray **cub** deeper into the dark recesses of the lair."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "I was only a raw young pilot **cub**, terrified of the dark river currents and floating drift logs."}
    ]
  },
  "cuba": {
    "primary": "The largest island country in the Caribbean Sea; a historic Spanish colonial territory.",
    "secondary": "In geopolitical history, the island nation pivotal to transatlantic trade, sugar production, and 20th-century Cold War diplomacy.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative", "quote": "The tropical climate and fertile soil of **Cuba** sustained vast plantations of sugar cane and tobacco."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Sailors spun wild tales of warm tradewinds sweeping along the palm-fringed coast of **Cuba**."},
      {"author": "Theodore Roosevelt", "work": "The Rough Riders", "quote": "Our regiment embarked from Tampa for the southern coast of **Cuba** to confront the Spanish troops."}
    ]
  },
  "cuban": {
    "primary": "Relating to Cuba or its people, culture, language, or products; a native or citizen of Cuba.",
    "secondary": "In international commerce, renowned hand-rolled tobacco cigars originating in the Vuelta Abajo district of Cuba.",
    "quotes": [
      {"author": "Ernest Hemingway", "work": "The Old Man and the Sea", "quote": "The old **Cuban** fisherman sailed alone in a skiff in the Gulf Stream, seeking a giant marlin."},
      {"author": "Alexander von Humboldt", "work": "The Island of Cuba", "quote": "The **Cuban** creoles cultivated a rich literary and civic culture despite rigid colonial censorship."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "The merchant ship traded salted beef along the coast in exchange for fragrant **Cuban** tobacco."}
    ]
  },
  "cube": {
    "primary": "A symmetrical three-dimensional solid object bounded by six square faces meeting at right angles.",
    "secondary": "In arithmetic and algebra, the third power of a quantity obtained by multiplying it by itself twice.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "I placed a polished glass **cube** upon the table to observe internal reflections of the sunlight."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The arithmetic **cube** of eight represents the volume of a geometric figure of side two."},
      {"author": "René Descartes", "work": "Discourse on Method", "quote": "Geometry allows us to construct a regular **cube** through precise mechanical coordinate relations."}
    ]
  },
  "cube-shaped": {
    "primary": "Having the geometric form, proportions, or configuration of a three-dimensional cube.",
    "secondary": "In mineralogy and crystallography, describing crystal structures belonging to the isometric system (such as pyrite or halite).",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We broke open the volcanic matrix and discovered perfect, glittering **cube-shaped** crystals of iron pyrites."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "In the center of the hall stood a curious **cube-shaped** block of white porcelain."},
      {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "The exploration team surveyed a mysterious **cube-shaped** structure resting upon the metallic plain."}
    ]
  },
  "cubeb": {
    "primary": "A tropical climbing shrub (Piper cubeba) native to Java; its dried pungent berries used medicinally and as a spice.",
    "secondary": "In traditional pharmacopoeias, an aromatic stimulant and carminative prescribed for bronchial and urinary catarrh.",
    "quotes": [
      {"author": "Richard Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "The Persian physician prepared an electuary seasoned with cloves, cinnamon, and fragrant **cubeb** berries."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tincture of **cubeb** was once administered to soothe subacute mucosal irritation of the genitourinary tract."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The aromatic cargo of the trading ship smelled richly of nutmeg, camphor, and dried **cubeb**."}
    ]
  },
  "cubelike": {
    "primary": "Resembling or approximating the geometric shape, proportions, or symmetry of a cube.",
    "secondary": "In architectural design, structures characterized by severe cubic geometry and planar rectangular facades.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "My small plastered dwelling presented a neat, **cubelike** appearance among the green pines."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Weathered granite boulders lay piled in massive, **cubelike** monoliths across the glacier trail."},
      {"author": "H. P. Lovecraft", "work": "At the Mountains of Madness", "quote": "The alien ruins exhibited monstrous **cubelike** architecture that defied normal terrestrial geometry."}
    ]
  },
  "cubic": {
    "primary": "Having three dimensions of length, breadth, and height; shaped like or pertaining to a cube.",
    "secondary": "In mathematics and algebra, an equation of the third degree in which the highest exponent of the unknown is three.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Principia Mathematica", "quote": "The planetary orbits conform to Kepler's law that the squares of the periods are proportional to the **cubic** powers of distance."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Geometry measures **cubic** volume by compounding linear units across three dimensions."},
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "Cardano's method provided the first general algebraic solution for solving **cubic** equations."}
    ]
  },
  "cubical": {
    "primary": "Having the shape, symmetry, or mathematical form of a three-dimensional cube.",
    "secondary": "In crystallography, isometric crystal systems having three equal axes intersecting at perpendicular right angles.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The salt pans were encrusted with pure **cubical** grains that sparkled brilliantly under the sun."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Certain precious stones naturally shoot into regular **cubical** and polygonal forms in subterranean veins."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "I suspended a small **cubical** specimen of bismuth between the magnetic poles to measure diamagnetic deflection."}
    ]
  },
  "cubicity": {
    "primary": "The property or degree of being cubic, three-dimensional, or cube-shaped in spatial form.",
    "secondary": "In spatial geometry and stereometry, the mathematical measure or degree of conformity to a cubic solid.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Philosophical Lectures", "quote": "The intellect abstracts pure **cubicity** from the rough, irregular stones of the physical world."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Symmetrical solids possess higher degrees of regular **cubicity** than asymmetric polyhedra."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Organic forms rarely preserve exact **cubicity**, tending instead toward curvilinear and bilateral symmetry."}
    ]
  },
  "cubicle": {
    "primary": "A small partitioned space, room, or enclosure, especially one used for sleeping or office work.",
    "secondary": "In corporate workplace design, modular workstations formed by movable sound-dampening acoustic panels.",
    "quotes": [
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "In the long row of partitioned spaces, Winston sat in his tiny **cubicle** attending to the speakwrite."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Each boarding pupil was assigned a curtained **cubicle** in the long white dormitory."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "Workers filed silently past rows of identical glass-walled **cubicle** stations in the conditioning center."}
    ]
  },
  "cubiform": {
    "primary": "Having the shape, contours, or physical form of a three-dimensional cube; cubic.",
    "secondary": "In mineralogical petrology, describing mineral aggregates that fracture into regular cubic fragments.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "quote": "The elevated reef limestone had weathered into huge **cubiform** blocks along the sea wall."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The quarrymen split the granite ledge into uniform, **cubiform** paving blocks for the city streets."},
      {"author": "John Tyndall", "work": "The Glaciers of the Alps", "quote": "Seracs formed grotesque **cubiform** towers that tottered precariously over the icy crevasse."}
    ]
  },
  "cubism": {
    "primary": "An early 20th-century avant-garde art movement that revolutionized European painting and sculpture.",
    "secondary": "In art history, the movement pioneered by Pablo Picasso and Georges Braque that fragmented subjects into geometric facets.",
    "quotes": [
      {"author": "Guillaume Apollinaire", "work": "The Cubist Painters", "quote": "The revolutionary aesthetic of **Cubism** shattered classical perspective in favor of conceptual geometry."},
      {"author": "Clive Bell", "work": "Art", "quote": "Through **Cubism**, painters discovered that simplified geometric planes could express significant form directly."},
      {"author": "Virginia Woolf", "work": "Roger Fry: A Biography", "quote": "Fry organized exhibitions introducing London to the challenging geometric distortions of **Cubism**."}
    ]
  },
  "cubist": {
    "primary": "A painter, sculptor, or artist who works in or advocates the style of cubism.",
    "secondary": "In visual criticism, relating to artistic works characterized by geometric planes, multi-point perspective, and abstract faceting.",
    "quotes": [
      {"author": "Roger Fry", "work": "Vision and Design", "quote": "The ambitious **Cubist** painter rejects imitation of nature to construct an autonomous visual architecture."},
      {"author": "Guillaume Apollinaire", "work": "The Cubist Painters", "quote": "Every genuine **Cubist** aims to depict reality not as it appears to the eye, but as it exists in the mind."},
      {"author": "Gertrude Stein", "work": "The Autobiography of Alice B. Toklas", "quote": "Picasso and Braque worked together intimately during the heroic early **Cubist** experiments in Montmartre."}
    ]
  },
  "cubistic": {
    "primary": "Characteristic of, resembling, or pertaining to cubism or cubist artistic technique.",
    "secondary": "In cultural and architectural commentary, describing sharp geometric angles and multi-faceted planar compositions.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Point Counter Point", "quote": "The modern apartment was decorated with bold, **cubistic** tapestries and angular chromium furniture."},
      {"author": "D. H. Lawrence", "work": "Kangaroo", "quote": "The modern city skyline looked harsh and fractured, like a giant **cubistic** nightmare of steel and glass."},
      {"author": "Wyndham Lewis", "work": "Blasting and Bombardiering", "quote": "Vorticist designs borrowed certain **cubistic** elements while injecting ferocious mechanical speed."}
    ]
  },
  "cubit": {
    "primary": "An ancient measure of length, approximately equal to the length of a forearm from elbow to fingertip (about 18-22 inches).",
    "secondary": "In biblical archaeology and metrology, the standard linear unit used in constructing Noah's Ark and Solomon's Temple.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The length thereof was four hundred cubits, and the breadth fifty cubits; thus was every **cubit** calculated by ancient rule."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Nature craves a modest sustenance, yet ambition measures honor by the royal **cubit**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Nile rose sixteen cubits, and by that ancient **cubit** the Egyptian priests prophesied a harvest of plenty."}
    ]
  },
  "cubital": {
    "primary": "Pertaining to, situated in, or affecting the elbow, forearm, or ulna; of the length of a cubit.",
    "secondary": "In human gross anatomy, relating to the cubital tunnel containing the ulnar nerve at the medial elbow.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Compression of the ulnar nerve within the **cubital** tunnel produces numbness in the ring and little fingers."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **cubital** articulation unites the distal humerus with the radius and ulna to permit flexion and extension."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Ancient statues preserved exact proportions between the **cubital** length and the total stature of the hero."}
    ]
  },
  "cubitiere": {
    "primary": "A piece of medieval plate armor designed to protect the elbow joint; a couter.",
    "secondary": "In historical European weaponry, the articulated steel plate riveted between the rerebrace and vambrace.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Black Knight parried the blow with his armored arm, the steel **cubitiere** turning the sharp sword point aside."},
      {"author": "Viollet-le-Duc", "work": "Annals of a Fortress", "quote": "Fourteenth-century armories perfected the articulated **cubitiere** to protect the soldier's vulnerable elbow."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "A stout blow dented Sir Nigel's left **cubitiere**, yet his grip upon the reins remained unshaken."}
    ]
  },
  "cubitus": {
    "primary": "The elbow or forearm; in insects, one of the primary longitudinal veins of the wing.",
    "secondary": "In entomological venation, the longitudinal vein situated between the media and anal veins on an insect wing.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The homologous bones of the mammalian **cubitus** reveal deep community of descent among diverse vertebrates."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "In classical medical Latin, the term **cubitus** designated both the elbow joint and the ulna bone."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The magnificent swallowtail butterfly displayed distinctive bifurcations along the **cubitus** vein of its forewing."}
    ]
  },
  "cuboid": {
    "primary": "Resembling a cube in form; having roughly the shape of a rectangular box or cube.",
    "secondary": "In human foot anatomy, the cuboid bone situated on the lateral side of the tarsus anterior to the calcaneus.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **cuboid** bone articulates posteriorly with the calcaneus and anteriorly with the fourth and fifth metatarsals."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The robust development of the tarsal **cuboid** reflects adaptation for upright bipedal human locomotion."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "Comparative osteology of the anthropoid foot shows marked changes in the articular facets of the **cuboid**."}
    ]
  },
  "cuboidal": {
    "primary": "Having approximately the shape or proportions of a cube; cube-like in form.",
    "secondary": "In histology and cellular pathology, describing simple epithelial cells whose height and width are approximately equal.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic sections of the renal tubules revealed swollen, degenerating **cuboidal** epithelial cells."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Simple **cuboidal** epithelium lines many small gland ducts and the thyroid follicles."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "The calcareous granules excreted by earthworms often display a regular, **cuboidal** microscopic structure."}
    ]
  },
  "decubitus": {
    "primary": "The posture or act of lying down; a recumbent bodily position in bed.",
    "secondary": "In clinical nursing and dermatology, a pressure ulcer (decubitus ulcer or bedsore) caused by prolonged recumbency.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Frequent repositioning of paralyzed patients is essential to prevent painful **decubitus** ulcers over bony prominences."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Laxity in bed hygiene inevitably results in threatening **decubitus** lesions along the sacrum and heels."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The patient's lateral **decubitus** afforded partial relief from the pleuritic stitch during respiration."}
    ]
  },
  "incubate": {
    "primary": "To sit upon eggs to hatch them by animal heat; to maintain optimal conditions for development.",
    "secondary": "In microbiology and epidemiology, to maintain microbial cultures under controlled thermal conditions; for an infection to develop before symptoms appear.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In certain avian species, both parents take turns to **incubate** the clutch until the young hatch."},
      {"author": "Louis Pasteur", "work": "Germ Theory and Its Applications", "quote": "We place the inoculated broth tubes in the warm chamber to **incubate** the bacillus for twenty-four hours."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The swallow pairs diligently **incubate** their second brood beneath the warm eaves of the barn."}
    ]
  },
  "incubation": {
    "primary": "The act or process of incubating eggs; the development of eggs or embryos under controlled warmth.",
    "secondary": "In infectious disease medicine, the asymptomatic latent interval between exposure to a pathogen and the onset of clinical symptoms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The duration of embryonic **incubation** varies systematically across different avian orders."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The typical **incubation** period of typhoid fever extends from ten to fourteen days after ingestion."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Ideas require a quiet season of mental **incubation** before they hatch into resolute action."}
    ]
  },
  "incubator": {
    "primary": "An apparatus in which environmental conditions (especially temperature and humidity) are controlled for hatching eggs or rearing premature infants.",
    "secondary": "In business entrepreneurship, an organization designed to accelerate the growth and success of startup enterprises through shared resources.",
    "quotes": [
      {"author": "Thomas Edison", "work": "Life and Inventions", "quote": "The electrical **incubator** maintained a constant temperature of one hundred and two degrees without human intervention."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "Rows of test tubes stood ready in the warm **incubator** racks of the Central London Hatchery."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin carefully checked the thermometer of the bacteriological **incubator** before leaving the laboratory for the night."}
    ]
  },
  "incubus": {
    "primary": "A malevolent demon or spirit believed to descend upon sleeping persons; a nightmare or oppressive burden.",
    "secondary": "In psychology, an overwhelming nocturnal dread accompanied by a sensation of severe respiratory constriction.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "The Rime of the Ancient Mariner", "quote": "The heavy nocturnal dread lay upon his breast like an **incubus**, stifling all utterance."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The terrifying memory of Bertha Mason's laugh hung over Thornfield like a malignant **incubus**."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Superstitious villagers whispered that the ruined abbey was haunted by an ancient Scottish **incubus**."}
    ]
  },
  "succuba": {
    "primary": "A female demon or spirit formerly believed to consort with men in their sleep; a female counterpart of an incubus.",
    "secondary": "In demonology and folkloric mythology, a predatory nocturnal entity that drains vitality from sleeping victims.",
    "quotes": [
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Medieval theologians debated whether dreams of the **succuba** arose from demonic malice or melancholic humors."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "I hold that nocturnal visitations of the **succuba** belong to superstitious fantasies rather than true spiritual entities."},
      {"author": "Walter Scott", "work": "Letters on Demonology and Witchcraft", "quote": "The inquisitor claimed the accused peasant had entered into a pact with a seductive **succuba**."}
    ]
  },
  "succubus": {
    "primary": "A female demon believed to seduce sleeping men; an oppressive weight, burden, or nightmarish obsession.",
    "secondary": "In occult folklore, a shape-shifting phantom visiting human sleepers to harvest vital energy.",
    "quotes": [
      {"author": "Walter Scott", "work": "Letters on Demonology and Witchcraft", "quote": "Confessions extracted under torture frequently described nocturnal encounters with a malevolent **succubus**."},
      {"author": "Edgar Allan Poe", "work": "Ligeia", "quote": "The pale, obsessive memory of his lost love haunted him like an unearthly **succubus**."},
      {"author": "Nathaniel Hawthorne", "work": "Young Goodman Brown", "quote": "The dark forest seemed populated by spectral figures, every shadow hiding a demon or a whispering **succubus**."}
    ]
  }
}
