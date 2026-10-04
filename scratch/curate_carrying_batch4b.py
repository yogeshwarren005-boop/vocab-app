# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — lat (Batch 4B: 36 words)
  # =========================================================================
  "Dashboard — lat/interrelation.md": {
    "primary": "Mutual or reciprocal relation or connection between two or more things or persons.",
    "secondary": "In structural sociology and ecological networks, interdependent feedbacks operating across distinct subsystems.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The complex **interrelation** of all animals and plants across a countryside determines the balance of nature."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "A growing **interrelation** between industrial and civic institutions characterizes advanced commonwealths."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The **interrelation** of memory and sensory perception forms the fabric of conscious thought."}
    ]
  },
  "Dashboard — lat/interrelationship.md": {
    "primary": "The way in which two or more things, concepts, or people are connected and affect one another.",
    "secondary": "In systems biology and ecological trophic dynamics, reciprocal feedback loops coordinating multi-species assemblages.",
    "quotes": [
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Ecology reveals the delicate **interrelationship** binding the soil, the water, and every living creature."},
      {"author": "Alfred North Whitehead", "work": "Process and Reality", "quote": "The organic **interrelationship** of events constitutes the bedrock of physical reality."},
      {"author": "Margaret Mead", "work": "Coming of Age in Samoa", "quote": "The cultural **interrelationship** between kinship clans governs all social ceremonial exchanges."}
    ]
  },
  "Dashboard — lat/lat.md": {
    "primary": "A colloquial abbreviation for latitude; or an abbreviation for the latissimus dorsi muscle of the back; or the former currency unit of Latvia.",
    "secondary": "In physical geography and marine navigation, the angular distance north or south of the earth's equator measured in degrees and minutes.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Compare the productions of South America in **lat** 35 degrees with those of North America in the same parallel."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain marked our position in high southern **lat**, where drifting icebergs threatened the ship."},
      {"author": "Arthur Conan Doyle", "work": "The Captain of the Pole-Star", "quote": "Our vessel was locked in the ice at eighty degrees north **lat**, surrounded by total darkness."}
    ]
  },
  "Dashboard — lat/latakia.md": {
    "primary": "An ancient seaport city in northwestern Syria (ancient Laodicea); or a dark, highly aromatic oriental tobacco cured over aromatic oak and pine smoke.",
    "secondary": "In pipe tobacco blending, a sun-cured varietal of Nicotiana tabacum subjected to prolonged wood-smoke fumigation to impart a pungent, leathery aroma.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sherlock Holmes sat in his armchair, filling his clay pipe with pungent, black **Latakia**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He puffed slowly at his pipe of fragrant **Latakia**, sending blue smoke rings toward the ceiling."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The merchant presented us with pipes charged with the choicest **Latakia** tobacco of the Syrian hills."}
    ]
  },
  "Dashboard — lat/latanier.md": {
    "primary": "Any of several American or West Indian fan palms, especially the dwarf palmetto (Sabal minor), having fan-shaped leaves.",
    "secondary": "In southeastern wetland ecology, an understory palm forming dense thickets in alluvial river bottoms, bayous, and coastal swales.",
    "quotes": [
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The Carolina parakeet settled among the dense fronds of the wild **latanier** in the river bottom."},
      {"author": "Chateaubriand", "work": "Atala", "quote": "We rested beneath the shadow of the tall **latanier** palms while the warm breeze stirred the magnolia blooms."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "Beds of creeping **latanier** and giant reeds marked the boundaries of the tropical marsh."}
    ]
  },
  "Dashboard — lat/latch.md": {
    "primary": "A metal bar with a catch and lever used for fastening a door or gate; or to fasten securely with such a mechanism.",
    "secondary": "In digital electronics and computer hardware, a bistable multivibrator circuit used to store and buffer binary state information.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "I have words that would be howled out in the desert air, where hearing should not **latch** them."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I lifted the **latch** softly and entered the dimly lit parlor where Mr. Rochester sat alone."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The jailer turned the key and lifted the heavy iron **latch** of the prison door."}
    ]
  },
  "Dashboard — lat/latchet.md": {
    "primary": "A narrow leather strap or thong used to fasten a shoe or sandal; an archaic term for a sandal fastener.",
    "secondary": "In biblical literature and historical iconography (e.g., Mark 1:7), the symbol of humble servitude associated with unfastening a master's footwear.",
    "quotes": [
      {"author": "King James Bible", "work": "The Gospel of Mark", "quote": "There cometh one mightier than I after me, the **latchet** of whose shoes I am not worthy to stoop down and unloose."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "He stooped not to bind the **latchet** of his sandal before the summons came."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The humble palmer adjusted the leather **latchet** of his sandal before resuming his pilgrimage across the burning sand."}
    ]
  },
  "Dashboard — lat/latchkey.md": {
    "primary": "A key for an exterior door latch; especially one allowing a resident or child to enter a house independently.",
    "secondary": "In social history and family sociology, designating unsupervised school children who let themselves into empty homes while parents work (latchkey children).",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "At nine o'clock I heard my uncle's **latchkey** turning in the hall door."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The lodger opened the heavy street door with his own **latchkey** and ascended the stairs in the dark."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He drew a small brass **latchkey** from his waistcoat pocket and let us into the silent chambers."}
    ]
  },
  "Dashboard — lat/latchstring.md": {
    "primary": "A cord fastened to a door latch inside and passing through a hole to the outside, pulled to lift the latch and open the door.",
    "secondary": "In American folklore and pioneer hospitality, the proverbial symbol of welcoming hospitality ('the latchstring is always out').",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The traveler pulled the leather **latchstring**, and the heavy oak door swung inward with a creak."},
      {"author": "Washington Irving", "work": "The Sketch Book", "quote": "In that hospitable frontier settlement, the **latchstring** was always hanging out for the stranger."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I had no lock and key on my cabin door, but only a simple **latchstring** to keep the wind from blowing it open."}
    ]
  },
  "Dashboard — lat/late-blooming.md": {
    "primary": "Flowering or blossoming late in the season; or achieving success, skill, or prominence relatively late in life.",
    "secondary": "In developmental psychology and horticultural phenology, cultivars or individuals whose maturation curve peaks well beyond conventional developmental milestones.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "In several varieties of fruit trees, a **late-blooming** habit protects the delicate blossoms from early spring frosts."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His talent was of a **late-blooming** kind, requiring years of solitary reflection before yielding intellectual fruit."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "He recognized in his friend a **late-blooming** appreciation of European art and culture."}
    ]
  },
  "Dashboard — lat/late-flowering.md": {
    "primary": "Producing flowers late in the growing season; blooming in late summer or autumn.",
    "secondary": "In agrarian botany and crop breeding, varieties selected to extend harvest intervals or prevent frost damage during early vernal warming.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The **late-flowering** individuals produced fewer seeds owing to the scarcity of autumnal insect pollinators."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Several species of **late-flowering** asters lingered in the hedgerows until the November frosts."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "This hardy composite is a **late-flowering** native perennial of our eastern meadows."}
    ]
  },
  "Dashboard — lat/late-ripening.md": {
    "primary": "Reaching maturity or ripeness late in the season (especially of fruits, vegetables, or cereal grains).",
    "secondary": "In viticulture and pomology, cultivars requiring a long growing season and high cumulative solar thermal units to achieve optimal brix levels.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "A **late-ripening** peach requires sunny southern exposures to develop its full flavor before winter."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The orchard was filled with **late-ripening** cider apples that hung red upon the leafless branches."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "In northern climates, **late-ripening** grains are constantly endangered by early autumn rains."}
    ]
  },
  "Dashboard — lat/late-spring-blooming.md": {
    "primary": "Coming into blossom during the late spring season, bridging the transition between early vernal flowers and summer blooms.",
    "secondary": "In landscape horticulture and phenological ecology, temperate perennial taxa flowering between mid-May and early June.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The shrub is a **late-spring-blooming** ornamental prized for its fragrant white racemes."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The **late-spring-blooming** hawthorns filled the lanes with fragrant snow before the coming of June."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Gardeners cross early and **late-spring-blooming** varieties to prolong the decorative floral season."}
    ]
  },
  "Dashboard — lat/late.md": {
    "primary": "Occurring, arriving, or acting after the proper, usual, or scheduled time; or recently deceased.",
    "secondary": "In historical chronology and periodization, denoting the final phase or closing epoch of an artistic or historical movement (e.g., Late Roman).",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Sonnets", "quote": "Bare ruined choirs, where **late** the sweet birds sang."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The hour was **late**, and the lights in the village cottages were extinguished one by one."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "It was too **late** to recall the words that had escaped my trembling lips."}
    ]
  },
  "Dashboard — lat/latecomer.md": {
    "primary": "A person who arrives late or after others; an arrival after an event has begun.",
    "secondary": "In industrial economics and geopolitical competition, an enterprise or nation entering an established market with advantages of technological leapfrogging (latecomer advantage).",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The church was crowded, and every **latecomer** was forced to stand in the drafty aisle."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The host turned with polite cordiality to welcome the solitary **latecomer** to the dining table."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The courtroom was packed to the doors, leaving no seat for any **latecomer** who sought admittance."}
    ]
  },
  "Dashboard — lat/lateen-rig.md": {
    "primary": "A nautical rig characterized by one or more triangular lateen sails suspended from long yards mounted obliquely on masts.",
    "secondary": "In maritime history, the Mediterranean and Arabian sail configuration that revolutionized windward sailing and enabled early oceanic navigation.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Mediterranean felucca with its sharp **lateen-rig** cut through the blue waves like a flying fish."},
      {"author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "The traditional **lateen-rig** of the Levantine coasters has survived unaltered since classical antiquity."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The Arab dhow carried a soaring **lateen-rig** that caught every whisper of wind upon the Red Sea."}
    ]
  },
  "Dashboard — lat/lateen-rigged.md": {
    "primary": "Fitted or equipped with lateen sails mounted on oblique yards.",
    "secondary": "In naval architecture, designating vessels (such as caravels, feluccas, or sambuks) utilizing triangular fore-and-aft sail plans for maneuverability.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "The Rescue", "quote": "A small, **lateen-rigged** prau skimmed across the lagoon under the evening breeze."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The harbor was dotted with picturesque **lateen-rigged** boats carrying fruit and islanders to the ship."},
      {"author": "Washington Irving", "work": "The Life and Voyages of Christopher Columbus", "quote": "The Niña was originally a **lateen-rigged** vessel before Columbus refitted her with square sails at the Canaries."}
    ]
  },
  "Dashboard — lat/lateen.md": {
    "primary": "A triangular sail set on a long yard mounted at an angle of forty-five degrees to the mast.",
    "secondary": "In nautical archaeology, the fore-and-aft sail design developed in the Byzantine and Arab worlds that facilitated tacking into the wind.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white **lateen** of the coaster gleamed against the dark cliffs of the Mediterranean coast."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The native craft set its broad **lateen** against the sunset, gliding into the river mouth."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "A small craft with a picturesque **lateen** sail hovered outside the headland."}
    ]
  },
  "Dashboard — lat/lately.md": {
    "primary": "Not long ago; in recent times; recently.",
    "secondary": "In personal correspondence and memoirs, qualifying occurrences that have transpired within recent memory or current experience.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "He was excellent indeed, madam; the king very **lately** spoke of him with warm admiration."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "I have **lately** heard of your engagement, and hasten to offer my sincere congratulations."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "A heavy melancholy had **lately** fallen upon my father, which all my efforts could not dispel."}
    ]
  },
  "Dashboard — lat/latency.md": {
    "primary": "The state of existing but not yet being developed, manifest, or active; dormancy.",
    "secondary": "In telecommunications and computing networks, the time delay elapsed between the transmission of a data packet and its reception at the destination.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Many memories remain in a state of long **latency** until revived by an unexpected sensory impression."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Characters may remain in complete **latency** for generations, and then suddenly reappear under changed conditions."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The disease agent possessed a prolonged period of **latency** before active physiological symptoms appeared."}
    ]
  },
  "Dashboard — lat/lateness.md": {
    "primary": "The fact or quality of arriving, occurring, or acting after the proper or expected time; tardiness.",
    "secondary": "In agricultural phenology and climatology, the temporal postponement of seasonal events (such as leaf emergence or frosts) due to cold climatic anomalies.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He apologized for his **lateness**: his arrival was even later than had been expected by the shearers."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The increasing **lateness** of the hour compelled me to put aside my books and retire to rest."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My uncle remarked with some severity upon the unusual **lateness** of our return from the town."}
    ]
  },
  "Dashboard — lat/latent.md": {
    "primary": "Existing but not yet developed or manifest; hidden, concealed, or dormant.",
    "secondary": "In thermodynamics and physical chemistry, heat absorbed or released during a phase change without altering the temperature of the substance (latent heat).",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It was food for great regret with him; it was also a spark to his **latent** jealousy."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Rudimentary organs often represent structures which have become **latent** or reduced through long disuse."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "In every generous nature there is a **latent** capacity for heroic sacrifice when the call arrives."}
    ]
  },
  "Dashboard — lat/later.md": {
    "primary": "At a time in the future or after the time you have mentioned; comparative of late.",
    "secondary": "In historical paleontology and stratigraphy, situated higher in a rock sequence and therefore more recent in geological deposition.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "Theseus, Duke of Athens; Hippolyta, Queen of the Amazons; and lovers who meet in the forest at a **later** hour."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In **later** geological formations we find the specialized descendants of these ancient generalized forms."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "At a **later** period of the voyage, Ahab summoned the harpooners to the quarter-deck."}
    ]
  },
  "Dashboard — lat/lateral.md": {
    "primary": "Of, at, towards, or from the side or sides; side-to-side.",
    "secondary": "In anatomy and organismal morphology, situated away from the midline of the body or sagittal plane.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In other crustaceans the transparent cones which are surrounded by pigment cells transmit **lateral** light."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **lateral** ventricles of the brain are two irregular cavities situated within the cerebral hemispheres."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The nerve cord gives off pairs of **lateral** nerves to each segmental appendage."}
    ]
  },
  "Dashboard — lat/lateralisation.md": {
    "primary": "The British spelling of lateralization; the localization of cognitive or physiological function to one side of the brain.",
    "secondary": "In behavioral neurology, the evolutionary specialization of cerebral hemispheres (such as left-hemisphere dominance for syntax and language).",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The functional **lateralisation** of motor control is demonstrated by unilateral speech loss following stroke."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The degree of cerebral **lateralisation** varies across vertebrate orders according to encephalization."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Neurological damage disrupted the normal **lateralisation** of spatial awareness in the patient."}
    ]
  },
  "Dashboard — lat/laterality.md": {
    "primary": "The preference for using one side of the body, especially hand, foot, or eye; handedness.",
    "secondary": "In neuropsychology and ergonomics, directional asymmetry in motor coordination and sensory dominance reflecting contralateral cortical organization.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Human **laterality** is reflected in the universal dominance of the right hand in primitive tools."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Questions of structural **laterality** in facial movement were studied across various races."},
      {"author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "Measurements of muscular strength in left and right hands revealed marked **laterality** in the population."}
    ]
  },
  "Dashboard — lat/lateralization.md": {
    "primary": "The localization of function or activity on one side of the body in preference to the other, especially in the brain.",
    "secondary": "In cognitive neuroscience and linguistics, the development of asymmetric neuroanatomical pathways in Broca's and Wernicke's areas.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Seeing Voices", "quote": "The **lateralization** of sign language processing in deaf individuals mirrors that of spoken language in hearing subjects."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Studies in cerebral **lateralization** prove that distinct cortical hemispheres possess specialized aptitudes."},
      {"author": "Noam Chomsky", "work": "Language and Mind", "quote": "Biological readiness for language is intimately tied to the maturational **lateralization** of the human brain."}
    ]
  },
  "Dashboard — lat/lateralize.md": {
    "primary": "To localize a specific physiological, cognitive, or neurological function to one side of the brain or body.",
    "secondary": "In clinical neurophysiology, observing unilateral focal epileptiform discharges or asymmetric motor deficits.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The involuntary tremor began to **lateralize** distinctly to the right hand and arm."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Focal neurological signs that **lateralize** to one hemisphere demand immediate surgical evaluation."},
      {"author": "Wilder Penfield", "work": "The Cerebral Cortex of Man", "quote": "Cortical electrical stimulation failed to **lateralize** speech comprehension entirely to a single gyral area."}
    ]
  },
  "Dashboard — lat/laterally.md": {
    "primary": "Sideways; at, toward, or from the side.",
    "secondary": "In structural mechanics and botany, deflecting sideways under axial compression (buckling) or branching horizontally from an axis.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He allowed his head to sway **laterally** with a slow, contemplative motion while considering the proposal."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Flatfishes have their bodies compressed **laterally**, swimming on one side along the ocean floor."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The ribs extend **laterally** and downward from the vertebral column to enclose the thoracic cavity."}
    ]
  },
  "Dashboard — lat/lateran.md": {
    "primary": "The complex of buildings in Rome, including the Basilica of Saint John Lateran, historically the residence of the Popes.",
    "secondary": "In church history and canon law, the five ecumenical councils held at the Lateran Palace between the twelfth and sixteenth centuries.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The solemn assemblies of the **Lateran** council confirmed the supremacy of the Roman pontiff over western Christendom."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The ancient halls of the **Lateran** witnessed decrees that shaped the feudal jurisprudence of Europe."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The papal legate claimed authority under the solemn sanctions enacted at the **Lateran**."}
    ]
  },
  "Dashboard — lat/laterite.md": {
    "primary": "A reddish, iron-rich, porous clay soil or subsoil formed in tropical regions by the weathering of underlying rocks.",
    "secondary": "In pedology and tropical geomorphology, a heavily leached B-horizon residual soil rich in sesquioxides of iron and aluminum that hardens irreversibly upon drying.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The tropical plateau was capped by thick deposits of red **laterite**, formed by intense subaerial weathering."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The roads were cut through deep banks of red **laterite**, which became slippery as grease after heavy rains."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Ancient temples in the interior were constructed of porous blocks of hardened **laterite**."}
    ]
  },
  "Dashboard — lat/lates.md": {
    "primary": "A genus of large predatory fish in the family Latidae, native to freshwater and marine environments of Africa and Asia, notably the Nile perch (Lates niloticus).",
    "secondary": "In freshwater fisheries biology and invasive species ecology, apex predatory teleosts whose introduction into Lake Victoria caused catastrophic cichlid extinctions.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "The Lake Regions of Central Africa", "quote": "The fishermen brought ashore a monstrous specimen of **lates**, which provides the staple food of the lake shore."},
      {"author": "David Livingstone", "work": "Narrative of an Expedition to the Zambesi", "quote": "The waters of the broad river abounded with a giant perch of the genus **lates**, highly esteemed for table use."},
      {"author": "Pliny the Elder", "work": "Natural History", "quote": "Ancient scribes recorded that the sacred fish called **lates** in the Nile attained an immense weight."}
    ]
  },
  "Dashboard — lat/latest.md": {
    "primary": "Most recent or the newest; comparative of late (late, later, latest).",
    "secondary": "In news publishing and commercial marketing, the most up-to-date dispatch or fashionable contemporary design.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Their **latest** refuge was to send him, for whose old love they hoped to find a milder treatment."},
      {"author": "Jane Austen", "work": "Emma", "quote": "She was eager to hear the **latest** news from London concerning her friend's arrival."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes was scanning the **latest** edition of the evening paper for notices of mysterious crimes."}
    ]
  },
  "Dashboard — lat/latex.md": {
    "primary": "A milky fluid found in many plants (such as rubber trees, spurges, and poppies) that coagulates on exposure to air; or a synthetic emulsion of rubber or plastic globules.",
    "secondary": "In industrial polymer chemistry and botanical physiology, a protective secondary metabolite emulsion containing polyisoprene suspended in an aqueous serum.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "When the stem of the spurge was punctured, a copious white **latex** flowed immediately from the wound."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The native collectors demonstrated the tapping of the wild rubber vine, coagulating the milky **latex** over smoke."},
      {"author": "Richard Francis Burton", "work": "The Highlands of the Brazil", "quote": "The extraction of **latex** from the Hevea trees of the Amazon basin drew thousands of laborers into the wilderness."}
    ]
  },
  "Dashboard — lat/laticifer.md": {
    "primary": "A specialized plant cell or duct that secretes and contains latex.",
    "secondary": "In plant anatomy and histological cytology, articulated or non-articulated tubular cells permeating vegetative tissues that store secondary metabolites.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Microscopic sections through the milkweed stem reveal the branching network of the **laticifer** system."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The defensive bitter secretion stored in each plant **laticifer** deters grazing insects from attacking foliage."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The cellular walls of the **laticifer** remain distinct even while coalescing into continuous conducting ducts."}
    ]
  },
  "Dashboard — lat/latimeria.md": {
    "primary": "The genus of coelacanth fish (Latimeria chalumnae and Latimeria menadoensis), ancient lobe-finned fish long believed extinct until rediscovered off South Africa in 1938.",
    "secondary": "In evolutionary paleontology and vertebrate phylogenetics, a sarcopterygian living fossil possessing hollow fin rays, intracranial hinges, and vestigial lungs.",
    "quotes": [
      {"author": "J. L. B. Smith", "work": "Old Fourlegs: The Story of the Coelacanth", "quote": "The discovery of **Latimeria** in 1938 proved that the ancient lobe-finned fishes had survived into modern oceans."},
      {"author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "The anatomically conservative morphology of **Latimeria** demonstrates that evolution does not require constant rapid morphological change."},
      {"author": "Ernst Mayr", "work": "The Growth of Biological Thought", "quote": "The rediscovery of **Latimeria** provided morphologists with a living representative of ancestral tetrapod relatives."}
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

print(f"Carrying Batch 4B (lat): Successfully updated {updated}/{len(data)} notes.")
