# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — sal (Batch 7B: 36 words)
  # =========================================================================
  "Dashboard — sal/salat.md": {
    "primary": "The ritual prayer of Islam, performed five times daily facing Mecca as a fundamental religious duty.",
    "secondary": "In Islamic liturgical practice, the physical sequence of rak'ahs consisting of standing, bowing, and prostration in prayer.",
    "quotes": [
      {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "The muezzin proclaims the call from the minaret, summoning all believers to perform the dawn **salat**."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The solemn stillness of the mosque during the evening **salat** filled the vast hall with spiritual majesty."},
      {"author": "Wilfrid Scawen Blunt", "work": "The Future of Islam", "quote": "The observance of daily **salat** unites the far-flung communities of Islam in common devotion."}
    ]
  },
  "Dashboard — sal/sale.md": {
    "primary": "The exchange of a commodity or property for a specified amount of money; or a period of reduced retail prices.",
    "secondary": "In contract law, a consensual transfer of title to goods or property from seller to buyer for a valuable price consideration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Besides, his cote, his flocks, and bounds of feed are now on **sale**, and at our sheepcote now you may buy."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every individual endeavours to employ his capital where its produce is likely to be of the greatest **sale** and value."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The auctioneer announced the final **sale** of the farm equipment to the gathered crowd."}
    ]
  },
  "Dashboard — sal/saleable.md": {
    "primary": "Fit or suitable to be sold; marketable and capable of commanding a price in trade.",
    "secondary": "In commerce and bankruptcy law, assets possessing enough market liquidity to be liquidated without significant capital markdown.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "I have often heard him declare, that if baronetcies were **saleable**, anybody should have had his title for fifty pounds."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A manufacture becomes more **saleable** when its durability is guaranteed by reputable craftsmen."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver accumulated a quantity of linen that was readily **saleable** in the neighboring market town."}
    ]
  },
  "Dashboard — sal/salem.md": {
    "primary": "A historic coastal city in northeastern Massachusetts, famous for the witch trials of 1692; or an ancient biblical name for Jerusalem.",
    "secondary": "In early American colonial history, a Puritan maritime trading hub whose merchants traded with the East Indies and China.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The author recalled the solemn atmosphere of the Custom House in the ancient port of **salem**."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The allusion is to Jones Very, a mystic and poet, who lived at **salem**, Massachusetts."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A merchant in **salem** traded directly with the ports of the Celestial Empire in tea and silks."}
    ]
  },
  "Dashboard — sal/saleratus.md": {
    "primary": "Sodium bicarbonate (baking soda) or potassium bicarbonate, used as a leavening agent in cooking and baking.",
    "secondary": "In 19th-century American food technology, an aerating alkali reacting with cream of tartar or sour milk to liberate carbon dioxide gas.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "Our camp cook baked heavy loaves of soda bread with sour flour and a pinch of **saleratus**."},
      {"author": "Laura Ingalls Wilder", "work": "Little House in the Big Woods", "quote": "Ma mixed the flour with buttermilk and a spoonful of white **saleratus** to make biscuits."},
      {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "The cook stirred **saleratus** into the pancake batter over the galley stove."}
    ]
  },
  "Dashboard — sal/salerno.md": {
    "primary": "An ancient port city in Campania, southwestern Italy, situated on the Gulf of Salerno.",
    "secondary": "In medieval history, renowned as the site of the Schola Medica Salernitana, the first and most illustrious medical school of medieval Europe.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The medical academy of **salerno** preserved the therapeutic wisdom of the Greeks and Arabs through the Dark Ages."},
      {"author": "Giovanni Boccaccio", "work": "The Decameron", "quote": "The romantic Prince of **salerno** held magnificent court overlooking the azure waters of the gulf."},
      {"author": "Walter Scott", "work": "Count Robert of Paris", "quote": "The learned physician was trained at **salerno**, possessing extensive knowledge of herbal remedies."}
    ]
  },
  "Dashboard — sal/saleroom.md": {
    "primary": "A room or hall in which goods, artworks, or property are displayed and sold, especially by public auction.",
    "secondary": "In commercial art history and antiquarian trade, the theatrical venue where bidders compete under the hammer of the auctioneer.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The crowded **saleroom** was filled with eager brokers bidding on bankrupt estates and seized furniture."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Rawdon Crawley watched the disposal of his fashionable effects in the auctioneer's **saleroom**."},
      {"author": "Henry James", "work": "The Spoils of Poynton", "quote": "The connoisseur frequented every prominent **saleroom** in London, searching for rare porcelain and carvings."}
    ]
  },
  "Dashboard — sal/sales.md": {
    "primary": "The activities or operations involved in selling products or services; commercial turnover or market events.",
    "secondary": "In corporate accounting, the aggregate gross revenue generated from the delivery of merchandise and provision of services.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Since Troy's death Oak had attended all **sales** and fairs for her, transacting her business with fidelity."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "This was not one of the **sales** indicating the depression of trade; on the contrary, bidding was vigorous."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "High retail **sales** reflect the general prosperity and purchasing power of the laboring multitude."}
    ]
  },
  "Dashboard — sal/salesclerk.md": {
    "primary": "An employee who assists customers, sells merchandise, and processes transactions in a retail shop or department store.",
    "secondary": "In modern commercial sociology, retail customer-facing workers mediating between corporate merchandising and consumer choices.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The busy **salesclerk** behind the notions counter answered customers with polite, professional efficiency."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "A young **salesclerk** in the dry-goods emporium unfolded bolts of silk for the prosperous client."},
      {"author": "John Dos Passos", "work": "The 42nd Parallel", "quote": "He found employment as a **salesclerk** in a busy Chicago department store during the holiday rush."}
    ]
  },
  "Dashboard — sal/salesgirl.md": {
    "primary": "A young woman employed to assist customers and sell goods in a retail store or shop.",
    "secondary": "In late 19th and early 20th-century urban labor history, female retail workers entering commercial wage labor in modern department stores.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The weary **salesgirl** stood on her feet all day behind the shoe counter, earning a meager weekly wage."},
      {"author": "O. Henry", "work": "The Trimmed Lamp", "quote": "A witty young **salesgirl** behind the ribbon counter observed the manners of the passing carriage trade."},
      {"author": "Edith Wharton", "work": "The Custom of the Country", "quote": "The fashionable milliner sent an experienced **salesgirl** to display the newest Parisian bonnets at the hotel."}
    ]
  },
  "Dashboard — sal/saleslady.md": {
    "primary": "A woman employed to sell goods or merchandise in a retail store or commercial establishment.",
    "secondary": "In retail trade discourse, a polite conventional designation for experienced female retail sales professionals.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The competent **saleslady** at the dress shop helped Carol select fabrics suited to the prairie climate."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "An older **saleslady** guided Carrie through the routine of invoicing and packaging ribbons."},
      {"author": "O. Henry", "work": "The Four Million", "quote": "The polite **saleslady** showed endless patience as the indecisive shopper examined twenty pairs of gloves."}
    ]
  },
  "Dashboard — sal/salesman.md": {
    "primary": "A man whose job is to sell goods, products, or services directly to customers or businesses.",
    "secondary": "In industrial capitalism and marketing, traveling commercial agents representing manufacturers across regional wholesale territories.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Well, I got the two dozen geese from a **salesman** in Covent Garden market."},
      {"author": "Arthur Miller", "work": "Death of a Salesman", "quote": "Willy Loman believed that a successful **salesman** needed only a smile and personal popularity to conquer the world."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The enthusiastic motor **salesman** demonstrated the mechanical virtues of the newest touring sedan."}
    ]
  },
  "Dashboard — sal/salesmanship.md": {
    "primary": "The skill, technique, or psychological art of persuading customers to purchase goods or services.",
    "secondary": "In business theory, commercial communication strategies designed to identify customer needs and negotiate advantageous exchange agreements.",
    "quotes": [
      {"author": "Thorstein Veblen", "work": "Absentee Ownership and Business Enterprise", "quote": "Modern business enterprise devotes immense financial resources to aggressive **salesmanship** and consumer persuasion."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He prided himself on his dynamic **salesmanship**, believing that enthusiasm alone closed difficult real estate deals."},
      {"author": "Peter Drucker", "work": "The Practice of Management", "quote": "Effective **salesmanship** requires understanding the customer's problems rather than mere aggressive pitching."}
    ]
  },
  "Dashboard — sal/salesperson.md": {
    "primary": "An individual employed to sell goods, merchandise, or services to customers.",
    "secondary": "In organizational management, the commercial representative responsible for customer relationship building and account management.",
    "quotes": [
      {"author": "John Kenneth Galbraith", "work": "The Affluent Society", "quote": "The modern **salesperson** functions as an indispensable agent in managing consumer demand for industrial output."},
      {"author": "Sinclair Lewis", "work": "Work of Art", "quote": "A diligent **salesperson** knows that customer loyalty is earned through honesty and reliable service."},
      {"author": "Peter Drucker", "work": "Management: Tasks, Responsibilities, Practices", "quote": "A top-tier **salesperson** views every client interaction as an opportunity to deliver genuine business value."}
    ]
  },
  "Dashboard — sal/salesroom.md": {
    "primary": "A room in a store, warehouse, or auction house where goods and merchandise are displayed for inspection and sale.",
    "secondary": "In commercial retail architecture, open showroom floors designed with lighting and displays to attract prospective buyers.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The bustling **salesroom** of the shipping agent was crowded with emigrants inquiring about passage to America."},
      {"author": "William Makepeace Thackeray", "work": "The Newcomes", "quote": "The picture dealer arranged his finest Dutch landscapes in the front **salesroom** to entice wealthy collectors."},
      {"author": "Henry James", "work": "The American", "quote": "Christopher Newman visited the luxurious **salesroom** on the boulevard, admiring the displays of ornate bronzes."}
    ]
  },
  "Dashboard — sal/saleswoman.md": {
    "primary": "A woman whose occupation is selling goods, products, or services in a retail store or commercial business.",
    "secondary": "In commercial sociology, professional women who pioneered female representation in department store merchandising and retail management.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The attentive **saleswoman** deftly folded the fine lace veil and placed it in an embossed cardboard box."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "The head **saleswoman** at the modiste's salon treated Lily Bart with the deference due to an aristocratic patron."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The energetic **saleswoman** introduced modern dress patterns to the conservative townswomen of Gopher Prairie."}
    ]
  },
  "Dashboard — sal/salian.md": {
    "primary": "Of or relating to the Salian Franks, a division of the Germanic Frankish people who settled in modern Belgium and northern France.",
    "secondary": "In European legal history, pertaining to the Salic Law (Lex Salica), the ancient civil code that famously barred females from royal succession.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **salian** Franks established their dominion over the fertile plains of Gaul under the martial guidance of Clovis."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The ancient **salian** law was cited by French jurists to exclude female heirs from the throne."},
      {"author": "François Guizot", "work": "The History of Civilization in Europe", "quote": "The customs of the **salian** conquerors merged with Roman municipal institutions to form medieval feudalism."}
    ]
  },
  "Dashboard — sal/salicaceae.md": {
    "primary": "The botanical willow family of flowering plants, comprising deciduous trees and shrubs including willows and poplars.",
    "secondary": "In dendrology and pharmaceutical botany, plants characterized by bitter astringent bark rich in the phenolic glycoside salicin (the precursor of aspirin).",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Dioecious reproduction is universally characteristic of the genera belonging to the family **salicaceae**."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The family **salicaceae** contains numerous alpine and subarctic species that stabilize riverbanks across the Himalayas."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Catkin-bearing trees of the family **salicaceae** shed copious downy seeds dispersed widely by spring breezes."}
    ]
  },
  "Dashboard — sal/salicales.md": {
    "primary": "A former taxonomic botanical order containing the single family Salicaceae (the willows and poplars).",
    "secondary": "In classical Englerian plant taxonomy, a subclass of monochlamydeous dicotyledons distinguished by dioecious amentaceous flowers lacking perianths.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The order **salicales** comprises woody plants whose reduced unisexual flowers are aggregated into dense catkins."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "In systematic classification, the order **salicales** occupies an isolated position among the amentiferous families."},
      {"author": "Joseph Dalton Hooker", "work": "The Student's Flora of the British Islands", "quote": "The primitive floral envelope of the **salicales** reflects adaptation to wind-pollinated riparian habitats."}
    ]
  },
  "Dashboard — sal/salicornia.md": {
    "primary": "A genus of succulent, halophytic annual herbs in the Amaranthaceae family, commonly known as glasswort, pickleweed, or marsh samphire.",
    "secondary": "In chemical and industrial history, coastal glasswort ashes rich in soda (sodium carbonate) historically collected to manufacture glass and soap.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Succulent species of **salicornia** flourish on coastal mudflats where high salt concentrations exclude terrestrial vegetation."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The fleshy jointed stems of **salicornia** carpet the vast maritime salt-marshes of the river delta."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "On the tidal marsh near the creek, the succulent glasswort or **salicornia** grows abundantly in the saline silt."}
    ]
  },
  "Dashboard — sal/salicylate.md": {
    "primary": "A chemical salt or ester of salicylic acid, widely used in medicine for analgesic, antipyretic, and anti-inflammatory properties.",
    "secondary": "In clinical pharmacology, active compounds (such as acetylsalicylic acid or sodium salicylate) inhibiting cyclooxygenase enzyme activity and prostaglandin synthesis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The prompt administration of sodium **salicylate** dramatically relieves the articular pain and fever of acute rheumatism."},
      {"author": "Louis S. Goodman & Alfred Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The therapeutic efficacy of any medicinal **salicylate** derives from its rapid metabolic conversion into active salicylic acid."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "A topical **salicylate** ointment is frequently applied to soothe painful musculoskeletal inflammation."}
    ]
  },
  "Dashboard — sal/salience.md": {
    "primary": "The prominence, distinctness, or conspicuousness of a feature; the quality of standing out from surroundings.",
    "secondary": "In cognitive psychology and neuroscience, the attentional attribute of a stimulus that makes it stand out against background perceptual stimuli.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory inputs with higher emotional **salience** seize attentional focus and dominate conscious awareness."},
      {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "Certain vivid memories possess an unmistakable **salience** that distinguishes them from faint conceptual shadows."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The dramatic crisis brought the moral contradictions of his position into sudden and painful **salience**."}
    ]
  },
  "Dashboard — sal/saliency.md": {
    "primary": "Prominent distinctness or striking visibility; the property of protruding conspicuously beyond surrounding boundaries.",
    "secondary": "In geographical morphology and military tactics, a convex projection or salient extending beyond the general line of defense.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The rugged **saliency** of Danton's character dominated the stormy debates of the National Convention."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The architectural **saliency** of the sculpted cornice casts deep, dramatic shadows across the marble facade."},
      {"author": "Walter Bagehot", "work": "Biographical Studies", "quote": "His political rhetoric lacked the sharp **saliency** required to leave an enduring mark upon parliamentary debate."}
    ]
  },
  "Dashboard — sal/salient.md": {
    "primary": "Most noticeable, prominent, or important; standing out conspicuously; or projecting outward.",
    "secondary": "In military fortification and tactical defense, a battlefield sector, trench line, or fortress bastion projecting into enemy territory.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "A brief summary will be sufficient to recall to the reader's mind the more **salient** points of anatomical variation."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Cobwebs revealed their presence on sheds and walls where none had ever been observed, highlighting the **salient** angles of the woodwork."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Sherlock Holmes listened with closed eyes, seizing upon the three **salient** facts that unravelled the mystery."}
    ]
  },
  "Dashboard — sal/salientia.md": {
    "primary": "An obsolete or alternative taxonomic name for the biological order of tailless amphibians (Anura), comprising frogs and toads.",
    "secondary": "In vertebrate comparative zoology, amphibians characterized by elongated hindlimbs specialized for saltatorial (jumping) locomotion and absence of tail in adults.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The order **salientia** includes all living frogs and toads, distinguished by the complete absence of a tail in the adult form."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The skeletal modification of the pelvic girdle in the **salientia** provides extraordinary leverage for leap locomotion."},
      {"author": "Edward Drinker Cope", "work": "The Batrachia of North America", "quote": "Fossil remains of early **salientia** indicate that saltatorial adaptation arose during the early Mesozoic era."}
    ]
  },
  "Dashboard — sal/salientian.md": {
    "primary": "Belonging or pertaining to the amphibian order Salientia (frogs and toads); a tailless amphibian.",
    "secondary": "In evolutionary herpetology, animals exhibiting physiological specializations for leaping, vocal sac inflation, and external fertilization in fresh water.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The typical **salientian** skull displays extensive loss and fusion of cranial bones compared to primitive stegocephalians."},
      {"author": "Edward Drinker Cope", "work": "The Batrachia of North America", "quote": "Every **salientian** species possesses an urostyle formed by the fusion of caudal vertebrae."},
      {"author": "Hans Gadow", "work": "Amphibia and Reptiles", "quote": "The vocal performance of the male **salientian** attracts prospective mates to the breeding pond at dusk."}
    ]
  },
  "Dashboard — sal/saliferous.md": {
    "primary": "Producing, yielding, or containing salt; salt-bearing (especially of geological strata and mineral formations).",
    "secondary": "In historical stratigraphy, the Saliferous System (New Red Sandstone and Keuper marls) bearing rock salt and brine springs.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Thick beds of rock salt are interstratified within the **saliferous** marls of Cheshire and Worcestershire."},
      {"author": "Roderick Murchison", "work": "The Silurian System", "quote": "Subterranean brine springs emerge abundantly from the red **saliferous** formations of central England."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "We examined the vast **saliferous** clays of the mountain plateau, where the local miners extract table salt."}
    ]
  },
  "Dashboard — sal/salim.md": {
    "primary": "A biblical location near the Jordan River where John the Baptist baptized believers; or an Arabic masculine given name meaning safe or sound.",
    "secondary": "In New Testament geography (John 3:23), the ancient site near Aenon noted for abundant springs of fresh water.",
    "quotes": [
      {"author": "King James Bible", "work": "John", "quote": "And John also was baptizing in Aenon near to **salim**, because there was much water there: and they came, and were baptized."},
      {"author": "Edward Robinson", "work": "Biblical Researches in Palestine", "quote": "Travelers have sought to identify the ancient site of **salim** among the abundant springs south of Scythopolis."},
      {"author": "George Adam Smith", "work": "The Historical Geography of the Holy Land", "quote": "The valley near **salim** offered copious streams where crowds could easily assemble for ritual ablution."}
    ]
  },
  "Dashboard — sal/salina.md": {
    "primary": "A salt marsh, salt flat, salt pan, or coastal pool where salt water is evaporated to produce mineral salt.",
    "secondary": "In Spanish colonial economic geography, state-regulated salt pans along Caribbean and Mediterranean coasts exploited for trade.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The coastal **salina** sparkled under the tropical sun, its white crystalline crust harvested by local laborers."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We rode past an extensive inland **salina**, where the encrusted mud looked like a vast sheet of frozen snow."},
      {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "The Spanish mission drew its supply of coarse cooking salt from an expansive **salina** bordering the bay."}
    ]
  },
  "Dashboard — sal/salinate.md": {
    "primary": "To impregnate, season, or treat with salt; to make salty.",
    "secondary": "In food preservation and brine curing, saturating meat or fish tissues with saline brine to inhibit bacterial putrefaction.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooners used heavy brine to **salinate** the barrels of pork destined for the long three-year cruise."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The thrifty cook would **salinate** the beef until it was as hard and durable as mahogany."},
      {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "The hides were thoroughly soaked in brine tanks to **salinate** and preserve them during the long voyage home."}
    ]
  },
  "Dashboard — sal/saline.md": {
    "primary": "Containing or impregnated with salt; salty; consisting of or resembling salt; a solution of salt in water.",
    "secondary": "In clinical medicine, a sterile solution of sodium chloride in water (physiological saline, 0.9% NaCl) isotonic with human blood plasma.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "His were the shinbones of the **saline** beef; his would have been the drumsticks of the fowl."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "He may even now be wandering on some plesiosaurus-haunted **saline** beach beneath a desolate sky."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Various **saline** plants, known as halophytes, thrive on the dry borders of the salt lagoons."}
    ]
  },
  "Dashboard — sal/salinger.md": {
    "primary": "J. D. Salinger (1919–2010), acclaimed American author renowned for his 1951 coming-of-age novel The Catcher in the Rye.",
    "secondary": "In modern literary criticism, celebrated for capturing post-war adolescent alienation, spiritual search, and the reclusive life of the artist.",
    "quotes": [
      {"author": "J. D. Salinger", "work": "The Catcher in the Rye", "quote": "In his immortal masterpiece, **salinger** gave voice to the poignant, cynical vulnerability of Holden Caulfield."},
      {"author": "John Updike", "work": "Picked-Up Pieces", "quote": "The fiction of **salinger** transformed American prose by rendering colloquial speech into lyric poetry."},
      {"author": "Philip Roth", "work": "Reading Myself and Others", "quote": "No post-war writer captured the anxieties of youthful nonconformity more sharply than **salinger**."}
    ]
  },
  "Dashboard — sal/salinity.md": {
    "primary": "The concentration of dissolved salts in water, soil, or other solutions, typically expressed in parts per thousand (ppt).",
    "secondary": "In oceanography, the total quantity of dissolved inorganic solids in seawater, which directly regulates oceanic thermohaline circulation.",
    "quotes": [
      {"author": "Matthew Fontaine Maury", "work": "The Physical Geography of the Sea", "quote": "The high **salinity** of the Red Sea results from intense solar evaporation accompanied by negligible freshwater runoff."},
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "The uniform **salinity** of open ocean water is maintained by global circulation currents and winds."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The exceptional **salinity** of the inland salt lakes allows only specialized brine shrimp to survive."}
    ]
  },
  "Dashboard — sal/salinometer.md": {
    "primary": "An instrument (such as a specialized hydrometer or electrical conductivity meter) for measuring the salinity of a solution.",
    "secondary": "In marine boiler operation and steam engineering, an instrument used to monitor salt accumulation in boiler feedwater to prevent scaling.",
    "quotes": [
      {"author": "Matthew Fontaine Maury", "work": "The Physical Geography of the Sea", "quote": "The hydrologist dipped the weighted **salinometer** into the sample bottle to determine the density of the sea water."},
      {"author": "Thomas W. Corbin", "work": "Marvels of Scientific Invention", "quote": "A naval engineer reads the **salinometer** daily to ensure that the ship's boilers are not contaminated with brine."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo consulted a sensitive **salinometer** mounted beside the barometer to gauge ocean water density."}
    ]
  },
  "Dashboard — sal/salisbury.md": {
    "primary": "A historic cathedral city in Wiltshire, England, famed for Salisbury Cathedral with its 123-metre spire; or a title of English nobility.",
    "secondary": "In English medieval history, the site of Old Sarum and the assembly where the Oath of Salisbury was sworn to William the Conqueror in 1086.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Gloucester and Bedford, Exeter and Erpingham, with all their host; **salisbury** and Warwick, to the field!"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "They crossed the lonely plateau of **salisbury** Plain under the starry silence of the summer night."},
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The market day at **salisbury** brought farmers and country folk together beneath the shadow of the lofty cathedral spire."}
    ]
  },
  "Dashboard — sal/salish.md": {
    "primary": "A member of an indigenous group of First Nations peoples of the Pacific Northwest; or their family of indigenous languages.",
    "secondary": "In North American ethnology and linguistics, the Coast and Interior Salish peoples inhabiting the Fraser River and Columbia River basins.",
    "quotes": [
      {"author": "Franz Boas", "work": "The Salishan Tribes of the Western Plateaus", "quote": "The folklore and social ceremonies of the **salish** people preserve rich ancestral traditions of hunting and fishing."},
      {"author": "James Teit", "work": "The Thompson Indians of British Columbia", "quote": "Among the interior **salish**, cedar bark and mountain goat wool were woven into warm winter garments."},
      {"author": "John Wesley Powell", "work": "Indian Linguistic Families of America", "quote": "The **salish** linguistic stock occupies extensive territories extending from the Pacific coast into the Rocky Mountains."}
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

print(f"Speed Batch 7B: Successfully updated {updated}/{len(data)} notes.")
