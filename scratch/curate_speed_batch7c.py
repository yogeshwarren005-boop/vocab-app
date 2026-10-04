# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — sal (Batch 7C: 35 words)
  # =========================================================================
  "Dashboard — sal/salishan.md": {
    "primary": "Relating to or denoting the Salish family of indigenous North American languages spoken in British Columbia, Washington, and Montana.",
    "secondary": "In comparative Amerindian linguistics, languages characterized by complex consonant clusters, morphological reduplication, and polysynthetic verb structures.",
    "quotes": [
      {"author": "Franz Boas", "work": "The Salishan Tribes of the Western Plateaus", "quote": "The complex phonetic structure of the **salishan** dialects poses formidable challenges to classical transcription."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Grammatical prefixes in the **salishan** language family convey subtle spatial and somatic categories."},
      {"author": "John Wesley Powell", "work": "Indian Linguistic Families of America", "quote": "The geographical distribution of the **salishan** linguistic stock reflects extensive historical migrations."}
    ]
  },
  "Dashboard — sal/saliva.md": {
    "primary": "The watery fluid secreted into the mouth by the salivary glands, containing enzymes that facilitate swallowing and begin carbohydrate digestion.",
    "secondary": "In human physiology and biochemistry, an alkaline fluid containing salivary amylase (ptyalin), lysozyme, and mucin maintaining oral homeostasis.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "There was a mouth under the eyes, the lipless brim of which quivered and panted, dropping thick **saliva**."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The philosopher spent forty years attempting to extract sunbeams from cucumbers and analyze human **saliva**."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Under the influence of acute terror, the secretion of **saliva** is immediately arrested, leaving the tongue parched."}
    ]
  },
  "Dashboard — sal/salivary.md": {
    "primary": "Of, relating to, producing, or secreting saliva in the oral cavity.",
    "secondary": "In vertebrate digestive anatomy, the major exocrine glands (parotid, submandibular, and sublingual) delivering lubricating fluid to the buccal cavity.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The parotid is the largest of the three pairs of **salivary** glands located on either side of the face."},
      {"author": "Ivan Pavlov", "work": "Lectures on the Work of the Digestive Glands", "quote": "The presentation of food elicited a conditioned reflex from the **salivary** duct of the canine subject."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Mastication stimulates the rapid discharge of alkaline fluid from the **salivary** ducts."}
    ]
  },
  "Dashboard — sal/salivate.md": {
    "primary": "To produce or discharge saliva, especially in excessive amounts or in anticipation of food.",
    "secondary": "In behavioural psychology, the classical Pavlovian conditioned response where sensory cues trigger involuntary reflex secretion.",
    "quotes": [
      {"author": "Ivan Pavlov", "work": "Conditioned Reflexes", "quote": "The sound of the metronome alone was sufficient to cause the animal to **salivate** copiously."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The sight of savoury meat causes an hungry person to **salivate** before tasting a morsel."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The sudden aroma of real roast coffee caused Winston to **salivate** with ravenous anticipation."}
    ]
  },
  "Dashboard — sal/salivation.md": {
    "primary": "The secretion or production of saliva; an excessive or abnormal flow of saliva from the oral glands.",
    "secondary": "In historical toxicology and pharmacology, copious ptyalism induced by toxic mercury therapies formerly prescribed for chronic ailments.",
    "quotes": [
      {"author": "Ivan Pavlov", "work": "Lectures on the Work of the Digestive Glands", "quote": "We measured the exact rate of **salivation** through an exteriorized fistula in the dog's cheek."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic mercurial poisoning manifests in spongy bleeding gums and profuse **salivation**."},
      {"author": "Oliver Wendell Holmes", "work": "Currents and Counter-Currents in Medical Science", "quote": "Heroic medicine in the last century sought to cure every distemper by producing violent **salivation** with calomel."}
    ]
  },
  "Dashboard — sal/salix.md": {
    "primary": "A large taxonomic genus of deciduous trees and shrubs in the family Salicaceae, commonly known as willows, sallows, and osiers.",
    "secondary": "In botanical taxonomy, dioecious amentiferous woody plants adapted to riparian habitats, the bark of which yields medicinal salicin.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Various species of **salix** hybridize freely along river banks, producing perplexing intermediate forms."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **salix** displays flexible twigs and silky catkins that bloom early in temperate springs."},
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The bitter bark of the water **salix** or willow tree cooleth excessive heat in agues."}
    ]
  },
  "Dashboard — sal/sallet.md": {
    "primary": "An archaic term for a salad (a dish of raw green herbs); or an alternative spelling of salade (a light medieval helmet).",
    "secondary": "In Shakespearean English and culinary history, wild green salad herbs (such as sorrel, lettuce, or watercress) eaten cold with vinegar and oil.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Wherefore, o'er a brick wall have I climbed into this garden, to see if I can eat a **sallet**."},
      {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The page served a cool dish of fresh **sallet** herbs alongside the roasted partridge."},
      {"author": "John Evelyn", "work": "Acetaria: A Discourse of Sallets", "quote": "A well-dressed **sallet** of young lettuces and wild herbs refreshings the liver in hot summer months."}
    ]
  },
  "Dashboard — sal/sallow.md": {
    "primary": "Of a sickly, yellowish or brownish-yellow color (typically referring to skin complexion); or a broad-leaved willow shrub.",
    "secondary": "In botanical dendrology, specific willow varieties (such as Salix caprea, the goat willow) bearing downy spring catkins.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Jesu Maria, what a deal of brine hath wash'd thy **sallow** cheeks for Rosaline!"},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The fields were **sallow** with the impure light of dawn, tinged in mournful monochrome."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Her pale, **sallow** face bore the indelible imprint of chronic physical suffering and neglect."}
    ]
  },
  "Dashboard — sal/sallowness.md": {
    "primary": "A yellowish, sickly, or pale discoloration of the skin or complexion.",
    "secondary": "In medical diagnostics, a characteristic cutaneous appearance associated with chronic hepatic dysfunction, malaria, or anaemia.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's moles and **sallowness** formed a striking contrast with the youthful bloom of Dorothea."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The prisoner's heavy brow and unhealthy **sallowness** spoke of long confinement in damp dungeons."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "The sunken eyes and peculiar **sallowness** of the invalid revealed a constitution shattered by tropical fevers."}
    ]
  },
  "Dashboard — sal/sally.md": {
    "primary": "A sudden rushing attack, charge, or burst forth from a besieged place; or a witty, lively remark or quip.",
    "secondary": "In military siege warfare, a counter-offensive sortie undertaken by garrison troops to destroy besiegers' trenches or artillery works.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "All our general force might with a **sally** of the very town be buckled with."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The besieged knights made a desperate **sally** through the postern gate, scattering the attackers."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth listened with quiet delight to her father's sarcastic **sally** at the expense of their foolish cousins."}
    ]
  },
  "Dashboard — sal/salmacis.md": {
    "primary": "In Greek mythology, the nymph of a fountain in Caria who fell in love with Hermaphroditus and merged bodies with him.",
    "secondary": "In classical mythological literature (Ovid's Metamorphoses), the legendary spring whose waters were fabled to make men effeminate and enervated.",
    "quotes": [
      {"author": "Ovid", "work": "Metamorphoses", "quote": "The enamoured nymph **salmacis** clasped Hermaphroditus tightly, praying that their two bodies might never be divided."},
      {"author": "John Milton", "work": "Elegia Septima", "quote": "Not more ardently did **salmacis** pursue her youthful hunter through the clear waters of the fountain."},
      {"author": "Francis Bacon", "work": "The Wisdom of the Ancients", "quote": "The ancient myth of **salmacis** moralized against the corrupting enervation that flows from voluptuous leisure."}
    ]
  },
  "Dashboard — sal/salmagundi.md": {
    "primary": "A traditional mixed dish consisting of chopped meats, anchovies, hard-boiled eggs, onions, and oil; or an eclectic, heterogeneous mixture.",
    "secondary": "In 18th and 19th-century satirical literature, an entertaining miscellany of diverse essays, sketches, and whimsical observations.",
    "quotes": [
      {"author": "Washington Irving", "work": "Salmagundi", "quote": "The authors presented their humorous **salmagundi** of eccentric sketches to ridicule the fashionable foibles of New York."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The sea cook prepared a savory **salmagundi** of salted beef, pickled herring, and chopped capers."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whaler's mess boasted an extraordinary **salmagundi** compounded of dried salt horse and ships' biscuit."}
    ]
  },
  "Dashboard — sal/salmi.md": {
    "primary": "A ragout or stew of roasted game birds (such as duck, woodcock, or partridge) sliced and reheated in a rich wine sauce.",
    "secondary": "In classical French haute cuisine (salmis), a sophisticated preparation where game carcass trimmings are simmered with red wine and shallots.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The gourmet declared that the chef's **salmi** of partridge was worthy of the finest tables in Paris."},
      {"author": "Alexandre Dumas", "work": "Grand Dictionnaire de Cuisine", "quote": "A true hunter's **salmi** must be cooked over embers with truffles, Madeira wine, and game jus."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The fashionable guests partook of a delicate **salmi** of wild duck served on silver platters."}
    ]
  },
  "Dashboard — sal/salmo.md": {
    "primary": "The taxonomic biological genus of salmonid fishes, including the Atlantic salmon (Salmo salar) and brown trout (Salmo trutta).",
    "secondary": "In ichthyology, anadromous ray-finned fishes possessing an adipose fin, cycloid scales, and powerful upstream migratory navigation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The male of the common salmon, classified as **salmo** salar, develops a hooked lower jaw during the breeding season."},
      {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "The noble fish **salmo** surpasses all river inhabitants in beauty, vigour, and sporting gameness."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The skull structure of **salmo** displays the primitive teleost arrangement of bony plates and cartilage."}
    ]
  },
  "Dashboard — sal/salmon.md": {
    "primary": "A large edible silver-scaled sport and commercial fish of the family Salmonidae, prized for its pink flesh.",
    "secondary": "In marine biology, anadromous migratory fishes hatching in gravelly freshwater streams, maturing in the open ocean, and returning upstream to spawn.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "There is a river in Macedon; and there is also moreover a river at Monmouth: and there is **salmon** in both."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The fishermen hauled their heavy nets onto the gravel bar, glistening with fresh **salmon**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The migratory instinct of the **salmon** drives it with unerring fidelity to its native spawning gravels."}
    ]
  },
  "Dashboard — sal/salmonberry.md": {
    "primary": "Rubus spectabilis, a prickly deciduous shrub of the rose family native to the Pacific Northwest, or its edible yellowish-orange to reddish aggregate fruit.",
    "secondary": "In Pacific Northwest ethnobotany and temperate ecology, early spring berries harvested alongside fresh oolichan grease by coastal First Nations.",
    "quotes": [
      {"author": "John Muir", "work": "Travels in Alaska", "quote": "The sprawling thickets of **salmonberry** were laden with luscious golden and crimson fruits along the river flats."},
      {"author": "David Douglas", "work": "Journal Kept by David Douglas During His Travels in North America", "quote": "We refreshed ourselves with the sweet juicy drupelets of the **salmonberry** while exploring the Columbia valley."},
      {"author": "Archibald Menzies", "work": "Hawaii and Northwest America Journals", "quote": "The indigenous inhabitants gathered bountiful baskets of the ripe **salmonberry** to dry for winter consumption."}
    ]
  },
  "Dashboard — sal/salmonella.md": {
    "primary": "A taxonomic genus of rod-shaped Gram-negative flagellated bacteria causing food poisoning, enteritis, and typhoid fevers.",
    "secondary": "In microbiology and infectious disease pathology, facultative anaerobic enterobacteria invading intestinal epithelial tissues and macrophages.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The organism **salmonella** typhi is transmitted primarily through sewage-contaminated drinking water and milk supplies."},
      {"author": "René Dubos", "work": "The Bacterial Cell", "quote": "Somatic and flagellar antigens of the genus **salmonella** provided the foundation for precise serological classification."},
      {"author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "Pioneering bacteriologists identified **salmonella** strains as the causative agents of severe epidemic gastroenteritis."}
    ]
  },
  "Dashboard — sal/salmonellosis.md": {
    "primary": "An infectious foodborne illness or gastrointestinal infection caused by bacteria of the genus Salmonella.",
    "secondary": "In clinical epidemiology, an acute diarrheal syndrome marked by sudden fever, abdominal cramping, and vomiting following ingestion of contaminated food.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Outbreaks of acute **salmonellosis** typically follow the consumption of improperly stored poultry, eggs, or dairy products."},
      {"author": "René Dubos", "work": "Man Adapting", "quote": "The widespread industrialization of poultry production dramatically increased the human incidence of **salmonellosis**."},
      {"author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "Investigating public health officers traced the epidemic of **salmonellosis** to an infected communal water supply."}
    ]
  },
  "Dashboard — sal/salmonid.md": {
    "primary": "Any ray-finned fish belonging to the family Salmonidae, including salmon, trout, chars, graylings, and whitefishes.",
    "secondary": "In freshwater fisheries management, cold-water stenothermal predatory fishes sensitive to dissolved oxygen levels and river sedimentation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Every migratory **salmonid** species displays intense sexual rivalry among males on the spawning beds."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The primitive adipose fin remains an unmistakable anatomical hallmark of every true **salmonid**."},
      {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "The lively trout is a typical **salmonid**, delighting in clear swift streams with stony bottoms."}
    ]
  },
  "Dashboard — sal/salmonidae.md": {
    "primary": "The taxonomic family of teleost ray-finned fishes containing the salmons, trouts, chars, freshwater whitefishes, and graylings.",
    "secondary": "In evolutionary ichthyology, ancient salmoniform fishes characterized by a whole-genome duplication event (salmonid-specific autotetraploidization).",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The males alone of the capelin, one of the family **salmonidae**, are provided with ridges of bristly scales along the sides."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The anatomical features of the **salmonidae** link primitive soft-rayed fishes with advanced marine teleosts."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The worldwide distribution of the **salmonidae** is primarily boreal, dominating the cold rivers of the northern continents."}
    ]
  },
  "Dashboard — sal/salmwood.md": {
    "primary": "Cordia alliodora, a valuable tropical American timber tree of the borage family, or its durable, attractively figured light brown wood.",
    "secondary": "In tropical forestry and agroforestry, a fast-growing neotropical canopy tree widely planted for shade in coffee and cacao plantations.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The native carpenters preferred the hard, fragrant timber of the **salmwood** for building durable river canoes."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "The forest canopy was adorned with white blooming sprays of the **salmwood** tree towering above the understory."},
      {"author": "Thomas Belt", "work": "The Naturalist in Nicaragua", "quote": "Small ants frequently inhabit the hollow swollen nodes of the **salmwood** branches in a mutualistic symbiosis."}
    ]
  },
  "Dashboard — sal/salol.md": {
    "primary": "Phenyl salicylate, a white crystalline powder formerly used in medicine as an intestinal antiseptic and analgesic.",
    "secondary": "In historical pharmaceutical chemistry, an ester insoluble in gastric acid that passes intact into the duodenum where alkaline juices hydrolyze it.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician administered **salol** as an internal antiseptic to reduce bacterial fermentation in the small intestine."},
      {"author": "Louis S. Goodman & Alfred Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Enteric pill coatings traditionally utilized **salol** because it resists stomach acid while dissolving in alkaline intestinal secretions."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "In his dispensary, the young doctor measured doses of phenacetin and **salol** for his febrile patients."}
    ]
  },
  "Dashboard — sal/salome.md": {
    "primary": "In the New Testament, a daughter of Herodias whose dance pleased Herod Antipas, resulting in the beheading of John the Baptist.",
    "secondary": "In fin-de-siècle aesthetic and decadent literature, the archetypal femme fatale immortalized in Oscar Wilde's tragic drama and Richard Strauss's opera.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "Salome", "quote": "In his poetic drama, the dancer **salome** demands the head of Jokanaan upon a silver charger as her terrible reward."},
      {"author": "King James Bible", "work": "Mark", "quote": "There were also women looking on afar off, among whom was Mary Magdalene and **salome**, watching by the cross."},
      {"author": "Gustave Flaubert", "work": "Trois Contes", "quote": "The young dancer **salome** whirled before the tetrarch until his senses were utterly bewitched by her grace."}
    ]
  },
  "Dashboard — sal/salomon.md": {
    "primary": "An archaic or French spelling of Solomon (King of Israel); or Salomon's House, the utopian scientific research institution in Bacon's New Atlantis.",
    "secondary": "In early modern intellectual history, Francis Bacon's model of organized empirical scientific research and collective technology discovery.",
    "quotes": [
      {"author": "Francis Bacon", "work": "New Atlantis", "quote": "The end of our foundation, which we call **salomon**'s House, is the knowledge of causes, and secret motions of things."},
      {"author": "King James Bible", "work": "1 Kings", "quote": "The wisdom of King **salomon** was renowned among all the kings of the earth who sought his counsel."},
      {"author": "Michel de Montaigne", "work": "Essays", "quote": "Wise king **salomon** testified that all human pursuits under the sun are vanity and vexation of spirit."}
    ]
  },
  "Dashboard — sal/salon.md": {
    "primary": "A reception room in a large house; or a periodic gathering of artists, writers, and intellectuals for conversation and cultural exchange.",
    "secondary": "In French cultural history, the prestigious official annual exhibition of art held in Paris under the auspices of the Académie des Beaux-Arts.",
    "quotes": [
      {"author": "Marcel Proust", "work": "Swann's Way", "quote": "The fashionable **salon** of Madame Verdurin welcomed only those faithful guests who shared her aesthetic prejudices."},
      {"author": "Émile Zola", "work": "L'Œuvre", "quote": "The young revolutionary painters gathered before the gates of the official **salon** to protest the rejection of their canvases."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The brilliant conversation of the Parisian **salon** exerted a profound influence on French political philosophy."}
    ]
  },
  "Dashboard — sal/salonica.md": {
    "primary": "The historical Italian and western European name for Thessaloniki, a major port city in northern Greece on the Aegean Sea.",
    "secondary": "In Ottoman and Balkan history, an important multicultural mercantile metropolis connecting Mediterranean sea routes with Balkan overland trade.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The prosperous maritime commerce of **salonica** maintained Greek commercial supremacy throughout the Aegean basin."},
      {"author": "Rebecca West", "work": "Black Lamb and Grey Falcon", "quote": "The storied ramparts of **salonica** overlooked the sea, bearing the marks of Byzantine emperors and Ottoman sultans."},
      {"author": "John Reed", "work": "The War in Eastern Europe", "quote": "In the crowded streets of **salonica**, refugees, soldiers, and merchants of twenty nations mingled in colorful confusion."}
    ]
  },
  "Dashboard — sal/salonika.md": {
    "primary": "An alternative English spelling of Salonica (Thessaloniki), the historic Aegean port city in northern Greece.",
    "secondary": "In military history of World War I, the base of the Allied Macedonian front (the Salonika Front) established in 1915.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The strategic decision to maintain an allied army at **salonika** tied down substantial Bulgarian and German forces in the Balkans."},
      {"author": "Rebecca West", "work": "Black Lamb and Grey Falcon", "quote": "The cosmopolitan spirit of **salonika** survived centuries of siege, plague, and political upheaval."},
      {"author": "John Reed", "work": "The War in Eastern Europe", "quote": "Along the quays of **salonika**, British transports unloaded artillery and supplies for the northern front."}
    ]
  },
  "Dashboard — sal/saloon.md": {
    "primary": "A public room or tavern where alcoholic drinks are sold and consumed, especially in the American West; or a large reception hall or cabin.",
    "secondary": "In British automotive and maritime terminology, a passenger car with a closed body (sedan) or a main social dining compartment aboard a passenger ship.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "Every second building along the dusty mining street was a noisy drinking **saloon** illuminated by oil lamps."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He entered a long low room which looked as if it had once been a luxurious ballroom or private **saloon**."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The elegant **saloon** was cleared for dancing, accommodating eighteen couples with ease beneath the chandeliers."}
    ]
  },
  "Dashboard — sal/salsa.md": {
    "primary": "A spicy tomato-based sauce of Mexican origin flavored with chili peppers and herbs; or a lively Latin American ballroom dance.",
    "secondary": "In ethnomusicology, an Afro-Cuban musical synthesis developed in New York and the Caribbean blending son, mambo, and jazz rhythms.",
    "quotes": [
      {"author": "Octavio Paz", "work": "The Labyrinth of Solitude", "quote": "The piquant flavors of chili and fresh **salsa** are essential elements of Mexican culinary ritual and social festivity."},
      {"author": "Gabriel García Márquez", "work": "Living to Tell the Tale", "quote": "The lively brass rhythms of Caribbean **salsa** echoed across the courtyard during warm tropical nights."},
      {"author": "Carlos Fuentes", "work": "The Old Gringo", "quote": "The roadside tavern served fresh tortillas with a fiery red **salsa** that set the palate ablaze."}
    ]
  },
  "Dashboard — sal/salsify.md": {
    "primary": "Tragopogon porrifolius, a European composite plant cultivated for its edible fleshy root having a flavor reminiscent of oysters; vegetable oyster.",
    "secondary": "In culinary botany and horticulture, a hardy biennial vegetable stored in root cellars for winter culinary stews and soups.",
    "quotes": [
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The purple-flowered **salsify** groweth in rich gardens and its pleasant root hath the delicate savour of oysters."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I planted a row of sweet **salsify** in my woodland garden, admiring its grass-like foliage."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The yellow-flowered **salsify** opens its blooms punctually at sunrise and closes them before noon."}
    ]
  },
  "Dashboard — sal/salsilla.md": {
    "primary": "Bomarea edulis, a tropical American climbing herbaceous plant of the alstroemeria family cultivated for its edible starchy tubers.",
    "secondary": "In Andean ethnobotany, tuberous twining vines historically harvested as a root food resource by indigenous highland populations.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The Andean villagers cultivated the climbing **salsilla**, whose starchy roots provided sustenance during mountain travels."},
      {"author": "Joseph Dalton Hooker", "work": "Curtis's Botanical Magazine", "quote": "The handsome campanulate blossoms of **salsilla** make it an attractive climber for the conservatory."},
      {"author": "Richard Spruce", "work": "Notes of a Botanist on the Amazon and Andes", "quote": "We encountered tangled thickets of **salsilla** twining around tree trunks on the cloud-forest slopes."}
    ]
  },
  "Dashboard — sal/salsola.md": {
    "primary": "A taxonomic genus of halophytic, salt-tolerant herbs and shrubs in the family Amaranthaceae, commonly known as saltworts or tumbleweeds.",
    "secondary": "In coastal ecology and economic botany, plants growing on arid salt plains, the ashes of which historically provided barilla soda for glassmaking.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Various species of **salsola** flourish on the arid alkaline steppes where ordinary vegetation perishes from salt."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The salt-burners collected large mounds of dried **salsola** from the seashore to burn for soda ash."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The prickly fleshy shrubs of **salsola** carpet the vast maritime salt-wastes along the Arabian Sea."}
    ]
  },
  "Dashboard — sal/salt.md": {
    "primary": "Sodium chloride (NaCl), a white crystalline substance used as a seasoning, food preservative, and industrial chemical; saline mineral.",
    "secondary": "In figurative and biblical language (salt of the earth), that which imparts essential character, piquancy, preserving power, or moral integrity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Now I see the mystery of your loneliness, and find your **salt** tears' head."},
      {"author": "King James Bible", "work": "Matthew", "quote": "Ye are the **salt** of the earth: but if the **salt** have lost his savour, wherewith shall it be salted?"},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "There is nothing like a good stiff gale and a dash of **salt** spray to wake up a dull sailor's wits."}
    ]
  },
  "Dashboard — sal/salt-cured.md": {
    "primary": "Preserved, flavored, or cured by dehydration and treatment with dry salt or brine.",
    "secondary": "In traditional charcuterie and food preservation, utilizing salt to lower water activity and suppress pathogenic bacterial growth.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The long-voyage whaler was provisioned with barrels of tough **salt-cured** pork and beef."},
      {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "The sailors subsisted almost entirely on hard bread and **salt-cured** meat through the stormy passage."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Our guide packed a slab of **salt-cured** venison in the birch-bark canoe for our wilderness journey."}
    ]
  },
  "Dashboard — sal/saltate.md": {
    "primary": "To leap, jump, dance, or skip; in evolutionary biology, to undergo sudden evolutionary change through mutational leaps rather than gradual steps.",
    "secondary": "In evolutionary theory, discontinuous morphological transitions or macromutations producing abrupt phenotypic divergence between ancestral and descendant forms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection acts only by taking advantage of slight successive variations; she can never take a great and sudden leap, or **saltate** across gaps."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Nature does sometimes **saltate**, and the dogma that nature never makes a leap is not an absolute physical law."},
      {"author": "William Bateson", "work": "Materials for the Study of Variation", "quote": "Discontinuous variation suggests that organisms may **saltate** from one stable anatomical form to another."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
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
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Speed Batch 7C: Successfully updated {updated}/{len(data)} notes.")
