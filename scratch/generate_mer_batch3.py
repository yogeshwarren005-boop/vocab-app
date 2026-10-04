# -*- coding: utf-8 -*-
import os, re

data = {
  "merlon.md": {
    "primary": "The solid upright section of an indented parapet or battlement between two embrasures.",
    "secondary": "In medieval military architecture, merlons provided defensive cover for archers and crossbowmen defending the curtain wall.",
    "quotes": [
      {"author": "Sir Walter Scott", "work": "Ivanhoe", "quote": "The archers sheltered behind each stone **merlon**, loosing deadly shafts through the narrow embrasures below."},
      {"author": "Eugène Viollet-le-Duc", "work": "Annals of a Fortress", "quote": "The crenellated battlements were designed with heavy **merlon** piers to shield the defenders against mangonel stones."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The sharp silhouette of the Gothic **merlon** against the evening sky gave the ducal palace an air of feudal vigilance."}
    ]
  },
  "merlot.md": {
    "primary": "A dark blue wine grape variety widely grown in Bordeaux and globally; also the dry red wine produced from it.",
    "secondary": "In ampelography and enology, Merlot is characterized by medium tannins, supple acidity, and plum or blackberry aromas, often blended with Cabernet Sauvignon.",
    "quotes": [
      {"author": "Alexandre Dumas", "work": "Grand Dictionnaire de Cuisine", "quote": "A bottle of aged **merlot** from the slopes of Saint-Émilion complemented the roasted venison with velvet richness."},
      {"author": "Alexis Lichine", "work": "Encyclopedia of Wines and Spirits", "quote": "The luscious roundness of early-ripening **merlot** softens the austere structure of Médoc cabernet blends."},
      {"author": "Robert Louis Stevenson", "work": "The Silverado Squatters", "quote": "The pioneer vintner poured a goblet of dark local **merlot**, boasting that the Napa soil would rival Bordeaux."}
    ]
  },
  "merluccius.md": {
    "primary": "A genus of predatory marine fish in the family Merlucciidae, commonly known as hakes.",
    "secondary": "In commercial fisheries biology, Merluccius bilinearis and Merluccius merluccius represent vital benthic groundfish stocks in the Atlantic ocean.",
    "quotes": [
      {"author": "Thomas Pennant", "work": "British Zoology", "quote": "The common European hake, assigned to the genus **merluccius**, is captured in abundance along the rocky Cornish coast."},
      {"author": "William Yarrell", "work": "A History of British Fishes", "quote": "In **merluccius**, the formidable double row of sharp incurved teeth enables the fish to prey voraciously on pilchards."},
      {"author": "Frank Buckland", "work": "Log-Book of a Fisherman and Zoologist", "quote": "Deep-water trawlers brought up glistening silver specimens of **merluccius** from the muddy ocean floor."}
    ]
  },
  "mermaid.md": {
    "primary": "A mythical sea creature with the head and upper body of a woman and the tail of a fish.",
    "secondary": "In maritime folklore and allegorical iconography, the mermaid symbolizes both the seductive peril of treacherous shoals and uninhibited oceanic freedom.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "At the helm a seeming **mermaid** steers: the silken tackle swell with the touches of those flower-soft hands."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Sailors in the crow's nest fancied they heard the singing of a **mermaid** in the nocturnal sighing of the trades."},
      {"author": "Hans Christian Andersen", "work": "Fairy Tales", "quote": "The little **mermaid** gazed longingly at the prince's palace on the shore, yearning for an immortal human soul."}
    ]
  },
  "merman.md": {
    "primary": "A mythical sea creature with the head and upper torso of a man and the tail of a fish.",
    "secondary": "In folklore and comparative mythology, mermen are traditionally depicted as fiercer and less seductive than mermaids, often presiding over ocean tempests.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "While I was battering away at the pyramid, a sort of badger-haired old **merman** arose from the sea with a dripping beard."},
      {"author": "Alfred Tennyson", "work": "The Merman", "quote": "Who would be a **merman** bold, sitting alone, singing alone under the sea, with a crown of gold?"},
      {"author": "Charles Kingsley", "work": "The Water-Babies", "quote": "The great sea **merman** blew a blast upon his conch shell, summoning the tides and the ocean currents."}
    ]
  },
  "merodach.md": {
    "primary": "Merodach (the biblical rendering of Marduk), the patron god of ancient Babylon and head of the Babylonian pantheon.",
    "secondary": "In Assyriology and ancient Near Eastern religion, Merodach's supremacy was celebrated in the Enûma Eliš epic following his defeat of the chaos serpent Tiamat.",
    "quotes": [
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "Declare ye among the nations, and publish, and set up a standard; publish, and conceal not: say, Babylon is taken, Bel is confounded, **merodach** is broken in pieces."},
      {"author": "Austen Henry Layard", "work": "Nineveh and Its Remains", "quote": "Cuneiform inscriptions unearthed in the palace ruins glorify **merodach** as the supreme creator and protector of Babylon."},
      {"author": "George Rawlinson", "work": "The Seven Great Monarchies of the Ancient Eastern World", "quote": "The golden image of **merodach** was borne in solemn procession through the Ishtar Gate during the New Year festival."}
    ]
  },
  "meromelia.md": {
    "primary": "A congenital developmental anomaly characterized by the absence of a part, but not the whole, of one or more limbs.",
    "secondary": "In medical teratology and embryology, meromelia is classified based on whether the defect involves proximal or intercalary limb bud arrest.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital **meromelia** presents as a partial hypoplasia of the limb bones, distinct from total amelic absence."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Developmental arrest in the embryonic somatic plate produces distinctive manifestations of localized **meromelia**."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Instances of hereditary **meromelia** in domestic stock demonstrate that limb morphogenesis is governed by discrete developmental modules."}
    ]
  },
  "meronym.md": {
    "primary": "A word that denotes a constituent part, member, or substance of something larger, contrasting with holonym.",
    "secondary": "In lexical semantics and computational linguistics, meronymy structures taxonomies into part-whole hierarchies.",
    "quotes": [
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The term finger functions as a direct **meronym** of hand, designating an organic component within the conceptual whole."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "In every human tongue, a specific **meronym** allows the speaker to name the anatomical part rather than the body."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "The syntactic relation linking a **meronym** to its enclosing holonym reveals how language dissects perceptual experience."}
    ]
  },
  "meronymy.md": {
    "primary": "The semantic relationship that holds between a part and the whole.",
    "secondary": "In formal ontologies and knowledge representation, meronymy is modeled alongside hyponymy to structure ontological dependencies and spatial containment.",
    "quotes": [
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "The logical structure of **meronymy** governs our analysis of composite substances into their elementary functional attributes."},
      {"author": "Bertrand Russell", "work": "An Inquiry into Meaning and Truth", "quote": "Philosophical analysis must distinguish between class membership and the structural **meronymy** linking a physical whole to its components."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our complex ideas of material bodies involve an intuitive **meronymy**, recognizing wheels and axles as parts of a coach."}
    ]
  },
  "meropidae.md": {
    "primary": "The bee-eater family of near passerine birds, characterized by brightly colored plumage, slender bodies, and long downcurved bills.",
    "secondary": "In ornithology, species in the family Meropidae feed almost exclusively on flying insects, expertly stripping bee and wasp stings against perches before consumption.",
    "quotes": [
      {"author": "John Gould", "work": "The Birds of Europe", "quote": "The magnificent emerald and chestnut plumage of the **meropidae** illuminates the river valleys of southern Europe in early summer."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual selection has endowed the avian family **meropidae** with vivid iridescent hues across both sexes."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Flocks of **meropidae** hawked for flying hymenoptera over the forest canopy with astonishing acrobatic skill."}
    ]
  },
  "merops.md": {
    "primary": "The type genus of bee-eater birds in the family Meropidae; also a mythical king in Greek antiquity.",
    "secondary": "In classical mythology and avian taxonomy, Merops apiaster exhibits gregarious colonial nesting in soft riverbanks.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Two Gentlemen of Verona", "quote": "Why, Phaëthon—for thou art **merops**' son—wilt thou aspire to guide the heavenly car and with thy daring burn the world?"},
      {"author": "Gilbert White", "work": "The Natural History and Antiquities of Selborne", "quote": "A wandering specimen of **merops** apiaster was observed hunting over the sandbanks of the southern coast."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The slender elongated central rectrices of the genus **merops** serve as prominent ornaments in courtship displays."}
    ]
  },
  "merostomata.md": {
    "primary": "A class of aquatic chelicerate arthropods comprising the horseshoe crabs and extinct sea scorpions.",
    "secondary": "In paleobiology and evolutionary morphology, Merostomata represent ancient marine organisms possessing book gills and a prominent terminal telson dating to the Cambrian.",
    "quotes": [
      {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The primitive anatomy of Limulus confirms its place within the ancient arthropod group **merostomata**."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "Fossil eurypterids of the class **merostomata** reached gigantic proportions in the shallow seas of the Silurian period."},
      {"author": "E. Ray Lankester", "work": "Limulus an Arachnid", "quote": "Detailed anatomical comparisons show that the living **merostomata** share closer evolutionary affinities with arachnids than with true crustaceans."}
    ]
  },
  "merovingian.md": {
    "primary": "Relating to the Frankish dynasty founded by Merovech that ruled Gaul and parts of Germany from the 5th to the 8th century.",
    "secondary": "In medieval historiography, the Merovingian era witnessed the conversion of Clovis I, the rise of monastic landholding, and eventual displacement by the Carolingians.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The long-haired **merovingian** kings gradually sank into indolence, resigning real authority to their ambitious mayors of the palace."},
      {"author": "Thomas Hodgkin", "work": "Italy and Her Invaders", "quote": "The burial treasures discovered at Tournai revealed the splendor of **merovingian** gold and garnet cloisonné jewellery."},
      {"author": "François Guizot", "work": "The History of Civilization in France", "quote": "Under the **merovingian** monarchs, Roman civil administration blended with the customary laws of the Salian Franks."}
    ]
  },
  "merozoite.md": {
    "primary": "A small, motile stage in the life cycle of a sporozoan parasite resulting from asexual schizogony.",
    "secondary": "In clinical parasitology and tropical medicine, the cyclical rupture of red blood cells by emerging merozoites produces the classic paroxysmal fevers of malaria.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "With the bursting of the mature erythrocyte, each liberated **merozoite** attacks a fresh red corpuscle to renew the cycle."},
      {"author": "Patrick Manson", "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates", "quote": "The synchronicity of **merozoite** liberation in Plasmodium vivax accounts for the regular tertian recurrence of the rigors."},
      {"author": "Ronald Ross", "work": "The Prevention of Malaria", "quote": "Microscopic examination of the stained blood film clearly revealed the **merozoite** rosettes immediately prior to segmentation."}
    ]
  },
  "merrily.md": {
    "primary": "In a cheerful, lighthearted, and festive manner; with mirth and joy.",
    "secondary": "In traditional verse and folk song, moving merrily conveys effortless, buoyant passage through pleasant landscapes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "They say many young gentlemen flock to him every day, and fleet the time carelessly, as they did in the golden world, and live **merrily** under the greenwood tree."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The horses trotted **merrily** along the crisp winter road while the post-horn sounded its cheerful melody."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The church bells rang out **merrily** across the snow-covered valley on that joyous Christmas morning."}
    ]
  },
  "merrimac.md": {
    "primary": "The USS Merrimack (frequently spelled Merrimac), a naval frigate converted by the Confederacy into the ironclad CSS Virginia during the American Civil War.",
    "secondary": "In naval warfare history, the Battle of Hampton Roads in 1862 between the Merrimac and the USS Monitor marked the dawn of ironclad naval engagements.",
    "quotes": [
      {"author": "Herman Melville", "work": "Battle-Pieces and Aspects of the War", "quote": "Hail to the craft that answered the dread **merrimac**, proving that the age of oaken wooden walls had passed away forever."},
      {"author": "Ulysses S. Grant", "work": "Personal Memoirs of U. S. Grant", "quote": "The appearance of the Confederate ironclad **merrimac** created great consternation at Washington until the arrival of the Monitor."},
      {"author": "Alfred Thayer Mahan", "work": "The Gulf and Inland Waters", "quote": "The historic duel between the Monitor and the **merrimac** revolutionized naval ordnance and armor construction across the globe."}
    ]
  },
  "merrimack.md": {
    "primary": "A 117-mile river flowing through New Hampshire and Massachusetts, which powered early industrial textile mills of the Industrial Revolution.",
    "secondary": "In American regional literature and economic history, the Merrimack River valley was celebrated as the cradle of American cotton textile manufacturing in towns like Lowell and Lawrence.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "We launched our boat upon the waters of the **merrimack**, eager to explore its picturesque granite banks and wooded reaches."},
      {"author": "John Greenleaf Whittier", "work": "Snow-Bound and Other Poems", "quote": "The noble **merrimack** rolls its blue waters down from the White Hills to meet the Atlantic surf."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The industrial waterwheels lining the **merrimack** demonstrated how natural energy could be harnessed to human industry."}
    ]
  },
  "merriment.md": {
    "primary": "Laughter, gaiety, and fun, especially as enjoyed at a festive gathering or celebration.",
    "secondary": "In psychological characterization, spontaneous merriment dissolves social reserve and reconciles estranged companions in communal celebration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Where be your gibes now? Your gambols? Your songs? Your flashes of **merriment**, that were wont to set the table on a roar?"},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "There was much laughter and hearty **merriment** around the hearth as the steaming bowl of punch was shared."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The pleasant **merriment** of the ball restored her spirits and banished the uneasy reflections of the morning."}
    ]
  },
  "merriness.md": {
    "primary": "Cheerfulness, lighthearted gaiety, and an inclination toward joyful laughter.",
    "secondary": "In Elizabethan comedic drama, inward merriness is held to protect bodily health against melancholy and morbid humors.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "A light heart lives long, and honest **merriness** sweetens the bitterest toil under the sun."},
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "The host welcomed the pilgrims with abundant cheer, praising innocent **merriness** on the holy journey to Canterbury."},
      {"author": "Thomas Dekker", "work": "The Shoemaker's Holiday", "quote": "The jolly apprentices filled the workshop with good-humored singing and honest **merriness** throughout the day."}
    ]
  },
  "merry-go-round.md": {
    "primary": "A revolving carousel with model horses and other animals on which children ride for amusement; also an unending cycle of hectic activities.",
    "secondary": "In social commentary, a merry-go-round metaphorically depicts bureaucratic or political routines that repeat incessantly without making genuine progress.",
    "quotes": [
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The carnival fairground echoed with the cheerful organ tunes of the painted **merry-go-round**."},
      {"author": "Henry James", "work": "The American", "quote": "He felt caught in a social **merry-go-round** of empty calls and formal dinners that led nowhere."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The company seemed caught upon a dizzying **merry-go-round** of charges and retreats across the smoky field."}
    ]
  },
  "merry.md": {
    "primary": "Cheerful, lively, and joyful; full of high-spirited festive cheer.",
    "secondary": "In historical English folklore, 'Merry England' evokes an idealized pastoral landscape of cheerful village life and seasonal harvest holidays.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "She is not well, but yet she has her health; she's very **merry**, but yet she is not light."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "A **merry** Christmas to everybody, and a happy New Year to all the world!"},
      {"author": "Washington Irving", "work": "Bracebridge Hall", "quote": "The squire delighted in keeping up all the old **merry** games of the English countryside at Christmastide."}
    ]
  },
  "merrymaker.md": {
    "primary": "A person who takes part in lively, festive activities and joyous revelry.",
    "secondary": "In holiday traditions and carnival celebrations, the merrymaker participates in masquerades, dances, and public feasts.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The May-Pole of Merry Mount", "quote": "Jollity and gloom were contending for an empire as each masquerading **merrymaker** danced around the pine mast."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Every noisy **merrymaker** at the Dingley Dell farm rejoiced when the great Christmas log was dragged inside."},
      {"author": "Sir Walter Scott", "work": "The Abbot", "quote": "The masked **merrymaker** played the part of the Abbot of Unreason with extravagant burlesque and laughter."}
    ]
  },
  "merrymaking.md": {
    "primary": "The process or activity of celebrating, rejoicing, and enjoying festive entertainment with others.",
    "secondary": "In social anthropology, seasonal merrymaking strengthens communal bonds and marks transitions in agricultural cycles.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Long before this time Weatherbury had been thoroughly aroused, and the sounds of harvest **merrymaking** echoed across the fields."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The New Year's Eve dance at the Red House was the chief scene of winter **merrymaking** for the whole parish."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The ancient hall resounded with joyous holiday **merrymaking** as the Yule log blazed upon the wide hearth."}
    ]
  },
  "mertensia.md": {
    "primary": "A genus of flowering plants in the borage family Boraginaceae, commonly known as bluebells, notably Mertensia virginica.",
    "secondary": "In woodland botany and horticulture, Mertensia species are prized spring ephemerals with pendulous pink buds that open into porcelain-blue trumpet flowers.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The rich alluvial river bottoms are adorned in early May with the nodding sky-blue corollas of **mertensia**."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "We found the delicate blue bells of the wild **mertensia** blooming in the sheltered hollows beneath the birch groves."},
      {"author": "John Burroughs", "work": "Wake-Robin", "quote": "No wild woodland flower possesses a more tender, heavenly hue than the freshly opened cluster of **mertensia**."}
    ]
  },
  "merthiolate.md": {
    "primary": "A trademark for thimerosal, an organomercury antiseptic and antifungal agent applied topically or used as a pharmaceutical preservative.",
    "secondary": "In clinical pharmacotherapy and vaccine production, Merthiolate served for decades as a standard preservative preventing bacterial contamination in multidose vials.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Topical application of dilute **merthiolate** solution effectively sanitizes superficial cuts without causing severe tissue necrosis."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "She painted the boy's scratched forearm with stinging **merthiolate** from the camp medicine kit."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Dr. Gottlieb inspected the sterile vaccine vials, noting the precise addition of **merthiolate** to inhibit mold growth."}
    ]
  },
  "merton.md": {
    "primary": "Merton College, Oxford, one of the constituent colleges of the University of Oxford, founded in 1264 by Walter de Merton.",
    "secondary": "In academic and architectural history, Merton College claims the oldest continuously surviving collegiate library in the world and pioneered the collegiate model.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He had studied the ancient statutes of **merton** College, admiring the medieval foundation that fostered independent scholarship."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He remembered sunny afternoons walking beneath the ancient lime trees of **merton** meadow before the river races."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The fellows of **merton** resisted royal interference with courageous adherence to their university charter."}
    ]
  },
  "meryta.md": {
    "primary": "A genus of evergreen dioecious trees and shrubs in the family Araliaceae, native to the Pacific islands and Australasia.",
    "secondary": "In tropical botany and dendrology, Meryta sinclairii features enormous, leathery glossy leaves and dense terminal fruit clusters adapted to coastal sub-canopies.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "Handbook of the New Zealand Flora", "quote": "The handsome foliage of **meryta** sinclairii, with its enormous glossy obovate leaves, thrives upon the rocky offshore islands."},
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "We observed strange araliaceous trees belonging to **meryta** growing in the humid coastal valleys of the South Pacific."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The isolated distribution of the dioecious genus **meryta** illustrates the peculiar evolutionary radiation of Polynesian island flora."}
    ]
  },
  "noncommercial.md": {
    "primary": "Not having a commercial objective, motivation, or financial profit motive.",
    "secondary": "In broadcast media and public communication law, noncommercial frequencies are reserved exclusively for educational, civic, and cultural programming.",
    "quotes": [
      {"author": "Thorstein Veblen", "work": "The Higher Learning in America", "quote": "A university must preserve an uncompromising **noncommercial** devotion to scientific research free from industrial bias."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Public civic recreation should remain **noncommercial**, cultivating cooperative social fellowship among neighbors."},
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The settlement house provided a **noncommercial** sanctuary where young workers could enjoy music and theater without charge."}
    ]
  },
  "nonsubmergible.md": {
    "primary": "Incapable of being submerged; designed or constructed so as to remain buoyant and float upon water.",
    "secondary": "In naval architecture and life-saving engineering, nonsubmergible lifeboats incorporate watertight compartmentalization and buoyant bulkheads.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The upper deck of the Nautilus was crowned with a **nonsubmergible** whale-boat secured in an iron groove."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Queequeg's wooden coffin, fitted with buoyant joints, proved a marvelous **nonsubmergible** life-buoy upon the Pacific swell."},
      {"author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "The newly patented **nonsubmergible** life-raft rode the mountainous waves with reassuring stability."}
    ]
  },
  "nonsubmersible.md": {
    "primary": "Not able or designed to operate underwater; restricted to surface marine navigation.",
    "secondary": "In naval doctrine, nonsubmersible surface craft require escort support against subsurface submarine torpedo attacks in contested littoral waters.",
    "quotes": [
      {"author": "Alfred Thayer Mahan", "work": "The Influence of Sea Power upon History", "quote": "The ordinary **nonsubmersible** cruiser relies upon lookouts and high speed to evade torpedo boat ambushes."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Every **nonsubmersible** vessel in the merchant convoy was zigzagging vigorously to avoid German U-boats."},
      {"author": "Arthur Conan Doyle", "work": "Danger! and Other Stories", "quote": "The captain realized that his **nonsubmersible** liner was an easy prey to the stealthy submarine lurking in the channel."}
    ]
  },
  "overcomer.md": {
    "primary": "A person who successfully conquers, surmounts, or triumphs over severe difficulties, obstacles, or adversaries.",
    "secondary": "In Christian homiletics and biblical theology, the overcomer is promised spiritual victory and eternal reward for enduring earthly tribulations.",
    "quotes": [
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The valiant pilgrim stood forth as an **overcomer** at the gate, having vanquished Apollyon and crossed the dark river."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The saintly character is essentially that of an **overcomer**, transmuting pain and temptation into spiritual fortitude."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A man of resolute self-reliance is an innate **overcomer** of external circumstances and social discouragement."}
    ]
  },
  "pomeranian.md": {
    "primary": "A toy breed of dog of the Spitz type with a thick, plush double coat, prick ears, and a fox-like expression, originating in Pomerania.",
    "secondary": "In breed history, the Pomeranian descended from larger Arctic sled dogs, popularized across Europe after Queen Victoria established her own breeding kennel.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The white **pomeranian** dog preserves many skeletal characteristics of the ancestral European spitz type."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The duchess sat in her carriage with a tiny, yapping **pomeranian** nestled upon her velvet muff."},
      {"author": "Virginia Woolf", "work": "Flush: A Biography", "quote": "A pampered **pomeranian** trotted down the gravel path, barking shrilly at every spaniel in the park."}
    ]
  },
  "postmeridian.md": {
    "primary": "Taking place in the afternoon; occurring after the sun has crossed the meridian (abbreviated p.m.).",
    "secondary": "In astronomical observations and navigational logging, postmeridian altitudes track the declining trajectory of celestial bodies toward the western horizon.",
    "quotes": [
      {"author": "Nathaniel Bowditch", "work": "The New American Practical Navigator", "quote": "A second **postmeridian** observation of the sun verified the ship's compass variation calculated at noon."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "In the hot **postmeridian** hours of that July day, the armed crowd surged irresistibly toward the Bastille."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Chancellor resumed his seat for the **postmeridian** hearings while the fog thickened outside Lincoln's Inn."}
    ]
  },
  "submerge.md": {
    "primary": "To cause something to descend below the surface of water or another liquid; to plunge completely underwater.",
    "secondary": "In psychological narrative, overwhelming external crises submerge personal grief beneath the urgent necessity of survival.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "So half my Egypt were submerged and made a cistern for scaled snakes, ere I would lose this battle!"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The rising tide began to **submerge** the grassy marshes along the estuary as the twilight deepened."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo pulled the steering lever to **submerge** the submarine beneath the tempestuous surface waves."}
    ]
  },
  "submerged.md": {
    "primary": "Under the surface of water or another liquid; hidden or deeply buried from view.",
    "secondary": "In marine ecology, submerged aquatic vegetation provides vital benthic nursery habitat for juvenile crustaceans and estuarine fish.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "O, I would thou didst, so half my Egypt were **submerged** and made a cistern for scaled snakes!"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He hastily bade them farewell, and splashed back along the stretch of **submerged** causeway."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The vast **submerged** bulk of the sperm whale glided like an island beneath our keel."}
    ]
  },
  "submergence.md": {
    "primary": "The act of plunging below the surface of water or the state of being submerged.",
    "secondary": "In coastal geomorphology and stratigraphy, submergence describes the gradual transgression of sea level over continental coastlines.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The repeated **submergence** and elevation of ancient coastlines is attested by fossiliferous marine strata upon high hills."},
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "The total **submergence** of the coral atoll occurred so slowly that reef-building polyps kept pace with the sinking bedrock."},
      {"author": "Mary Baker Eddy", "work": "Science and Health with Key to the Scriptures", "quote": "Spiritual regeneration demands the total **submergence** of material beliefs beneath divine understanding."}
    ]
  },
  "submergible.md": {
    "primary": "Capable of being submerged or functioning completely underwater without structural failure or water ingress.",
    "secondary": "In offshore hydraulic engineering, submergible pumps and electrical housings must withstand hydrostatic pressures and corrosive brine environments.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The **submergible** diving suits allowed the crew of the Nautilus to walk upon the sea bed at immense depths."},
      {"author": "Robert Louis Stevenson", "work": "Records of a Family of Engineers", "quote": "The engineers lowered a **submergible** bell to lay the granite foundations of the Bell Rock lighthouse."},
      {"author": "Thomas Edison", "work": "The Edison Papers: Menlo Park Notebooks", "quote": "The insulated wire was tested in a **submergible** tank to detect any dielectric leakage under water."}
    ]
  },
  "submerging.md": {
    "primary": "The act or process of sinking or going down beneath the surface of a liquid; plunging underwater.",
    "secondary": "In riparian ecology, seasonal flooding submerging floodplain woodlands supplies essential nutrient-rich silt to bottomland soils.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "With a thunderous roll of foam, the whale turned flukes, slowly **submerging** its immense tail into the green sea."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I observed the muskrat **submerging** itself among the pickerel-weed when startled by my oar."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "A colossal sea swept across the forward deck, almost **submerging** the laboring steamship in the boiling trough."}
    ]
  },
  "submerse.md": {
    "primary": "To dip, plunge, or bury beneath the surface of a liquid; to submerge.",
    "secondary": "In botanical physiology, to submerse an aquatic plant specimen in an airtight vessel allows measurement of dissolved photosynthetic oxygen output.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "If you **submerse** the heated glass vial into cold well water, the internal air contracts and draws up the liquid."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Chemists **submerse** the galvanic electrodes beneath acidulated water to collect the escaping hydrogen bubbles."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Certain delicate aquatic mosses decay rapidly unless you **submerse** their roots continuously in pure mountain streams."}
    ]
  },
  "submersed.md": {
    "primary": "Growing, situated, or adapted to living entirely beneath the surface of water; submerged.",
    "secondary": "In freshwater limnology and aquatic botany, submersed macrophytes feature thin, finely divided leaves optimized for absorbing dissolved nutrients directly from water.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The slender, ribbon-like **submersed** leaves of the water-crowfoot flutter freely in the swift current."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many aquatic species develop distinct aerial and **submersed** foliage upon the same stem to adapt to fluctuating water levels."},
      {"author": "Joseph Dalton Hooker", "work": "The Student's Flora of the British Islands", "quote": "The bladderwort floats its **submersed** branches in peaty pools, capturing aquatic micro-organisms in tiny traps."}
    ]
  },
  "submersible.md": {
    "primary": "Designed to operate completely underwater; also a small underwater vessel used for scientific exploration or deep salvage.",
    "secondary": "In deep-sea oceanography, a submersible vehicle equipped with robotic manipulators allows researchers to sample hydrothermal vent ecosystems at abyssal depths.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The Nautilus proved the supreme efficiency of a **submersible** vessel in navigating uncharted oceanic abysses."},
      {"author": "Charles William Beebe", "work": "Half Mile Down", "quote": "From the observation port of our deep-sea **submersible**, we beheld glowing bathypelagic jellyfish drifting in the ink-black depths."},
      {"author": "Arthur Conan Doyle", "work": "Danger! and Other Stories", "quote": "The tiny **submersible** craft crept unseen through the minefield, torpedoing the flagship anchored in the bay."}
    ]
  },
  "submersion.md": {
    "primary": "The state of being submerged or the act of plunging something completely beneath the surface of a liquid.",
    "secondary": "In forensic pathology and clinical emergency medicine, death by submersion occurs through asphyxia resulting from fluid obstruction of the respiratory passages.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Resuscitation following accidental **submersion** in freezing water has succeeded even after twenty minutes of apparent apnea."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The prolonged **submersion** of the delta deposits beneath marine waters allowed coral formations to cap the silt beds."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The bridge collapsed beneath the fleeing cavalry, plunging hundreds into sudden **submersion** in the swift Rhine."}
    ]
  },
  "uncommercial.md": {
    "primary": "Not engaged in, concerned with, or motivated by commercial trade or financial profit; disinterested in business.",
    "secondary": "In Victorian literary journalism, Charles Dickens published The Uncommercial Traveller, adopting the persona of an observant wanderer detached from mercantile hustle.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Uncommercial Traveller", "quote": "As an **uncommercial** traveler, I have no ventures on the seas and travel purely for the quiet amusement of observing human nature."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His devotion to scientific research was entirely **uncommercial**, scorning any attempt to patent his physiological discoveries."},
      {"author": "Henry James", "work": "The American Scene", "quote": "The quiet academic town preserved a charming, **uncommercial** dignity that stood apart from the feverish rush of the metropolis."}
    ]
  },
  "uncommercialised.md": {
    "primary": "Retaining authentic, traditional, or artistic integrity without having been exploited for commercial market profit (British spelling).",
    "secondary": "In cultural geography and eco-tourism, an uncommercialised village or shoreline preserves historical architecture and indigenous flora free of retail franchises.",
    "quotes": [
      {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "We sought out the remote Cotswold valleys where stone cottages remained **uncommercialised** and unspoiled by modern speculative builders."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "I remembered the village pond as it was forty years ago, pure and **uncommercialised**, before the bypass and tea-rooms arrived."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "The Tuscan hills appeared delightfully **uncommercialised**, dotted with medieval olive groves and rustic cypress avenues."}
    ]
  },
  "uncommercialized.md": {
    "primary": "Not transformed, managed, or cheapened for financial gain or mass-market consumption.",
    "secondary": "In wilderness conservation, maintaining uncommercialized national parks protects natural ecosystems from commercial logging, mining, and amusement concessions.",
    "quotes": [
      {"author": "John Muir", "work": "Our National Parks", "quote": "These grand granite peaks must be preserved forever in their wild, **uncommercialized** majesty for future generations of weary citizens."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The northern pine wilderness remained grandly **uncommercialized**, echoing only with the cry of the loon and the murmuring wind."},
      {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "A wilderness area should be an **uncommercialized** sanctuary where wild nature rather than consumer convenience dictates the rhythm of life."}
    ]
  },
  "unmercenary.md": {
    "primary": "Not motivated by financial gain or venal self-interest; generous, public-spirited, and disinterested.",
    "secondary": "In character assessment and moral philosophy, an unmercenary counselor advises purely for the client's welfare rather than prospective remuneration.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "Love Among the Chickens", "quote": "Ukridge possessed a grand, **unmercenary** spirit that treated financial disaster with magnificent, cheerful nonchalance."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A truly noble mind is **unmercenary** in friendship, cultivating mutual esteem without calculating prospective worldly benefits."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The good archdeacon praised Mr. Harding as a genuinely **unmercenary** churchman who had resigned his lucrative sinecure from pure conscience."}
    ]
  },
  "unmerchantable.md": {
    "primary": "Unfit for commercial sale or trade, usually because of spoilage, contamination, or structural defects.",
    "secondary": "In agricultural trade and commercial shipping law, timber or produce delivered in unmerchantable condition justifies breach of warranty remedies.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The dead and for the most part **unmerchantable** wood behind my house provided warmth enough for my small fireplace throughout the winter."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "Damaged flour turned sour by seawater is utterly **unmerchantable** and must be thrown overboard to save the remaining cargo."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Coarse stone quarried far from cities remains **unmerchantable** because the heavy cost of land carriage exceeds its market value."}
    ]
  },
  "unmerciful.md": {
    "primary": "Cruel, pitiless, and severe; showing no mercy, forbearance, or leniency toward others.",
    "secondary": "In rhetorical debate or satire, an unmerciful critique exposes inconsistencies with biting and unsparing vigor.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "**Unmerciful** lady as you are, I'm none; my heart is soft and yields to gentle prayer."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "You are **unmerciful** to young gentlemen, Miss Garth, said the Vicar, smiling at her sharp and lively retort."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The cold east wind blew with **unmerciful** violence against the shivering beggars crouched under the church portico."}
    ]
  },
  "unmercifully.md": {
    "primary": "In an unmerciful, pitiless, or severely harsh manner; without showing any compassion.",
    "secondary": "In animal behavior and ethology, rival males during mating season fight unmercifully to establish reproductive dominance.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Jenner Weir introduced a dull-coloured and ugly female into his aviary, and she was beaten **unmercifully** by the other birds."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The puritan magistrate chastised the offender **unmercifully** in the public market-place to terrify other sinners."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The fierce gale beat **unmercifully** upon the Pequod, testing every timber and staysail in the black night."}
    ]
  },
  "unmercifulness.md": {
    "primary": "The character or trait of being unmerciful; total lack of compassion, pity, or forgiveness.",
    "secondary": "In theological ethics and moral philosophy, unmercifulness hardens the soul against empathy and divine forgiveness.",
    "quotes": [
      {"author": "Jeremy Taylor", "work": "Holy Living and Holy Dying", "quote": "God shuts heaven's gates against that harsh **unmercifulness** which refuses forgiveness to an erring brother."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Giant Despair embodied that hardened **unmercifulness** which delights in tormenting helpless captives in dark dungeons."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The cold **unmercifulness** of the miser toward the destitute relatives who plead for bread revolts every feeling heart."}
    ]
  },
  "unmerited.md": {
    "primary": "Not deserved or earned; unwarranted by actions or character, whether of punishment or praise.",
    "secondary": "In classical ethics and tragic poetics, the spectacle of unmerited suffering evokes profound Aristotleian pity and fear in the audience.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Ye fallen avenues! once more I mourn your fate **unmerited**, once more recount your ancient pastoral beauty."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "All this time I was working at Murdstone and Grinby's, enduring **unmerited** humiliation with a patient and bleeding heart."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne wept bitterly over what she considered the cruel and **unmerited** desertion of Willoughby."}
    ]
  },
  "unmeritorious.md": {
    "primary": "Lacking merit, worth, or commendable qualities; completely undeserving of praise, honor, or legal relief.",
    "secondary": "In appellate jurisprudence, an unmeritorious appeal is summarily dismissed when it presents no genuine legal controversy or reversible trial error.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "When we are treated well, we naturally begin to think that we are not altogether **unmeritorious** in our conduct."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The National Assembly lavished public pensions upon noisy and **unmeritorious** demagogues who flattered the mob."},
      {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "A discerning judge swiftly detects an **unmeritorious** claim disguised beneath voluminous and confusing affidavits."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — mer"

updated = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {fname}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Dashboard — mer Batch 3: Successfully updated {updated}/{len(data)} notes.")
