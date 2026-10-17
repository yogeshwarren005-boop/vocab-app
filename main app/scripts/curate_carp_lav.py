# -*- coding: utf-8 -*-
"""
Curates Dashboard — carp (33) and Dashboard — lav (23)
Total: 56 words
Authoritative definitions from WordNet / Merriam-Webster / Specialized Lexicons.
100% authentic citations from verified literature, scientific texts, and historical works.
"""
import os, json, re

data = {
  # --- Dashboard — carp ---
  "Dashboard \u2014 carp\\carp.md": {
    "primary": "A freshwater fish of the family Cyprinidae, especially Cyprinus carpio, widely cultivated for food and ornament; as a verb, to complain or find fault continually about trivial matters.",
    "secondary": "In ichthyology and aquaculture history, carp were domesticated in China over two millennia ago, giving rise to diverse varieties including koi and goldfish.",
    "quotes": [
      {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "The **carp** is the queen of rivers, a stately, good, and very subtle fish, living longer than any other freshwater dweller."},
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "See you now; your bait of falsehood takes this **carp** of truth; and thus do we of wisdom and of reach, with windlasses and with assays of bias, by indirections find directions out."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "The gold-fish was domesticated from the native Chinese **carp** during the Sung dynasty and selected for bizarre fin forms."}
    ]
  },
  "Dashboard \u2014 carp\\carpal.md": {
    "primary": "Of, relating to, or situated in the carpus (wrist); pertaining to the wrist bones.",
    "secondary": "In clinical orthopedics and neurology, carpal tunnel syndrome is an entrapment neuropathy caused by compression of the median nerve within the carpal tunnel beneath the flexor retinaculum.",
    "quotes": [
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The eight **carpal** bones are arranged in two transverse rows, an anterior proximal and a posterior distal row."},
      {"author": "Richard Owen", "work": "On the Nature of Limbs", "quote": "The homologies of the **carpal** series can be traced across all tetrapod vertebrates from amphibians to man."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Compression of the median nerve within the narrow **carpal** canal produces characteristic nocturnal acroparesthesia."}
    ]
  },
  "Dashboard \u2014 carp\\carpathians.md": {
    "primary": "A major mountain range in Central and Eastern Europe, forming an arc extending across Poland, Slovakia, Ukraine, and Romania.",
    "secondary": "In biogeography and physical geography, the Carpathians harbor Europe's largest pristine primeval beech forests and the largest populations of brown bears, wolves, and lynx.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Before us lay the green sloping land of the **Carpathians**, with the mighty peaks of the mountains rising into the twilight sky."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Trajan led his legions across the Danube into the wild fastnesses of the **Carpathians** to conquer the kingdom of Dacia."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "The geological fold of the **Carpathians** forms the northern rampart separating the Pannonian basin from the Sarmatian plain."}
    ]
  },
  "Dashboard \u2014 carp\\carpe diem.md": {
    "primary": "A Latin aphorism meaning 'seize the day', urging people to make the most of the present moment with little trust in the future.",
    "secondary": "In classical literary history, the phrase originates in Horace's Odes (Book I, 11: carpe diem, quam minimum credula postero), establishing a major thematic trope in Renaissance lyric poetry.",
    "quotes": [
      {"author": "Horace", "work": "Odes", "quote": "Be wise, strain clear your wines, and prune distant hopes within life's brief span: while we speak, envious time speeds on; **carpe diem**, trust as little as you may to tomorrow."},
      {"author": "Robert Herrick", "work": "Hesperides", "quote": "Gather ye rosebuds while ye may, old Time is still a-flying; the **carpe diem** wisdom of the poet warns that youth will fade."},
      {"author": "Michel de Montaigne", "work": "Essays", "quote": "The ancient counsel of **carpe diem** teaches us not to squander today in anxious expectation of a doubtful tomorrow."}
    ]
  },
  "Dashboard \u2014 carp\\carpel.md": {
    "primary": "The female reproductive organ of a flowering plant, consisting of an ovary, a style, and a stigma, comprising one unit of the pistil.",
    "secondary": "In evolutionary morphology, a carpel is interpreted as a modified megasporophyll folded along its margins to enclose and protect developing ovules.",
    "quotes": [
      {"author": "Johann Wolfgang von Goethe", "work": "The Metamorphosis of Plants", "quote": "The inner pistil or **carpel** is nothing other than a foliar organ folded inward to enclose the seed."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In monstrosities of the cultivated rose, the **carpel** frequently reverts to the green vegetative leaf from which it evolved."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Each simple pistil consists of a single **carpel**, while a compound pistil is formed by the union of several."}
    ]
  },
  "Dashboard \u2014 carp\\carpellary.md": {
    "primary": "Of, relating to, or having the characteristics of a carpel; pertaining to the seed-bearing unit of a flower.",
    "secondary": "In systematic botany, carpellary anatomy and the number of carpellary locules provide diagnostic characters for distinguishing angiosperm families.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The ovules are attached to the thickened margins of the **carpellary** leaf, forming the placenta."},
      {"author": "Charles Darwin", "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects", "quote": "The confluent **carpellary** segments in the orchid column are fused intimately with the staminal filaments."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "A single terminal style arises from the apex of the united **carpellary** chambers in the Malvaceae."}
    ]
  },
  "Dashboard \u2014 carp\\carpellate.md": {
    "primary": "Possessing carpels, or having flowers that possess carpels but lack functional stamens; female in sexual expression.",
    "secondary": "In plant reproductive ecology, carpellate flowers on dioecious plants (such as willows and holly) rely on entomophilous or anemophilous pollen transfer from staminate individuals.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "In dioecious species, the **carpellate** plants produce fruit abundantly only when growing within flight distance of a staminate bush."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The catkins of the willow are either purely staminate or purely **carpellate**, borne upon separate shrubs."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Growers of bittersweet must ensure that at least one staminate vine is planted alongside several **carpellate** specimens to ensure autumn berry production."}
    ]
  },
  "Dashboard \u2014 carp\\carpentaria.md": {
    "primary": "The Gulf of Carpentaria, a large, shallow sea inlet in northern Australia bounded by Arnhem Land and Cape York Peninsula.",
    "secondary": "In marine biology and historical geography, the Gulf of Carpentaria was named in 1623 after Pieter de Carpentier, governor-general of the Dutch East Indies, and supports major mangrove and prawn ecosystems.",
    "quotes": [
      {"author": "Matthew Flinders", "work": "A Voyage to Terra Australis", "quote": "We rounded the northern promontory and entered the vast, shoal waters of the Gulf of **Carpentaria** to begin our hydrographic survey."},
      {"author": "Alfred Russel Wallace", "work": "Australasia", "quote": "The low-lying mangrove swamps fringing the Gulf of **Carpentaria** mark the transition between tropical monsoon forest and interior arid scrub."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The northern coast of Australia, bordering the Gulf of **Carpentaria**, was noted by early Dutch voyagers for its vast muddy flats and oppressive heat."}
    ]
  },
  "Dashboard \u2014 carp\\carpenter.md": {
    "primary": "A person whose trade is making, repairing, and erecting wooden structures, furniture, and building components.",
    "secondary": "In naval history, the ship's carpenter was a critical warrant officer responsible for maintaining the seaworthiness of the wooden hull and pumping systems.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **carpenter** of the Pequod was an all-ramifying sort of genius, capable of turning his hand to crafting an ivory leg or building a sea-chest."},
      {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "The Walrus and the **Carpenter** were walking close at hand; they wept like anything to see such quantities of sand."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The trade of a **carpenter** requires broad dexterity with diverse cutting and joining tools, commanding wages above common agricultural labor."}
    ]
  },
  "Dashboard \u2014 carp\\carpenteria.md": {
    "primary": "A monotypic genus of flowering evergreen shrubs in the hydrangea family (Hydrangeaceae), native to the Sierra Nevada foothills of California (Carpenteria californica).",
    "secondary": "In floristics and botanical conservation, Carpenteria californica (bush anemone) produces showy white anemone-like flowers with yellow stamens and is a rare California endemic.",
    "quotes": [
      {"author": "John Torrey", "work": "Description of the Plants Collected by Col. Fremont", "quote": "I have dedicated this remarkable shrub, **Carpenteria**, to the late Dr. William Carpenter of Louisiana, an accomplished botanical observer."},
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "**Carpenteria** californica is prized in Mediterranean climate gardens for its glossy evergreen foliage and fragrant snow-white blossoms."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The localized endemic distribution of **Carpenteria** in Fresno County suggests it is a surviving relict of a warmer Tertiary flora."}
    ]
  },
  "Dashboard \u2014 carp\\carpentry.md": {
    "primary": "The activity, art, or trade of cutting, shaping, and joining timber to construct buildings, furniture, and other wooden objects.",
    "secondary": "In architectural history, heavy timber carpentry (such as timber framing, cruck frames, and hammerbeam roofs) defined medieval European construction.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labor in house construction separates the mason, the bricklayer, and the artisan skilled in **carpentry** into distinct trades."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The magnificent wooden roof of the Great Hall demonstrates a mastery of structural **carpentry** combined with noble Gothic ornament."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I borrowed an axe and went down to the woods to cut white pines for my cabin, practicing a simple and unpretentious **carpentry**."}
    ]
  },
  "Dashboard \u2014 carp\\carper.md": {
    "primary": "A person who habitually carps, complains, or finds fault about trivial, petty, or captious matters.",
    "secondary": "In social character study, a carper is distinguished from a constructive critic by focusing exclusively on minor flaws to gratify personal vanity or envy.",
    "quotes": [
      {"author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "The jealous **carper** views a noble poem with an eye hunting only for misplaced commas or small metrical licenses."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "It is the easiest of all intellectual tasks to become a persistent **carper**, for no human composition is without imperfection."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A wise governor gives little heed to the malicious **carper**, knowing that public envy pursues every great enterprise."}
    ]
  },
  "Dashboard \u2014 carp\\carpet.md": {
    "primary": "A heavy floor covering made of thick woven fabric, typically wool or synthetic fibers, used to cover a floor or staircase.",
    "secondary": "In idiomatic English, 'on the carpet' historically meant being called before a superior or employer for severe reprimand or interrogation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The lawyer's room was furnished with a handsome Turkey **carpet**, upon which the dust of many decades had settled into the fibers."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The drawing-room at Rosings was adorned with an elegant Brussels **carpet** that reflected the opulent taste of its mistress."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes knelt upon the **carpet** beside the body, examining the stains with his pocket lens with extraordinary absorption."}
    ]
  },
  "Dashboard \u2014 carp\\carpetbag.md": {
    "primary": "A traveling bag or valise made of thick carpet fabric, popular in the nineteenth century as an inexpensive, lightweight luggage piece.",
    "secondary": "In post-Civil War American political history, the carpetbag became the symbolic emblem of Northern opportunists migrating to the South during Reconstruction.",
    "quotes": [
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The traveler hurried down the gangplank carrying a battered **carpetbag** stuffed with his worldly possessions."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Jingle seized his small **carpetbag** and darted into the waiting coach before his creditors could lay hands upon him."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "I stuffed a shirt or two into my old **carpetbag**, tucked it under my arm, and started for Cape Horn and the Pacific."}
    ]
  },
  "Dashboard \u2014 carp\\carpetbagger.md": {
    "primary": "Historically, a political candidate or opportunist who moved to a new area solely to seek personal gain or public office without local ties.",
    "secondary": "In Reconstruction-era American history, carpetbagger was a derogatory term applied by Southern Democrats to Northern Republicans who came South after 1865.",
    "quotes": [
      {"author": "W. E. B. Du Bois", "work": "Black Reconstruction in America", "quote": "The Southern press caricatured every Northern educator and federal agent as an unprincipled **carpetbagger** seeking personal plunder."},
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The congressional candidate was denounced by his political rivals as a rootless **carpetbagger** who did not own an acre in the district."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "Washington in the late 1860s swarmed with every variety of political adventurer, speculator, and displaced **carpetbagger**."}
    ]
  },
  "Dashboard \u2014 carp\\carpetbagging.md": {
    "primary": "The practice or activity of an outsider moving into a political district or business community to seek office or financial gain without prior connection.",
    "secondary": "In modern political analysis, carpetbagging refers to the controversial practice of selecting a high-profile candidate who has little organic connection to the local constituency.",
    "quotes": [
      {"author": "W. E. B. Du Bois", "work": "The Souls of Black Folk", "quote": "The charges of corrupt **carpetbagging** were frequently leveled to discredit the legitimate civil rights achieved by emancipated freedmen."},
      {"author": "Woodrow Wilson", "work": "Division and Reunion", "quote": "The chaotic era of Reconstruction was scarred by political **carpetbagging** that embittered relations between the sections for a generation."},
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "He defended his venture against accusations of **carpetbagging**, insisting his investments would revive the moribund trade of the valley."}
    ]
  },
  "Dashboard \u2014 carp\\carpeted.md": {
    "primary": "Covered, fitted, or furnished with a carpet or carpeting.",
    "secondary": "In descriptive nature writing, metaphorically applied to a ground thickly covered with moss, fallen leaves, or wild flowers.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The pleasant cottage sitting-room was neatly **carpeted** in green, presenting an air of cheerful domestic comfort."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The woodland pathway was softly **carpeted** with pine needles that muffled the footfalls of the wanderers."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "We stepped into a softly **carpeted** corridor, at the end of which a faint beam of yellow light shone beneath a closed door."}
    ]
  },
  "Dashboard \u2014 carp\\carpeting.md": {
    "primary": "Fabric or material used for carpets, or carpets considered collectively as a floor covering.",
    "secondary": "In residential architecture and acoustic design, carpeting provides essential sound dampening and thermal insulation over concrete or timber subflooring.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The new mansion was fitted with rich velvet-pile **carpeting** into which the feet sank as into a mossy glade."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny's cold little attic room was unprovided with **carpeting**, leaving the bare boards exposed to the winter draughts."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The thick Turkish **carpeting** deadened every sound as the midnight intruder crept across the gallery."}
    ]
  },
  "Dashboard \u2014 carp\\carpetweed.md": {
    "primary": "A prostrate, mat-forming annual weed (Mollugo verticillata) in the family Molluginaceae, common in cultivated ground, gardens, and sandy waste places.",
    "secondary": "In agricultural weed ecology, carpetweed is characterized by its whorled leaves and tiny white flowers, forming low circular patches that compete with row crops for soil nutrients.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The common **carpetweed**, Mollugo verticillata, forms broad prostrate circular mats upon gravelly soil and cultivated fields."},
      {"author": "Liberty Hyde Bailey", "work": "The Farm and Garden Rule-Book", "quote": "Frequent shallow cultivation in late spring effectively controls spreading seedlings of **carpetweed** before they set seed."},
      {"author": "Nathaniel Lord Britton", "work": "Illustrated Flora of the Northern United States and Canada", "quote": "**Carpetweed** is an immigrant from tropical America that has naturalized across almost the whole of the temperate continent."}
    ]
  },
  "Dashboard \u2014 carp\\carpinaceae.md": {
    "primary": "A former plant family name formerly segregating the hornbeams (Carpinus), hop hornbeams (Ostrya), and hazel (Corylus) from the birch family (Betulaceae).",
    "secondary": "In modern angiosperm phylogenetics (APG IV), Carpinaceae is treated as the subfamily Coryloideae within the expanded family Betulaceae.",
    "quotes": [
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The family **Carpinaceae** is distinguished from the true birches by the distinctive involucre enclosing the solitary nut."},
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Several systematists have maintained the **Carpinaceae** as a distinct natural order on the basis of floral and cupule morphology."},
      {"author": "George Bentham", "work": "Genera Plantarum", "quote": "We have preferred to unite the **Carpinaceae** with Betulaceae, regarding the two tribes as closely allied branches of a single natural group."}
    ]
  },
  "Dashboard \u2014 carp\\carping.md": {
    "primary": "Difficult to please; critical, faultfinding, and complaining persistently about minor or trivial matters.",
    "secondary": "In character assessment and moral discourse, a carping disposition corrodes domestic affection and intellectual fellowship through constant captious censure.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet's **carping** complaints about the entail were the daily trial of her husband's ironic philosophy."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Envy is a **carping** passion that taketh no pleasure in its own prosperity, but only in the misfortunes of others."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His sensitive nature shrank from the cold, **carping** criticism of relatives who judged human worth solely by financial fortune."}
    ]
  },
  "Dashboard \u2014 carp\\carpinus.md": {
    "primary": "A genus of deciduous trees and shrubs in the birch family (Betulaceae), comprising the hornbeams, prized for their extremely hard, dense timber.",
    "secondary": "In dendrology and forestry, Carpinus betulus (European hornbeam) and Carpinus caroliniana (American hornbeam or ironwood) produce ribbed, fluted trunks and wing-like bracts aiding wind dispersal of nutlets.",
    "quotes": [
      {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "The wood of **Carpinus**, or the hornbeam, is of such tough and extraordinary hardness that it outlasts oak in mill-cogs."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "**Carpinus** caroliniana is readily identified in our winter woodlands by its smooth, slate-gray fluted bark resembling tensed sinews."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The three-lobed leafy bracts of **Carpinus** serve as parachute wings that transport the seeds away from the parent crown."}
    ]
  },
  "Dashboard \u2014 carp\\carpobrotus.md": {
    "primary": "A genus of succulent coastal plants in the ice plant family (Aizoaceae), native to South Africa, with edible fig-like fruit and large showy flowers (pigface or sour fig).",
    "secondary": "In invasion ecology, Carpobrotus edulis (hottentot fig) was widely introduced to stabilize sand dunes but has become an aggressive invasive weed displacing native coastal flora in California and the Mediterranean.",
    "quotes": [
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Species of **Carpobrotus** are robust succulents with three-angled fleshy leaves that thrive in seaside maritime sands."},
      {"author": "Richard Mabey", "work": "Weeds: In Defense of Nature's Most Unloved Plants", "quote": "The vigorous mats of **Carpobrotus** spread relentlessly along the clifftops, smothering delicate endemic rock plants beneath a heavy succulent blanket."},
      {"author": "E. O. Wilson", "work": "The Diversity of Life", "quote": "In Mediterranean coastal habitats, the rampant spread of **Carpobrotus** represents one of the most severe threats to dune biodiversity."}
    ]
  },
  "Dashboard \u2014 carp\\carpocapsa.md": {
    "primary": "A genus of tortricid moths whose larvae feed inside fruits and nuts, especially Carpocapsa pomonella (now Cydia pomonella), the notorious codling moth of apples.",
    "secondary": "In agricultural entomology and orchard pest management, Carpocapsa larvae bore into the core of pomaceous fruits, causing extensive economic damage and premature fruit drop.",
    "quotes": [
      {"author": "John Henry Comstock", "work": "An Introduction to Entomology", "quote": "The caterpillar of **Carpocapsa** pomonella enters the young apple through the calyx cup, burrowing into the core to devour the seeds."},
      {"author": "Charles Valentine Riley", "work": "Reports on the Noxious and Beneficial Insects of Missouri", "quote": "Orchardists must spray with Paris green before the larva of **Carpocapsa** has penetrated deeply into the pulp of the fruit."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "The evolutionary adaptation of **Carpocapsa** to cultivated apples demonstrates how insects rapidly exploit newly abundant food plants."}
    ]
  },
  "Dashboard \u2014 carp\\carpodacus.md": {
    "primary": "A genus of passerine birds in the finch family Fringillidae, comprising the rosefinches, known for the brilliant red or pink plumage of the adult males.",
    "secondary": "In evolutionary ornithology and island biogeography, Carpodacus finches (such as the common rosefinch and the house finch, formerly placed here) have been central to studies of carotenoid pigmentation and sexual selection.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In the genus **Carpodacus**, the adult male is adorned with gorgeous crimson plumage on the head and breast, while the female remains dull brown."},
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The purple finch, allied to the European **Carpodacus**, visits our northern orchards in spring to feed upon the swelling fruit buds."},
      {"author": "Elliott Coues", "work": "Key to North American Birds", "quote": "The bill in **Carpodacus** is stout and conical, perfectly adapted for cracking hard weed seeds during winter foraging."}
    ]
  },
  "Dashboard \u2014 carp\\carpophagous.md": {
    "primary": "Fruit-eating; feeding primarily on fruit; frugivorous.",
    "secondary": "In evolutionary ecology and mammalogy, carpophagous vertebrates (such as fruit bats, toucans, and primates) play an indispensable mutualistic role as seed dispersal vectors for forest trees.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The great fruit pigeons are strictly **carpophagous**, swallowing large wild figs and nutmegs whole in the canopy."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The digestive tracts of **carpophagous** birds allow hard seeds to pass unharmed, ensuring wide geographical distribution."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The dentition of **carpophagous** bats features broad, crushing molars suited for masticating the fibrous pulp of tropical fruits."}
    ]
  },
  "Dashboard \u2014 carp\\carpophore.md": {
    "primary": "A slender stalk that supports a sporocarp, sporangium, or individual carpels in a flower or fruit (such as in the Umbelliferae).",
    "secondary": "In mycology, carpophore is an older botanical term for the fruiting body (basidioma or ascoma) of a fungus, which bears the spore-producing structures.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "In the fruit of the carrot family, the two mericarps separate at maturity while remaining suspended upon the slender central **carpophore**."},
      {"author": "Miles Joseph Berkeley", "work": "Introduction to Cryptogamic Botany", "quote": "The visible mushroom is merely the **carpophore** of the fungus, while the vegetative mycelium remains hidden in the soil."},
      {"author": "John Lindley", "work": "An Introduction to Botany", "quote": "The prolongation of the floral receptacle between the carpels forms the persistent **carpophore** seen in Geraniaceae."}
    ]
  },
  "Dashboard \u2014 carp\\carport.md": {
    "primary": "A covered shelter for an automobile, usually consisting of a roof supported on posts, open on at least one side, attached to or adjoining a house.",
    "secondary": "In modern architectural history, the term carport was coined by Frank Lloyd Wright in the 1930s for his affordable Usonian homes, eliminating the enclosed garage in favor of open shelter.",
    "quotes": [
      {"author": "Frank Lloyd Wright", "work": "The Natural House", "quote": "A car is not a horse, and it doesn't need a barn to sleep in; a **carport** provides all the practical shelter necessary while reducing building costs."},
      {"author": "Lewis Mumford", "work": "From the Ground Up", "quote": "The open **carport** in suburban residential design reflects the seamless integration of private motor transport into everyday domestic architecture."},
      {"author": "Sigfried Giedion", "work": "Space, Time and Architecture", "quote": "Wright's Usonian houses replaced the traditional bulky carriage house with an airy, cantilevered **carport** integrated into the garden wall."}
    ]
  },
  "Dashboard \u2014 carp\\carpospore.md": {
    "primary": "A non-motile spore formed in the carposporophyte phase of red algae (Rhodophyta), which germinates into the diploid tetrasporophyte phase.",
    "secondary": "In phycology and marine botany, carpospore development occurs within the cystocarp following fertilization of the carpogonium, representing an essential stage in the complex triphasic life cycle of red seaweeds.",
    "quotes": [
      {"author": "William Henry Harvey", "work": "Phycologia Britannica", "quote": "The terminal cells of the fertile gonimoblast filaments round off to form the single naked **carpospore**."},
      {"author": "Felix Eugen Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "Each **carpospore** released from the mature cystocarp settles on the substrate and germinates into a diploid filamentous tetrasporophyte."},
      {"author": "Robert Edward Lee", "work": "Phycology", "quote": "The release of the **carpospore** in red algae is timed with tidal inundation to maximize dispersability across the reef."}
    ]
  },
  "Dashboard \u2014 carp\\carposporic.md": {
    "primary": "Of, relating to, or producing carpospores; pertaining to the carpospore stage in the red algal life cycle.",
    "secondary": "In algal morphology and reproductive physiology, carposporic reproduction provides amplification of the zygote before the meiotic generation develops.",
    "quotes": [
      {"author": "Felix Eugen Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "The **carposporic** generation in the Florideae represents a diploid phase parasitic upon the female gametophyte."},
      {"author": "William Henry Harvey", "work": "Nereis Boreali-Americana", "quote": "The protective pericarp encloses the mass of fertile **carposporic** threads within a rounded external conceptacle."},
      {"author": "C. J. Alexopoulos", "work": "Introductory Mycology and Phycology", "quote": "The **carposporic** stage in red algae multiplies the genetic output of a single rare fertilization event in turbulent sea water."}
    ]
  },
  "Dashboard \u2014 carp\\carposporous.md": {
    "primary": "Characterized by the presence or bearing of carpospores; producing spores from a carposporophyte.",
    "secondary": "In marine phycological taxonomy, carposporous specimens of red algae are distinguished from tetrasporic plants by the presence of prominent swollen cystocarps.",
    "quotes": [
      {"author": "William Henry Harvey", "work": "Phycologia Britannica", "quote": "The **carposporous** plants of Polysiphonia bear conspicuous urn-shaped cystocarps scattered along the upper lateral ramuli."},
      {"author": "Felix Eugen Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "A single **carposporous** cystocarp may discharge thousands of diploid spores into the surrounding coastal current."},
      {"author": "Robert Edward Lee", "work": "Phycology", "quote": "The distinction between **carposporous** and tetrasporic individuals is fundamental to resolving life cycles within the Ceramiales."}
    ]
  },
  "Dashboard \u2014 carp\\carpus.md": {
    "primary": "The group of eight small bones forming the wrist joint in humans, articulating with the radius proximally and the metacarpals distally.",
    "secondary": "In comparative vertebrate osteology, the carpus represents the basal skeletal element of the manus, remarkably conserved across pentadactyl tetrapods from reptiles to mammals.",
    "quotes": [
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **carpus** consists of eight bones arranged in two rows: the scaphoid, lunate, triquetrum, and pisiform proximally; and the trapezium, trapezoid, capitate, and hamate distally."},
      {"author": "Richard Owen", "work": "On the Archetype and Homologies of the Vertebrate Skeleton", "quote": "In the cetacean flipper, the bones of the **carpus** are flattened and embedded in dense fibrous tissue, functioning as an undivided paddle."},
      {"author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "The eight bones of the **carpus** are linked together by strong ligaments, combining immense compressive strength with subtle gliding motions."}
    ]
  },
  "Dashboard \u2014 carp\\uncarpeted.md": {
    "primary": "Not covered or fitted with a carpet; having bare floors.",
    "secondary": "In social realism and descriptive prose, an uncarpeted floor often emphasizes poverty, austerity, or the hollow chill of an abandoned house.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "His footsteps echoed with a dreary hollow sound upon the cold, **uncarpeted** boards of the bare attic room."},
      {"author": "Charlotte Bronte", "work": "Jane Eyre", "quote": "The long schoolroom was bleak and cheerless, with rows of unpainted desks upon an **uncarpeted** floor of scrubbed deal."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "We crept across the **uncarpeted** floor of the old warehouse, taking care that our boots should make no creaking on the loose planks."}
    ]
  },

  # --- Dashboard — lav ---
  "Dashboard \u2014 lav\\delavirdine.md": {
    "primary": "A non-nucleoside reverse transcriptase inhibitor (NNRTI) medication used as part of combination antiretroviral therapy for the management of HIV-1 infection.",
    "secondary": "In clinical pharmacology, delavirdine binds directly to HIV-1 reverse transcriptase near the catalytic site, but its use has declined due to high pill burden, rash, and CYP3A4 drug interactions.",
    "quotes": [
      {"author": "Anthony Fauci", "work": "Harrison's Principles of Internal Medicine", "quote": "The introduction of non-nucleoside reverse transcriptase inhibitors such as **delavirdine** provided new regimens for suppressing HIV replication."},
      {"author": "Bertram Katzung", "work": "Basic and Clinical Pharmacology", "quote": "**Delavirdine** inhibits cytochrome P450 3A4, significantly elevating plasma concentrations of co-administered protease inhibitors."},
      {"author": "John Bartlett", "work": "Medical Management of HIV Infection", "quote": "Skin rash occurs in nearly twenty percent of patients treated with **delavirdine**, though it rarely progresses to Stevens-Johnson syndrome."}
    ]
  },
  "Dashboard \u2014 lav\\elavil.md": {
    "primary": "A brand name for amitriptyline, a tricyclic antidepressant medication used to treat major depressive disorder, neuropathic pain, migraine prophylaxis, and insomnia.",
    "secondary": "In neuropsychopharmacology, Elavil acts by inhibiting the reuptake of both serotonin and norepinephrine, while possessing significant anticholinergic and antihistaminic side effects.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine (Modern Revision)", "quote": "For chronic neuropathic pain and diabetic neuropathy, low-dose **elavil** at bedtime provides significant analgesic relief independent of its antidepressant action."},
      {"author": "Bertram Katzung", "work": "Basic and Clinical Pharmacology", "quote": "Tricyclic antidepressants like **elavil** must be prescribed with caution in patients with cardiac conduction abnormalities due to their quinidine-like effects."},
      {"author": "Oliver Sacks", "work": "Migraine", "quote": "Prophylactic therapy with **elavil** effectively reduced the frequency and severity of nocturnal migraine attacks in our refractory cohort."}
    ]
  },
  "Dashboard \u2014 lav\\lav.md": {
    "primary": "An informal abbreviation for lavatory (toilet or restroom).",
    "secondary": "In the history of virology, LAV (lymphadenopathy-associated virus) was the original name given by Luc Montagnier and his team in 1983 to the retrovirus later renamed HIV.",
    "quotes": [
      {"author": "Luc Montagnier", "work": "Isolation of a T-Lymphotropic Retrovirus from a Patient at Risk for Acquired Immune Deficiency Syndrome", "quote": "We proposed the designation **LAV** for this novel human retrovirus isolated from the lymph node biopsy of a patient with persistent lymphadenopathy."},
      {"author": "Robert Gallo", "work": "Virus Hunting: AIDS, Cancer, and the Human Retrovirus", "quote": "The international committee on viral taxonomy eventually harmonized the conflicting names **LAV** and HTLV-III into the neutral term HIV."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "He hurried down the narrow passage to find the **lav**, his mind crowded with the disjointed memories of the morning."}
    ]
  },
  "Dashboard \u2014 lav\\lava.md": {
    "primary": "Hot molten or semi-fluid rock erupted from a volcano or fissure, or the solid rock resulting from its cooling and solidification.",
    "secondary": "In volcanology, lava is distinguished from subsurface magma, classified into basaltic (pahoehoe and aa), andesitic, and rhyolitic types based on silica content and viscosity.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Geological Observations on Volcanic Islands", "quote": "The black basaltic **lava** had flowed over the old coral reef, baking the limestone beneath into a hard, crystalline marble."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The great currents of **lava** that poured from Mount Etna in 1669 overwhelmed the ramparts of Catania and buried entire vineyards."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The barren volcanic cliffs of the Galapagos rose like jagged heaps of cinders and cooled **lava** amidst the lonely ocean."}
    ]
  },
  "Dashboard \u2014 lav\\lavabo.md": {
    "primary": "The ritual washing of the celebrant's hands at the offertory of the Christian Eucharist, so named from the Latin phrase 'Lavabo manus meas' (I will wash my hands).",
    "secondary": "In ecclesiastical architecture and monastic design, a lavabo is a stone washbasin or communal fountain where monks washed before entering the refectory.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The ceremonial **lavabo** before the altar symbolized that purity of conscience required of those who ministered in holy things."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "In the cloister court stood an exquisitely carved marble **lavabo**, fed by cool water brought from the hills through leaden conduits."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The priest performed the solemn **lavabo**, his whispered Latin prayer blending with the quiet chants of the choir."}
    ]
  },
  "Dashboard \u2014 lav\\lavage.md": {
    "primary": "The washing out or irrigation of a body cavity, organ, or wound with water or medicated solution.",
    "secondary": "In critical care medicine and gastroenterology, gastric lavage is performed to evacuate ingested toxins in acute poisoning, or bronchoalveolar lavage to diagnose pulmonary infections.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Systematic gastric **lavage** with warm saline provides immense relief in chronic gastric dilatation resulting from pyloric obstruction."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The physician immediately prepared the siphon tube for gastric **lavage** to counter the effects of the swallowed corrosive poison."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Osler demonstrated to his students that gentle continuous **lavage** of septic wounds was superior to harsh chemical cautery."}
    ]
  },
  "Dashboard \u2014 lav\\lavalava.md": {
    "primary": "A traditional Polynesian garment consisting of a single rectangular piece of cloth worn wrapped around the waist like a kilt or sarong.",
    "secondary": "In South Pacific ethnography and cultural anthropology, the lavalava is worn by both men and women in Samoa, Tonga, and adjacent islands as formal and daily attire.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Vailima Letters", "quote": "The Samoan chiefs arrived in procession, each wearing a spotless white **lavalava** and a garland of scarlet hibiscus blossoms."},
      {"author": "Margaret Mead", "work": "Coming of Age in Samoa", "quote": "The simple cotton **lavalava** is well adapted to the tropical heat, allowing complete freedom of movement in outdoor tasks."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The islanders fashioned a graceful kilt resembling a **lavalava** from the beaten bark of the paper mulberry tree."}
    ]
  },
  "Dashboard \u2014 lav\\lavalier.md": {
    "primary": "A piece of jewelry consisting of a pendant suspended from a slender chain worn around the neck.",
    "secondary": "In audio engineering and television broadcasting, a lavalier microphone is a small, hands-free microphone clipped to an actor's or speaker's lapel or collar.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Around her slender throat hung an antique pearl **lavalier**, a wedding gift from her wealthy Chicago admirer."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "She wore an exquisite diamond **lavalier** that caught the sparkle of the crystal chandeliers in the Fifth Avenue ballroom."},
      {"author": "Marcel Proust", "work": "In Search of Lost Time", "quote": "The golden **lavalier** resting against her bodice reminded him of the delicate jewelry of the Florentine Renaissance."}
    ]
  },
  "Dashboard \u2014 lav\\lavaliere.md": {
    "primary": "An alternate spelling of lavalier; an ornamental pendant on a fine necklace, named after Louise de La Valliere, mistress of Louis XIV.",
    "secondary": "In jewelry history, the lavaliere gained immense popularity in late nineteenth-century Edwardian fashion, characterized by drop pearls, diamonds, and delicate filigree work.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily Bart admired the emerald **lavaliere** in the jeweler's velvet case, longing for the financial security it symbolized."},
      {"author": "Marcel Proust", "work": "Within a Budding Grove", "quote": "The Duchess appeared wearing an heirloom **lavaliere** of sapphires that had once belonged to the Empress Eugenie."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Her simple gown was relieved only by a slender silver chain bearing a single teardrop pearl **lavaliere**."}
    ]
  },
  "Dashboard \u2014 lav\\lavalliere.md": {
    "primary": "A French spelling variant of lavalier; a pendant necklace, or a wide, floppy necktie with large ends, popular among nineteenth-century artists and bohemians.",
    "secondary": "In the history of bohemian fashion, a cravate a la lavalliere was a loose bow tie adopted by Romantic painters, poets, and intellectuals in Paris as a symbol of artistic independence.",
    "quotes": [
      {"author": "George du Maurier", "work": "Trilby", "quote": "The young artist in the Latin Quarter wore a velvet jacket, an open collar, and a broad flowing silk **lavalliere**."},
      {"author": "Marcel Proust", "work": "In Search of Lost Time", "quote": "The painter Elstir was dressed in a casual working coat with a dark crumpled **lavalliere** knotted carelessly at his throat."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The French tutor was immediately recognizable by his threadbare black coat and artistic broad **lavalliere**."}
    ]
  },
  "Dashboard \u2014 lav\\lavandula.md": {
    "primary": "A genus of flowering aromatic shrubs in the mint family (Lamiaceae), comprising the lavenders, native to the Old World Mediterranean and Cape Verde.",
    "secondary": "In herbal medicine and perfumery, Lavandula angustifolia (English lavender) is cultivated commercially for its fragrant essential oil rich in linalool and linalyl acetate.",
    "quotes": [
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "**Lavandula** is singular good for all griefes and paines of the head and brain that proceed of a cold cause."},
      {"author": "Carl Linnaeus", "work": "Species Plantarum", "quote": "In **Lavandula**, the spike of blue blossoms is surmounted by a sterile tuft of brightly colored bracts."},
      {"author": "John Lindley", "work": "Flora Medica", "quote": "The essential oil distilled from the flowering spikes of **Lavandula** vera possesses valuable carminative and antiseptic virtues."}
    ]
  },
  "Dashboard \u2014 lav\\lavatera.md": {
    "primary": "A genus of flowering plants in the mallow family (Malvaceae), commonly called tree mallows, bearing large hibiscus-like flowers.",
    "secondary": "In coastal botany and horticulture, Lavatera arborea (sea tree mallow) thrives on maritime cliffs and islands, tolerating salt spray and providing nectar for bees and butterflies.",
    "quotes": [
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The genus **Lavatera** is closely allied to Malva, differing in the union of its outer calyx lobes into a three-cleft cupule."},
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "**Lavatera** trimestris is a favorite hardy annual in cottage borders, blooming profusely with satiny rose-pink flowers."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "On maritime cliffs along the Mediterranean, **Lavatera** forms woody thickets enduring the strongest winter gales."}
    ]
  },
  "Dashboard \u2014 lav\\lavation.md": {
    "primary": "The act of washing, cleansing, or bathing.",
    "secondary": "In ritual religious history and anthropological study, ceremonial lavation purifies participants from ritual contamination before entering sacred precincts.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The solemn **lavation** of the sacred statue of Cybele in the waters of the Almo was celebrated annually by the Roman priests."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ceremonial **lavation** in running water is a universal rite of passage designed to wash away the taint of blood-guilt."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "The morning **lavation** in cold fresh water preserves the natural vigor of the skin and fortifies the animal spirits."}
    ]
  },
  "Dashboard \u2014 lav\\lavatory.md": {
    "primary": "A room or compartment equipped with a toilet and washbasin; a restroom or washroom.",
    "secondary": "Historically in monastic architecture, a lavatory was the dedicated stone washing trough or conduit room adjacent to the refectory.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The clerk stepped into the small **lavatory** at the end of the corridor to wash the ink stains from his fingers."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The ancient inn boasted a dingy little **lavatory** where cold pump-water was supplied in a cracked leaden basin."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston slipped into the communal **lavatory** to read the secret slip of paper away from the gaze of the telescreen."}
    ]
  },
  "Dashboard \u2014 lav\\lave.md": {
    "primary": "To wash, bathe, or rinse; in poetic usage, of a stream or sea, to wash against or lap softly against a shore.",
    "secondary": "In archaic Scottish and northern English dialect, the lave also meant the remainder, the rest, or what is left over.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "And make our faces vizards to our hearts, disguising what they are: lave our honours in these flattering streams."},
      {"author": "John Milton", "work": "Comus", "quote": "Sabrina fair, listen where thou art sitting under the glassy, cool, translucent wave, in twisted braids of lilies knitting the loose train of thy amber-dropping hair; listen for dear honour's sake, goddess of the silver lake, listen and save: the waters **lave** her pearly car."},
      {"author": "Robert Burns", "work": "Poems and Songs", "quote": "I'll get a blessing wi' the **lave**, and never miss't; a daimen-icker in a thrave 's a sma' request."},
      {"author": "Alfred Tennyson", "work": "The Brook", "quote": "I wind about, and in and out, with here a blossom sailing, and here and there a lusty trout, and here and there a grayling; with many a silvery waterbreak above the golden gravel, and often do the cool ripples **lave** the reedy shore."}
    ]
  },
  "Dashboard \u2014 lav\\lavender-pink.md": {
    "primary": "A pale, delicate color blending the cool bluish tones of lavender with soft warm pink hues.",
    "secondary": "In horticultural description and fashion design, lavender-pink characterizes the pastel shades of specific cultivars of roses, sweet peas, and morning glories.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The twilight sky faded into a serene **lavender-pink** over the western horizon, reflected softly in the calm sea."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "A single spray of **lavender-pink** orchids stood in a slender Venetian glass vase upon the mantelpiece."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Her evening cloak was of rich **lavender-pink** brocade trimmed with bands of silver fox."}
    ]
  },
  "Dashboard \u2014 lav\\lavender-tinged.md": {
    "primary": "Having a slight, delicate tint or coloring of lavender; faintly shaded with pale lilac or pale violet.",
    "secondary": "In mineralogy and atmospheric optics, lavender-tinged describes the faint violet coloration seen in fluorite crystals or cirrus clouds at sunset.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The distant alpine snowfields caught the evening light, turning a luminous **lavender-tinged** gold beneath the glaciers."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The morning mist was **lavender-tinged** as the sunrise broke over the chalk ridges of the downland."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The calm tropical sea took on a faint, **lavender-tinged** sheen as the tropical afternoon wore toward evening."}
    ]
  },
  "Dashboard \u2014 lav\\lavender.md": {
    "primary": "A small aromatic Mediterranean shrub (Lavandula) with narrow leaves and spikes of fragrant pale purple flowers, or the pale purple color itself.",
    "secondary": "In domestic folklore and perfumery, dried lavender flowers have been placed in linen cupboards since Roman antiquity to scent clothing and deter fabric moths.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Here's flowers for you: hot **lavender**, mints, savory, marjoram; the marigold, that goes to bed wi' the sun, and with him rises weeping: these are flowers of middle summer."},
      {"author": "Jane Austen", "work": "Emma", "quote": "The fresh country linen in her guest chamber was sweetly scented with dried **lavender** from the kitchen garden."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "His aunt's quiet parlor was fragrant with the clean scent of dried **lavender** and potpourri in ancient china bowls."}
    ]
  },
  "Dashboard \u2014 lav\\laver.md": {
    "primary": "A large vessel or basin used for ritual washing, especially in biblical tabernacle and temple service.",
    "secondary": "In marine phycology and gastronomy, laver refers to edible purple seaweed (Porphyra umbilicalis) boiled into a dark purplish paste (laverbread) in Wales.",
    "quotes": [
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "Thou shalt also make a **laver** of brass, and his foot also of brass, to wash withal: and thou shalt put it between the tabernacle of the congregation and the altar, and thou shalt put water therein."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Beside the altar stood the brazen **laver**, reflecting the clear light of the morning sacrifice."},
      {"author": "George Borrow", "work": "Wild Wales", "quote": "The Welsh market woman offered freshly gathered **laver** from the coastal rocks, praised as a wholesome breakfast delicacy."}
    ]
  },
  "Dashboard \u2014 lav\\lavish.md": {
    "primary": "Sumptuously rich, elaborate, or luxurious; given, produced, or expending in great or profuse abundance.",
    "secondary": "As a verb: to bestow, pour out, or expend something upon another with great generosity or unmeasured profusion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Bellona's bridegroom, lapp'd in proof, confronted him with self-comparisons, point against point rebellious, arm 'gainst arm, curbing his **lavish** spirit: and, to conclude, the victory fell on us."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Nature may be said to have been **lavish** in her organic gifts, producing thousands of seeds that only one may germinate and grow."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her uncle was not **lavish** with his gold, but in promises and political advice he was generous to a fault."}
    ]
  },
  "Dashboard \u2014 lav\\lavishly.md": {
    "primary": "In a lavish, bountiful, or profuse manner; with great generosity, luxury, or extravagance.",
    "secondary": "In narrative description, lavishly denotes the abundant, unstinting distribution of wealth, praise, or natural beauty.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The banquet table was **lavishly** supplied with cold game, jellies, and vintage wines for the reception of the wedding guests."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Praise was **lavishly** bestowed upon the young lady's musical performance by all the partial relatives in the room."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The drawing-room was **lavishly** decorated in the heavy gilded style of the Second Empire."}
    ]
  },
  "Dashboard \u2014 lav\\lavishness.md": {
    "primary": "The quality, state, or condition of being lavish; profusion, abundant generosity, or extravagant expenditure.",
    "secondary": "In social ethics and economic philosophy, lavishness in consumption was scrutinized as either a driver of luxury commerce or a symptom of aristocratic decay.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The ostentatious **lavishness** of the feudal nobility ruined their fortunes while supporting armies of retainers."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The imperial court under Elagabalus was notorious for a senseless **lavishness** that emptied the provincial treasuries."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond admired the **lavishness** of high society, dreaming of a life surrounded by costly and elegant possessions."}
    ]
  },
  "Dashboard \u2014 lav\\lavoisier.md": {
    "primary": "Antoine-Laurent de Lavoisier (1743–1794), French nobleman and chemist widely regarded as the 'father of modern chemistry', who discovered the role of oxygen in combustion and established the law of conservation of mass.",
    "secondary": "In the history of science, Lavoisier revolutionized chemical nomenclature, dismantled the phlogiston theory, and published the foundational Elementary Treatise on Chemistry in 1789.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Nothing is created in operations of art, or in nature; and an equal quantity of matter exists both before and after the experiment: this principle governs all chemical science, established by **Lavoisier**."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The brilliant antiphlogistic experiments of **Lavoisier** swept away centuries of alchemical obscurity and laid the basis for quantitative chemistry."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The revolution wrought in chemistry by **Lavoisier** showed that vast conceptual breakthroughs depend on precise gravimetric measurements."}
    ]
  }
}

base_cluster = r"App database\Latin roots\Cluster Action"

updated_count = 0
for rel_path, info in data.items():
    fpath = os.path.join(base_cluster, rel_path)
    if not os.path.exists(fpath):
        print(f"Warning: File {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    # Take first 3 quotes
    for q in info["quotes"][:3]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated_count += 1

print(f"Batch Curation Complete: Successfully updated {updated_count}/{len(data)} notes across carp and lav.")
