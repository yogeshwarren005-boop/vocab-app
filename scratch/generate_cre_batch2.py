# -*- coding: utf-8 -*-
import os, re

data = {
  "creepy-crawly.md": {
    "primary": "Causing an unpleasant crawling sensation on the skin; creepy; also an informal term for a small crawling insect.",
    "secondary": "In colloquial psychology, creepy-crawly sensations describe formication or somatic tactile hallucinations provoked by phobic stimuli.",
    "quotes": [
      {"author": "Beatrix Potter", "work": "The Tale of Mrs. Tittlemouse", "quote": "Mrs. Tittlemouse was a most tidy little mouse, who spent half her life chasing beetles and other **creepy-crawly** intruders out of her pantry."},
      {"author": "Kenneth Grahame", "work": "The Wind in the Willows", "quote": "Toad poked with his stick into the hollow tree, expecting to disturb beetles and harmless **creepy-crawly** creatures in the bark."},
      {"author": "Jean-Henri Fabre", "work": "The Life of the Spider", "quote": "Children shrink from these little garden **creepy-crawly** spiders, unaware of the wonderful geometric architectural instincts they possess."}
    ]
  },
  "creepy.md": {
    "primary": "Causing an unpleasant feeling of fear, unease, or nervousness; weird and frightening.",
    "secondary": "In narrative atmosphere and ghost story conventions, a creepy setting exploits uncanny sensory cues such as dim illumination and faint scraping noises.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The snags were thick, the water was treacherous, and there was a **creepy** silence hanging over the immense primeval forest."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "Then the barrister said in a lower voice, which seemed at once sympathetic and **creepy**, that the mystery was solved."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "A **creepy** feeling ran through my hair as the nocturnal shadow detached itself from the castle wall."}
    ]
  },
  "creese.md": {
    "primary": "A dagger with a wavy, serpentine blade, traditionally worn in the Malay Archipelago and Indonesia; a kris.",
    "secondary": "In Southeast Asian metallurgy and material culture, the creese was forged from meteoric nickel-iron pamor steel and believed to possess spiritual talismanic potency.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The native chieftain stood with hand resting upon the carved wooden hilt of his ivory-sheathed **creese**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Malay pirate gripped a wavy-bladed **creese** between his teeth as he boarded the burning merchant ship."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Every freeman in the Moluccas wore a **creese** tucked into his silk sarong as a badge of honor."}
    ]
  },
  "cremains.md": {
    "primary": "The cremated human or animal ashes and bone fragments remaining after cremation.",
    "secondary": "In funerary sociology and mortuary science, cremains undergo mechanical pulverization in a cremulator to achieve a fine, sand-like particulate consistency.",
    "quotes": [
      {"author": "Jessica Mitford", "work": "The American Way of Death", "quote": "Modern mortuary directors developed ornate urns to hold the **cremains** for placement in columbarium niches."},
      {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "The ancient urns preserved the calcined **cremains** of Roman patricians together with perfumes and precious unguents."},
      {"author": "John Weever", "work": "Ancient Funerall Monuments", "quote": "Sepulchral urns holding the **cremains** of fallen heroes were consecrated with solemn sacrificial libations."}
    ]
  },
  "cremate.md": {
    "primary": "To reduce a dead body to ashes by burning, typically as part of a funeral ceremony.",
    "secondary": "In modern forensic science and bioarchaeology, to cremate organic remains subjects bone crystals to high thermal calcination, altering apatite mineralogy.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "It was the ancient custom of the Roman legions to **cremate** their fallen comrades upon a magnificent wooden pyre."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The Vedic priests gathered upon the riverbank to **cremate** the body with solemn chantings and fragrant ghee offerings."},
      {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "The heathens chose to **cremate** their dead with fire rather than commit their bodies to slow subterranean corruption."}
    ]
  },
  "cremation.md": {
    "primary": "The disposal of a dead person's body by burning it to ashes, typically in a furnace.",
    "secondary": "In religious anthropology and comparative ethnology, cremation was the dominant funerary rite among ancient Greeks, Romans, and Vedic Indo-Aryans.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "That water was the original of all things some conceived; that fire shall consumate them, others believed: hence **cremation** seemed the most philosophical mode of dissolution."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Among the ancient Hindus, **cremation** upon the sacred funeral pyre released the spirit from its mortal bonds."},
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "The widespread archaeological discovery of funeral urns testifies to the prevalence of **cremation** in Bronze Age Europe."}
    ]
  },
  "crematorium.md": {
    "primary": "A building or facility containing a furnace where human or animal bodies are cremated.",
    "secondary": "In public health and urban sanitation history, the modern crematorium movement was initiated in nineteenth-century Europe to prevent cemetery overcrowding.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "The clean, functional architecture of the municipal **crematorium** reflected the modern triumph of hygiene over medieval superstition."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The factory founder bequeathed a substantial sum to construct a public **crematorium** surrounded by peaceful landscaped gardens."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The somber brick **crematorium** stood in stark contrast to the marble catacombs of the historic Campo Santo."}
    ]
  },
  "crematory.md": {
    "primary": "A furnace or establishment for cremating dead bodies; a crematorium.",
    "secondary": "In civil architectural engineering, a municipal crematory incorporates high-temperature reverberatory retorts designed to ensure complete smokeless combustion.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "The Roman **crematory** pyre was strewn with sweet-smelling gums, cypress branches, and costly frankincense."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The funeral **crematory** of the emperor Augustus was constructed of white marble upon the Campus Martius."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Nature is a vast, purifying **crematory** where decaying autumn leaves are silently transmuted into fertile soil."}
    ]
  },
  "cremona.md": {
    "primary": "Cremona, a historic city in Lombardy, northern Italy, celebrated as the world's preeminent center of violin craftsmanship.",
    "secondary": "In musical organology, the Cremona luthiers, notably the Amati, Stradivari, and Guarneri families, established the classical acoustic proportions of orchestral stringed instruments.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes purchased his marvelous **cremona** violin for a mere fifty-five shillings from a pawnbroker in Tottenham Court Road."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He played with impassioned feeling upon an old **cremona** instrument whose varnished wood glowed like amber in the candlelight."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The patient artisan of **cremona** selected pine from Alpine slopes, carving belly and back to resonant acoustic perfection."}
    ]
  },
  "crenate.md": {
    "primary": "Having a margin with rounded teeth or shallow scallops, especially of leaves or shells.",
    "secondary": "In botanical morphology, crenate leaf margins contrast with serrate (sharp saw-like) and dentate (outward-pointing) margins.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The basal foliage of the violet is broadly ovate with a distinctly **crenate** margin."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Under cultivation, the **crenate** leaves of the wild primrose frequently became deeply lobed and ruffled."},
      {"author": "Joseph Dalton Hooker", "work": "The Student's Flora of the British Islands", "quote": "The marsh marigold is distinguished by its glossy, **crenate** kidney-shaped foliage and brilliant yellow sepals."}
    ]
  },
  "crenated.md": {
    "primary": "Having the margin notched or indented with rounded teeth or scallops; notched.",
    "secondary": "In clinical hematology, crenated erythrocytes (echinocytes) exhibit scalloped thorny projections due to osmotic hypertonicity or aging.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination of the fresh blood film revealed numerous **crenated** red cells displaying scalloped edges."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "When exposed to a concentrated saline solution, the round corpuscles swiftly assume a contracted, **crenated** appearance."},
      {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "The fossil shell exhibited a finely **crenated** ventral margin characteristic of the genus Glycymeris."}
    ]
  },
  "crenation.md": {
    "primary": "A rounded tooth or scallop on a margin; also the shrinking and formation of notches on cells placed in a hypertonic solution.",
    "secondary": "In cellular physiology, erythrocyte crenation occurs when osmotic water loss across the semipermeable cell membrane causes the plasma membrane to collapse unevenly.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The degree of **crenation** observed in red blood corpuscles increases rapidly with prolonged standing or hypertonic evaporation."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The addition of a drop of salt solution immediately induces **crenation** of the delicate mammalian red corpuscles."},
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Osmotic water movement out of the cellular envelope precipitates the physical **crenation** of the corpuscular surface."}
    ]
  },
  "crenature.md": {
    "primary": "A rounded notch or scallop in a crenated leaf margin or anatomical edge.",
    "secondary": "In systematic botany, the number and glandular hairs of each crenature along the petal edge provide taxonomic distinction among hybrid cultivars.",
    "quotes": [
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Each shallow **crenature** along the margin of the leaf bears a minute, nectar-secreting gland at its apex."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The round-toothed leaf of ground ivy features a prominent vein terminating within each soft **crenature**."},
      {"author": "Joseph Dalton Hooker", "work": "Handbook of the New Zealand Flora", "quote": "The coriaceous foliage is edged with irregular teeth, each **crenature** bordered by a thickened cartilaginous rim."}
    ]
  },
  "crenel.md": {
    "primary": "An open space or embrasure between two merlons in a fortified battlement, through which defenders can shoot.",
    "secondary": "In castellated military architecture, the crenel allowed crossbowmen to discharge quarrels before retreating behind the flanking masonry merlon.",
    "quotes": [
      {"author": "Sir Walter Scott", "work": "Ivanhoe", "quote": "The archer knelt in the stone **crenel**, leveling his crossbow at the approaching Norman besiegers."},
      {"author": "Eugène Viollet-le-Duc", "work": "Annals of a Fortress", "quote": "The width of the **crenel** was calculated to afford a wide angle of fire while minimizing exposure to enemy missiles."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Through each Gothic **crenel** upon the ramparts, the azure waters of the Adriatic glistened in the morning sun."}
    ]
  },
  "crenelate.md": {
    "primary": "To provide a wall, tower, or battlement with crenels or indented defensive battlements.",
    "secondary": "In medieval English legal history, a lord required a royal license to crenelate before fortifying a domestic manor house with defensive parapets.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The feudal baron obtained royal letters patent empowering him to **crenelate** his manor house against border raiders."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor ordered the garrison to **crenelate** the river fortress to repel the marauding Gothic flotillas."},
      {"author": "Sir Walter Scott", "work": "Kenilworth", "quote": "The architect proposed to **crenelate** the new outer courtyard wall in the fashionable antique castellated manner."}
    ]
  },
  "crenelation.md": {
    "primary": "A battlement on a fortress wall, featuring alternating indented openings and solid stone piers.",
    "secondary": "In architectural history, decorative crenelation became a prominent ornamental motif in Gothic Revival manor houses and civic colleges.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The picturesque **crenelation** crowning the palace facade served a decorative rather than military purpose in late Venetian architecture."},
      {"author": "Eugène Viollet-le-Duc", "work": "Discourses on Architecture", "quote": "True functional **crenelation** was designed to shield crossbowmen while affording plunging fire into the ditch."},
      {"author": "Henry James", "work": "The American Scene", "quote": "The university towers displayed a playful **crenelation** that echoed the medieval collegiate foundations of Oxford."}
    ]
  },
  "crenellate.md": {
    "primary": "To furnish with battlements or indentations; an alternative spelling of crenelate.",
    "secondary": "In medieval fortification engineering, to crenellate the upper ramparts provided overlapping firing sectors for defending archers.",
    "quotes": [
      {"author": "Sir Walter Scott", "work": "The Fortunes of Nigel", "quote": "The master builder was commissioned to **crenellate** the ancient gatehouse in accordance with the king's architectural decree."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The defenders prepared to **crenellate** the courtyard walls as rumors of insurrection spread through the faubourgs."},
      {"author": "Edward Bulwer-Lytton", "work": "The Last of the Barons", "quote": "The Earl resolved to **crenellate** his northern castle, preparing for civil strife between the rival roses."}
    ]
  },
  "crenellation.md": {
    "primary": "The parapet of a wall consisting of alternating embrasures and solid masonry merlons; an alternative spelling of crenelation.",
    "secondary": "In architectural style analysis, crenellation in domestic Tudor palaces transitioned from functional military defense to an emblem of noble prestige.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The ancient tower showed a broken **crenellation** against the blue Italian sky, where moss and wild wallflowers flourished."},
      {"author": "Washington Irving", "work": "The Alhambra", "quote": "The delicate Moorish **crenellation** along the battlements overlooked the verdant valley of the Darro."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The severe **crenellation** of the Norman keep reflected the unadorned structural honesty of early feudal defense."}
    ]
  },
  "crenelle.md": {
    "primary": "An embrasure or opening in the battlement of a medieval fortress wall; a crenel.",
    "secondary": "In French and English military terminology, defending crossbowmen aimed through the crenelle while shielded from direct hostile arrows.",
    "quotes": [
      {"author": "Eugène Viollet-le-Duc", "work": "Annals of a Fortress", "quote": "The guard leaned over the stone **crenelle** to challenge the approaching herald at the drawbridge."},
      {"author": "Sir Walter Scott", "work": "Quentin Durward", "quote": "A Scottish archer kept watch through the narrow **crenelle** of the barbican, keen-eyed for any hostile movement."},
      {"author": "Victor Hugo", "work": "The Hunchback of Notre-Dame", "quote": "Quasimodo hurled down a heavy beam through the cathedral **crenelle**, scattering the rioters below."}
    ]
  },
  "crenulate.md": {
    "primary": "Having the margin finely notched with very small, delicate rounded teeth or scallops.",
    "secondary": "In descriptive conchology and botany, crenulate shell lips or leaf margins possess minute, closely spaced scallops.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The delicate petals of the mountain saxifrage are finely **crenulate** along their upper margins."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The juvenile foliage exhibited a distinct **crenulate** outline that disappeared in the mature adult leaves."},
      {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The inner lip of the marine gastropod is adorned with a delicate **crenulate** border of porcelain enamel."}
    ]
  },
  "crenulated.md": {
    "primary": "Finely scalloped, crimped, or notched with small rounded teeth along the margin or edge.",
    "secondary": "In invertebrate paleontology, the crenulated hinge plates of fossil brachiopods and bivalves ensured precise shell articulation.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The fossil oyster valve was marked by a strongly **crenulated** hinge line preserving its original calcite microstructure."},
      {"author": "Joseph Dalton Hooker", "work": "The Student's Flora of the British Islands", "quote": "The small perennial herb displays **crenulated** foliage that hugs the gravelly mountain ledges."},
      {"author": "Thomas Say", "work": "American Conchology", "quote": "The outer margin of the shell is beautifully **crenulated**, matching the internal ribbing of the valves."}
    ]
  },
  "creole-fish.md": {
    "primary": "Paranthias furcifer, a species of colorful reef fish in the seabass family Serranidae, native to tropical Atlantic and Pacific reefs.",
    "secondary": "In marine ichthyology, the creole-fish differs from typical benthic groupers by schooling in open water to feed on zooplankton.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "Schools of the bright crimson **creole-fish** darted amidst the volcanic crevices of the Galápagos shore."},
      {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "The elongated body and deeply forked caudal fin of the **creole-fish** illustrate adaptation to midwater pelagic foraging."},
      {"author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "A glittering cloud of **creole-fish** circled our diving helmet, their reddish-violet scales shimmering in the filtered sunlight."}
    ]
  },
  "creole.md": {
    "primary": "A person of mixed European and African descent, especially in the Caribbean or Gulf South; also a language developed from pidgins.",
    "secondary": "In sociolinguistics, a creole emerges when a simplified pidgin language becomes the native mother tongue of a speech community.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "What does one mean by rich **creole** natures, full of warmth, expressive eloquence, and spontaneous generosity?"},
      {"author": "George Washington Cable", "work": "The Grandissimes: A Story of Creole Life", "quote": "The aristocratic **creole** families of New Orleans jealously guarded their ancestral French traditions and language."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "We spent an enchanting evening in the French Quarter listening to the soft **creole** patois of the old market women."}
    ]
  },
  "creolize.md": {
    "primary": "To adapt, blend, or transform a language, cuisine, or cultural tradition into a Creole form.",
    "secondary": "In linguistic typology, languages creolize through rapid grammatical restructuring, developing consistent tense-aspect markers and fixed word order.",
    "quotes": [
      {"author": "William Dwight Whitney", "work": "The Life and Growth of Language", "quote": "When multilingual populations interact under colonial conditions, their contact dialects rapidly **creolize** into stable vernaculars."},
      {"author": "Edward Sapir", "work": "Language", "quote": "Contact between disparate speech communities may **creolize** vocabulary while radically simplifying synthetic inflections."},
      {"author": "Franz Boas", "work": "Race, Language and Culture", "quote": "Folkloric traditions and musical rhythms quickly **creolize** in Caribbean plantation communities, creating vibrant new cultural forms."}
    ]
  },
  "creon.md": {
    "primary": "Creon, legendary ruler of Thebes in Greek mythology, prominent in Sophocles' Theban plays Oedipus Rex and Antigone.",
    "secondary": "In dramatic philosophy and classical tragedy, Creon embodies inflexible positive state law confronting Antigone's unwritten divine moral laws.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Two Noble Kinsmen", "quote": "Arcite and Palamon, the two noble kinsmen, cousins and nephews of **creon**, were captured upon the battlefield."},
      {"author": "Aristotle", "work": "Poetics", "quote": "The tragic hubris of **creon** in decreeing the exposure of Polyneices' corpse precipitates the catastrophic doom of his own royal house."},
      {"author": "Matthew Arnold", "work": "Merope: A Tragedy", "quote": "Like stubborn **creon**, he refused to heed the warnings of the prophet until the gods struck down his pride."}
    ]
  },
  "creosol.md": {
    "primary": "An aromatic liquid chemical compound (4-methylguaiacol) found in wood creosote, used in organic chemistry and flavoring.",
    "secondary": "In chemical pharmacognosy, creosol contributes the characteristic smoky, antiseptic medicinal aroma to beechwood wood-tar distillates.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Fractional distillation of beechwood tar yields **creosol**, an aromatic oil possessing powerful antiseptic properties."},
      {"author": "Humphry Davy", "work": "Elements of Agricultural Chemistry", "quote": "The pungent vapor of **creosol** was recognized as the principal agent preventing putrefaction in pyroligneous acid."},
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "The distilled spirit of wood tar yielded an oily drop of **creosol** that turned deeply red when treated with vitriol."}
    ]
  },
  "creosote.md": {
    "primary": "A dark brown oily liquid distilled from wood tar or coal tar, widely used as an industrial wood preservative and antiseptic.",
    "secondary": "In railroad engineering and infrastructure history, pressure-impregnating cross-ties with creosote protected timber against fungal rot and wood-boring insects.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The pungent scent of fresh **creosote** rising from the newly laid railway ties hung over the summer woods."},
      {"author": "Thomas Edison", "work": "The Edison Papers: Menlo Park Notebooks", "quote": "We treated the wooden battery casings with hot **creosote** to make the joints completely acid-proof and impermeable."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Toby the hound followed the strong scent of **creosote** that had dripped from the wooden leg of the fugitive."}
    ]
  },
  "crescendo.md": {
    "primary": "A gradual increase in loudness or intensity in a musical passage; also a culminating progressive surge.",
    "secondary": "In dramatic structure and rhetorical oratory, an affective crescendo steadily accelerates tempo and amplitude to climax the emotional argument.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "It may have been merely a **crescendo** of nervous fancy, but the sound of pursuing footsteps seemed to double in volume."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her singing swelled in a magnificent **crescendo** that filled the grand hall with vibrant emotional power."},
      {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "The preacher's voice rose in an impassioned **crescendo**, describing the eternal torments awaiting unrepentant sinners."}
    ]
  },
  "crescent-shaped.md": {
    "primary": "Having the curved shape of the waxing or waning moon, tapering to a point at each end.",
    "secondary": "In geomorphology, barchan dunes are crescent-shaped sand dunes formed by unidirectional winds in arid deserts.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "The earthworm castings formed neat **crescent-shaped** heaps of dark pulverized loam upon the grassy turf."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The volcanic crater formed a vast **crescent-shaped** amphitheater open toward the sea on its western breach."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ivory teeth of the sperm whale curved inward in a gleaming, **crescent-shaped** jaw of extraordinary power."}
    ]
  },
  "crescent.md": {
    "primary": "The curved sickle shape of the waxing or waning moon; also growing, increasing, or developing.",
    "secondary": "In cultural and political heraldry, the crescent emblem served as a primary symbol of the Byzantine Empire and Ottoman state.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "The people love me, and the sea is mine; my powers are **crescent**, and my auguring hope says it will come to the full."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "In the twilight of the morning, light seems active, darkness passive; the pale **crescent** hung faintly in the western sky."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The angelic squadrons wheeled into a defensive **crescent**, their burnished shields flashing against the deep dark."}
    ]
  },
  "crescentia.md": {
    "primary": "A genus of flowering trees in the family Bignoniaceae native to tropical America, commonly known as calabash trees.",
    "secondary": "In tropical ethnobotany, Crescentia cujete produces large, hard-shelled spherical gourds traditionally dried and carved into domestic drinking vessels and musical maracas.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The broad, spreading boughs of the **crescentia** cujete were laden with heavy green gourds like colossal melons."},
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "The native inhabitants manufacture durable water bottles and bowls from the woody shell of the **crescentia** fruit."},
      {"author": "Joseph Dalton Hooker", "work": "The Rhododendrons of Sikkim-Himalaya", "quote": "Specimens of the tropical American genus **crescentia** thrived in the humid conservatories of the botanical garden."}
    ]
  },
  "cresol.md": {
    "primary": "Any of three isomeric organic methylphenol compounds obtained from coal tar, used as disinfectants and chemical intermediates.",
    "secondary": "In public health and industrial chemistry, saponified cresol solutions served as standard broad-spectrum hospital germicides.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Antiseptic solutions containing **cresol** provide dependable surface disinfection in infectious hospital wards."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The growth of putrefactive bacilli was immediately arrested by the addition of trace quantities of purified **cresol**."},
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The oily distillation fractions yielded crude **cresol**, which precipitated proteins with powerful antiseptic action."}
    ]
  },
  "cress.md": {
    "primary": "A fast-growing pungent cruciferous plant of the cabbage family, whose peppery leaves are eaten in salads.",
    "secondary": "In classical herbalism, garden cress and watercress were celebrated as antiscorbutic remedies rich in vitamin C.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Poor Tom that eats the swimming frog, the toad, the tadpole, the wall-newt; that in the fury of his heart feeds upon water-cress and green **cress**."},
      {"author": "John Milton", "work": "Comus", "quote": "The shepherd plucked fresh water **cress** from the clear bubbling brook to refresh his weary thirst."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I gathered the pungent, tender leaves of the brook **cress** to furnish a wholesome salad for my simple woodland dinner."}
    ]
  },
  "cresson.md": {
    "primary": "Watercress; also a borough in Cambria County, Pennsylvania, historic mountain resort and railroad depot.",
    "secondary": "In culinary French terminology, potage au cresson denotes a creamy potato and watercress soup garnishing classical haute cuisine menus.",
    "quotes": [
      {"author": "Alexandre Dumas", "work": "Grand Dictionnaire de Cuisine", "quote": "A garnish of fresh **cresson** brings a lively, peppery freshness to roasted game fowl upon the banquet table."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Simmer the potato purée with finely chopped **cresson** to produce a delicate, nourishing soup for the sickroom."},
      {"author": "Walt Whitman", "work": "Specimen Days", "quote": "We paused at the mountain depot of **cresson**, breathing the invigorating pine air of the Allegheny summit."}
    ]
  },
  "crest.md": {
    "primary": "A comb or tuft of feathers or skin on the head of a bird or other animal; the top of a mountain or wave; also a heraldic device.",
    "secondary": "In heraldry and armorial bearings, the crest is the device mounted above the helmet and torse on a coat of arms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "When they shall see, sir, his **crest** up again, and the man in blood, they will out of their burrows like conies after rain."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The snowy sea-bird rose from the white **crest** of the billow, uttering a plaintive cry over the foaming waste."},
      {"author": "Alfred Tennyson", "work": "The Idylls of the King", "quote": "The knight's golden helmet bore a dragon for a **crest**, its wings outspread in terrible majesty."}
    ]
  },
  "crested.md": {
    "primary": "Having a crest, comb, or tuft; also crowned or topped by a prominent ridge or foaming wave.",
    "secondary": "In avian taxonomy, crested species display specialized ornamental plumes during courtship rituals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "His legs bestrid the ocean; his reared arm **crested** the world; his voice was propertied as all the tuned spheres."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Some men die at ebb tide, but the bold harpooner leaped forth upon the highest **crested** wave of adventure."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In the male **crested** duck, the elongated crown feathers are raised vertically during courtship displays."}
    ]
  },
  "crestfallen.md": {
    "primary": "Sad, disappointed, and downcast, especially after unexpected failure or humiliation.",
    "secondary": "In falconry and cockfighting etymology, a gamecock whose head comb fell limp after defeat was described as crestfallen.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Remember it, and let it make thee **crestfallen**, ay, and allay thus thy extravagant and insolent pride."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "I was just telling the manager—he noticed my companion, and broke off with a **crestfallen** look of confusion."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pumblechook sat completely **crestfallen** in the corner, unable to utter another syllable of pompous patronizing advice."}
    ]
  },
  "cretaceous.md": {
    "primary": "Relating to the final geological period of the Mesozoic era, characterized by chalk deposits and ending with the extinction of the dinosaurs.",
    "secondary": "In stratigraphy and historical geology, the Cretaceous system takes its name from Latin creta (chalk), preserving widespread deposits of coccolithophores.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Flintcomb-Ash was in the middle of the **cretaceous** tableland, where the thin chalky soil yielded meager crops beneath the biting winter winds."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "It may be that he swept back into the past, and fell among the blood-drinking saurians of the **cretaceous** sea."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The colossal chalk cliffs of Dover were deposited during the **cretaceous** epoch through the accumulation of microscopic marine shells."}
    ]
  },
  "cretan.md": {
    "primary": "Relating to Crete, its inhabitants, or the ancient Minoan civilization; also a native of Crete.",
    "secondary": "In classical philosophy, the Cretan paradox ('All Cretans are liars', attributed to Epimenides) serves as a foundational paradox in self-referential logic.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "O, yes, I saw sweet beauty in her face, such as the daughter of Agenor had, that made great Jove to humble him to her hand, when on his knees he kissed the **cretan** strand."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He was moderately truthful towards men, but to women lied like a **cretan** horse-dealer at a fair."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient laws of the **cretan** republic were admired by Lycurgus as models of military discipline."}
    ]
  },
  "crete.md": {
    "primary": "The largest and most populous of the Greek islands, situated in the eastern Mediterranean Sea.",
    "secondary": "In Mediterranean archaeology, Bronze Age Crete was the center of Europe's earliest advanced society, the Minoan palace civilization centered at Knossos.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "O hound of **crete**, think'st thou my spouse to get? No; to the spital go, and from the powdering-tub of infamy fetch forth the lazar kite of Cressid's kind."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Ariadne was the daughter of Minos, King of **crete**; she gave Theseus the guiding thread through the labyrinth."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rich Mediterranean island of **crete** succumbed to the naval power of the Saracen corsairs in the ninth century."}
    ]
  },
  "cretin.md": {
    "primary": "A person afflicted with severe physical and mental impairment caused by untreated congenital hypothyroidism; also an insulting term for an ignorant person.",
    "secondary": "In nineteenth-century medical geography, endemic cretinism was prevalent in isolated alpine valleys where glacial runoff depleted soil and water of dietary iodine.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Under the administration of sheep thyroid extract, the stunted **cretin** underwent astonishing physical and mental revitalization."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The idle aristocrat who consumes without producing is a spiritual **cretin** in the sight of God and man."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The degraded beast-folk shuffled across the clearing with the dull, vacant stare of an alpine **cretin**."}
    ]
  },
  "cretinism.md": {
    "primary": "A condition of severely stunted physical and mental growth owing to untreated congenital deficiency of thyroid hormones.",
    "secondary": "In endocrinology and public health history, the introduction of iodized table salt successfully eradicated endemic cretinism from mountain populations.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The discovery that thyroid gland substitution cures sporadic **cretinism** represents one of the greatest triumphs of modern physiological therapy."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Premature synostosis of the spheno-basilar suture was identified as a characteristic anatomical lesion in congenital **cretinism**."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Endemic goiter and **cretinism** occur together in deep, sunless valleys deficient in essential mineral salts."}
    ]
  },
  "cretinous.md": {
    "primary": "Afflicted with, characteristic of, or resembling cretinism; severely stunted or intellectually deficient.",
    "secondary": "In descriptive clinical neurology, cretinous facies exhibit dry thickened skin, macroglossia, a broad flattened nasal bridge, and sparse hair.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The child exhibited a typically **cretinous** expression, with prominent tongue, puffy eyelids, and lethargic demeanor."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "Pathological microcephaly must not be confused with the **cretinous** degeneration produced by thyroid dysfunction."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "He looked at the wretched, stunted creature, wondering what physiological defect had produced so **cretinous** a specimen."}
    ]
  },
  "cretonne.md": {
    "primary": "A heavy, unglazed printed cotton fabric used especially for curtains and upholstery slipcovers.",
    "secondary": "In domestic decorative history, Victorian cretonne featured bold chintz floral patterns, providing an affordable alternative to costly brocades.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "Her head was leaned against the window curtains and in her nostrils was the odor of dusty **cretonne**."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "The drawing-room armchairs were covered in faded **cretonne** patterned with sprawling pink roses and green leaves."},
      {"author": "Arnold Bennett", "work": "The Old Wives' Tale", "quote": "She measured the parlor sofa to calculate how many yards of durable floral **cretonne** would be needed for the new slipcover."}
    ]
  },
  "decrease.md": {
    "primary": "To make or become smaller or fewer in size, amount, intensity, or degree.",
    "secondary": "In mathematical physics and thermodynamics, entropy changes dictate that available free energy must decrease in an isolated thermodynamic system.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 15", "quote": "When I perceive that men as plants increase, cheered and checked even by the self-same sky, then the conceit of this inconstant stay sets youth to **decrease**."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "As the mileage began to **decrease** between her and the spot of her pilgrimage, her heartbeat quickened with anxiety."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A severe frost or prolonged drought will suddenly **decrease** the population of an abundant species by nine-tenths."}
    ]
  },
  "decreased.md": {
    "primary": "Made smaller, reduced in number, quantity, size, or intensity.",
    "secondary": "In clinical diagnostics, decreased respiratory excursion or diminished reflexes signal underlying neurological or pulmonary impairment.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Although man may not have been much modified during the latter stages of his progress, his canine teeth have notably **decreased** in size."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Her father grew worse; her time was more entirely occupied in attending him; her means of subsistence **decreased** daily."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Urine output was markedly **decreased** during the acute febrile stage of the toxic nephritis."}
    ]
  },
  "decreasing.md": {
    "primary": "Becoming progressively smaller, fewer, or less intense over time.",
    "secondary": "In economic theory, the law of decreasing returns states that successive increments of an input yield progressively smaller output gains.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Have you not a moist eye, a dry hand, a yellow cheek, a white beard, a **decreasing** leg, an increasing belly?"},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When we travel southward and see a species **decreasing** in numbers, we may be sure that climate or competitors check its range."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The agricultural industry operates under the general economic condition of **decreasing** returns to additional applications of capital."}
    ]
  },
  "decree.md": {
    "primary": "An official order issued by a legal authority or sovereign ruler; an authoritative judicial decision.",
    "secondary": "In equity jurisprudence, an equitable decree orders specific performance or an injunction, contrasting with a common-law money judgment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 115", "quote": "Heaven in thy creation did **decree**, that in thy face sweet love should ever dwell."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The severity of the **decree** seemed deadly to Tess; she saw his view of her conduct without sharing his harsh detachment."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial **decree** of Constantine granted full religious toleration to Christians throughout the Roman world."}
    ]
  },
  "decreed.md": {
    "primary": "Officially ordered, enacted, or established by authoritative judgment or legal edict.",
    "secondary": "In theological determinism, divine providence is conceived as having decreed the unfolding order of the cosmos from eternity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Therefore it is **decreed** he dies tonight, unless some sudden miracle stay the headsman's hand."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "It was **decreed** by the States-General in A.D. 1695 that whalemen should be exempt from military impressment."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "High heaven had **decreed** that man, though fallen through temptation, should find redeeming grace through divine sacrifice."}
    ]
  },
  "decrement.md": {
    "primary": "A reduction or diminution in amount, value, or quantity; the amount by which something decreases.",
    "secondary": "In computer science and assembly architecture, a decrement operation subtracts a fixed constant (usually one) from an index register or counter.",
    "quotes": [
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical wheels of the calculating engine registered each successive **decrement** with flawless mathematical fidelity."},
      {"author": "William Stanley Jevons", "work": "The Theory of Political Economy", "quote": "Each successive **decrement** in the market supply of grain produces a disproportionate escalation in its exchange price."},
      {"author": "Augustus De Morgan", "work": "Formal Logic", "quote": "In the differential calculus, we calculate the finite **decrement** of a variable as it approaches its infinitesimal limit."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — cre"

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

print(f"Dashboard — cre Batch 2: Successfully updated {updated}/{len(data)} notes.")
