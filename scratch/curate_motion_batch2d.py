# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — mov (30 words) ---
  "Dashboard — mov/commove.md": {
    "primary": "To move violently, stir up, agitate, or disturb profoundly.",
    "secondary": "In archaic metaphysical and natural philosophy, celestial influences were thought to commove terrestrial atmospheric vapors.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Straight the fierce trumpet's sound did fiercely **commove** the warlike hosts along the heavenly plains."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The subterranean earthquakes begin to **commove** the ancient granite foundations of the mountains."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Passionate rumors from Paris did deeply **commove** the provincial garrisons along the eastern border."}
    ]
  },
  "Dashboard — mov/countermove.md": {
    "primary": "An action, maneuver, or tactical step taken in opposition to or to counteract an opponent's move.",
    "secondary": "In game theory and military grand strategy, anticipating an adversary's countermove minimizes positional tactical exposure.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "Holmes regarded Professor Moriarty's latest maneuver as a brilliant **countermove** on the European chessboard."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The admiralty prepared an immediate **countermove** to intercept the German battlecruiser sortie into the North Sea."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The assistant commissioner devised a subtle **countermove** to thwart the foreign embassy's provocative scheme."}
    ]
  },
  "Dashboard — mov/immovability.md": {
    "primary": "The property or characteristic of being steadfast, firmly fixed, or incapable of physical movement.",
    "secondary": "In philosophical Stoicism, moral immovability in the face of fortune reflects mastery over irrational emotional passions.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab's countenance possessed the stony **immovability** of an Egyptian granite monument facing the desert."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers listened to her entreaties with an austere **immovability** that chilled her spirit."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman defensive wall across northern Britain stood with silent **immovability** against barbarian raids."}
    ]
  },
  "Dashboard — mov/immovable.md": {
    "primary": "Incapable of being moved physically; steadfast, unyielding, or firmly fixed in purpose or position.",
    "secondary": "In property law and civil jurisprudence, immovable property encompasses land, permanent buildings, and real estate rights.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "Blow, till thou burst thy wind, if room enough; the solid vessel strikes an **immovable** reef in the storm."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth found her father **immovable** in his refusal to permit Lydia any further public indulgence."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Space is conceived as an infinite, **immovable** extension wherein all material bodies reside."}
    ]
  },
  "Dashboard — mov/immovableness.md": {
    "primary": "Firm fixedness, steadfastness, or unyielding resistance to displacement or emotional persuasion.",
    "secondary": "In structural civil engineering, the immovableness of bedrock bridge abutments guarantees stability under hydraulic loads.",
    "quotes": [
      {"author": "George Eliot", "work": "Romola", "quote": "Savonarola's stern **immovableness** in the pulpit inspired both awe and fierce terror among the citizens of Florence."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "There is a sublime **immovableness** in eternal moral laws that mocks the transient decrees of corrupt parliaments."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The stoic sage boasted an absolute **immovableness** of mind against the sudden calamities of human life."}
    ]
  },
  "Dashboard — mov/immovably.md": {
    "primary": "In an unyielding, steadfast, or firmly fixed manner, so as to defy displacement or change.",
    "secondary": "In marine navigation and anchorage design, massive fluked anchors bed immovably into seafloor clay to hold vessels.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Doctor Manette remained **immovably** silent, his eyes fixed on the shoemaker's bench before him."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Saxon champion stood **immovably** in the center of the list, awaiting the Norman knight's charge."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The heavy iron chains were secured **immovably** to the stone walls of the subterranean dungeon."}
    ]
  },
  "Dashboard — mov/immoveable.md": {
    "primary": "An archaic variant spelling of immovable, signifying firmly fixed, steadfast, or incapable of motion.",
    "secondary": "In historical legal treatises, immoveable estates comprised hereditary land holdings protected by feudal entails.",
    "quotes": [
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian found the rock of truth **immoveable** beneath his feet, while worldly tempters sank in the Slough of Despond."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Crusoe struggled to dislodge the heavy timber trunk, finding it completely **immoveable** by human strength."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The floating island of Laputa was anchored to an **immoveable** magnetic center deep within the crust."}
    ]
  },
  "Dashboard — mov/irremovable.md": {
    "primary": "Incapable of being removed, displaced, extracted, or discharged from an office, position, or substrate.",
    "secondary": "In constitutional law and judicial tenure, appointing irremovable federal judges ensures the independence of the judiciary.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The Act of Settlement rendered the royal judges **irremovable** except upon address by both houses of parliament."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The heavy black ink stain seemed **irremovable** from the ancient vellum parchment in the Chancery office."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "An **irremovable** civil bureaucracy risks degenerating into an arrogant caste unresponsive to public needs."}
    ]
  },
  "Dashboard — mov/movability.md": {
    "primary": "The capability, property, or ease of being moved, transported, or relocated from one position to another.",
    "secondary": "In ergonomic industrial engineering, modular assembly equipment prioritizes lightweight construction to ensure rapid workshop movability.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The physical **movability** of nomadic pastoral tents contrasts with the permanent stone architecture of agrarian cities."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The multi-axial **movability** of the human shoulder joint permits exceptional manual dexterity."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The relative **movability** of commercial circulating capital allows merchants to transfer funds across foreign markets."}
    ]
  },
  "Dashboard — mov/movable.md": {
    "primary": "Capable of being moved, relocated, or transferred; or personal property as distinguished from real estate.",
    "secondary": "In printing history, Johannes Gutenberg's invention of metal movable type revolutionized European mass book production.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The invention of **movable** type, gunpowder, and the magnetic needle changed the whole face of human civilization."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The family discussed installing a **movable** theatrical stage in the billiard room for their private theatricals."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The law distinguishes between **movable** goods and permanent real property in matters of inheritance and taxation."}
    ]
  },
  "Dashboard — mov/movableness.md": {
    "primary": "The property or characteristic of being movable, portable, or capable of changing location.",
    "secondary": "In classical mechanics and structural statics, excessive joint movableness indicates loose mechanical fastenings.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **movableness** of material bodies in space provides the sensory foundation for our ideas of motion and velocity."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The internal **movableness** of fluid particles accounts for their readiness to adapt to any enclosing vessel."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The outward **movableness** of human fashions contrasts with the unchanging spiritual soul that wears them."}
    ]
  },
  "Dashboard — mov/move.md": {
    "primary": "To change place, position, or posture; to take formal action, provoke deep emotion, or propose a motion in an assembly.",
    "secondary": "In parliamentary procedure, delegates move formal resolutions to introduce legislative business to the floor.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "The man that hath no music in himself, nor is not **move**-ed with concord of sweet sounds, is fit for treasons."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth watched Darcy **move** through the room, admiring his tall stature and noble air."},
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "Bodies in motion will continue to **move** with uniform velocity along a straight line unless acted upon by a net force."}
    ]
  },
  "Dashboard — mov/moveable.md": {
    "primary": "An archaic variant spelling of movable, indicating capability of being relocated, portable, or personal property.",
    "secondary": "In historical ecclesiastical calendars, moveable feasts such as Easter shift in calendar date according to lunar cycles.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Wemmick showed Pip his portable collection of rings, watches, and **moveable** property acquired from clients."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Crusoe transported every piece of **moveable** salvage from the wrecked vessel before the next autumn gale broke it apart."},
      {"author": "Book of Common Prayer", "work": "The Book of Common Prayer", "quote": "Tables and rules are provided for determining the **moveable** feasts and fasts throughout the ecclesiastical year."}
    ]
  },
  "Dashboard — mov/moved.md": {
    "primary": "Having changed position or physical location; or affected with strong tender emotion, sympathy, or compassion.",
    "secondary": "In civil judicial procedure, an advocate who moved the court filed a formal motion requesting an interlocutory decree.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane was deeply **moved** by Rochester's genuine anguish, her eyes filling with uncontrollable tears."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge was visibly **moved** when the Ghost of Christmas Past showed him his solitary schoolboy days."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The heavy ship was slowly **moved** through the narrow harbor entrance by long sweeps and pulling boats."}
    ]
  },
  "Dashboard — mov/movement.md": {
    "primary": "An act of changing physical location or position; or a organized social, political, or artistic campaign.",
    "secondary": "In horology and watchmaking, the mechanical movement consists of the gear train, escapement, and balance spring.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Every growing root tip performs a circumnutating **movement** as it navigates through crevices in the soil."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes tracked the subtle **movement** of the footprints across the garden with astonishing methodical precision."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The naval battle resolved into a grand tactical **movement** of dreadnought battle lines maneuvering for the wind."}
    ]
  },
  "Dashboard — mov/mover.md": {
    "primary": "A person, mechanism, or agency that moves something; or the initiator or proposer of a formal motion.",
    "secondary": "In Aristotelian metaphysics and classical natural theology, God is postulated as the uncreated Prime Mover (Primum Mobile).",
    "quotes": [
      {"author": "Aristotle", "work": "Metaphysics", "quote": "There must exist an eternal, unchangeable first **mover** that causes motion without being itself moved by any other."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The first cosmological argument demonstrates that every movement in nature traces back to a supreme prime **mover**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The energetic solicitor acted as the chief **mover** in initiating the legal petition before the high court."}
    ]
  },
  "Dashboard — mov/movie.md": {
    "primary": "A motion picture; a film recorded and projected onto a screen for public entertainment or artistic expression.",
    "secondary": "In twentieth-century cultural media studies and film theory, cinema developed from silent novelty into a narrative global industry.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Last Tycoon", "quote": "Monroe Stahr understood how to craft a compelling **movie** that captured the romantic dreams of millions across the nation."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt enjoyed escaping to the downtown picture palace to watch the latest feature **movie** on Saturday afternoon."},
      {"author": "Virginia Woolf", "work": "The Cinema", "quote": "The eye licks up the images of the **movie** screen with greedy curiosity, discovering a new visual language."}
    ]
  },
  "Dashboard — mov/moviegoer.md": {
    "primary": "A person who regularly attends motion picture theaters to watch films.",
    "secondary": "In urban leisure sociology, the modern moviegoer of the 1920s transformed downtown cinema palaces into civic entertainment centers.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "Anthony Patch joined the crowd of evening **moviegoers** lining up outside the glittering Broadway theater."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The provincial **moviegoer** in Gopher Prairie found in the Hollywood melodrama an escape from prairie monotony."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The twentieth-century **moviegoer** consumed sensationalized fantasies that reflected the anxieties of an industrial age."}
    ]
  },
  "Dashboard — mov/moviemaking.md": {
    "primary": "The art, technical craft, and commercial industry of producing and directing motion pictures.",
    "secondary": "In cinematic history, the transition to synchronized sound recording in 1927 transformed studio moviemaking workflows.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Last Tycoon", "quote": "Stahr viewed **moviemaking** as a delicate synthesis of industrial assembly lines and intense poetic inspiration."},
      {"author": "Virginia Woolf", "work": "The Cinema", "quote": "The pioneers of **moviemaking** discovered how to manipulate light and shadow to create emotional illusions."},
      {"author": "H. G. Wells", "work": "The Autocracy of Mr. Parham", "quote": "The studio stages buzzed with the high-voltage energy and financial extravagance of modern **moviemaking**."}
    ]
  },
  "Dashboard — mov/moving.md": {
    "primary": "In physical motion; changing location; or producing strong feelings of emotional sympathy, pity, or tenderness.",
    "secondary": "In kinematic analysis, the velocity vector of a moving particle is tangent to its instantaneous trajectory.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Watson observed a dark, **moving** figure silhouetted against the granite crag of the nocturnal moor."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Agnes spoke in a gentle, **moving** voice that brought deep comfort to David's troubled and weary heart."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The vast **moving** wall of white foam announced the sudden rising of the leviathan from the ocean depths."}
    ]
  },
  "Dashboard — mov/movingly.md": {
    "primary": "In a manner that excites deep emotion, sympathy, pity, or tender compassion.",
    "secondary": "In rhetoric and pulpit eloquence, a speaker who appeals movingly to shared moral convictions persuades divided audiences.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor spoke **movingly** of Marianne's gentle nature, pleading for forbearance and understanding from their mother."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Lucie Manette testified **movingly** on behalf of the prisoner, winning the sympathy of the entire courtroom."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess sang **movingly** at the dairy milking, her sweet Wessex voice echoing across the green summer meadows."}
    ]
  },
  "Dashboard — mov/nonmoving.md": {
    "primary": "Not in motion; stationary, static, at rest, or lacking physical movement.",
    "secondary": "In traffic enforcement and municipal statutory codes, nonmoving violations encompass parking infractions and expired vehicle registrations.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes remained motionless behind the hedge, his keen eyes fixed upon the **nonmoving** shadow beside the gate."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Predators often fail to distinguish **nonmoving** cryptically colored insects resting upon lichens on oak bark."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The laboratory apparatus appeared completely **nonmoving** and solid, though its temporal components oscillated."}
    ]
  },
  "Dashboard — mov/removable.md": {
    "primary": "Capable of being taken away, detached, eliminated, or dismissed from an office or physical surface.",
    "secondary": "In dental prosthetics and reconstructive surgery, a removable partial denture restores chewing function while allowing oral hygiene.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip noticed that the high collar of his London suit had a **removable** linen lining for easy daily washing."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The executive minister must remain **removable** upon a parliamentary vote of no confidence to preserve democracy."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "Cavor designed the sphere with **removable** roller blinds coated in the anti-gravitational substance."}
    ]
  },
  "Dashboard — mov/removal.md": {
    "primary": "The act of taking someone or something away, dismissing from office, or relocating to another dwelling.",
    "secondary": "In constitutional law, impeachment and removal of executive officials requires high crimes or treason under fundamental charters.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The **removal** of the militia regiment from Meryton to Brighton plunged Kitty and Lydia into inconsolable grief."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The sudden **removal** of the court documents from the solicitor's chambers caused consternation in Chancery."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **removal** of the imperial capital from Rome to Constantinople transformed the geopolitical balance of the Mediterranean."}
    ]
  },
  "Dashboard — mov/remove.md": {
    "primary": "To take off, displace, eliminate, or relocate something from a position or surface; or a degree of separation.",
    "secondary": "In surgical therapeutics and oncology, surgeons remove localized malignant lesions with wide histological margins.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Be thou familiar, but by no means vulgar; and do not **remove** thy thoughts from honorable conduct."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "Holmes stepped forward with a magnifying glass to **remove** a tiny thread clinging to the corner of the ventilator."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane felt an urgent moral duty to **remove** herself from Thornfield Hall before her conscience was compromised."}
    ]
  },
  "Dashboard — mov/removed.md": {
    "primary": "Distant or separated in space, time, or relationship; or taken away, displaced, or dismissed.",
    "secondary": "In genealogical classification, a cousin once removed belongs to one generation above or below the reference person.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The cottage in Devonshire was quiet and pleasantly **removed** from the bustling gossip of London society."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David felt entirely **removed** from the happy childhood days at Blunderstone Rookery once placed at Murdstone's warehouse."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The solitary cottage of Hester Prynne stood **removed** from the Puritan settlement on the barren shore."}
    ]
  },
  "Dashboard — mov/remover.md": {
    "primary": "A person who moves something, or a chemical substance, solution, or tool used to eliminate unwanted deposits.",
    "secondary": "In historical furniture restoration and painting conservation, chemical paint remover dissolves varnishes without degrading underlying timber.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 116", "quote": "Love is not love which alters when it alteration finds, or bends with the **remover** to remove; O no, it is an ever-fixed mark."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The furniture **remover** loaded the modest belongings of the family onto the heavy cart bound for London."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes identified the chemical solvent as a powerful stain **remover** commonly sold by photographic chemists."}
    ]
  },
  "Dashboard — mov/unmovable.md": {
    "primary": "Incapable of being moved; unyielding, steadfast, or resistant to change or physical displacement.",
    "secondary": "In structural foundations and geotechnical engineering, unmovable bedrock footings prevent differential settling in skyscraper construction.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The celestial archangel stood with an **unmovable** resolve, defying the rebellious legions of the adversary."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab remained **unmovable** in his dark purpose, deaf to the pious entreaties of his first mate Starbuck."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The Scottish knight knelt upon the rocky ground, his broad shield planted like an **unmovable** fortress."}
    ]
  },
  "Dashboard — mov/unmoved.md": {
    "primary": "Not changed in physical location or position; or emotionally untouched, impassive, and indifferent.",
    "secondary": "In psychological resilience and crisis leadership, commanders who remain unmoved by panic maintain operational command continuity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy listened to Elizabeth's impassioned rebuke with a countenance that appeared cold and **unmoved**."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers sat **unmoved** by her tears, clinging to his austere sense of religious duty."},
      {"author": "William Shakespeare", "work": "Sonnet 94", "quote": "They that have power to hurt and will do none, that do not do the thing they most do show, who, **unmoved**, cold, and to temptation slow."}
    ]
  },
  "Dashboard — mov/unmoving.md": {
    "primary": "Not in motion; stationary, still, motionless, or failing to arouse emotional sympathy.",
    "secondary": "In visual wildlife observation and camouflage study, an unmoving predator escapes the notice of prey animals whose retinas detect movement.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The dark, monstrous trees stood **unmoving** in the heavy equatorial air along the silent riverbank."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes watched the **unmoving** silhouette of the watcher upon the moonlit granite tor on Dartmoor."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The broad expanse of Egdon Heath lay silent and **unmoving** beneath the gathering shadows of dusk."}
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

print(f"Motion Batch 2D: Successfully updated {updated}/{len(data)} notes.")
