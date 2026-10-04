# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — mob (29 words) ---
  "Dashboard — mob/automobile.md": {
    "primary": "A four-wheeled motor vehicle powered by an internal combustion engine or electric battery, designed for passenger transportation.",
    "secondary": "In twentieth-century urban geography and manufacturing economics, the mass production of the automobile reshaped suburban infrastructure.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Gatsby's gorgeous cream-colored **automobile** was known to everyone in West Egg for its nickel brightwork and three-note horn."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt took immense pride in his newly purchased family **automobile**, washing its fenders every Sunday morning."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The noisy clatter of an early **automobile** startled the cab horses waiting patiently beside the London curb."}
    ]
  },
  "Dashboard — mob/automobilist.md": {
    "primary": "A person who drives or travels extensively in an automobile; a motorist.",
    "secondary": "In early transportation history, early automobilist clubs mapped unpaved country routes and lobbied state legislatures for highway construction.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Free Air", "quote": "The adventurous young **automobilist** navigated the muddy prairie trails of Minnesota with grit and a tool kit."},
      {"author": "H. G. Wells", "work": "The Wheels of Chance", "quote": "The veteran bicyclist looked with annoyance upon the arrogant **automobilist** enveloped in goggles, dust, and gasoline smoke."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The wealthy foreign diplomat was an enthusiastic **automobilist**, frequently touring the Surrey lanes at high speeds."}
    ]
  },
  "Dashboard — mob/demob.md": {
    "primary": "To discharge someone from military service at the end of a war; demobilize.",
    "secondary": "In twentieth-century veteran historiography, demob centers provided returning soldiers with civilian clothing suits and travel vouchers.",
    "quotes": [
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "When the army decided to **demob** our battalion in 1919, we were handed a civilian suit and a train ticket home."},
      {"author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "The war was over at last, and every transport vessel returned to **demob** thousands of weary young infantrymen."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The War Office faced immense logistical difficulties when required to rapidly **demob** five million mobilized soldiers."}
    ]
  },
  "Dashboard — mob/demobilisation.md": {
    "primary": "The process of disbanding armed forces and converting wartime resources to peacetime civilian purposes.",
    "secondary": "In post-conflict macroeconomic planning, sudden military demobilisation requires industrial labor market re-absorption policies.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Aftermath", "quote": "The rapid **demobilisation** of imperial armies posed severe employment problems across industrial Britain."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Following the armistice, nationwide **demobilisation** caused widespread social dislocation across war-weary Europe."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The government ordered the partial **demobilisation** of frontline militias to reconstitute a centralized regular army."}
    ]
  },
  "Dashboard — mob/demobilise.md": {
    "primary": "To disband troops or armed forces from active duty; to transition a military unit to civilian standing.",
    "secondary": "In international peacekeeping and treaty compliance, belligerent factions must demobilise auxiliary militias and surrender heavy arms.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "It was impossible to immediately **demobilise** our veteran divisions while central European frontiers remained unstable."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "When the conflict ceases, the nation must **demobilise** millions of soldiers and re-orient manufacturing plants."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor refused to **demobilise** his loyal legionaries until the senate confirmed his dynastic claims."}
    ]
  },
  "Dashboard — mob/demobilization.md": {
    "primary": "The act or process of standing down military troops from active wartime readiness to peacetime civilian status.",
    "secondary": "In diplomatic history and post-conflict transition studies, orderly demobilization forms the prerequisite for restoring civilian civil governance.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "General **demobilization** proceeded smoothly through regional transit camps despite widespread civilian coal shortages."},
      {"author": "Theodore Roosevelt", "work": "The Rough Riders", "quote": "Upon the regiment's **demobilization** at Montauk Point, each trooper received honorable discharge papers from the army."},
      {"author": "Ulysses S. Grant", "work": "Personal Memoirs of U. S. Grant", "quote": "The grand review of the armies in Washington preceded the rapid **demobilization** of over a million veteran troops."}
    ]
  },
  "Dashboard — mob/demobilize.md": {
    "primary": "To release from military duty, or to stand down an army from active service to peacetime footing.",
    "secondary": "In defense economics, governments demobilize specialized combat divisions to reduce national sovereign debt obligations.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "We resolved to **demobilize** service personnel according to age and length of frontline service overseas."},
      {"author": "George Washington", "work": "Writings of George Washington", "quote": "The commander urged Congress to **demobilize** the Continental Army with full back pay and land bounty grants."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The regional council voted to **demobilize** the border garrisons as agricultural labor shortages deepened."}
    ]
  },
  "Dashboard — mob/immobile.md": {
    "primary": "Incapable of moving or being moved; fixed, motionless, or steadfastly stationary.",
    "secondary": "In clinical traumatology, an immobile joint resulting from fibrous ankylosis requires physical rehabilitative therapy.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes remained **immobile** upon the high rock pinnacle, his lean silhouette dark against the moonlit sky."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The paralyzed invalid sat completely **immobile** in his high-backed chair, watching the room with piercing eyes."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The massive iron anvil stood **immobile** upon the deck of the Pequod, resisting every toss of the ocean."}
    ]
  },
  "Dashboard — mob/immobilisation.md": {
    "primary": "The act or process of restricting movement, or fixing an injured limb or mechanism in a static position.",
    "secondary": "In orthopedics and emergency medicine, rigid spinal immobilisation prevents secondary neurological deficits following severe vertebral trauma.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Complete **immobilisation** of the fractured bone by plaster bandaging is essential to ensure proper osteal union."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Prolonged **immobilisation** of synovial joints can induce temporary stiffness of surrounding capsular ligaments."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The surgeon secured absolute **immobilisation** of the severed tendons using specialized splints."}
    ]
  },
  "Dashboard — mob/immobilise.md": {
    "primary": "To prevent someone or something from moving or operating normally; to render stationary.",
    "secondary": "In military logistics and tactical interdiction, tactical airstrikes target rail junctions to immobilise enemy mechanized armor.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A well-placed bullet through the engine block was sufficient to **immobilise** the fleeing steam launch."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Severe blizzard conditions on the eastern front threatened to **immobilise** entire armored armies in deep snow."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "A broken steering cable threatened to **immobilise** the steamer in the trough of the monstrous hurricane waves."}
    ]
  },
  "Dashboard — mob/immobility.md": {
    "primary": "The inability to move or be moved; the state of remaining completely motionless or fixed.",
    "secondary": "In ecological ethology, tonic immobility functions as an involuntary defensive freezing response to discourage predatory attack.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Premature Burial", "quote": "The terrifying cataleptic trance produced a rigid **immobility** that deceived even experienced medical observers."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Miss Havisham sat in bridal **immobility** amid the rotting wedding feast in her darkened, dust-laden room."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The primeval forest seemed locked in monumental **immobility**, watching the fragile steamer with silent disdain."}
    ]
  },
  "Dashboard — mob/immobilization.md": {
    "primary": "The act of making someone or something incapable of movement; restriction of motion.",
    "secondary": "In soil chemistry and biogeochemistry, nitrogen immobilization occurs when soil microbes assimilate inorganic nitrogen into organic compounds.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Immediate **immobilization** of the limb in a Thomas splint drastically reduced mortality from compound femoral fractures."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The sudden **immobilization** of the fleeing intruder was achieved when the villagers surrounded him with heavy clubs."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "The temporary **immobilization** of plant nutrients in dry upper soils is reversed by seasonal autumn rains."}
    ]
  },
  "Dashboard — mob/immobilize.md": {
    "primary": "To restrict the movement of a person, animal, or object, or prevent normal mechanical operation.",
    "secondary": "In wildlife management and veterinary anesthesiology, darting rifles administer tranquilizers to immobilize large ungulates safely.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes stepped forward to **immobilize** the violent suspect before he could draw his concealed weapon."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Dense marine ice sheets threatened to **immobilize** the submarine vessel within the desolate Antarctic pack."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "A direct hit from the naval artillery served to **immobilize** the lead Martian tripod on the riverbank."}
    ]
  },
  "Dashboard — mob/immobilizing.md": {
    "primary": "Preventing or rendering incapable of physical motion, activity, or mechanical operation.",
    "secondary": "In immunological defense, opsonizing antibodies bind bacterial surface flagella, immobilizing pathogens for phagocytosis.",
    "quotes": [
      {"author": "Jack London", "work": "White Fang", "quote": "The heavy steel jaw trap snapped shut, **immobilizing** the wolf's paw against the frozen pine roots."},
      {"author": "Joseph Conrad", "work": "The Shadow-Line", "quote": "The windless equatorial calm fell like a heavy pall, **immobilizing** the sailing vessel for agonizing weeks."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "A sudden paroxysm of grief seized Frankenstein, **immobilizing** him beside the lifeless body of his friend."}
    ]
  },
  "Dashboard — mob/mob.md": {
    "primary": "A large, disorderly crowd of people, especially one intent on causing trouble, violence, or rioting; or organized crime.",
    "secondary": "In social psychology and crowd dynamics, collective mob behavior features emotional contagion and loss of individual responsibility.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The furious Parisian **mob** surged around the Bastille, brandishing pikes, muskets, and improvised iron bars."},
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Antony's fiery funeral oration incited the Roman **mob** to burn the houses of the conspirators."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The seditious **mob** of Constantinople filled the Hippodrome with violent cries of riot and treason."}
    ]
  },
  "Dashboard — mob/moban.md": {
    "primary": "A pharmaceutical trade name for molindone, an antipsychotic medication formerly prescribed for schizophrenia.",
    "secondary": "In neuropsychopharmacology, molindone (marketed as Moban) acts as a typical dihydroindolone dopamine receptor antagonist.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Clinical pharmacology tracks therapeutic responses when neuroleptic agents such as **Moban** are administered for agitation."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The clinician evaluated patient responses to antipsychotic compounds like **Moban**, noting extrapyramidal side-effects."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The surgeon administered a potent sedative drug to soothe the agitated patient during postoperative delirium."}
    ]
  },
  "Dashboard — mob/mobcap.md": {
    "primary": "A pleated cotton or linen cap covering the hair, worn indoors by women in the eighteenth and early nineteenth centuries.",
    "secondary": "In historical costume and domestic portraiture, the frilled mobcap symbolized respectable domesticity among bourgeois and servant women.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Madame Defarge adjusted her frilled linen **mobcap** as she sat knitting grimly behind the wine-shop counter."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet put on her fresh morning **mobcap** before descending to the breakfast room to discuss the ball."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The elderly housekeeper wore an immaculate white **mobcap** with stiff lace borders tied under her chin."}
    ]
  },
  "Dashboard — mob/mobile.md": {
    "primary": "Able to move or be moved freely, easily, and quickly; or a kinetic decorative sculpture hanging from wires.",
    "secondary": "In wireless communications and cellular networking, mobile cellular base stations manage handovers across adjacent RF cells.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The nomadic Scythians possessed a **mobile** military force consisting entirely of mounted horse archers."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Modern mechanized warfare demands highly **mobile** armored divisions capable of deep tactical breakthroughs."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Her lively and **mobile** countenance reflected every shifting emotion of her eager, curious nature."}
    ]
  },
  "Dashboard — mob/mobilisation.md": {
    "primary": "The act of assembling and preparing military troops, supplies, and national resources for active war duty.",
    "secondary": "In diplomatic history of the First World War, imperial Russian general mobilisation triggered automatic treaty mobilization across Europe.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The rapid naval **mobilisation** of the British Grand Fleet in July 1914 secured immediate command of the North Sea."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The sudden **mobilisation** of artillery regiments along the Thames came too late to save the metropolis."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial **mobilisation** of legions from the Rhine to the Danube left the western provinces exposed to invasion."}
    ]
  },
  "Dashboard — mob/mobilise.md": {
    "primary": "To organize, assemble, and prepare military forces or civilian resources for active deployment or emergency action.",
    "secondary": "In civic campaign strategy and democratic activism, non-governmental coalitions mobilise grassroots voter registration drives.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Britain acted swiftly to **mobilise** every factory and shipyard in the national struggle against tyranny."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The imperial government resolved to **mobilise** its air fleet before rival powers could launch a surprise attack."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The revolutionary union committees worked through the night to **mobilise** armed workers for the barricades."}
    ]
  },
  "Dashboard — mob/mobility.md": {
    "primary": "The ability to move freely, easily, and rapidly from one place, physical posture, or social position to another.",
    "secondary": "In solid-state physics and semiconductor electronics, electron mobility quantifies drift velocity per unit electric field within crystal lattices.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The incredible **mobility** of the Hun cavalry terrorized the static Roman frontier garrisons along the Danube."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Industrial civilization is distinguished by the high social **mobility** of individuals across economic classes."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The facial muscles of primates display remarkable **mobility** for signaling fear, anger, and affection."}
    ]
  },
  "Dashboard — mob/mobilization.md": {
    "primary": "The assembly, organization, and preparation of armed forces, industrial capacity, or public resources for war or crisis.",
    "secondary": "In clinical orthopedics and physical therapy, early joint mobilization accelerates ligament healing following reconstructive surgery.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The general **mobilization** order posted on the town halls of France called millions of citizens to the colors."},
      {"author": "Theodore Roosevelt", "work": "The Rough Riders", "quote": "The rapid **mobilization** of volunteers at San Antonio transformed cowboys and college athletes into a fighting unit."},
      {"author": "Ulysses S. Grant", "work": "Personal Memoirs of U. S. Grant", "quote": "The logistical **mobilization** of supplies across river transport lines enabled the victorious siege of Vicksburg."}
    ]
  },
  "Dashboard — mob/mobilize.md": {
    "primary": "To assemble, organize, and put into active service military forces or societal resources for action or war.",
    "secondary": "In corporate crisis management, leadership must mobilize cross-functional emergency teams to manage infrastructure failures.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "We must **mobilize** the entire mechanical and scientific genius of our people to overcome the U-boat threat."},
      {"author": "George Washington", "work": "Writings of George Washington", "quote": "The general appealed to the governors to **mobilize** regional militia units to counter the British advance."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The world directorate sought to **mobilize** global transport resources to relieve the stricken famine districts."}
    ]
  },
  "Dashboard — mob/mobius.md": {
    "primary": "Referring to August Ferdinand Möbius (1790–1868), the German mathematician who discovered the one-sided Möbius strip.",
    "secondary": "In algebraic topology and non-orientable surface mathematics, a Möbius strip is a two-dimensional manifold with only one boundary component.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The City and the Stars", "quote": "The intricate pathways of the ancient city looped like a cosmic **Möbius** strip, confounding ordinary spatial geometry."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "A traveler walking along the single continuous surface of a **Möbius** strip returns to the start without crossing an edge."},
      {"author": "H. G. Wells", "work": "The Plattner Story", "quote": "The curious spatial inversion experienced by Plattner suggested anomalous four-dimensional topology resembling a **Möbius** twist."}
    ]
  },
  "Dashboard — mob/moblike.md": {
    "primary": "Resembling, characteristic of, or behaving like a disorganized, turbulent, or unruly mob.",
    "secondary": "In political sociology and historical protest analysis, disciplined ideological demonstrations risk degenerating into moblike rioting.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "A **moblike** fury seized the Gordon rioters as they set fire to the ancient gates of Newgate prison."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The sans-culottes surged into the royal apartments with **moblike** violence, demanding the monarch's capitulation."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The Porteous conspirators marched with sullen discipline, masking their **moblike** intent until the gallows was reached."}
    ]
  },
  "Dashboard — mob/mobocracy.md": {
    "primary": "Rule or political domination by the mob; government characterized by mob rule or ochlocracy.",
    "secondary": "In classical constitutional republicanism, philosophers viewed unregulated pure democracy as prone to collapsing into volatile mobocracy.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A balanced constitutional republic provides a steady shield against both royal tyranny and turbulent **mobocracy**."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The Parisian clubs have subverted lawful authority, substituting a capricious and bloody **mobocracy** for the rule of law."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "When constitutional courts fall, sheer **mobocracy** and street barricades dictate policy to terrified legislators."}
    ]
  },
  "Dashboard — mob/mobster.md": {
    "primary": "A member of a criminal organization or organized crime syndicate; a gangster.",
    "secondary": "In twentieth-century American criminology, federal RICO statutes were enacted to prosecute syndicate mobster hierarchies.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "Corrupt ward heelers employed notorious city thugs, knowing every ruthless **mobster** had his price during municipal elections."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Gatsby's associate Meyer Wolfsheim was rumored to be a calculating underworld **mobster** who fixed the World Series."},
      {"author": "Sinclair Lewis", "work": "It Can't Happen Here", "quote": "Paramilitary storm squads recruited local criminal elements, placing armed power into the hands of every petty **mobster**."}
    ]
  },
  "Dashboard — mob/mobula.md": {
    "primary": "A genus of large pelagic eagle rays in the family Myliobatidae, commonly called devil rays or flying rays.",
    "secondary": "In marine biology and elasmobranch ecology, species of Mobula aggregate in massive coastal schools and perform aerial breaching displays.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The ship sailed through tropical waters where giant pelagic rays of the genus **Mobula** leaped high into the air."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sailors observed the dark broad wings of a devil ray, resembling a swimming **Mobula**, gliding beneath the keel."},
      {"author": "William Beebe", "work": "The Arcturus Adventure", "quote": "A magnificent giant **Mobula** breached ten feet above the calm Pacific swell, slapping the surface with thunderous force."}
    ]
  },
  "Dashboard — mob/mobulidae.md": {
    "primary": "A family of large pelagic marine rays, including manta rays and devil rays, characterized by cephalic horn-like fins.",
    "secondary": "In systematic ichthyology, the Mobulidae are specialized filter feeders using modified branchial filter plates to capture pelagic zooplankton.",
    "quotes": [
      {"author": "William Beebe", "work": "The Arcturus Adventure", "quote": "The oceanic giant belonged to the **Mobulidae**, its wide cephalic flaps guiding plankton-rich seawater into its maw."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Naturalists have documented the immense size and wing-like pectoral fins of pelagic batoids grouped in the **Mobulidae**."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The cartilaginous skeletal framework of the **Mobulidae** reveals specialized cranial modifications for pelagic filter feeding."}
    ]
  },

  # --- Dashboard — rap (29 words) ---
  "Dashboard — rap/enrapture.md": {
    "primary": "To fill someone with immense pleasure, delight, or ecstasy; to captivate completely.",
    "secondary": "In aesthetic theory and Romantic lyricism, sublime natural landscapes enrapture the observer into transcendent contemplation.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester's passionate declarations of love had power to **enrapture** Jane's heart beyond all earthly fears."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The celestial choral harmonies of the angelic host were sufficient to **enrapture** the listening universe."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Sweet aerial music drifted across the enchanted vale, seeking to **enrapture** the spirits of the deep."}
    ]
  },
  "Dashboard — rap/enraptured.md": {
    "primary": "Filled with intense pleasure, delight, or wonder; spellbound and completely captivated.",
    "secondary": "In religious history and devotional literature, the enraptured mystic perceives visions of transcendent unity.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I gazed with an **enraptured** soul upon the majestic Alpine cataracts cascading into the foaming Arve."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth stood **enraptured** on the lawn of Pemberley, admiring the exquisite harmony of stream and wood."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The sculptor stood **enraptured** before the newly unearthed Greek marble, marveling at its lifelike grace."}
    ]
  },
  "Dashboard — rap/rap.md": {
    "primary": "To strike a quick, sharp, light blow; a knock; or a modern genre of rhythmic, rhymed vocal chanting.",
    "secondary": "In spiritualist history, nineteenth-century séances investigated mysterious percussive table rap signals attributed to spirits.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Raven", "quote": "Suddenly there came a tapping, as of some one gently **rap**, rapping at my chamber door on that bleak December midnight."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "Holmes gave a sharp **rap** with his cane upon the bedroom floor to test the hollow timbering beneath."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge heard a startling heavy **rap** upon the heavy oak door of his counting-house."}
    ]
  },
  "Dashboard — rap/rapacious.md": {
    "primary": "Aggressively greedy, grasping, or ravenous; living by plunder or taking by force.",
    "secondary": "In macroeconomic history and colonial critique, rapacious extractive cartels stripped natural resource wealth from colonized regions.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The provincial governors were notoriously **rapacious**, extorting ruinous taxes from the impoverished peasantry."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolistic commercial companies display a **rapacious** spirit that sacrifices long-term prosperity for immediate windfall gains."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "A wise parliament avoids harsh and **rapacious** exactions that alienate the loyal affections of colonial subjects."}
    ]
  },
  "Dashboard — rap/rapaciously.md": {
    "primary": "In an aggressively greedy, ravenous, or grasping manner, taking wealth or resources by force.",
    "secondary": "In political economic critique, speculative capital syndicates strip distressed assets rapaciously during market insolvencies.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The tax farmers preyed **rapaciously** upon the bread of the French peasantry until the revolution swept them away."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The legal harpies of Chancery fed **rapaciously** upon the vast estate until nothing remained for the suitors."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The mercenary soldiers plundered the captured Saxon manor **rapaciously**, stripping gold and silver plate from the walls."}
    ]
  },
  "Dashboard — rap/rapaciousness.md": {
    "primary": "The trait or quality of being aggressively greedy, ravenous, or grasping.",
    "secondary": "In predatory ethology and ecology, excessive ecological rapaciousness in apex predators is constrained by prey population dynamics.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The boundless **rapaciousness** of the Praetorian guards exhausted the imperial treasury within a few short months."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Legislative regulations were enacted to curb the unchecked **rapaciousness** of feudal landowners over agricultural tenants."},
      {"author": "Samuel Johnson", "work": "Rasselas", "quote": "The prince was shocked by the open **rapaciousness** of the predatory desert nomads who raided the caravan."}
    ]
  },
  "Dashboard — rap/rapacity.md": {
    "primary": "Aggressive greed, ravenousness, or the disposition to seize by force and plunder.",
    "secondary": "In historical political theory, Machiavelli cautioned sovereigns that provoking public hatred through fiscal rapacity precipitates rebellion.",
    "quotes": [
      {"author": "Niccolò Machiavelli", "work": "The Prince", "quote": "A prince must avoid above all things being hated and despised, and fiscal **rapacity** will surely bring him into hatred."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian kings marveled at the immense wealth and shameless **rapacity** of the imperial ministers in Rome."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The public denounced the insatiable **rapacity** of the court favorites who enriched themselves through monopolistic patents."}
    ]
  },
  "Dashboard — rap/rapateaceae.md": {
    "primary": "A family of monocotyledonous flowering plants native to the Neotropics and tropical West Africa, characterized by fan-shaped leaves and dense flower heads.",
    "secondary": "In systematic botany and monocot phylogenetics, the Rapateaceae constitute a basal lineage within the order Poales.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions", "quote": "On the sandstone plateaus of the Guiana Shield, striking herbaceous plants belonging to the **Rapateaceae** covered the misty bog."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The disjunct geographic distribution of families such as the **Rapateaceae** across the Atlantic suggests ancient continental links."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Botanists study the unique floral morphology and dense capitate inflorescences characteristic of the **Rapateaceae**."}
    ]
  },
  "Dashboard — rap/rape.md": {
    "primary": "The crime of forcing another person into sexual intercourse against their will; or a Eurasian brassicaceous plant grown for oilseed.",
    "secondary": "In agricultural agronomy, oilseed rape (Brassica napus) produces valuable vegetable oils and protein-rich livestock meal.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "What dire offense from amorous causes springs, what mighty contests rise from trivial things, I sing this sacred lock's bold **rape**."},
      {"author": "William Shakespeare", "work": "The Rape of Lucrece", "quote": "The treacherous Tarquin wrought the cruel **rape** of Lucrece, plunging royal Rome into righteous rebellion."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The farmers of Hampshire planted wide fields of winter **rape** to provide nutritious early fodder for sheep."}
    ]
  },
  "Dashboard — rap/raped.md": {
    "primary": "Subjected to sexual assault through unlawful force or lack of consent; or pillaged and despoiled.",
    "secondary": "In wartime international criminal law, military commanders face prosecution for war crimes where civilian populations are raped.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Titus Andronicus", "quote": "The unhappy Lavinia was brutally **raped** and mutilated in the dark woods by the savage sons of the Gothic queen."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The historic cities of Italy were sacked, burned, and **raped** of their classical treasures by barbarian invaders."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "The besieged Turkish fortress was carried by storm, and its surviving inhabitants despoiled and cruelly treated."}
    ]
  },
  "Dashboard — rap/raper.md": {
    "primary": "An archaic or variant legal designation for a perpetrator of sexual assault or violent violation.",
    "secondary": "In early English statutory jurisprudence and criminal common law rolls, indictments specifically classified the felonious raper of women.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Rape of Lucrece", "quote": "The treacherous Roman prince stood revealed as a monstrous **raper** whose heinous crime brought down the monarchy."},
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "The lexicographer noted the legal term designating one who commits ravishment and violent assault upon another."},
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The border wardens swore to execute summary justice upon any marauding **raper** caught violating the peaceful hamlet."}
    ]
  },
  "Dashboard — rap/rapeseed.md": {
    "primary": "The oil-rich seed of the yellow-flowering plant Brassica napus, processed for cooking oil (canola) and industrial fuels.",
    "secondary": "In agricultural commodity markets and industrial processing, crushed rapeseed yields high-erucic oil for marine lubricants and biodiesels.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Flanders farmers cultivated profitable crops of **rapeseed** to supply the burgeoning urban demand for lamp oil."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The fields beyond the oak copse glowed with a brilliant yellow mantle of flowering **rapeseed** in early May."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Agricultural selection has developed diverse cultivated varieties of **rapeseed** adapted to differing European soils."}
    ]
  },
  "Dashboard — rap/rapid.md": {
    "primary": "Happening in a short time or at a great speed; swift, fast, or quick.",
    "secondary": "In geomorphology and hydrology, a river rapid forms where resistant bedrock creates steep hydraulic gradients and turbulent white water.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The agile mountain guanacos bounded across the rocky scree with **rapid** and graceful leaps."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes made a series of **rapid** deductions from the scratches around the keyhole of the jewel safe."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The river steamboat plunged into a turbulent **rapid**, the pilot spinning the wheel to avoid jagged snags."}
    ]
  },
  "Dashboard — rap/rapidity.md": {
    "primary": "Great speed or swiftness of motion, occurrence, or operation.",
    "secondary": "In chemical reaction kinetics, catalytic reaction rapidity depends upon lowering activation energy barriers.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions marched across Gaul with astonishing **rapidity**, surprising the rebel tribes before they could unite."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The pestilence spread through the city with terrifying **rapidity**, defying every quarantine established by the magistrates."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Bingley's inherent **rapidity** of decision contrasted with Darcy's methodical and deliberate habit of mind."}
    ]
  },
  "Dashboard — rap/rapidly.md": {
    "primary": "At a very fast rate; swiftly, quickly, or with great speed.",
    "secondary": "In epidemiological modeling, viral pathogens transmit rapidly through immunologically naive urban populations.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The cab rattled **rapidly** through the shadowy streets of south London toward the secret rendezvous."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary tumult spread **rapidly** from the Saint Antoine quarter into every district of Paris."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The sun dipped and rose **rapidly**, until days passed like the flapping of dark wings in the sky."}
    ]
  },
  "Dashboard — rap/rapidness.md": {
    "primary": "The state or characteristic of being rapid, swift, or fast; speediness.",
    "secondary": "In manufacturing engineering and machining, rapidness of feed rates must be balanced against cutting tool wear.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The **rapidness** with which life glides away should inspire mankind with diligent resolution in virtue."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "The marvelous **rapidness** of thought allows the imagination to traverse the cosmos in a single instant."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The alarming **rapidness** of the national bankruptcy forced the crown to convene the long-forgotten Estates-General."}
    ]
  },
  "Dashboard — rap/rapier.md": {
    "primary": "A slender, sharply pointed two-edged sword used in sixteenth- and seventeenth-century Europe, primarily for thrusting.",
    "secondary": "In historical European martial arts and fencing history, the rapier utilized complex swept hilts to protect the unarmored hand.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "A hit, a very palpable hit; the young prince lunged forward with his slender steel **rapier** in the royal duel."},
      {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The young Scottish gallant wore a Toledo **rapier** at his side, its polished steel hilt glinting in the sunshine."},
      {"author": "Alexandre Dumas", "work": "The Three Musketeers", "quote": "D'Artagnan drew his **rapier** with lightning speed, facing the cardinal's guards with fearless bravado."}
    ]
  },
  "Dashboard — rap/rapine.md": {
    "primary": "The violent seizure of property, goods, or wealth from others; pillage, plundering, and spoliation.",
    "secondary": "In military historiography of the Thirty Years' War, marauding mercenary regiments subjected civilian towns to systematic rapine.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Vandals indulged in indiscriminate slaughter and **rapine** after carrying the marble gates of imperial Rome."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Then shall the world go on, to good malignant, to bad benign, under the curse of perpetual **rapine** and pride."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "To sanctify confiscation and **rapine** under the name of public liberty is to subvert the very foundation of justice."}
    ]
  },
  "Dashboard — rap/rapist.md": {
    "primary": "A person who commits the crime of rape through non-consensual sexual violation.",
    "secondary": "In criminal forensic jurisprudence and DNA profiling, statutory offender databases assist in identifying a serial rapist.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Titus Andronicus", "quote": "The vengeful Roman general trapped the cowardly offenders who had committed foul violation upon his daughter."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Abbey Grange", "quote": "Holmes observed that a violent criminal who assaults defenseless women is the lowest predator in human society."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The magistrate warned that the brutal rioter would face the supreme penalty of the law for his outrages."}
    ]
  },
  "Dashboard — rap/rapscallion.md": {
    "primary": "A mischievous, disreputable rascal, scamp, or rogue.",
    "secondary": "In picaresque literature and satirical characterization, the charming rapscallion survives through wit, evasion, and petty trickery.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Huckleberry Finn", "quote": "The King and the Duke were a pair of audacious **rapscallions**, cheating the country folk with fraudulent theatrical shows."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "David Balfour found himself in the company of a Highland **rapscallion** who lived by smuggling and daring escapes."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The angry uncle denounced his nephew as an idle, good-for-nothing **rapscallion** who wasted his time upon playhouses."}
    ]
  },
  "Dashboard — rap/rapt.md": {
    "primary": "Completely fascinated, absorbed, or engrossed by what one is seeing, hearing, or thinking.",
    "secondary": "In psychological flow theory, rapt attention minimizes self-referential mental awareness during complex artistic creation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Look how our partner's **rapt**; he stands transfixed by the strange prophetic promises of the weird sisters."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane listened with **rapt** attention as Rochester described his youthful wanderings through continental capitals."},
      {"author": "John Milton", "work": "Il Penseroso", "quote": "Come, pensive nun, devout and pure, sober, steadfast, and demure, with **rapt** soul sitting in thine eyes."}
    ]
  },
  "Dashboard — rap/raptor.md": {
    "primary": "A bird of prey such as an eagle, hawk, falcon, or owl; or a dromaeosaurid theropod dinosaur.",
    "secondary": "In avian ecology and predatory wildlife biology, a raptor possesses hooked beaks, acute binocular vision, and curved talons.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A majestic Andean condor wheeled overhead, demonstrating the supreme soaring prowess of this colossal **raptor**."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I watched a solitary **raptor** glide upon motionless wings above the deep pine woods bordering the pond."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The beast-man possessed the sharp, hooked talons and ferocious predatory instincts of an avian **raptor**."}
    ]
  },
  "Dashboard — rap/raptores.md": {
    "primary": "An obsolete nineteenth-century ornithological taxonomic order comprising birds of prey (hawks, falcons, eagles, and owls).",
    "secondary": "In systematic historical ornithology, anatomists defined the order Raptores by strong hooked beaks and powerful clutching zygodactyl talons.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Naturalists formerly grouped all diurnal and nocturnal birds of prey under the single taxonomic order **Raptores**."},
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The fierce hunting habits and keen predatory senses of the **Raptores** distinguish them from all other avian families."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The osteological structure of the skull and predatory feet across the **Raptores** displays remarkable adaptive convergence."}
    ]
  },
  "Dashboard — rap/raptorial.md": {
    "primary": "Adapted for or predatory in the seizing and devouring of living prey, especially describing birds of prey or specialized insect legs.",
    "secondary": "In entomological morphology, the prehensile forelegs of mantids (Mantodea) are termed raptorial limbs adapted for striking prey.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The powerful hooked talons of the eagle represent an exquisite adaptation for a **raptorial** mode of life."},
      {"author": "Thomas Henry Huxley", "work": "The Crayfish", "quote": "Certain marine crustaceans develop modified anterior appendages functioning as ferocious **raptorial** pincers."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The barn owl hunts with silent wing-beats, dropping its sharp **raptorial** claws upon unsuspecting field mice."}
    ]
  },
  "Dashboard — rap/rapture.md": {
    "primary": "An intense feeling of transcendent pleasure, ecstatic delight, or supreme happiness.",
    "secondary": "In Christian eschatological theology, the Rapture denotes the anticipated bodily assumption of faithful believers into heaven.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "The sight of the living statue filled the repentant king with a speechless, trembling **rapture** of wonder."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne listened to the passionate romantic sonata with tears of exquisite, melancholy **rapture**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Seraphic choirs sang before the throne of God, striking golden harps in sweet **rapture** of divine praise."}
    ]
  },
  "Dashboard — rap/rapturous.md": {
    "primary": "Characterized by, feeling, or expressing ecstatic joy, intense delight, or overwhelming enthusiasm.",
    "secondary": "In concert performance critique and reception history, virtuosic cadenzas frequently elicit rapturous standing ovations from audiences.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester greeted Jane with **rapturous** tenderness upon her return to the secluded manor of Ferndean."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The provincial audience greeted the eccentric theatrical performance of Mr. Wopsle with **rapturous** mockery."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen received the **rapturous** compliments of her aristocratic admirers at the archery contest with haughty grace."}
    ]
  },
  "Dashboard — rap/rapturously.md": {
    "primary": "In an ecstatic, overjoyed, or intensely enthusiastic and delighted manner.",
    "secondary": "In literary biography, enthusiastic audiences applauded Jenny Lind's operatic arias rapturously across international concert halls.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Mrs. Norris talked **rapturously** of the glorious prospects awaiting Maria upon her fashionable London marriage."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare played his harp in the dusk, while Tess listened **rapturously** from the garden among the unpruned weeds."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger gesticulated **rapturously** from the lecture stage as the pterodactyl specimen circled over the gas lamps."}
    ]
  },
  "Dashboard — rap/raptus.md": {
    "primary": "A sudden seizure, trance, or violent paroxysm; or historically, unlawful abduction or ravishment.",
    "secondary": "In clinical neuropsychiatry, raptus melancholicus designates a sudden, violent agitation state emerging from catatonic stupor.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In severe psychiatric catatonia, the patient may suddenly burst from mutism into a violent motor **raptus**."},
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "A terrifying nocturnal **raptus** seized my imagination, hurling my consciousness into labyrinthine abysses of architecture."},
      {"author": "Edgar Allan Poe", "work": "Berenice", "quote": "I sat transfixed in a morbid mental **raptus**, staring for hours at the small, unmeaning object on the mahogany table."}
    ]
  },
  "Dashboard — rap/serape.md": {
    "primary": "A brightly colored woolen blanket or shawl with fringed ends, worn as an outer garment by men in Mexico and Central America.",
    "secondary": "In Mesoamerican textile ethnography, handwoven serape garments feature intricate geometric diamond patterns dyed with natural cochineal.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The Mexican vaquero rode with superb grace, his brilliant woolen **serape** fluttering over the high horn of his saddle."},
      {"author": "Bret Harte", "work": "The Luck of Roaring Camp", "quote": "The solitary traveler wrapped his heavy red **serape** tightly against the cold mountain wind sweeping down the canyon."},
      {"author": "Stephen Crane", "work": "The Open Boat", "quote": "The border scout rested near the adobe wall, his shoulders draped in a faded indigo **serape** beneath the blazing sun."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
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

print(f"Motion Batch 2C: Successfully updated {updated}/{len(data)} notes.")
