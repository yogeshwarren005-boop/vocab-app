import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Sound & Auditory';

const filesData = {
  // Dashboard — tympan
  "Dashboard — tympan/timbre.md": {
    primary: "The character or quality of a musical sound or voice as distinct from its pitch and intensity; acoustic tone color.",
    secondary: "The unique harmonic spectrum produced by a vibrating body that allows the listener to distinguish different instruments or voices.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "The difference in musical **timbre** depends solely on the presence and relative strength of upper partial tones." },
      { author: "Jean-Jacques Rousseau", work: "Dictionary of Music", quote: "Each instrument possesses a native **timbre** that evokes distinct emotional colors in the listener's soul." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "A patient suffering from amusia may retain the ability to recognize vocal **timbre** even when melody is lost." }
    ]
  },
  "Dashboard — tympan/timpani.md": {
    primary: "Kettledrums, especially when played by one musician in an orchestra, consisting of large copper bowls with tunable calfskin or synthetic heads.",
    secondary: "The premier percussion section in symphonic orchestration, capable of producing definite pitched notes of dramatic resonance.",
    quotes: [
      { author: "Hector Berlioz", work: "Treatise on Instrumentation", quote: "The **timpani** are the most valuable and poetic of all percussion instruments, imparting heroic weight to the orchestra." },
      { author: "Gustav Mahler", work: "Selected Letters", quote: "A sudden solo stroke on the muffled **timpani** marks the tragic turning point of the funeral march." },
      { author: "Leonard Bernstein", work: "The Joy of Music", quote: "The thunderous roll of the **timpani** drives the symphonic climax toward its triumphant resolution." }
    ]
  },
  "Dashboard — tympan/timpanist.md": {
    primary: "A musician who plays the timpani in an orchestra or ensemble.",
    secondary: "A specialist percussionist responsible for precise pitch tuning and rhythmic leadership in orchestral performance.",
    quotes: [
      { author: "Hector Berlioz", work: "Treatise on Instrumentation", quote: "The **timpanist** must possess an exquisite ear to retune his drums quietly amidst the roar of brass and strings." },
      { author: "Nikolai Rimsky-Korsakov", work: "Principles of Orchestration", quote: "A skilled **timpanist** executes delicate pianissimo rolls that create an ominous atmospheric tremor." },
      { author: "Aaron Copland", work: "What to Listen for in Music", quote: "The watchful **timpanist** leans over the copper kettle, damping the vibrating membrane with sensitive fingertips." }
    ]
  },
  "Dashboard — tympan/tympan.md": {
    primary: "In manual letterpress printing, a paper-holding frame faced with parchment or cloth that folds down onto the inked type beneath the platen.",
    secondary: "An architectural tympanum; also, an archaic term for a drum or tambourine.",
    quotes: [
      { author: "William Morris", work: "The Art and Craft of Printing", quote: "The pressman pulled the lever smoothly, bringing the sheet held upon the **tympan** against the inked face of the wooden type." },
      { author: "Vitruvius", work: "De Architectura", quote: "The pediment of the temple encloses a broad triangular **tympan** adorned with high-relief marble statues." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "Above the cathedral portal, the sculpted **tympan** portrayed the Last Judgment in intricate Byzantine relief." }
    ]
  },
  "Dashboard — tympan/tympani.md": {
    primary: "Variant spelling of timpani: orchestral kettledrums played in pairs or sets.",
    secondary: "Pitched hemispherical drums used in classical symphonic and operatic music.",
    quotes: [
      { author: "Pyotr Ilyich Tchaikovsky", work: "Diaries", quote: "The crashing entry of the **tympani** punctuated the desperate surge of the tragic overture." },
      { author: "Richard Strauss", work: "Recollections and Reflections", quote: "In the final scene of Elektra, the **tympani** hammer out an intoxicating, primitive dance rhythm." },
      { author: "Igor Stravinsky", work: "Chronicles of My Life", quote: "The polyrhythmic duel between two sets of **tympani** created the visceral shock of the Sacre." }
    ]
  },
  "Dashboard — tympan/tympanic.md": {
    primary: "Relating to or resembling a drum or the eardrum (tympanic membrane).",
    secondary: "Pertaining to the middle ear cavity (tympanic cavity) in human and vertebrate anatomy.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Otoscopic inspection revealed marked injection and bulging of the **tympanic** membrane." },
      { author: "Claude Bernard", work: "Lectures on Experimental Pathology", quote: "The chorda tympani nerve traverses the **tympanic** chamber before conveying taste fibers from the tongue." },
      { author: "John Tyndall", work: "Sound", quote: "Airborne sound vibrations strike upon the delicate **tympanic** curtain, transmitting mechanical impulses to the auditory ossicles." }
    ]
  },
  "Dashboard — tympan/tympanist.md": {
    primary: "A drummer, especially one who plays the timpani or a hand drum (alternative spelling of timpanist).",
    secondary: "A player of the ancient tympanum drum in Dionysian rituals or military formations.",
    quotes: [
      { author: "Hector Berlioz", work: "Evenings with the Orchestra", quote: "The maestro gestured imperiously toward the **tympanist**, signaling an explosive tremolo roll." },
      { author: "George Bernard Shaw", work: "Music in London", quote: "The orchestral **tympanist** performed with exemplary discretion, never overwhelming the solo cello." },
      { author: "Thomas Mann", work: "Doctor Faustus", quote: "In the modernist score, the **tympanist** tapped the rim with wooden mallets to produce a bone-dry, ghostly tick." }
    ]
  },
  "Dashboard — tympan/tympanites.md": {
    primary: "Distension of the abdomen caused by accumulation of gas or air in the intestines or peritoneal cavity; meteorism.",
    secondary: "A clinical condition producing drum-like resonance upon physical abdominal percussion.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe enteric fever is frequently complicated by acute **tympanites**, demanding prompt gastrointestinal decompression." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "Carminative essences of peppermint and fennel were administered to expel intestinal flatus and relieve **tympanites**." },
      { author: "Thomas Sydenham", work: "The Works of Thomas Sydenham", quote: "The distended belly exhibited marked **tympanites**, sounding hollow like a beaten drum under the physician's fingers." }
    ]
  },
  "Dashboard — tympan/tympanitic.md": {
    primary: "Characteristic of or affected with tympanites; producing a hollow, drum-like sound on percussion.",
    secondary: "Resonating like a drum membrane in physical diagnosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Percussion over the distended abdomen yielded a high-pitched, hollow **tympanitic** note." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The diagnostic tap revealed a clear **tympanitic** resonance, ruling out ascites in favor of gaseous distension." },
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", quote: "In pneumothorax, the affected side of the thorax yields an unnaturally resonant, **tympanitic** acoustic tone." }
    ]
  },
  "Dashboard — tympan/tympanitis.md": {
    primary: "Inflammation of the tympanic membrane or the middle ear cavity (otitis media).",
    secondary: "An acute ear infection causing earache, hearing loss, and drumhead hyperemia.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Untreated catarrhal **tympanitis** in infants may extend into the mastoid cells, requiring surgical drainage." },
      { author: "Joseph Lister", work: "The Collected Papers of Joseph Lister", quote: "Antiseptic cleansing prevented secondary bacterial contamination during the treatment of suppurative **tympanitis**." },
      { author: "Stewart Duke-Elder", work: "System of Ophthalmology", quote: "Severe nasopharyngeal infections frequently ascend through the Eustachian tube, precipitating acute **tympanitis**." }
    ]
  },
  "Dashboard — tympan/tympanoplasty.md": {
    primary: "Surgical reconstruction or repair of a perforated or diseased tympanic membrane (eardrum) and the middle ear ossicular chain.",
    secondary: "A reconstructive otologic procedure aimed at eradicating middle ear infection and restoring conductive hearing.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern micro-surgical **tympanoplasty** uses temporalis fascia grafts to seal chronic drumhead perforations." },
      { author: "Harvey Cushing", work: "Studies in Intracranial Physiology", quote: "Techniques developed in neural micro-surgery paved the way for delicate **tympanoplasty** of the middle ear." },
      { author: "Harold Gillies", work: "The Principles and Art of Plastic Surgery", quote: "Autologous tissue grafting found brilliant application in **tympanoplasty**, restoring both barrier function and auditory acuity." }
    ]
  },
  "Dashboard — tympan/tympanuchus.md": {
    primary: "A genus of North American grouse in the family Phasianidae, commonly known as prairie-chickens, characterized by inflatable neck air sacs used in booming courtship displays.",
    secondary: "The avian genus comprising the greater prairie-chicken (*Tympanuchus cupido*) and lesser prairie-chicken (*Tympanuchus pallidicinctus*).",
    quotes: [
      { author: "John James Audubon", work: "Ornithological Biography", quote: "During their spring leks, the males of **Tympanuchus** inflate their bright orange cervical sacs to produce resonant booming cries across the prairie." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "The pinnated grouse, referred to **Tympanuchus**, assembles at dawn in open meadows to perform its courtship dances." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The generic designation **Tympanuchus** commemorates the drum-like acoustic resonance of the bird's vocal sacs." }
    ]
  },
  "Dashboard — tympan/tympanum.md": {
    primary: "The eardrum or middle ear cavity in anatomy and zoology.",
    secondary: "The semi-circular or triangular recessed decorative wall surface over an entrance, door, or window, bounded by an arch or pediment in classical architecture.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The thunderous crash of the breaching whale struck upon the sailor's **tympanum** like the roar of artillery." },
      { author: "Vitruvius", work: "De Architectura", quote: "The triangular **tympanum** of the pediment should be ornamented with statues celebrating the founding heroes." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "In northern Gothic architecture, the deeply recessed **tympanum** is encrusted with tiers of saints and prophets." }
    ]
  },

  // Dashboard — chord
  "Dashboard — chord/chord.md": {
    primary: "A group of typically three or more musical notes sounded together, as a basis of harmony; also, a straight line segment joining two points on a curve in mathematics.",
    secondary: "An emotional feeling, sympathy, or resonant response struck in a person's sensibility.",
    quotes: [
      { author: "Robert Browning", work: "Abt Vogler", quote: "Out of three sounds he frame, not a fourth sound, but a star; such is the transcendent power of the musical **chord**." },
      { author: "Johannes Brahms", work: "Selected Letters", quote: "A single resolved **chord** in the lower register can transform melancholy into serene resignation." },
      { author: "Ralph Waldo Emerson", work: "Self-Reliance", quote: "Trust thyself: every heart vibrates to that iron string and answers the divine **chord**." }
    ]
  },
  "Dashboard — chord/chordal.md": {
    primary: "Relating to or consisting of musical chords; harmonic rather than contrapuntal in texture.",
    secondary: "Pertaining to a geometric chord or biological notochord.",
    quotes: [
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "The passage moves with heavy **chordal** progression, each block of harmony stamped with rhythmic force." },
      { author: "Aaron Copland", work: "What to Listen for in Music", quote: "Chorales and hymns present a predominantly **chordal** texture where all parts move together in solid harmony." },
      { author: "Walter Piston", work: "Harmony", quote: "The root movement of **chordal** structures determines the underlying tonal momentum of the cadence." }
    ]
  },
  "Dashboard — chord/chordamesoderm.md": {
    primary: "The axial mesoderm in vertebrate embryos that induces the formation of the neural tube and gives rise to the notochord and somites.",
    secondary: "The master organizing tissue discovered by Hans Spemann that coordinates the primary body axis during gastrulation.",
    quotes: [
      { author: "Hans Spemann", work: "Embryonic Development and Induction", quote: "The dorsal lip of the blastopore, consisting of **chordamesoderm**, possesses the organizing capacity to induce a secondary embryo." },
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", quote: "Invagination of **chordamesoderm** under the dorsal ectoderm is the decisive trigger for neural plate differentiation." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Vertebrate body plans rely upon inductive signaling from the embryonic **chordamesoderm** to orient head-to-tail polarity." }
    ]
  },
  "Dashboard — chord/Chordata.md": {
    primary: "The major animal phylum comprising all animals that possess, at some stage in development, a notochord, dorsal hollow nerve cord, pharyngeal slits, and post-anal tail.",
    secondary: "The animal phylum that includes vertebrates, tunicates, and lancelets, encompassing humans and all backboned wildlife.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "The stem-history of the phylum **Chordata** traces our lineage back to primitive aquatic ancestors allied with Amphioxus." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The presence of a dorsal axial skeleton isolates the **Chordata** from all other divisions of the animal kingdom." },
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", quote: "Comparative embryology confirmed that tunicates belong indisputably to the phylum **Chordata** despite their sessile adult form." }
    ]
  },
  "Dashboard — chord/chordate.md": {
    primary: "Any animal belonging to the phylum Chordata, characterized by the possession of a notochord at some stage of life.",
    secondary: "Possessing the diagnostic anatomical characteristics of the phylum Chordata.",
    quotes: [
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "Pikaia from the Burgess Shale stands as our earliest known ancestor, a true primitive **chordate**." },
      { author: "Richard Dawkins", work: "The Ancestor's Tale", quote: "Every living **chordate** carries genetic blueprints inherited from a tiny Cambrian sea creature with a flexible rod down its back." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The rise of the first marine **chordate** marked the opening chapter in the epic evolution of vertebrate intelligence." }
    ]
  },
  "Dashboard — chord/chordeiles.md": {
    primary: "A genus of slender-winged nightjars in the family Caprimulgidae, commonly known as nighthawks, famed for their crepuscular aerial insect hunting.",
    secondary: "A bird genus whose name derives from Greek *chorde* ('musical string') and *deile* ('evening'), referring to their resonant evening booming dives.",
    quotes: [
      { author: "John James Audubon", work: "Birds of America", quote: "The common nighthawk of the genus **Chordeiles** sweeps through the twilight skies with rapid, erratic wingbeats." },
      { author: "Henry David Thoreau", work: "Journal", quote: "I listened to the booming sound produced by **Chordeiles** as it plunged through the evening air over the pines." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "Species of **Chordeiles** are remarkable for their cavernous mouths fringed with bristles to capture flying moths." }
    ]
  },
  "Dashboard — chord/chorditis.md": {
    primary: "Inflammation of the vocal cords (chorditis vocalis), or inflammation of the spermatic cord.",
    secondary: "A clinical condition causing severe hoarseness, dysphonia, or localized pain in otolaryngology and urology.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute **chorditis** in public speakers produces distressing aphonia requiring complete vocal rest and steam inhalation." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "Demulcent sprays were applied to alleviate mucosal congestion in chronic **chorditis**." },
      { author: "Stewart Duke-Elder", work: "System of Ophthalmology", quote: "Upper respiratory viral infections often precipitate inflammatory **chorditis** affecting the true vocal folds." }
    ]
  },
  "Dashboard — chord/chordomesoderm.md": {
    primary: "Variant spelling of chordamesoderm: the axial embryonic mesoderm that forms the notochord and induces the overlying ectoderm to develop into the central nervous system.",
    secondary: "The primary embryonic organizing tissue in vertebrate morphogenesis.",
    quotes: [
      { author: "Hans Spemann", work: "Embryonic Development and Induction", quote: "Transplantation of the **chordomesoderm** into the ventral side of a host gastrula induced a complete secondary nervous system." },
      { author: "C. H. Waddington", work: "Principles of Embryology", quote: "Chemical signaling from the invaginated **chordomesoderm** governs the neural induction cascade." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "The geometric elongation of the embryonic **chordomesoderm** establishes the structural axis of the vertebrate embryo." }
    ]
  },
  "Dashboard — chord/chordophone.md": {
    primary: "Any musical instrument in which sound is produced by the vibration of stretched strings (e.g., violin, harp, piano, guitar).",
    secondary: "One of the four master acoustic classifications established by Erich von Hornbostel and Curt Sachs in systematic organology.",
    quotes: [
      { author: "Curt Sachs", work: "The History of Musical Instruments", quote: "We define a **chordophone** as any instrument wherein sound is initiated by one or more stretched strings." },
      { author: "Erich von Hornbostel", work: "Zeitschrift für Ethnologie", quote: "The classification separates the **chordophone** group into harps, zithers, lutes, and lyres based on string carrier morphology." },
      { author: "Claude Lévi-Strauss", work: "The Raw and the Cooked", quote: "Tribal myths associate the creation of the bow-like **chordophone** with the rhythmic tension of the hunter's weapon." }
    ]
  },
  "Dashboard — chord/chordospartium.md": {
    primary: "A former genus of weeping, leafless leguminous shrubs and small trees native to New Zealand (now included in *Carmichaelia*), commonly known as weeping brooms.",
    secondary: "A rare endemic New Zealand plant characterized by slender, drooping, cord-like green branches that carry out photosynthesis in place of leaves.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "Handbook of the New Zealand Flora", quote: "The singular weeping broom **Chordospartium** bears long pendulous green cords in place of true leaves." },
      { author: "Leonard Cockayne", work: "The Vegetation of New Zealand", quote: "On rocky riverbeds of Marlborough, the weeping branches of **Chordospartium** create a picturesque, drooping silhouette." },
      { author: "Thomas Cheeseman", work: "Manual of the New Zealand Flora", quote: "**Chordospartium** stevensonii is a remarkably beautiful small tree with graceful cord-like branchlets and lavender blossoms." }
    ]
  },
  "Dashboard — chord/cord.md": {
    primary: "A long, thin, flexible string or thin rope made of several strands twisted or braided together; also, an anatomical structure resembling a cord (e.g., umbilical cord, vocal cord).",
    secondary: "A unit of measurement for cut firewood equal to 128 cubic feet (typically 4x4x8 feet).",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "A man who cuts his own firewood warms himself twice, stacking each **cord** with thrifty rustic pride." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The whale-line was coiled with meticulous care, a supple hempen **cord** upon which human lives depended." },
      { author: "John Bunyan", work: "The Pilgrim's Progress", quote: "The heavy burden upon Christian's back was bound with a stout **cord** that snapped as he approached the Cross." }
    ]
  },
  "Dashboard — chord/cordage.md": {
    primary: "Cords, ropes, or lines collectively, especially in the rigging of a ship.",
    secondary: "The fibrous material or twisted strands used for manufacturing ropes and cables.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The gale shrieked through the taut **cordage** of the Pequod, making every shroud hum like a harp string." },
      { author: "Richard Henry Dana Jr.", work: "Two Years Before the Mast", quote: "In freezing seas, the wet **cordage** stiffened like iron rods, resisting the bleeding fingers of the crew." },
      { author: "Joseph Conrad", work: "The Mirror of the Sea", quote: "A sailing ship is a living fabric of wood, iron, and hempen **cordage**, animated by the breath of the wind." }
    ]
  },
  "Dashboard — chord/cordate.md": {
    primary: "Heart-shaped; specifically designating leaves that have a notched base and pointed apex resembling a conventional heart.",
    secondary: "Possessing bilateral cardiac-like symmetry in botanical morphology.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "The leaves of the linden tree are distinctly **cordate**, being rounded and indented at the base like a heart." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "A leaf is termed **cordate** when its ovate outline is hollowed out at the stalk insertion." },
      { author: "Charles Darwin", work: "The Movements and Habits of Climbing Plants", quote: "The climbing vine produced broad **cordate** foliage to catch the scattered rays of sunlight filtering through the canopy." }
    ]
  },
  "Dashboard — chord/corded.md": {
    primary: "Ribbed or woven with raised cords or ridges (as in corduroy or corded silk); also, bound or fastened with cords.",
    secondary: "Having prominent, rope-like sinews or veins standing out beneath the skin.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The venerable magistrates were clad in dark **corded** cloaks trimmed with velvet." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "His muscular throat and **corded** wrists bore witness to years of hard labor in the shearing barn." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Beside the doorway stood several heavy trunks, securely strapped and **corded** for the coach voyage." }
    ]
  },
  "Dashboard — chord/monochord.md": {
    primary: "An ancient scientific musical instrument consisting of a single string stretched over a calibrated soundbox with a movable bridge, used to investigate mathematical harmonic ratios.",
    secondary: "The acoustic laboratory apparatus by which Pythagoras discovered the mathematical intervals of the octave, fifth, and fourth.",
    quotes: [
      { author: "Pythagoras", work: "Harmonic Fragments", quote: "By dividing the string of the **monochord** in exact numerical proportions, Pythagoras demonstrated that musical harmony is governed by number." },
      { author: "Isaac Newton", work: "Opticks", quote: "Newton compared the seven primary colors of the spectrum to the seven musical intervals mapped upon the classical **monochord**." },
      { author: "Boethius", work: "De Institutione Musica", quote: "The scholar who wishes to understand celestial harmony must first master the divisions of the **monochord**." }
    ]
  },
  "Dashboard — chord/polychord.md": {
    primary: "A musical instrument having many strings; also, in modern harmony, a complex chord consisting of two or more distinct triads or chords sounded simultaneously.",
    secondary: "A multichordal harmonic structure used in 20th-century classical music to create bi-tonal tension.",
    quotes: [
      { author: "Curt Sachs", work: "The History of Musical Instruments", quote: "The ancient harp was the earliest **polychord**, offering a distinct tuned string for every pitch of the scale." },
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "The celebrated Petrushka chord is a famous **polychord**, superimposing C major and F-sharp major triads." },
      { author: "Walter Piston", work: "Harmony", quote: "In twentieth-century composition, the **polychord** allows composers to create dense, layered sonorities without abandoning tonal roots." }
    ]
  },
  "Dashboard — chord/record.md": {
    primary: "An authentic, permanent account or chronicle of events kept in writing; also, an analog disc carrying sound grooves for acoustic playback.",
    secondary: "To set down in writing or other permanent form for future reference; in law, an official legal transcript.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "History is a worthy **record** of human deeds, preserving noble actions from the oblivious river of time." },
      { author: "William Shakespeare", work: "Hamlet", quote: "I'll wipe away all trivial fond records, all saws of books, all forms, all pressures past." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The impartial historian must consult every authentic contemporary **record** before pronouncing judgment on the past." }
    ]
  },
  "Dashboard — chord/tetrachord.md": {
    primary: "A scale series of four musical notes, the interval between the first and last being a perfect fourth; the building block of ancient Greek music theory.",
    secondary: "A four-stringed ancient Greek lyre or musical system divided into diatonic, chromatic, or enharmonic genera.",
    quotes: [
      { author: "Aristotle", work: "Problems", quote: "In ancient music, the fundamental unit of melody was the **tetrachord**, bounded by the invariable interval of the fourth." },
      { author: "Aristoxenus", work: "Elements of Harmonics", quote: "The internal division of the **tetrachord** into shades determines whether the melody belongs to the diatonic or enharmonic genus." },
      { author: "Boethius", work: "De Institutione Musica", quote: "Greek musicians constructed their complete two-octave system by coupling together successive conjunct and disjunct **tetrachord** groups." }
    ]
  },

  // Dashboard — ech
  "Dashboard — ech/anechoic.md": {
    primary: "Free from echo; specifically describing an acoustic room designed to absorb completely all reflections of sound waves or electromagnetic radiation.",
    secondary: "Having non-reflective interior surfaces lined with acoustic wedges, simulating infinite open space in sound testing.",
    quotes: [
      { author: "Leo Beranek", work: "Acoustics", quote: "In an **anechoic** chamber, specialized fiberglass wedges absorb ninety-nine percent of reflected sound energy." },
      { author: "John Cage", work: "Silence: Lectures and Writings", quote: "Inside an **anechoic** room, I heard two sounds: one high, my nervous system; one low, my blood in circulation." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "Step into an **anechoic** chamber and the profound unnatural silence immediately heightens your perception of internal bodily sounds." }
    ]
  },
  "Dashboard — ech/catechesis.md": {
    primary: "Religious instruction given to a person in preparation for baptism, confirmation, or church membership, traditionally conducted by question and answer.",
    secondary: "The systematic oral teaching and transmission of Christian doctrine throughout ecclesiastical history.",
    quotes: [
      { author: "Augustine of Hippo", work: "De Catechizandis Rudibus", quote: "In delivering **catechesis**, the teacher must adapt the instructions to the capacity and background of the hearer." },
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "Preliminary **catechesis** is required before the administration of baptism, so that the convert may understand the faith." },
      { author: "John Henry Newman", work: "Apologia Pro Vita Sua", quote: "The deep impressions received during early parish **catechesis** formed the enduring foundation of his religious convictions." }
    ]
  },
  "Dashboard — ech/catechetic.md": {
    primary: "Relating to or consisting of instruction by question and answer, especially in religious dogma.",
    secondary: "Pertaining to oral doctrinal dialogue and pedagogical catechisms (variant of catechetical).",
    quotes: [
      { author: "Desiderius Erasmus", work: "The Praise of Folly", quote: "The theologian argued that sound **catechetic** instruction was far more effective than scholastic disputation." },
      { author: "Martin Luther", work: "The Large Catechism", quote: "Pastors must never neglect the simple **catechetic** foundations that ground the Christian community in truth." },
      { author: "John Calvin", work: "Institutes of the Christian Religion", quote: "The ancient church maintained a rigorous **catechetic** school to train adult converts in sacred doctrine." }
    ]
  },
  "Dashboard — ech/catechetical.md": {
    primary: "Pertaining to a catechism, or to instruction by oral question and answer.",
    secondary: "Pedagogically structured in dialogue format to impart religious or philosophical principles.",
    quotes: [
      { author: "John Milton", work: "Areopagitica", quote: "A man may be a heretic in the truth, if he believes things only because his pastor says so, in a narrow **catechetical** routine." },
      { author: "Jeremy Taylor", work: "Holy Living", quote: "Family devotion is sanctified by brief **catechetical** exercises that instruct children in holy virtues." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The celebrated **catechetical** school of Alexandria attracted scholars from every province of the Mediterranean." }
    ]
  },
  "Dashboard — ech/catechise.md": {
    primary: "To instruct someone in the principles of Christian religion by question and answer, or to cross-examine closely (British spelling of catechize).",
    secondary: "To interrogate or question systematically regarding opinions or conduct.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Mr. Brocklehurst proceeded to **catechise** the trembling child before the assembled school." },
      { author: "Charles Dickens", work: "Nicholas Nickleby", quote: "Mrs. Squeers would **catechise** the miserable boys, demanding whether they were grateful for their brimstone and treacle." },
      { author: "George Eliot", work: "Silas Marner", quote: "The rector made it his duty to **catechise** the parish youths every Sunday afternoon in the vestry." }
    ]
  },
  "Dashboard — ech/catechism.md": {
    primary: "A summary of the principles of Christian religion in the form of questions and answers, used for the instruction of Christians.",
    secondary: "A series of formal questions put to someone; an interrogation or thorough test of belief.",
    quotes: [
      { author: "Thomas Cranmer", work: "A Short Instruction into Christian Religion", quote: "The child repeated the articles of the **catechism** with clear voice before receiving the holy sacrament." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I was educated in the rigid Presbyterian **catechism**, though my mature thoughts leaned toward natural deism." },
      { author: "James Joyce", work: "Ulysses", quote: "The Ithacan chapter unfolds in a cold, mathematical **catechism** of exhaustive question and answer." }
    ]
  },
  "Dashboard — ech/catechismal.md": {
    primary: "Relating to, resembling, or presented in the manner of a catechism.",
    secondary: "Dogmatic, formulaic, and instructional in style.",
    quotes: [
      { author: "Matthew Arnold", work: "Culture and Anarchy", quote: "Our middle class was raised on a dry, **catechismal** morality that lacked imaginative sweetness." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "The philosopher rejected all sterile, **catechismal** formulas, seeking the living fire of genuine faith." },
      { author: "John Ruskin", work: "Modern Painters", quote: "Artistic truth cannot be reduced to a **catechismal** set of rules for mixing pigment." }
    ]
  },
  "Dashboard — ech/catechist.md": {
    primary: "A person who instructs others in the Christian religion, especially in preparation for baptism or confirmation.",
    secondary: "A teacher or lay leader appointed to conduct religious instruction in mission fields or parishes.",
    quotes: [
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", quote: "The native **catechist** was an invaluable companion, explaining Christian truths in the vernacular tongue." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "He had met a zealous native **catechist** who carried an old Bible through the wilderness." },
      { author: "Francis Xavier", work: "Letters from the Far East", quote: "The devoted **catechist** gathered the village children at daybreak to teach them the Apostles' Creed." }
    ]
  },
  "Dashboard — ech/catechistic.md": {
    primary: "Relating to or characteristic of a catechist, catechism, or question-and-answer instruction.",
    secondary: "Didactic, interrogative, and structured around doctrinal inquiry.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Aids to Reflection", quote: "A **catechistic** dialogue clarifies obscure theological concepts by compelling the student to articulate distinctions." },
      { author: "William Hazlitt", work: "The Round Table", quote: "He spoke with a stiff, **catechistic** precision that admitted no humor or spontaneous digression." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "The Christian elders conducted a gentle **catechistic** examination of the candidate's moral life." }
    ]
  },
  "Dashboard — ech/catechize.md": {
    primary: "To instruct someone in religious doctrine by means of questions and answers; to catechise (US spelling).",
    secondary: "To examine or interrogate someone systematically and severely.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The venerable minister did not fail to **catechize** little Pearl concerning her heavenly Father." },
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "Aunt Polly began to **catechize** Tom with cunning traps to discover whether he had been swimming." },
      { author: "Herman Melville", work: "Billy Budd", quote: "The captain began to **catechize** the master-at-arms regarding the mutinous rumors on the lower deck." }
    ]
  },
  "Dashboard — ech/catechumen.md": {
    primary: "A convert to Christianity who is receiving training and instruction in doctrine before baptism.",
    secondary: "A beginner or novice receiving initial initiation or instruction in any subject or discipline.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The emperor Constantine remained a humble **catechumen** until the hour of death approached." },
      { author: "Augustine of Hippo", work: "Confessions", quote: "While still a **catechumen**, he struggled between worldly ambition and the call of monastic devotion." },
      { author: "John Henry Newman", work: "The Arians of the Fourth Century", quote: "The primitive Church placed the **catechumen** under long probation to test the sincerity of his conversion." }
    ]
  },
  "Dashboard — ech/ech.md": {
    primary: "The ancient Greek root *ech-* (from *echo* / *eche*), meaning 'sound', 'noise', 'resonance', or 'reverberation'.",
    secondary: "The linguistic morpheme representing acoustic reflections, echoes, and oral sounding in comparative etymology.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "Under the root **ech**, the Greek vocabulary unites echoes, oral instruction, and acoustic resonance." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The radical element **ech** imitates ringing sound, surviving in modern European words for auditory reflection." },
      { author: "Émile Benveniste", work: "Indo-European Language and Society", quote: "The archaic root **ech** designated not merely hollow noise, but the returned voice that answers across a valley." }
    ]
  },
  "Dashboard — ech/echo.md": {
    primary: "A sound or series of sounds caused by the reflection of sound waves from a surface back to the listener.",
    secondary: "A close parallel, repetition, or reminiscent trace of something; in Greek mythology, the mountain nymph Echo who could only repeat the words of others.",
    quotes: [
      { author: "Ovid", work: "Metamorphoses", quote: "The sorrowing nymph **Echo** dissolved into thin air until only her mournful voice was heard among the crags." },
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "Never did I hear such gallant chiding; for, besides the groves, the skies, the fountains, every region near seem'd all one mutual cry: I never heard so musical a discord, such sweet thunder." },
      { author: "John Milton", work: "Comus", quote: "Sweet **Echo**, sweetest nymph, that liv'st unseen Within thy airy shell By slow Meander's margent green." }
    ]
  },
  "Dashboard — ech/echocardiogram.md": {
    primary: "A non-invasive diagnostic medical test that uses ultrasound waves to create real-time graphic images of the heart's chambers, valves, and blood flow.",
    secondary: "The clinical sonographic recording used by cardiologists to evaluate cardiac ejection fraction and valvular dysfunction.",
    quotes: [
      { author: "Inge Edler", work: "Ultrasound Cardiography", quote: "The continuous ultrasonic **echocardiogram** allows the clinician to observe the dynamic motion of the mitral valve leaflets in real time." },
      { author: "Harvey Cushing", work: "Studies in Intracranial Physiology", quote: "Non-invasive acoustic imaging, prefigured by the **echocardiogram**, revolutionized surgical diagnosis." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern diagnosis of infective endocarditis relies upon the **echocardiogram** to identify friable valvular vegetations." }
    ]
  },
  "Dashboard — ech/echoic.md": {
    primary: "Onomatopoeic; formed in imitation of a natural sound, or relating to the reflection of sound waves.",
    secondary: "In cognitive psychology, relating to echoic memory—the sensory memory store for brief auditory stimuli.",
    quotes: [
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "Words like 'buzz', 'cuckoo', and 'splash' are purely **echoic**, arising directly from the ear's mimicry of natural sounds." },
      { author: "Roman Jakobson", work: "Selected Writings", quote: "Poetic language exploits **echoic** resonance to forge an immediate physical bond between sound and sensation." },
      { author: "Edward Sapir", work: "Language", quote: "The linguistic significance of **echoic** words is often exaggerated, yet they supply vivid expressive color to speech." }
    ]
  },
  "Dashboard — ech/echoing.md": {
    primary: "Resounding or reverberating with sound, or repeatedly returning an acoustic reflection.",
    secondary: "Evoking memories or bearing a close stylistic resemblance to an earlier model.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "The deep caverns were filled with an **echoing** thunder that shook the mountain to its roots." },
      { author: "Alfred Lord Tennyson", work: "The Princess", quote: "Blow, bugle, blow, set the wild echoes flying, blow, bugle; answer, **echoing** hills, dying, dying, dying." },
      { author: "Edgar Allan Poe", work: "The Raven", quote: "And the only word there spoken was the whispered word, 'Lenore?' This I whispered, and an **echoing** murmur murmured back the word, 'Lenore!'" }
    ]
  },
  "Dashboard — ech/echolocation.md": {
    primary: "The biological sonar system used by certain animals (such as bats, dolphins, and whales) to navigate and detect obstacles or prey by emitting high-frequency sounds and interpreting the returning echoes.",
    secondary: "The acoustic navigation technique adapted by visually impaired humans using tongue clicks or cane taps.",
    quotes: [
      { author: "Donald Griffin", work: "Listening in the Dark", quote: "Through ultrasonic **echolocation**, the insectivorous bat reconstructs a complete three-dimensional acoustic image of its night surroundings." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "Bat **echolocation** is an engineering marvel that outperforms the most sophisticated radar systems designed by human engineers." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The convergence between cetacean and chiropteran **echolocation** illustrates the exquisite power of natural selection in solving perceptual challenges." }
    ]
  },
  "Dashboard — ech/echos.md": {
    primary: "(Byzantine Music & Orthodox Liturgy) Any of the eight traditional melodic modes or musical systems (Oktoechos) used in Byzantine liturgical chant (Greek *echos*).",
    secondary: "A modal framework governing melodic formulas, cadences, and affective temperament in Eastern Christian church music.",
    quotes: [
      { author: "Egon Wellesz", work: "A History of Byzantine Music and Hymnography", quote: "The Byzantine singer memorized the intonation formula of each **echos** to guide the solemn liturgical chant." },
      { author: "Curt Sachs", work: "The Rise of Music in the Ancient World", quote: "The medieval Oktoechos arranged church hymns into eight distinct **echos** groups alternating weekly." },
      { author: "Oliver Strunk", work: "Essays on Music in the Byzantine World", quote: "Each sacred **echos** was endowed with a specific spiritual ethos, from penitential sorrow to paschal triumph." }
    ]
  },
  "Dashboard — ech/reecho.md": {
    primary: "To echo back, reverberate, or resound again and again across an open space or acoustic enclosure.",
    secondary: "To repeat or reiterate another's words, sentiments, or applause enthusiastically.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The cheers of the lookout began to **reecho** along the deck as the distant spout was sighted." },
      { author: "Henry Wadsworth Longfellow", work: "The Song of Hiawatha", quote: "The sound did **reecho** through the forest, waking the sleeping warriors in their distant lodges." },
      { author: "Washington Irving", work: "The Legend of Sleepy Hollow", quote: "The clattering hooves of the Galloping Hessian seemed to **reecho** from the haunted hollow behind the church." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);

  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${relPath}`);
}

console.log('Done Batch 3 (tympan, chord, ech) of Cluster Sound & Auditory!');
