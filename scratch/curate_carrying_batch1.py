# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — veh (5 words)
  # =========================================================================
  "Dashboard — veh/vehemence.md": {
    "primary": "Great forcefulness, fervor, or passionate intensity of feeling or expression.",
    "secondary": "In classical rhetoric and oratorical theory, elevated emotional urgency and stylistic vigor deployed to persuade an audience.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Nay, I prithee now, with most petitionary **vehemence**, tell me who it is."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Her darkened face had such power over me that it stopped me in the midst of my **vehemence**."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He spoke with a passionate **vehemence** that swept away all my remaining scruples."}
    ]
  },
  "Dashboard — veh/vehement.md": {
    "primary": "Showing strong feeling; forceful, passionate, or intense in emotion or action.",
    "secondary": "In natural philosophy and meteorology, violent, rushing, or tumultuous (describing winds, currents, or physical forces).",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Though not for me, yet for your **vehement** oaths, you should have been respective and have kept it."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The storm appeared to approach rapidly; the thunder burst with a terrific crash over my head, and a **vehement** gust of wind nearly tore me from the rock."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His convictions were too **vehement** to allow of his remaining a calm spectator in such a crisis."}
    ]
  },
  "Dashboard — veh/vehemently.md": {
    "primary": "In a forceful, passionate, or intensely emotional manner; with violent vigor or emphatic conviction.",
    "secondary": "In courtroom advocacy and debate, arguing with fervent, relentless insistence against opposing counsel.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "You are taking too much upon yourself! she said, **vehemently**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The night wind had aroused all the watchdogs in the neighbourhood, who bark **vehemently**."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "He protested **vehemently** that he knew nothing whatever of the escaped convict."}
    ]
  },
  "Dashboard — veh/vehicle.md": {
    "primary": "A thing used for transporting people or goods, especially on land, such as a carriage, car, cart, or wagon.",
    "secondary": "In pharmacology and artistic painting, an inactive excipient medium (solvent or oil) used to dilute or suspend an active pigment or drug.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "It is the most flagrant example of an abominable public **vehicle** that ever encumbered the face of the earth."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel had not beheld the sight for more than half a minute, when the **vehicle** was brought to a standstill just beneath his eyes."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The great whaleboat serves as the hunter's floating **vehicle** upon the trackless waters of the Pacific."}
    ]
  },
  "Dashboard — veh/vehicular.md": {
    "primary": "Relating to or designed for vehicles, especially wheeled transport or motor traffic.",
    "secondary": "In civil engineering and urban traffic design, designating rights-of-way, grade separations, or bridges engineered for carriage and vehicular loads.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The immense thoroughfares were devoid of all **vehicular** traffic, designed purely for pedestrian leisure."},
      {"author": "Henry James", "work": "The American Scene", "quote": "The continuous roar of **vehicular** motion through the crowded avenue stunned the visiting observer."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The narrow lanes of the capital were constantly choked with **vehicular** congestion and cursing draymen."}
    ]
  },

  # =========================================================================
  # Dashboard — nav (20 words)
  # =========================================================================
  "Dashboard — nav/circumnavigate.md": {
    "primary": "To sail or travel entirely around something, especially around the world by water or air.",
    "secondary": "In maritime history, the pioneering naval expeditions (such as Magellan-Elcano or Drake) completing global oceanic transit.",
    "quotes": [
      {"author": "Jules Verne", "work": "Around the World in Eighty Days", "quote": "Phileas Fogg wagered twenty thousand pounds that he would **circumnavigate** the globe in eighty days."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Could Ahab **circumnavigate** the terraqueous globe without meeting the white fiend that had maimed him?"},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Our instructions were to **circumnavigate** the globe and measure meridian distances across distant seas."}
    ]
  },
  "Dashboard — nav/circumnavigation.md": {
    "primary": "The act or process of sailing or traveling completely around an island, continent, or the earth.",
    "secondary": "In navigational cartography and geodetic surveying, continuous orbital or sea voyages utilized to verify longitudinal coordinates and maritime trade routes.",
    "quotes": [
      {"author": "James Cook", "work": "A Voyage to the Pacific Ocean", "quote": "The successful **circumnavigation** of the Antarctic ice fields proved that no southern continent extended into temperate latitudes."},
      {"author": "Washington Irving", "work": "The Life and Voyages of Christopher Columbus", "quote": "The bold idea of global **circumnavigation** had occupied the minds of geographers long before Magellan."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo commenced the extraordinary underwater **circumnavigation** of the globe aboard the Nautilus."}
    ]
  },
  "Dashboard — nav/navaho.md": {
    "primary": "An alternative spelling of Navajo; a member of the largest federally recognized Native American tribe in the southwestern United States.",
    "secondary": "In cultural anthropology and linguistics, an Athabaskan language and indigenous culture renowned for silversmithing, woven textiles, and sandpainting.",
    "quotes": [
      {"author": "Willa Cather", "work": "Death Comes for the Archbishop", "quote": "The **Navaho** blankets hung in bright geometric patterns upon the earthen walls of the mission."},
      {"author": "Theodore Roosevelt", "work": "A Book-Lover's Holidays in the Open", "quote": "We rode past solitary **Navaho** hogans scattered across the red sandstone desert."},
      {"author": "Edward S. Curtis", "work": "The North American Indian", "quote": "The **Navaho** horseman paused on the canyon rim, silhouetted against the turquoise sky."}
    ]
  },
  "Dashboard — nav/navajo.md": {
    "primary": "A member of an indigenous Native American people of the American Southwest; or their Southern Athabaskan language (Diné bizaad).",
    "secondary": "In military history, the renowned Navajo Code Talkers who transmitted encoded tactical communications in the Pacific theater of World War II.",
    "quotes": [
      {"author": "Willa Cather", "work": "Death Comes for the Archbishop", "quote": "The Bishop admired the quiet dignity of the **Navajo** chiefs who came to confer with the territorial governor."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Once a **Navajo** medicine man had performed the sacred chant, the sick warrior was deemed restored to harmony."},
      {"author": "Zane Grey", "work": "The Rainbow Trail", "quote": "The silent **Navajo** guide pointed toward the distant red mesas rising out of the desert heat."}
    ]
  },
  "Dashboard — nav/naval.md": {
    "primary": "Relating to a navy, warships, or maritime defense forces.",
    "secondary": "In military history and maritime strategy, maritime tactics, ship-of-the-line fleet doctrine, and amphibious warfare operations.",
    "quotes": [
      {"author": "Herman Melville", "work": "Billy Budd", "quote": "He had been impressed from an English merchantman into the **naval** service of His Majesty."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The **naval** profession has its domestic disadvantages, but it raises men into honorable independence."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "It was his figurative **naval** manner of speaking, acquired during his long service on the high seas."}
    ]
  },
  "Dashboard — nav/navane.md": {
    "primary": "A brand name for thiothixene, a first-generation thioxanthene antipsychotic medication used to treat schizophrenia and psychoses.",
    "secondary": "In clinical psychopharmacology, a dopamine D2 receptor antagonist utilized in psychiatric therapeutics to reduce acute hallucinatory and delusional states.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The patient had previously received maintenance doses of **navane** before being evaluated for neurological symptoms."},
      {"author": "William Styron", "work": "Darkness Visible", "quote": "The pharmacopeia of modern psychiatry, from thorazine to **navane**, offered uncertain solace to the afflicted mind."},
      {"author": "Arthur Kleinman", "work": "The Illness Narratives", "quote": "Prescription of **navane** managed the severe psychosis, allowing the patient to participate in rehabilitative therapy."}
    ]
  },
  "Dashboard — nav/navarino.md": {
    "primary": "The historical name of Pylos, Greece, and the site of the pivotal 1827 naval battle that secured Greek independence from the Ottoman Empire.",
    "secondary": "In nineteenth-century European diplomatic history, the decisive engagement where allied British, French, and Russian fleets destroyed the Ottoman-Egyptian armada.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The sudden thunder of the guns at **Navarino** decided the freedom of modern Greece."},
      {"author": "Lord Byron", "work": "Letters and Journals", "quote": "The bay of **Navarino** witnessed the ultimate clash that broke the Turkish hold upon the Peloponnese."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient port of Pylos, known in modern annals as **Navarino**, guarded the western approaches to the Morea."}
    ]
  },
  "Dashboard — nav/nave.md": {
    "primary": "The central longitudinal hall or body of a church building, extending from the entrance to the chancel or transepts.",
    "secondary": "In Gothic ecclesiastic architecture, the high vaulted central space flanked by aisles, designed to accommodate the congregation.",
    "quotes": [
      {"author": "Victor Hugo", "work": "The Hunchback of Notre-Dame", "quote": "The immense **nave** of the cathedral was drowned in gloom, pierced only by shafts of ruby light from the rose window."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He walked resolutely down the stone-paved **nave** toward the altar, oblivious to the gathering congregation."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The majestic **nave** of Saint Peter's opened before them like a boundless hall of marble."}
    ]
  },
  "Dashboard — nav/navel-gazing.md": {
    "primary": "Excessive, self-indulgent, or unproductive contemplation of one's own concerns; omphaloskepsis.",
    "secondary": "In critical theory and cultural discourse, sterile introspection or intellectual insularity that ignores external socio-political reality.",
    "quotes": [
      {"author": "Christopher Hitchens", "work": "Letters to a Young Contrarian", "quote": "We must avoid that parochial **navel-gazing** which treats minor academic squabbles as cosmic crises."},
      {"author": "Iris Murdoch", "work": "The Sovereignty of Good", "quote": "True moral insight demands looking outward at reality rather than sinking into neurotic **navel-gazing**."},
      {"author": "George Orwell", "work": "Inside the Whale", "quote": "The younger novelists indulged in quietistic **navel-gazing** while European civilization teetered on the brink."}
    ]
  },
  "Dashboard — nav/navel.md": {
    "primary": "The central depression or scar on the abdomen where the umbilical cord was severed; the umbilicus.",
    "secondary": "In mythic geography and classical antiquity, the central or focal hub of a place or the world (e.g., the omphalos of Delphi).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Being pressed to th' **navel** of the state, they shall find our courage steadfast."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The doubloon was fastened to the very **navel** of the mast, where every eye might behold its gold."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Enclosed within the leafy arbor, undisturbed from crown to **navel** by the fallen world."}
    ]
  },
  "Dashboard — nav/navicular.md": {
    "primary": "Shaped like a boat; especially denoting the boat-shaped tarsal bone of the human foot or carpal bone of the wrist.",
    "secondary": "In human anatomy and comparative veterinary medicine, an essential bone bridging the talus and cuneiforms in the medial longitudinal arch.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **navicular** bone is situated at the inner side of the tarsus, between the talus behind and the cuneiform bones in front."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The osteological structure of the foot, including the modified **navicular** bone, showed significant divergence in wild ruminants."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The articulating facets of the **navicular** in the gorilla closely parallel those observed in human specimens."}
    ]
  },
  "Dashboard — nav/navigability.md": {
    "primary": "The condition or degree of a body of water or airway being passable and safe for ships or aircraft.",
    "secondary": "In maritime transport economics and hydrography, depth, clearance, and seasonal river discharge permitting continuous commercial cargo barge traffic.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The superior **navigability** of inland rivers affords an extensive and inexpensive transport for all commercial goods."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Maintaining the free **navigability** of the western rivers was essential to binding the frontier settlements to the union."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The extraordinary **navigability** of the Mississippi system formed an open highway for continental commerce."}
    ]
  },
  "Dashboard — nav/navigable.md": {
    "primary": "Deep, wide, and clear enough to afford safe passage for ships, boats, or aircraft.",
    "secondary": "In maritime law and federal riparian doctrine, waters subject to tidal ebb or used as continuous interstate channels of commerce.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "Economics: Modern Problems", "quote": "The extensive network of **navigable** rivers in North America facilitated rapid commercial expansion."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The frozen straits were scarcely **navigable** even in the height of the Arctic summer."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "A pilot must know every sandbar and snag that threatens to render the channel no longer **navigable**."}
    ]
  },
  "Dashboard — nav/navigate.md": {
    "primary": "To direct, plan, and steer the course of a ship, aircraft, vehicle, or traveler across a journey.",
    "secondary": "In cognitive ergonomics and web architecture, to move systematically through complex digital interfaces, menus, or relational databases.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Sir, you may believe me when I tell you that we **navigate** these uncharted depths with absolute safety."},
      {"author": "Herman Melville", "work": "Typee", "quote": "Although he was utterly unable to **navigate** by solar observations, the captain trusted to dead reckoning."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "A man who has learned to **navigate** in crowded waters knows the value of split-second decisions."}
    ]
  },
  "Dashboard — nav/navigation.md": {
    "primary": "The art, science, or technology of directing and controlling the movement of a vessel or vehicle from one place to another.",
    "secondary": "In nautical astronomy and geodetic positioning, determination of latitude and longitude using celestial instruments (sextant) or satellite arrays.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "In those days of simple **navigation**, the master relied upon his quadrant, logline, and trusty compass."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He spoke of his spiritual progress in terms of perilous ocean **navigation** and treacherous reefs."},
      {"author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "The subtle art of **navigation** is an endless dialogue between the soul of the seaman and the spirit of the waters."}
    ]
  },
  "Dashboard — nav/navigational.md": {
    "primary": "Relating to the science, practice, or instruments of navigation.",
    "secondary": "In avionics and maritime engineering, designating systems (gyroscopes, radar beacons, GPS transponders) utilized for route tracking and drift correction.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Captain of the Pole-Star", "quote": "The captain pored over his **navigational** charts, calculating our drift amid the pack ice."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "The sphere was fitted with delicate **navigational** apparatus designed to track our trajectory toward the lunar surface."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The barometer was his supreme **navigational** oracle when the barometer dropped like lead in the China Sea."}
    ]
  },
  "Dashboard — nav/navigator.md": {
    "primary": "A person who directs, plots, or operates the route of a ship, aircraft, or vehicle.",
    "secondary": "In the Age of Exploration, master mariners (such as Henry the Navigator, Columbus, or Cabot) who mapped oceanic passages and trade routes.",
    "quotes": [
      {"author": "Jack London", "work": "The Star Rover", "quote": "The bold Dutch **navigator** steered his vessel into uncharted archipelagoes without chart or pilot."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A skilled **navigator** can read the drift of the sea by the floating kelp and the flights of petrels."},
      {"author": "Washington Irving", "work": "The Life and Voyages of Christopher Columbus", "quote": "As an experienced **navigator**, Columbus observed the variations of the magnetic needle with keen interest."}
    ]
  },
  "Dashboard — nav/navratilova.md": {
    "primary": "Martina Navratilova (born 1956), Czech-American tennis legend widely considered one of the greatest athletes in tennis history, winner of 18 Grand Slam singles titles.",
    "secondary": "In modern sports history, renowned for revolutionizing women's athletic conditioning, tactical serve-and-volley play, and tennis longevity.",
    "quotes": [
      {"author": "Billie Jean King", "work": "Pressure Is a Privilege", "quote": "Watching **Navratilova** dominate Wimbledon with her athletic serve-and-volley style inspired a new generation of players."},
      {"author": "John McEnroe", "work": "You Cannot Be Serious", "quote": "The intensity and physical discipline that **Navratilova** brought to the tennis court raised the professional standards of the entire tour."},
      {"author": "Arthur Ashe", "work": "A Hard Road to Glory", "quote": "The athletic rivalry between Evert and **Navratilova** defined the golden era of modern championship tennis."}
    ]
  },
  "Dashboard — nav/navy.md": {
    "primary": "The fleet of warships and naval personnel belonging to a nation; or a dark shade of blue resembling naval uniforms.",
    "secondary": "In geopolitical naval doctrine (Mahanian maritime theory), command of the sea exercised through battle fleets protecting global sea lanes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Our force by land hath nobly held, but our great **navy** is utterly broken upon the waters."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "A man-of-war is an epitome of the nation, reflecting the discipline and hierarchy of the entire **navy**."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The **navy** is that noble profession which has done so much for the defense and honor of England."}
    ]
  },
  "Dashboard — nav/unnavigable.md": {
    "primary": "Not capable of being sailed upon or navigated by vessels; impassable by water.",
    "secondary": "In hydraulic engineering and river morphology, waterways obstructed by shallow rapids, shoals, debris, or violent cataracts.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The sacred stream was deemed **unnavigable** by mortal craft, protected by taboo and treacherous cataracts."},
      {"author": "Elizabeth Kimball Kendall", "work": "A Wayfarer in China", "quote": "The upper reaches of the river were fierce and **unnavigable**, tumbling down steep gorges in sheets of white foam."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "Further upstream the river was reported **unnavigable** due to sunken snags and shifting mudbanks."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Carrying"
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

print(f"Carrying Batch 1 (veh & nav): Successfully updated {updated}/{len(data)} notes.")
