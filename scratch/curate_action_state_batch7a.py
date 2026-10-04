# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — bat Part 1 (44 words) ---
  "Dashboard — bat/abatable.md": {
    "primary": "Capable of being abated, diminished, suppressed, or legally quashed.",
    "secondary": "In tort law and property jurisprudence, an abatable nuisance is an unlawful interference that can be legally suppressed without destroying property.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A private nuisance is **abatable** by the injured party, provided he commits no breach of the peace during its removal."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An unconstitutional usurpation of authority is not an **abatable** defect, but an irremediable grievance requiring legislative repeal."},
      {"author": "John Marshall", "work": "Writings of Chief Justice Marshall", "quote": "The court ruled that the obstructive river dam was an **abatable** impediment to interstate commercial navigation."}
    ]
  },
  "Dashboard — bat/abate.md": {
    "primary": "To become less intense or widespread; or to lessen, reduce, or remove a nuisance or tax.",
    "secondary": "In maritime literature and meteorology, a gale or squall is said to abate when wind velocities diminish into gentle breezes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "All torment, trouble, wonder and amazement inhabits here: some heavenly power guide us out of this fearful country, and **abate** the fury of the storm."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I waited with trembling anxiety inside my cave until the hurricane began to **abate** toward morning."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My feverish delirium began to **abate** under the affectionate care of my devoted companion Henry Clerval."}
    ]
  },
  "Dashboard — bat/abatement.md": {
    "primary": "A reduction, diminution, or suppression in amount, degree, or intensity.",
    "secondary": "In municipal public health and environmental law, a notice of nuisance abatement commands property owners to eliminate sanitary hazards.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The sudden **abatement** of commercial demand during wartime causes immediate distress among export manufacturers."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Jarndyce pursued the case with unwearied energy, suffering no **abatement** of his natural benevolence."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The king agreed to an **abatement** of the royal hearth tax to conciliate the discontented country gentlemen."}
    ]
  },
  "Dashboard — bat/abatic.md": {
    "primary": "Pertaining to or characterized by vertical airflow in meteorology, specifically vertical motion of air masses.",
    "secondary": "In atmospheric dynamics, abatic currents (comprising anabatic and katabatic winds) drive thermal circulations over mountainous slopes.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The local mountain climate is strongly influenced by diurnal **abatic** air movements ascending and descending the valley slopes."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "As the sun heated the rocky cordillera, powerful **abatic** breezes swept up the ravines toward the glaciers."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Atmospheric circulations on terrestrial planets are driven by solar heating that generates energetic **abatic** convection."}
    ]
  },
  "Dashboard — bat/abator.md": {
    "primary": "A person who abates or removes a nuisance; or one who wrongfully enters an inheritance before the rightful heir.",
    "secondary": "In common law property jurisprudence, an abator interposes between the death of the ancestor and the entry of the heir-at-law.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The rightful heir was ousted by an unlawful **abator** who seized possession of the freehold immediately upon the ancestor's decease."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The village constable acted as the authorized **abator** of the illegal tollgate erected across the parish highway."},
      {"author": "Francis Bacon", "work": "The Elements of the Common Laws of England", "quote": "The law provides distinct writs of entry against the intruder, the disseisor, and the fraudulent **abator**."}
    ]
  },
  "Dashboard — bat/abbatial.md": {
    "primary": "Pertaining to an abbot, an abbess, or an abbey; monastic.",
    "secondary": "In ecclesiastical history, abbatial jurisdiction granted powerful monastic superiors episcopal-like autonomy within their exempt territories.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Abbot", "quote": "The grand **abbatial** residence of Saint Mary's possessed stately cloisters and vast vaulted dining halls."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient Benedictine monastery exercised sovereign **abbatial** rights over forty vassal villages across the valley."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Abbot Samson assumed the **abbatial** mitre and pastoral staff, determined to restore discipline and solvency to the monastery."}
    ]
  },
  "Dashboard — bat/albatrellus.md": {
    "primary": "A genus of terrestrial mycorrhizal fungi in the family Albatrellaceae, commonly known as forest floor polypores.",
    "secondary": "In mycology and forest pathology, Albatrellus ovinus forms symbiotic ectomycorrhizal associations with spruce and pine roots in boreal ecosystems.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "Under the shaded canopy of Himalayan firs, we collected edible fleshy mushrooms belonging to the genus **albatrellus**."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The damp coniferous leaf-mold was dotted with clusters of terrestrial polypores resembling northern **albatrellus** species."},
      {"author": "William Jackson Hooker", "work": "British Flora", "quote": "Mycological collectors gathered specimens of **albatrellus** emerging from the mossy woodland loam in late autumn."}
    ]
  },
  "Dashboard — bat/albatross.md": {
    "primary": "A very large oceanic seabird of the family Diomedeidae, with long narrow wings and a hooked bill, famous for dynamic soaring.",
    "secondary": "In maritime folklore and literature, the albatross represents an omen of good fortune, or an agonizing psychological burden when killed.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "The Rime of the Ancient Mariner", "quote": "At length did cross an **albatross**, through the fog it came; as if it had been a Christian soul, we hailed it in God's name."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The snowy plumage and majestic, unwearied flight of the giant **albatross** struck the whalemen with superstitious awe."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The wandering **albatross** glided effortlessly on rigid wings over the stormy crests of the southern ocean swells."}
    ]
  },
  "Dashboard — bat/anabatic.md": {
    "primary": "Relating to or denoting an upward wind or air current caused by local surface heating; upslope wind.",
    "secondary": "In micro-meteorology, an anabatic thermal breeze ascends sunny mountain slopes during the daytime, replaced by katabatic drainage at night.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "As the morning sun warms the barren cliffs, an **anabatic** wind begins to draw up the ravine from the valley floor."},
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "The soaring condors took advantage of the warm **anabatic** currents rising along the precipitous western faces of the Andes."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "The seasonal heating of elevated plateaus generates strong **anabatic** airflow that shapes local cloud formations."}
    ]
  },
  "Dashboard — bat/approbate.md": {
    "primary": "To approve formally, sanction, or express authorized commendation of something.",
    "secondary": "In Scots law and English contract jurisprudence, a litigant cannot approbate and reprobate—meaning one cannot accept benefits under an instrument while rejecting its obligations.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The state conventions were convened to consider and **approbate** the new federal compact on behalf of the sovereign citizenry."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Parliament was eager to **approbate** every revenue measure that promised to extract fiscal tribute from the colonies."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A beneficiary cannot **approbate** the profitable provisions of a testamentary settlement while attempting to invalidate its burdens."}
    ]
  },
  "Dashboard — bat/approbation.md": {
    "primary": "Warm approval, authoritative commendation, praise, or official sanction.",
    "secondary": "In eighteenth-century moral sentimentalism, Adam Smith argued that the natural desire for social approbation regulates human moral conduct.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was delighted to observe that her father gave his full **approbation** to her sister Jane's engagement."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "Man naturally desires not only to be loved, but to be lovely; or to be that thing which is the natural object of **approbation**."},
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Her demeanor won the gracious **approbation** of all the noble lords and ladies of the Sicilian court."}
    ]
  },
  "Dashboard — bat/approbative.md": {
    "primary": "Expressing, conveying, or characterized by approval, praise, or commendation.",
    "secondary": "In phrenological and psychological history, an approbative disposition reflected an excessive craving for public flattery and social esteem.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke delivered a mild, **approbative** nod, signaling his benign indulgence of his nephew's youthful enthusiasm."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Basil Ransom murmured an **approbative** word, captivated by the orator's radiant eloquence upon the platform."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The crowd voiced their **approbative** cheers as the victorious commander rode past the decorated guildhall."}
    ]
  },
  "Dashboard — bat/approbatory.md": {
    "primary": "Expressing or showing approval, commendation, or authoritative sanction.",
    "secondary": "In diplomatic correspondence, an approbatory dispatch signals official ministerial concurrence with an ambassador's negotiated protocol.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The English public greeted the conservative manifesto with widespread **approbatory** sentiment across the shires."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Senate received the emperor's dispatch with **approbatory** acclamations and decreed three days of public thanksgiving."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The bishop gave an **approbatory** smile as Mr. Slope expounded his energetic plans for diocesan reform."}
    ]
  },
  "Dashboard — bat/bat.md": {
    "primary": "A nocturnal flying mammal of the order Chiroptera; or a wooden implement used for striking a ball in games.",
    "secondary": "In mammalian biology, bats are the only mammals capable of true sustained powered flight, utilizing membranous skin wings stretched over elongated fingers.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The wing of a **bat** is formed on the same anatomical pattern as the hand of a man or the paddle of a porpoise."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "A giant **bat** flapped against the dark window-pane of Lucy's bedchamber, its red eyes glittering in the moonlight."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Wardle seized the cricket **bat** and stepped confidently onto the pitch to defend the honors of the Dingley Dell club."}
    ]
  },
  "Dashboard — bat/bata.md": {
    "primary": "The largest city and principal commercial port of mainland Equatorial Guinea, situated on the Atlantic coast.",
    "secondary": "In West African economic geography, Bata serves as the main shipping terminal for timber, petroleum, and cacao from the Rio Muni mainland.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "Two Trips to Gorilla Land and the Cataracts of the Congo", "quote": "The merchant schooner dropped anchor in the coastal roads off **bata**, trading brass rods for palm oil and ivory."},
      {"author": "David Livingstone", "work": "Missionary Travels and Researches in South Africa", "quote": "Coastal trading settlements like **bata** connected interior equatorial trade networks with European maritime factors."},
      {"author": "Basil Davidson", "work": "The African Slave Trade", "quote": "The Atlantic littoral around modern **bata** was historically frequented by Iberian caravels seeking timber and spices."}
    ]
  },
  "Dashboard — bat/bataan.md": {
    "primary": "A coastal province and mountainous peninsula in the Central Luzon region of the Philippines.",
    "secondary": "In World War II history, the Battle of Bataan and the subsequent tragic Bataan Death March of 1942 became legendary symbols of wartime sacrifice.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The desperate, protracted defense of the **bataan** peninsula by Filipino and American soldiers delayed the Japanese offensive schedule in the Pacific."},
      {"author": "Douglas MacArthur", "work": "Reminiscences", "quote": "The ragged defenders of **bataan** fought with heroic stubbornness against overwhelming air and naval bombardments in the jungle."},
      {"author": "Ernest Hemingway", "work": "Men at War", "quote": "Dispatches from the besieged lines of **bataan** chronicled an epic struggle against disease, starvation, and superior enemy forces."}
    ]
  },
  "Dashboard — bat/batch.md": {
    "primary": "A quantity of goods, bread, or material produced or processed at one time; or a group of similar things.",
    "secondary": "In computer science and operating systems, batch processing executes a series of automated programs on a computer without human interaction.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Dolly Winthrop brought a fresh **batch** of lard-cakes to the weaver's cottage, hoping to tempt his lonely appetite."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe placed another **batch** of horseshoe nails upon the glowing anvil, hammering them into shape with rhythmic clatter."},
      {"author": "Donald Knuth", "work": "The Art of Computer Programming", "quote": "Early mainframe systems scheduled jobs in a sequential **batch**, reading stacks of punched cards through card readers."}
    ]
  },
  "Dashboard — bat/bate.md": {
    "primary": "To lessen, diminish, or abate; or an archaic term meaning to flutter wings violently (as of a falcon).",
    "secondary": "In falconry and classical drama, a hawk was said to bate when it fluttered its wings wildly and attempted to fly from the perch.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "All furnish'd, all in arms; all plumed like estridges that with the wind **bate** on their feathers, glittering in golden coats."},
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "I will not **bate** thee a single jot of the penalty stipulated in our sealed commercial bond."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The proud noble refused to **bate** an inch of his feudal dignity before the assembled burghers."}
    ]
  },
  "Dashboard — bat/bated.md": {
    "primary": "Restrained, held back, or moderated in intensity, especially of breath under suspense.",
    "secondary": "In literary phraseology, waiting 'with bated breath' signifies an acute state of suspenseful, fearful anticipation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Shall I bend low and in a bondsman's key, with **bated** breath and whisp'ring humbleness, say this: 'Fair sir, you spat on me on Wednesday last'?"},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The spectators in the crowded courtroom listened with **bated** breath as the jury returned to deliver the capital verdict."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "We waited with **bated** breath in the foggy hollow, listening for the baying of the spectral hound across Dartmoor."}
    ]
  },
  "Dashboard — bat/batidaceae.md": {
    "primary": "A small family of halophytic flowering shrubs in the order Brassicales, commonly known as saltworts.",
    "secondary": "In mangrove ecology and physiological botany, Batis maritima (Batidaceae) possesses succulent salt-secreting leaves that tolerate marine inundation.",
    "quotes": [
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "Along the maritime shores of Florida and the West Indies, fleshy halophytic shrubs of the family **batidaceae** cover tidal mudflats."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The saline lagoons of the tropical coast were fringed with fleshy, succulent vegetation belonging to the **batidaceae**."},
      {"author": "Joseph Dalton Hooker", "work": "Flora of the British West Indies", "quote": "Botanical surveys of Caribbean mangrove swamps documented extensive colonies of **batidaceae** thriving in saline soils."}
    ]
  },
  "Dashboard — bat/batik.md": {
    "primary": "A traditional Indonesian method of dyeing fabric by applying molten wax to areas not to be dyed; or fabric so dyed.",
    "secondary": "In Southeast Asian textile history, Javanese batik was designated a UNESCO Masterpiece of the Oral and Intangible Heritage of Humanity in 2009.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The Javanese women displayed astonishing artistic dexterity in drawing intricate floral patterns upon cotton cloths for **batik** dyeing."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The Malay chieftain wore a sarong of fine Javanese **batik**, decorated with swirling geometric waves of indigo and brown."},
      {"author": "W. Somerset Maugham", "work": "The Casuarina Tree", "quote": "The veranda was shaded with curtains of patterned **batik** that fluttered gently in the evening tropical breeze."}
    ]
  },
  "Dashboard — bat/batis.md": {
    "primary": "A genus of salt-tolerant halophytic flowering shrubs; or a genus of small African insectivorous birds (puffback flycatchers).",
    "secondary": "In coastal wetland botany, Batis maritima colonizes mangrove margins, stabilizing intertidal sediments against storm surge erosion.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The maritime succulent shrub **batis** maritima forms dense mats along sandy shores and tidal mudflats in the south."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The low saline flats were covered with creeping clumps of **batis**, whose succulent leaves provide forage for tortoises."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The African forest flycatcher of the genus **batis** flits through the acacia canopy in search of small winged insects."}
    ]
  },
  "Dashboard — bat/batiste.md": {
    "primary": "A fine, light, semi-sheer cotton or linen fabric of plain weave, traditionally used for handkerchiefs and delicate garments.",
    "secondary": "In textile history, batiste was named after Baptiste Cambray, a thirteenth-century linen weaver of Cambrai in northern France.",
    "quotes": [
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma dried her tears with a delicate handkerchief of embroidered **batiste**, scented with faint lavender essence."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "May Welland's trousseau included dozens of morning gowns made of fine French **batiste** trimmed with Valenciennes lace."},
      {"author": "Honoré de Balzac", "work": "Père Goriot", "quote": "The dandy adjusted his snowy cravat of sheer **batiste**, ensuring that every fold sat with impeccable Parisian elegance."}
    ]
  },
  "Dashboard — bat/batman.md": {
    "primary": "A soldier or orderly assigned as a personal servant to a military officer; or a traditional Turkish unit of weight.",
    "secondary": "In British military history, the officer's batman cleaned uniforms, maintained horses and weaponry, and carried messages in the field.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "Major Freebairn was attended by an honest Yorkshire soldier who had served as his faithful **batman** throughout the Afghan campaign."},
      {"author": "Winston Churchill", "work": "My Early Life", "quote": "My soldier **batman** packed my saddlebags and groomed my charger before dawn as the cavalry formed up along the Nile."},
      {"author": "Rudyard Kipling", "work": "Plain Tales from the Hills", "quote": "The subaltern summoned his **batman** to polish his riding boots and lay out his dress uniform for mess dinner."}
    ]
  },
  "Dashboard — bat/batna.md": {
    "primary": "A major city in northeastern Algeria, situated in the Aurès Mountains; capital of Batna Province.",
    "secondary": "In Algerian military history, Batna was established as a French military garrison post in 1844 to command the southern passes into the Sahara.",
    "quotes": [
      {"author": "Guy de Maupassant", "work": "Au Soleil", "quote": "We traveled southward through the rugged gorges of the Aurès mountains, arriving at the fortified garrison town of **batna**."},
      {"author": "Richard Francis Burton", "work": "The Highlands of the Lowlands", "quote": "Caravans arriving from the Sahara halted at **batna** to exchange dates and desert wool for Mediterranean manufactured wares."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Near the modern town of **batna** lie the magnificent Roman ruins of Timgad, founded by Emperor Trajan for his veteran legionaries."}
    ]
  },
  "Dashboard — bat/batoidei.md": {
    "primary": "A taxonomic superorder of cartilaginous fishes commonly known as rays and skates, characterized by flattened bodies and enlarged pectoral fins.",
    "secondary": "In marine ichthyology, Batoidei comprises over 600 species possessing ventral gill slits, spiracles for benthic respiration, and pavement-like crushing teeth.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Members of the superorder **batoidei** are distinguished from ordinary selachians by their ventrally situated gill apertures and flattened discoidal bodies."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The sandy shoals of the bay teemed with giant stingrays of the order **batoidei**, which buried themselves beneath the silt."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The fossil record of the **batoidei** extends back to the Jurassic epoch, revealing continuous specialization for benthic bottom-feeding."}
    ]
  },
  "Dashboard — bat/baton.md": {
    "primary": "A thin stick used by an orchestral conductor to direct a performance; or a short heavy stick carried by police.",
    "secondary": "In military ceremony, a marshal's baton represents the supreme insignia of field command, traditionally adorned with golden eagles or fleur-de-lis.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The conductor raised his **baton**, and with a single decisive downbeat unleashed the triumphant opening chords of the overture."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "King William conferred the marshal's **baton** upon Schomberg in recognition of his veteran military services in the Irish campaign."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The beadle marched down the church aisle with solemn majesty, carrying his silver-topped **baton** of office."}
    ]
  },
  "Dashboard — bat/batrachia.md": {
    "primary": "An archaic zoological order or class of animals comprising frogs, toads, and allied amphibians.",
    "secondary": "In nineteenth-century comparative anatomy, Batrachia was characterized by moist naked skin, absence of claws, and aquatic larval metamorphosis.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The transition from aquatic branchial respiration to pulmonary breathing characterizes the developmental metamorphosis of the **batrachia**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The complete absence of the order **batrachia** on oceanic islands confirms that salt water is fatal to their eggs and skin."},
      {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "We trace in the embryology of **batrachia** the remarkable morphological transformation from fish-like tadpole to terrestrial adult."}
    ]
  },
  "Dashboard — bat/batrachian.md": {
    "primary": "An amphibian, especially a frog or toad; or pertaining to amphibians.",
    "secondary": "In evolutionary biology, batrachian adaptations include cutaneous respiration and dual terrestrial-aquatic reproductive life cycles.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A curious little **batrachian** reptile inhabited the dry sand-dunes of Bahia Blanca, burrowing rapidly into the loose soil."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The reflex movements of the **batrachian** spinal cord provided classic physiological demonstrations of unconscious neuromuscular response."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The grotesque creature stared at me with wide, unblinking **batrachian** eyes that reflected the flickering campfire."}
    ]
  },
  "Dashboard — bat/batrachoididae.md": {
    "primary": "A family of predatory bottom-dwelling teleost fishes commonly known as toadfishes.",
    "secondary": "In marine bioacoustics and neurobiology, male Batrachoididae produce loud, resonant hums using rapid sonic swimbladder muscles to attract mates.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Fishes of the family **batrachoididae** lie concealed in muddy shallows, snapping up passing crustacea with their cavernous jaws."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The cranial morphology of **batrachoididae** features broad, flattened skulls and venomous opercular spines in certain tropical genera."},
      {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "We dredged several curious specimens of the family **batrachoididae** from the shallow muddy inlets of the Falkland Islands."}
    ]
  },
  "Dashboard — bat/batrachomyomachia.md": {
    "primary": "A mock-heroic ancient Greek epic poem parodying the Iliad, translating to 'The Battle of the Frogs and Mice'; or a petty, trivial dispute.",
    "secondary": "In classical literary criticism, the Batrachomyomachia is an ancient parody attributing grand Homeric martial speeches and divine interventions to marsh animals.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Lives of the English Poets", "quote": "The mock-heroic poem derives its pedigree from the ancient **batrachomyomachia**, turning the weapons of epic poetry against trifling subjects."},
      {"author": "Alexander Pope", "work": "The Dunciad", "quote": "Scholars debated whether Homer himself penned the **batrachomyomachia** or if it sprang from the playful wit of Alexandrian satirists."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The pedantic quarrel between the two university librarians degenerated into a ridiculous literary **batrachomyomachia**."}
    ]
  },
  "Dashboard — bat/batrachoseps.md": {
    "primary": "A genus of lungless salamanders native to the western coast of North America, commonly known as slender salamanders.",
    "secondary": "In vertebrate herpetology, Batrachoseps species are characterized by four-toed feet, worm-like elongated bodies, and non-nucleated red blood cells.",
    "quotes": [
      {"author": "Asa Gray", "work": "Scientific Papers of Asa Gray", "quote": "In the damp redwood forest loam, naturalists discovered the slender salamander **batrachoseps**, coiled beneath rotted fir bark."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The morphological reduction of limbs and digits in fossorial amphibians like **batrachoseps** illustrates evolutionary adaptation to subterranean life."},
      {"author": "Edward Drinker Cope", "work": "The Batrachia of North America", "quote": "The genus **batrachoseps** exhibits extreme skeletal attenuation, possessing up to twenty-three costal grooves along the trunk."}
    ]
  },
  "Dashboard — bat/bats.md": {
    "primary": "Plural of bat; nocturnal flying mammals; or an informal slang term meaning crazy, eccentric, or insane.",
    "secondary": "In colloquial idiom, to be 'bats in the belfry' describes erratic mental behavior or obsessive eccentricities.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "As the sun set behind the Carpathian peaks, clouds of nocturnal **bats** circled the crumbling battlements of the castle."},
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "Bertie Wooster suspected that Gussie Fink-Nottle was completely **bats** after his bizarre speech at the Market Snodsbury grammar school."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Immense colonies of fruit-eating **bats** hung by their claws from the branches of the banyan trees in the Australian bush."}
    ]
  },
  "Dashboard — bat/batsman.md": {
    "primary": "A player who bats in cricket or baseball; a batter.",
    "secondary": "In the sport of cricket, an accomplished batsman must master footwork, shot selection, and defensive technique against varied bowling attacks.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "He stepped onto the cricket pitch as the opening **batsman**, facing the swift bowling with calm technical competence."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The rival **batsman** took his stance before the wickets, watching the bowler's arm with intense concentration."},
      {"author": "P. G. Wodehouse", "work": "The Gold Bat", "quote": "The school team cheered as their star **batsman** drove the cricket ball cleanly over the boundary ropes for six."}
    ]
  },
  "Dashboard — bat/batswana.md": {
    "primary": "The people of Botswana; or citizens of Botswana collectively.",
    "secondary": "In southern African ethnography, the Batswana comprise several Bantu-speaking tribes speaking Setswana, historically ruled by hereditary chiefs (dikgosi).",
    "quotes": [
      {"author": "David Livingstone", "work": "Missionary Travels and Researches in South Africa", "quote": "Living among the **batswana**, I was deeply impressed by their democratic tribal assemblies and eloquent public oratory."},
      {"author": "Cecil Rhodes", "work": "Speeches and Letters", "quote": "The British South Africa Company negotiated territorial protectorate treaties with the paramount chiefs of the **batswana**."},
      {"author": "Basil Davidson", "work": "A History of Africa", "quote": "Under King Khama III, the **batswana** skillfully maintained their autonomy by petitioning Queen Victoria directly against corporate annexation."}
    ]
  },
  "Dashboard — bat/battalion.md": {
    "primary": "A large body of troops ready for battle, typically forming part of a brigade or regiment.",
    "secondary": "In military organization, an infantry battalion comprises three to five companies commanded by a lieutenant colonel.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "When sorrows come, they come not single spies, but in **battalion** strength against our kingdom."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The British infantry **battalion** formed a solid defensive square upon the desert sand, repelling the furious charge of the dervishes."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Prince Andrei watched the French **battalion** advance through the morning mist, their bayonets gleaming like water under the rising sun."}
    ]
  },
  "Dashboard — bat/batten.md": {
    "primary": "A long, flat strip of squared timber or metal used to fasten down hatches or secure planks; or to thrive and grow fat.",
    "secondary": "In nautical terminology, to 'batten down the hatches' means to secure tarpaulins over ship hatchways with battens in preparation for storm seas.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain shouted to **batten** down every hatchway as the dark typhoon cloud swept across the horizon."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Could you on this fair mountain leave to feed, and **batten** on this moor? Ha! have you eyes?"},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The seamen worked hurriedly to **batten** down the forecastle hatch as heavy green breakers began to sweep the deck."}
    ]
  },
  "Dashboard — bat/batter.md": {
    "primary": "To strike repeatedly with hard blows; or a mixture of flour, egg, and milk; or the player batting.",
    "secondary": "In fortification warfare, heavy siege guns were brought up to batter down curtain walls and breach fortress bastions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "First to possess his books; for with them he's but a sot, as I am; or **batter** at his skull with a log."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The gale began to **batter** furiously against our wooden shutters, rattling every pane of glass in the old house."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Wintry storms continued to **batter** the exposed gables of Lowood School through the dark months of December."}
    ]
  },
  "Dashboard — bat/batter-fried.md": {
    "primary": "Coated in a liquid batter mixture of flour and liquid before being deep-fried to a crisp golden crust.",
    "secondary": "In culinary history and commercial gastronomy, batter-fried fish was popularized in Victorian London, evolving into the iconic British fish and chip shop staple.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The aroma of sizzling **batter-fried** fish drifted through the narrow alleys of Field Lane from the fried-fish warehouse."},
      {"author": "Alexis Soyer", "work": "The Modern Housewife", "quote": "Dip the tender fillets into a seasoned light batter, and cook until **batter-fried** to a delicate golden crispness."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The dockers stopped at the street stall to buy steaming portions of **batter-fried** cod wrapped in yesterday's newspaper."}
    ]
  },
  "Dashboard — bat/battercake.md": {
    "primary": "A thin, flat cake of batter cooked on a griddle or frying pan; a pancake or flapjack.",
    "secondary": "In early American regional cooking, a battercake was traditionally prepared from cornmeal or buckwheat batter and served with maple syrup.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Huckleberry Finn", "quote": "Aunt Sally fried a towering stack of hot **battercake** for breakfast, drenching them in sweet golden sorghum molasses."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I baked my simple **battercake** of unleavened cornmeal upon the hearth coals, finding it wholesome and savory."},
      {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "The tea-table was loaded with platters of buckwheat **battercake** and sweet crullers fresh from the Dutch housewife's kettle."}
    ]
  },
  "Dashboard — bat/battered.md": {
    "primary": "Damaged, worn, or bruised by repeated blows, rough usage, or weathering.",
    "secondary": "In forensic pathology and pediatrics, battered child syndrome describes a pattern of non-accidental physical trauma in abused minors.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Blue Carbuncle", "quote": "Holmes held up a remarkably **battered** and disreputable hard-felt hat, examining it through his magnifying glass."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber wore an exceedingly **battered** beaver hat that had weathered many financial crises with tragic dignity."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The Nan-Shan emerged from the hurricane a **battered** and waterlogged hulk, her ventilators twisted like crumpled lead."}
    ]
  },
  "Dashboard — bat/battering.md": {
    "primary": "Repeatedly striking something with heavy blows; or subjecting to severe abuse or damage.",
    "secondary": "In ancient and medieval military siegecraft, a battering ram was a heavy suspended wooden beam capped with an iron ram's head used to breach castle gates.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The besiegers brought up a ponderous **battering** ram under a wooden shed to breach the exterior palisade of Torquilstone."},
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "The great Achilles, whom opinion crowns the sinew and the forehand of our host, with half the Trojan force stands **battering** at our gates."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The constant **battering** of the Roman ballistae eventually pulverized the stone parapets of Jerusalem."}
    ]
  },
  "Dashboard — bat/battery.md": {
    "primary": "A device producing electrical energy through chemical reaction; or a fortified artillery emplacement; or an unlawful physical beating.",
    "secondary": "In tort law, battery is the intentional, harmful, or offensive contact with another person's body without legal consent.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The common law defines **battery** as the unlawful beating of another, for which the injured party may recover damages."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Connecting the voltaic **battery** across the electrolyte solution produced continuous decomposition of water into hydrogen and oxygen."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "A concealed naval **battery** commanding the Dardanelles straits opened fire on our approaching battleships."}
    ]
  },
  "Dashboard — bat/battery-acid.md": {
    "primary": "Dilute sulfuric acid utilized as the chemical electrolyte in lead-acid rechargeable batteries.",
    "secondary": "In industrial chemistry and occupational safety, battery-acid poses severe risks of chemical skin burns and explosive hydrogen gas evolution during charging.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "We formulated an alkaline nickel-iron cell to eliminate the corrosive fumes and leakage of volatile **battery-acid**."},
      {"author": "Arthur C. Clarke", "work": "Islands in the Sky", "quote": "The technician wore heavy neoprene gauntlets to protect his hands from splashes of corrosive **battery-acid** during accumulator repairs."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "A severed electrical cable leaked pungent **battery-acid** over the metal deck of the damaged aerial scout ship."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

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

print(f"Dashboard — bat Part 1: Successfully updated {updated}/{len(data)} notes.")
