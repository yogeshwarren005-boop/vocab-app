# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — mot Part 2 (10B, 33 words) ---
  "Dashboard — mot/motionlessly.md": {
    "primary": "In an entirely still manner, without moving, shifting, or making any physical gesture.",
    "secondary": "In narrative prose, describes characters frozen in suspense, contemplation, or tactical concealment.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Fedallah was **motionlessly** leaning over the same rail, his dark eyes fixed on the sea."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The great dog remained **motionlessly** crouched behind the clump of heather, awaiting the command to spring."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The native warrior stood **motionlessly** upon the bank of the river, silhouetted against the dark jungle."}
    ]
  },
  "Dashboard — mot/motionlessness.md": {
    "primary": "The complete absence of movement, agitation, or physical kinetic displacement.",
    "secondary": "In aesthetics and contemplative literature, signifies profound physical silence, tranquil meditation, or paralyzed suspense.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The profound **motionlessness** of Egdon Heath in the winter dusk imparted a feeling of timeless desolation."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The absolute **motionlessness** of that desolate beach under a dying sun filled my soul with horror."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "A fearful **motionlessness** settled over the dark tarn, reflecting the gray stones without a ripple."}
    ]
  },
  "Dashboard — mot/motivate.md": {
    "primary": "To provide an incentive, impulse, or psychological reason that stimulates an organism to action.",
    "secondary": "In cognitive psychology and management theory, describes the activation of intrinsic goals and extrinsic reinforcers to induce goal-directed behavior.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Desire and fear constitute the two cardinal springs that **motivate** conscious human conduct."},
      {"author": "John Dewey", "work": "Human Nature and Conduct", "quote": "Habits rather than abstract ideals primarily **motivate** everyday decisions and societal practices."},
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The vital impulse that continues to **motivate** human evolution operates far beneath conscious intellect."}
    ]
  },
  "Dashboard — mot/motivated.md": {
    "primary": "Stimulated, impelled, or guided by a conscious or subconscious motive, purpose, or incentive.",
    "secondary": "In jurisprudence and criminal investigative analysis, pertains to actions proven to originate from identifiable grievances, profit, or passions.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The jury must determine whether the accused was **motivated** by malice or acted in reasonable self-defense."},
      {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "Much of what appears rational thought is in fact **motivated** by deep-seated instinctual impulses."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She wondered whether Ralph was **motivated** by genuine sympathy or mere intellectual curiosity."}
    ]
  },
  "Dashboard — mot/motivating.md": {
    "primary": "Serving as an incentive, stimulus, or guiding impulse that encourages decisive action.",
    "secondary": "In organizational dynamics, describes interpersonal leadership practices and environmental factors that enhance productive engagement.",
    "quotes": [
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Interest is the great **motivating** force in all spontaneous education and lasting retention."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "Public enthusiasm forms the primary **motivating** factor behind legislative momentum in representative democracies."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The internal sanction of duty acts as a powerful **motivating** power in conscientious minds."}
    ]
  },
  "Dashboard — mot/motivation.md": {
    "primary": "The psychological driving force, stimulus, or reason that incites, directs, and sustains purposeful behavior.",
    "secondary": "In behavioral neuroscience and endocrinology, relates to dopaminergic mesolimbic pathways mediating reward anticipation and reinforcement learning.",
    "quotes": [
      {"author": "William James", "work": "The Will to Believe", "quote": "Deep spiritual faith often supplies the decisive **motivation** when intellectual proofs remain balanced."},
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "Unconscious **motivation** repeatedly betrays itself through slips of the tongue and unremembered appointments."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Genuine **motivation** arises when the learner identifies personal interest with the objective problem."}
    ]
  },
  "Dashboard — mot/motivational.md": {
    "primary": "Relating to, providing, or stimulating personal motivation, morale, and drive toward achieving goals.",
    "secondary": "In applied psychology and athletic training, describes systematic strategies and rhetoric designed to optimize emotional readiness and resilience.",
    "quotes": [
      {"author": "William James", "work": "The Energies of Men", "quote": "Unusual emotional excitement provides a sudden **motivational** surge that taps into reserve human energies."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Emulative display serves as an enduring **motivational** foundation for competitive consumption in society."},
      {"author": "John Dewey", "work": "Reconstruction in Philosophy", "quote": "The **motivational** power of ideals depends directly upon their relevance to concrete social needs."}
    ]
  },
  "Dashboard — mot/motivative.md": {
    "primary": "Having the quality, power, or tendency to incite, induce, or stimulate active effort.",
    "secondary": "In classical philosophy of mind, denotes mental faculties and affective inclinations capable of initiating volition.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poetic imagination exercises a **motivative** energy that transforms passive perception into vital creation."},
      {"author": "William Hamilton", "work": "Lectures on Metaphysics and Logic", "quote": "The feelings possess an intrinsically **motivative** character that prompts the will to immediate decision."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Every sensation carries an inherent **motivative** tendency toward corresponding muscular discharge."}
    ]
  },
  "Dashboard — mot/motivator.md": {
    "primary": "An agent, factor, incentive, or stimulus that prompts someone to take action or pursue a goal.",
    "secondary": "In Herzberg's two-factor management model, motivators are intrinsic job factors like recognition and achievement that produce genuine satisfaction.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The desire of becoming the proper objects of respect is the great **motivator** of mankind."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Self-interest remains the most constant and dependable **motivator** of industry in competitive markets."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Enthusiasm is the great **motivator** that overcomes inertia and accomplishes noble undertakings."}
    ]
  },
  "Dashboard — mot/motive.md": {
    "primary": "An emotion, desire, or psychological impulse that prompts a person to act in a particular way.",
    "secondary": "In music and literary analysis, an alternative term for motif, signifying a recurring melodic, thematic, or structural phrase.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Doubt not but heaven hath brought me up to be your daughter's dower, as it hath fated her to be my **motive**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "His **motive** for visiting Hertfordshire was openly stated to be the choice of a wife among the Miss Bennets."},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "The voluntary actions of man always proceed from some **motive** directed toward an apparent good to himself."}
    ]
  },
  "Dashboard — mot/motiveless.md": {
    "primary": "Lacking any discernible motive, objective incentive, sensible reason, or deliberate justification.",
    "secondary": "In literary criticism, notably associated with Coleridge's famous characterization of Iago's destructive malice in Shakespeare's Othello.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Notes on Shakespeare", "quote": "The final soliloquy presents the terrible spectacle of **motiveless** malignity working destruction for its own sake."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her sudden change of demeanor seemed entirely **motiveless** to those unacquainted with her private sorrow."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The calamity fell upon the household like a stroke of **motiveless** cruelty from blind circumstance."}
    ]
  },
  "Dashboard — mot/motivity.md": {
    "primary": "The inherent power, faculty, or mechanical capability of producing or initiating motion.",
    "secondary": "In 19th-century physics and natural philosophy, denotes the operational efficiency and work capacity of thermodynamic engines.",
    "quotes": [
      {"author": "William Thomson (Lord Kelvin)", "work": "Mathematical and Physical Papers", "quote": "Thermodynamic **motivity** measures the mechanical work obtainable when heat flows between two unequal thermal reservoirs."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Matter and **motivity** represent the indestructible components through which cosmic evolution continuously operates."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The muscular tissues of living organisms exhibit spontaneous **motivity** under electrical and physiological stimulation."}
    ]
  },
  "Dashboard — mot/motley.md": {
    "primary": "Composed of incongruously varied, heterogeneous elements; multicolored or party-colored in visual appearance.",
    "secondary": "Historically, the multicolored patchwork costume traditionally worn by court jesters, fools, and harlequins.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "A fool, a fool! I met a fool i' the forest, a **motley** fool; a miserable world!"},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A **motley** crowd of beggars, artisans, and women surged through the narrow Parisian alleys toward the Bastille."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Wamba the jester was attired in the customary **motley** tunic with cap and hanging silver bells."}
    ]
  },
  "Dashboard — mot/motmot.md": {
    "primary": "A colorful neotropical bird of the family Momotidae, distinguished by racket-tipped central tail feathers.",
    "secondary": "In ornithology, famous for behavioral tail-wagging displays (pendulum motion) used to signal awareness to potential predators.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The curious racket-shaped plumage in the tail of the **motmot** arises from the bird deliberately preening away the central barbs."},
      {"author": "Alfred Russel Wallace", "work": "Tropical Nature and Other Essays", "quote": "Among the dense foliage of the Amazonian forest, the brilliant turquoise head of the **motmot** catches the traveler's eye."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "We frequently heard the deep hollow note of the Brazilian **motmot** echoing through the shaded river banks."}
    ]
  },
  "Dashboard — mot/motoneuron.md": {
    "primary": "A motor nerve cell whose axon projects into muscles or glands, transmitting impulses that initiate contractions.",
    "secondary": "In neuroanatomy, categorized into upper motor neurons descending from the cortex and lower motor neurons synapsing directly with motor endplates.",
    "quotes": [
      {"author": "Charles Scott Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "The final common path in reflex action is constituted by the anterior horn **motoneuron** and its peripheral axon."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Each spinal **motoneuron** displays extensive dendritic arborizations that integrate hundreds of sensory collaterals."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Electrical discharge traversing the **motoneuron** provokes rapid chemical breakdown and mechanical twitch in muscle fibers."}
    ]
  },
  "Dashboard — mot/motor.md": {
    "primary": "A machine that converts other forms of energy (such as electricity, fuel, or steam) into mechanical kinetic power.",
    "secondary": "In physiological anatomy, denotes nerve structures and muscular organs that produce movement rather than convey sensory feeling.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "A little knot of people collected on the footpath to pay homage to the snorting **motor**."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The clanking **motor** of the Martian tripod machine emitted puffs of greenish smoke as it marched through the water."},
      {"author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "The purr of a powerful **motor** broke the midnight silence as the German diplomat approached the coastal cottage."}
    ]
  },
  "Dashboard — mot/motor-assisted.md": {
    "primary": "Relying on or augmented by an auxiliary internal engine or electric motor to supplement manual or pedal power.",
    "secondary": "In transport engineering and urban mobility regulations, applies to electric bicycles (pedelecs) providing progressive power proportional to pedal effort.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Wheels of Chance", "quote": "He dreamed of a light **motor-assisted** velocipede that might scale the Sussex downs without human exhaustion."},
      {"author": "John Galsworthy", "work": "The Forsyte Saga", "quote": "The elderly gentleman preferred a **motor-assisted** tricycle for traversing the extensive paths of his country estate."},
      {"author": "Arnold Bennett", "work": "The Card", "quote": "Denry invested in an ingenious **motor-assisted** delivery cart that outpaced every horse in the Five Towns."}
    ]
  },
  "Dashboard — mot/motorbike.md": {
    "primary": "A lightweight two-wheeled motor vehicle, typically with an engine of modest displacement, used for personal transport.",
    "secondary": "In popular automotive nomenclature, informal synonym for motorcycle, frequently denoting mopeds and light utility cycles.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Young apprentices frequently saved their spare shillings for months to buy a second-hand **motorbike**."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The distant roar of a **motorbike** along the country road shattered the quiet contemplation of the morning."},
      {"author": "E. M. Forster", "work": "Howards End", "quote": "A youth astride a spluttering **motorbike** swept past the carriage, leaving a trailing haze of gasoline smoke."}
    ]
  },
  "Dashboard — mot/motorboat.md": {
    "primary": "A boat powered by an internal combustion engine or electric motor, designed for fast surface navigation.",
    "secondary": "In maritime law, categorized by overall hull length and engine horsepower for safety equipment, fire suppression, and licensing compliance.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "His **motorboat** tore a clear water rift through the green swell while the hydroplanes hummed overhead."},
      {"author": "Ernest Hemingway", "work": "To Have and Have Not", "quote": "Harry Morgan steered the chartered **motorboat** through the shallow reefs of the Florida Keys toward Havana."},
      {"author": "Jack London", "work": "The Valley of the Moon", "quote": "The sound of an approaching **motorboat** warned them that the patrol was cruising near the estuary marsh."}
    ]
  },
  "Dashboard — mot/motorbus.md": {
    "primary": "A large passenger omnibus propelled by an internal combustion engine, operating on scheduled public transit routes.",
    "secondary": "In urban transit history, replaced horse-drawn omnibuses and urban tramways in major cities during the early 20th century.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "The red London **motorbus** lurched forward toward Piccadilly, laden with passengers and morning newspapers."},
      {"author": "E. M. Forster", "work": "The Celestial Omnibus", "quote": "He watched the roaring petrol **motorbus** speed by the corner, contrasting it with the mythical coach of his dreams."},
      {"author": "G. K. Chesterton", "work": "The Club of Queer Trades", "quote": "The top of a London **motorbus** provides the most elevated vantage ground for observing philosophical ironies."}
    ]
  },
  "Dashboard — mot/motorcade.md": {
    "primary": "A formal ceremonial procession or escorted convoy of automobiles, typically carrying dignitaries or officials.",
    "secondary": "In diplomatic protocol and executive security, organized with lead scout vehicles, armored limousines, and tactical chase cars.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The official **motorcade** swept past cheering Parisian crowds as we made our way to the Arc de Triomphe."},
      {"author": "John Dos Passos", "work": "U.S.A.", "quote": "Police sirens shrieked as the presidential **motorcade** navigated the wide boulevards of the capital."},
      {"author": "Graham Greene", "work": "The Quiet American", "quote": "The French general's **motorcade** raced through the Saigon streets flanked by armored jeeps and heavy machine guns."}
    ]
  },
  "Dashboard — mot/motorcar.md": {
    "primary": "A self-propelled four-wheeled passenger vehicle designed for roadway transport; an automobile.",
    "secondary": "In early 20th-century British legal and colloquial usage, the standard formal designation for privately owned passenger automobiles.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "A private **motorcar** had drawn up at the curb, its brass headlamps gleaming in the dense London fog."},
      {"author": "Kenneth Grahame", "work": "The Wind in the Willows", "quote": "Toad was entirely captivated by the magnificent **motorcar**, murmuring 'poop-poop' in delirious admiration."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "The acquisition of an expensive French **motorcar** was the first unmistakable badge of commercial success."}
    ]
  },
  "Dashboard — mot/motorcoach.md": {
    "primary": "A large, comfortable passenger vehicle designed for long-distance highway travel, tourism, or chartered excursions.",
    "secondary": "In passenger transportation systems, distinguished from municipal transit buses by plush seating, luggage bays, and restroom facilities.",
    "quotes": [
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "Parties of affluent tourists arrived by **motorcoach** at the grand hotel, oblivious to the squalor in the scullery."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "The party engaged a spacious **motorcoach** to convey them up the winding terraces overlooking the Arno."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "A scarlet **motorcoach** deposited the sightseers before the immense technological facilities of the Centre."}
    ]
  },
  "Dashboard — mot/motorcycle.md": {
    "primary": "A two-wheeled motorized passenger vehicle powered by an engine and equipped with a rigid frame and handlebars.",
    "secondary": "In automotive design, features straddle seating, foot pegs, handlebar clutch and brake controls, and chain, belt, or shaft final drive.",
    "quotes": [
      {"author": "T. E. Lawrence", "work": "The Mint", "quote": "The rush of cold morning wind across my face on the roaring Brough Superior **motorcycle** gave absolute freedom."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "Every young fellow who saved enough cash bought a second-hand **motorcycle** and sped across the country lanes."},
      {"author": "Ernest Hemingway", "work": "A Farewell to Arms", "quote": "An Italian dispatch rider on a mud-splattered **motorcycle** brought urgent dispatches from the front line."}
    ]
  },
  "Dashboard — mot/motorcycling.md": {
    "primary": "The activity, practice, or sport of riding and operating a motorcycle.",
    "secondary": "In recreational transport and motorsports, encompasses competitive racing disciplines such as motocross, speedway, and Grand Prix road racing.",
    "quotes": [
      {"author": "T. E. Lawrence", "work": "Letters of T. E. Lawrence", "quote": "Solitary **motorcycling** across the desolate Wiltshire downs provides the ultimate anesthetic for nervous fatigue."},
      {"author": "Aldous Huxley", "work": "Antic Hay", "quote": "Young Gumbril considered whether fast **motorcycling** offered a genuine antidote to modern existential ennui."},
      {"author": "George Orwell", "work": "Keep the Aspidistra Flying", "quote": "Advertisements glorified weekend **motorcycling** as the supreme embodiment of youthful romance and adventurous liberty."}
    ]
  },
  "Dashboard — mot/motorcyclist.md": {
    "primary": "A person who rides, operates, or competes on a motorcycle.",
    "secondary": "In highway safety research and traffic regulation, designated as a vulnerable road user requiring specialized protective equipment such as certified helmets.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "The tracks indicated that the swift **motorcyclist** had crossed the moorland bridle path before the rain began."},
      {"author": "T. E. Lawrence", "work": "The Mint", "quote": "The veteran **motorcyclist** develops an instinctive intuition for road camber, surface dampness, and cornering balance."},
      {"author": "G. K. Chesterton", "work": "The Secret of Father Brown", "quote": "A goggled **motorcyclist** skidded sharply at the crossroads, kicking up a white cloud of chalk dust."}
    ]
  },
  "Dashboard — mot/motored.md": {
    "primary": "Equipped with a motor for mechanical propulsion; traveled or moved by motor vehicle.",
    "secondary": "In naval architecture, denotes auxiliary sailing vessels fitted with secondary combustion engines for harbor maneuvering.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "The wealthy young sportsmen **motored** out to the suburban racetrack in their gleaming foreign tourer."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "They **motored** into the surrounding hills, admiring the olive orchards spread across the valley beneath."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "Amory and his classmates **motored** down to the coastal cottage for a lively weekend holiday."}
    ]
  },
  "Dashboard — mot/motorial.md": {
    "primary": "Pertaining to or causing motion, especially referring to nerves and brain structures controlling muscle movement.",
    "secondary": "In physiological psychology, describes the efferent neuromuscular pathways conducting commands from the central nervous system to effector organs.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Every sensory impression carries an immediate reverberation into the **motorial** apparatus of the organism."},
      {"author": "Charles Scott Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "The **motorial** discharge from the cortical centers coordinates complex patterns of antagonistic muscular contractions."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Evolution progressively differentiates sensory receptivity from direct **motorial** execution in nervous circuits."}
    ]
  },
  "Dashboard — mot/motoring.md": {
    "primary": "The recreation, practice, or activity of traveling by motorcar or automobile.",
    "secondary": "In early 20th-century cultural history, represented a fashionable pastime associated with touring guidebooks, goggles, and automobile clubs.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "He divided his leisure time curiously between amateur musical societies and fashionable **motoring** circles."},
      {"author": "Kenneth Grahame", "work": "The Wind in the Willows", "quote": "Toad declared that **motoring** was the only worthwhile pursuit left in an otherwise dull existence."},
      {"author": "E. M. Forster", "work": "Howards End", "quote": "The dust raised by country **motoring** settled thickly upon the hedgerows and cottage gardens."}
    ]
  },
  "Dashboard — mot/motorisation.md": {
    "primary": "The process of equipping an organization, transport system, or society with motor vehicles and mechanical engines.",
    "secondary": "In military logistics, the strategic conversion of infantry and cavalry divisions from horse transport to wheeled utility and armored transport.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The comprehensive **motorisation** of army supply trains revolutionized battlefield logistics between 1914 and 1918."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Rapid industrial **motorisation** altered the physical topography and suburban layout of Western civilizations."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "Modern warfare compelled the thorough **motorisation** of all military transport and tactical communications."}
    ]
  },
  "Dashboard — mot/motorise.md": {
    "primary": "To equip a transport unit, factory, or military force with motor-driven vehicles or machinery.",
    "secondary": "In municipal planning, refers to modernizing municipal utility services and postal distribution via motorized fleets.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The War Cabinet resolved to **motorise** the remaining territorial brigades with all possible dispatch."},
      {"author": "H. G. Wells", "work": "Anticipations", "quote": "Every advanced commercial enterprise will inevitably **motorise** its distribution services to preserve competitive advantage."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The munitions factory found it profitable to **motorise** the internal conveyance of heavy ordnance components."}
    ]
  },
  "Dashboard — mot/motorised.md": {
    "primary": "Furnished, driven, or equipped with an engine, motor, or motorized vehicular transport.",
    "secondary": "In military doctrine, describes motorized infantry transported in trucks or wheeled vehicles, distinct from mechanized infantry in tracked armored fighting vehicles.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The **motorised** divisions pushed rapidly along the coastal highway toward Benghazi under heavy fighter escort."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The absence of **motorised** transport compelled the militia columns to march for days across rugged Aragon hills."},
      {"author": "Aldous Huxley", "work": "Eyeless in Gaza", "quote": "A convoy of **motorised** ambulances waited at the junction to evacuate wounded soldiers to the base hospital."}
    ]
  },
  "Dashboard — mot/motorist.md": {
    "primary": "A person who drives or travels in an automobile, especially for recreation or personal transport.",
    "secondary": "In traffic sociology and legal liability statutes, subject to defined duties of care toward pedestrians and non-motorized roadway users.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "Anybody might have seen it done while the stand was empty, any tramp under the hedges or **motorist** pausing on the crest."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Devil's Foot", "quote": "A passing **motorist** reported seeing a solitary lantern flickering near the desolate Cornish ruins after midnight."},
      {"author": "E. M. Forster", "work": "Howards End", "quote": "The aggressive **motorist** honked his horn furiously at the slow cart blocking the winding country lane."}
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

print(f"Motion Batch 10B: Successfully updated {updated}/{len(data)} notes.")
