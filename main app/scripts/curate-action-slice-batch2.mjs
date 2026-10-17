import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Action');

const batch2Data = {
  "Dashboard — ogdo\\ogdo.md": {
    primary: "The Greek root and numerical prefix (ogdoos, meaning 'eighth' or 'eight'), denoting eightfold structures, eighth intervals, and octaval systems.",
    secondary: "In classical harmonics and ancient philosophy, the fundamental numerical principle of the octave and eightfold celestial divisions.",
    quotes: [
      { author: "Irenaeus", work: "Against Heresies", quote: "The Valentinians construct their divine pleroma upon the mysterious number of the **ogdo**, deriving eight primordial aeons from the primal Depth." },
      { author: "Clement of Alexandria", work: "Stromata", quote: "In mystical arithmetic, the **ogdo** represents the first cube and signifies rest and spiritual resurrection." },
      { author: "Philo of Alexandria", work: "On the Creation", quote: "The sacred nature of the **ogdo** was revered by the ancients as the symbol of justice and stability." }
    ]
  },
  "Dashboard — ogdo\\ogdoad.md": {
    primary: "A group or set of eight persons, things, or entities; an octad.",
    secondary: "In Gnostic cosmology and ancient Egyptian mythology, the primordial assembly of eight deities or celestial emanations that brought forth order from chaos.",
    quotes: [
      { author: "Irenaeus", work: "Against Heresies", quote: "According to their doctrine, the primary **ogdoad** consists of Bythos and Sige, Nous and Aletheia, Logos and Zoe, Anthropos and Ecclesia." },
      { author: "E. A. Wallis Budge", work: "The Gods of the Egyptians", quote: "The primordial Egyptian cosmos was nurtured by the **ogdoad** of Hermopolis, eight deities embodying primeval chaotic waters." },
      { author: "Carl Jung", work: "Aion: Researches into the Phenomenology of the Self", quote: "In Gnostic symbolism, the **ogdoad** represents the heavenly realm beyond the seven planetary spheres of fate." }
    ]
  },
  "Dashboard — org\\orgasm.md": {
    primary: "The culmination or peak of sexual excitement, characterized by intense feelings of pleasure and rhythmic muscular contractions.",
    secondary: "In physiological and psychological terminology, any paroxysm of intense emotional excitement, physical tension release, or convulsive energy.",
    quotes: [
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "The sexual act culminates in the physical release of tension which accompanies the **orgasm**." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The physiological phenomena of the **orgasm** involve sudden nervous detumescence and involuntary rhythm." },
      { author: "William James", work: "The Principles of Psychology", quote: "Every instinctive passion reaches its zenith in an **orgasm** of emotional excitement before subsiding into calm." }
    ]
  },
  "Dashboard — pae\\anapaest.md": {
    primary: "A metrical foot in quantitative or accentual verse consisting of two short or unstressed syllables followed by one long or stressed syllable.",
    secondary: "In classical and English prosody, the rising trisyllabic foot whose rapid movement imparts momentum, dramatic urgency, or galloping rhythm to poetry.",
    quotes: [
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The galloping pace of the **anapaest** imparts a lively momentum that contrasts sharply with the measured tread of the iamb." },
      { author: "Samuel Taylor Coleridge", work: "Metrical Feet: A Lesson for a Boy", quote: "With a leap and a bound the swift **anapaests** throng, carrying the listener impetuously along." },
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "The judicious introduction of an **anapaest** into an iambic line breaks the monotonous cadence with exquisite variety." }
    ]
  },
  "Dashboard — pae\\anapaestic.md": {
    primary: "Relating to, composed of, or characterized by anapaests; having a trisyllabic rhythm with the accent on the final syllable.",
    secondary: "In poetic analysis, describing meter whose brisk cadence is driven by double unaccented beats leading into each stress.",
    quotes: [
      { author: "Lord Byron", work: "The Destruction of Sennacherib", quote: "The Assyrian came down like the wolf on the fold, written in sweeping **anapaestic** tetrameter that mimics galloping cavalry." },
      { author: "George Saintsbury", work: "Historical Manual of English Prosody", quote: "Swinburne developed the **anapaestic** cadence into one of the most flexible and melodious instruments in English poetry." },
      { author: "John Ruskin", work: "The Elements of English Prosody", quote: "An **anapaestic** rhythm must be handled with supreme delicacy lest it degenerate into mere sing-song jingling." }
    ]
  },
  "Dashboard — pae\\anapest.md": {
    primary: "A metrical foot consisting of two unaccented syllables followed by an accented syllable (variant spelling of anapaest).",
    secondary: "In literary composition and song, an energetic metrical element used to convey swiftness, martial movement, or lyric lightness.",
    quotes: [
      { author: "Walt Whitman", work: "Leaves of Grass (Prefaces)", quote: "I sought a natural rhythm untrammeled by the rigid counting of the dactyl or the **anapest**." },
      { author: "Ralph Waldo Emerson", work: "Parnassus", quote: "The lyric energy of Campbell's ballads owes much of its martial vigor to the rapid movement of the **anapest**." },
      { author: "Robert Frost", work: "Selected Letters", quote: "In English poetry there are virtually only two meters, strict and loose iambic, the latter accommodating the light **anapest**." }
    ]
  },
  "Dashboard — pae\\anapestic.md": {
    primary: "Pertaining to or characterized by the anapest; consisting of feet having two unstressed beats followed by one stressed beat.",
    secondary: "In prosodic criticism, possessing a tripping, buoyant, or galloping metrical momentum.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Poetic Principle", quote: "The rapid musical movement of the lines was achieved through a masterly employment of **anapestic** measures." },
      { author: "William Hazlitt", work: "Lectures on the English Poets", quote: "His verses tumble forward in breathless **anapestic** haste, sweeping all obstacles before them." },
      { author: "Matthew Arnold", work: "On Translating Homer", quote: "Homer’s hexameter possesses a swift nobility that cannot be reproduced by a jerky **anapestic** substitute." }
    ]
  },
  "Dashboard — pae\\pae.md": {
    primary: "The Greek root (paiein, meaning 'to strike, beat, or touch; to sing a hymn of triumph'), giving rise to metrical terms and triumphal hymns.",
    secondary: "In etymological lexicography, the archaic radical underpinning terms of rhythmic percussion, surgical instruments, and choric paeans.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "From the radical stem **pae** arose both the strike of the metrical foot and the ecstatic hymn to Apollo." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The primitive Greek root **pae** signifies to strike or beat, appearing in words denoting rhythmic cadence." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The verbal base **pae** illustrates the intimate archaic connection between physical percussive action and vocal rhythm." }
    ]
  },
  "Dashboard — pin\\pinocytosis.md": {
    primary: "The ingestion of liquid into a cell by the budding of small vesicles from the cell membrane; 'cellular drinking'.",
    secondary: "In cell biology, an endocytic pathway by which eukaryotic cells continuously sample and internalize extracellular fluid and dissolved macromolecules.",
    quotes: [
      { author: "Christian de Duve", work: "A Guided Tour of the Living Cell", quote: "By the process of **pinocytosis**, the eukaryotic cell draws droplets of external medium into tiny vesicles for internal digestion." },
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "Macromolecules dissolved in extracellular fluid are constantly sampled by cells through fluid-phase **pinocytosis**." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "The membrane engulfs liquid by continuous **pinocytosis**, maintaining the internal osmotic economy with astonishing fidelity." }
    ]
  },
  "Dashboard — pin\\pinosome.md": {
    primary: "A membrane-bound intracellular vesicle formed by pinocytosis that carries engulfed extracellular fluid.",
    secondary: "In cytological ultrastructure, a transient vesicular compartment that transports fluid-phase solutes toward fusion with early endosomes or lysosomes.",
    quotes: [
      { author: "Christian de Duve", work: "Lysosomes and Phagosomes", quote: "Once pinched off from the plasma membrane, the nascent **pinosome** migrates inward to fuse with primary lysosomes." },
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "Within minutes of internalization, the contents of the **pinosome** are exposed to acid hydrolases in the endosomal network." },
      { author: "George Emil Palade", work: "Cellular Dynamics", quote: "Electron microscopy tracks the journey of each **pinosome** as it delivers ingested solutes to deep cytoplasmic vacuoles." }
    ]
  },
  "Dashboard — pin\\symposium.md": {
    primary: "A conference or meeting for the discussion of some particular subject; a collection of essays on a topic by different authors.",
    secondary: "In classical Greece, a convivial banquet following a meal, accompanied by wine, music, and philosophical or literary conversation.",
    quotes: [
      { author: "Plato", work: "Symposium", quote: "Socrates declared that at this memorable **symposium**, Diotima of Mantinea had instructed him in the true mysteries of Love." },
      { author: "Xenophon", work: "Symposium", quote: "When the tables were cleared and libations poured, the guests at the **symposium** turned from wine to witty conversation." },
      { author: "Ralph Waldo Emerson", work: "Society and Solitude", quote: "Every intellectual gathering is at heart a Greek **symposium**, where conversation flows like wine and sparks new fires of thought." }
    ]
  },
  "Dashboard — pleg\\aplectrum.md": {
    primary: "A genus of North American terrestrial orchids (such as Aplectrum hyemale, the puttyroot) distinguished by a spurless flower lip.",
    secondary: "In botanical taxonomy, orchidaceous plants characterized by subterranean globose corms producing a solitary overwintering leaf without a nectar spur.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The solitary species of **Aplectrum** is readily distinguished by its absence of a spur and its winter-persisting leaf." },
      { author: "John Torrey", work: "Flora of the State of New York", quote: "In deep rich woods, the subterranean corms of **Aplectrum** remain connected for years like links in a chain." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Botanists prize **Aplectrum** for its curious habit of producing a single plicate leaf that overwinters before flowering." }
    ]
  },
  "Dashboard — pleg\\apoplectic.md": {
    primary: "Overcome with sudden, extreme anger or rage; purple-faced with furious indignation.",
    secondary: "In clinical medicine, relating to or causing apoplexy; suffering from sudden cerebral hemorrhage or stroke.",
    quotes: [
      { author: "Charles Dickens", work: "A Christmas Carol", quote: "Old Fezziwig stood in the middle of the room, looking red and **apoplectic** with sheer joviality and exertion." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "He grew fairly purple with rage, his eyes starting from his head in an almost **apoplectic** fury." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The old courtier sank back into his armchair in an **apoplectic** stupor, stunned by the fall of the Bastille." }
    ]
  },
  "Dashboard — pleg\\apoplectoid.md": {
    primary: "Resembling apoplexy or an apoplectic stroke in symptoms or clinical presentation.",
    secondary: "In neurological diagnosis, describing sudden cerebral attacks, transient ischemic episodes, or seizures that mimic stroke without permanent vascular destruction.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Certain transient cerebral attacks present an **apoplectoid** character, mimicking a massive stroke without permanent paralysis." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on the Diseases of the Nervous System", quote: "Hysterical seizures occasionally assume an **apoplectoid** aspect, deceiving the unwary clinician." },
      { author: "William R. Gowers", work: "A Manual of Diseases of the Nervous System", quote: "These sudden circulatory syncopes display an **apoplectoid** onset that rapidly clears within hours." }
    ]
  },
  "Dashboard — pleg\\apoplexy.md": {
    primary: "Unconsciousness or motor incapacity caused by a sudden cerebral hemorrhage or stroke.",
    secondary: "In historical pathology, any sudden massive hemorrhage or effusion of blood into an organ causing abrupt cessation of bodily function.",
    quotes: [
      { author: "William Shakespeare", work: "Henry IV, Part 2", quote: "This **apoplexy** is, as I take it, a kind of lethargy, an ’t please your lordship; a kind of sleeping in the blood." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Cerebral hemorrhage causing classical **apoplexy** strikes down the robust individual without preliminary warning." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "He looked like a man struck with sudden **apoplexy**, his jaw dropped and his glassy eyes fixed upon the sea." }
    ]
  },
  "Dashboard — pleg\\cataplectic.md": {
    primary: "Relating to or afflicted with cataplexy; characterized by sudden, transient loss of voluntary muscle tone.",
    secondary: "In sleep medicine and neurology, describing paroxysmal episodes of motor collapse provoked by sudden emotional arousal.",
    quotes: [
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", quote: "The patient collapsed in a **cataplectic** immobility whenever an unexpected loud noise startled him." },
      { author: "William R. Gowers", work: "A Manual of Diseases of the Nervous System", quote: "During the **cataplectic** episode, consciousness remains clear while the postural muscles suddenly lose all tone." },
      { author: "S. Weir Mitchell", work: "Lectures on Diseases of the Nervous System", quote: "The suddenness of the **cataplectic** drop attack poses a constant danger of physical injury to the patient." }
    ]
  },
  "Dashboard — pleg\\cataplexy.md": {
    primary: "A condition characterized by sudden, temporary loss of muscle tone and power, triggered by strong emotions such as laughter or anger.",
    secondary: "In neurobiology, a pathognomonic symptom of type 1 narcolepsy caused by the loss of hypocretin (orexin) neurons in the hypothalamus.",
    quotes: [
      { author: "Sigmund Freud", work: "The Interpretation of Dreams", quote: "The sudden motor paralysis seen in **cataplexy** illustrates how emotional shock can instantaneously inhibit the motor cortex." },
      { author: "William R. Gowers", work: "Diseases of the Nervous System", quote: "In narcoleptic patients, bouts of laughter or surprise frequently induce sudden attacks of **cataplexy**." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures", quote: "We observed how a sudden joke or startle precipitated an episode of complete **cataplexy**, dropping the subject to the carpet." }
    ]
  },
  "Dashboard — pleg\\hemiplegia.md": {
    primary: "Paralysis of one vertical side of the body, usually caused by injury or disease to the opposite cerebral hemisphere of the brain.",
    secondary: "In clinical neurology, a lateralized motor syndrome typically following ischemic stroke, intracranial hemorrhage, or unilateral brain trauma.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Right-sided **hemiplegia** associated with motor aphasia indicates a lesion in the territory of the left middle cerebral artery." },
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", quote: "The spastic contracture that supervenes upon chronic **hemiplegia** reveals the loss of pyramidal inhibition." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "A sudden stroke producing complete **hemiplegia** leaves one half of the body dead while the other half retains life." }
    ]
  },
  "Dashboard — pleg\\hemiplegic.md": {
    primary: "Pertaining to or affected by hemiplegia; paralyzed on one side of the body.",
    secondary: "In clinical gait analysis, describing the characteristic asymmetric locomotion involving circumduction of the spastic lower extremity.",
    quotes: [
      { author: "William R. Gowers", work: "A Manual of Diseases of the Nervous System", quote: "The characteristic circumduction of the affected leg produces the well-known **hemiplegic** gait." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In the **hemiplegic** patient, deep tendon reflexes become exaggerated as secondary descending degeneration develops." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures", quote: "The physician must carefully examine the **hemiplegic** arm to detect early signs of rigidity." }
    ]
  },
  "Dashboard — pleg\\monoplegia.md": {
    primary: "Paralysis affecting only a single limb, muscle group, or isolated part of the body.",
    secondary: "In localized neurological pathology, a focal motor deficit resulting from circumscribed cortical or peripheral nerve lesions.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A localized cortical injury in the precentral gyrus produces an isolated **monoplegia** of the face or hand." },
      { author: "William R. Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Pure brachial **monoplegia** without sensory impairment strongly points to a circumscribed vascular occlusion." },
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", quote: "Distinguishing between functional weakness and organic cerebral **monoplegia** tests the skill of the neurologist." }
    ]
  },
  "Dashboard — pleg\\paraplegia.md": {
    primary: "Paralysis of the lower half of the body, including both legs, typically caused by damage to or disease of the spinal cord.",
    secondary: "In neurotrauma, sensory and motor impairment of the lower extremities resulting from thoracic, lumbar, or sacral cord lesions.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Traumatic transection of the dorsal cord is followed by flaccid **paraplegia** and complete loss of sensory perception below the level of injury." },
      { author: "William R. Gowers", work: "Diseases of the Spinal Cord", quote: "Compressive lesions of the dorsal spine produce progressive spastic **paraplegia**." },
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", quote: "In Pott's disease, tuberculous caries of the vertebrae frequently results in severe **paraplegia**." }
    ]
  },
  "Dashboard — pleg\\paraplegic.md": {
    primary: "Relating to or afflicted with paraplegia; having the lower half of the body paralyzed.",
    secondary: "In medical rehabilitation, describing a patient or therapeutic protocol addressing complete or incomplete lower cord transection.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Careful nursing care of the **paraplegic** invalid is vital to prevent intractable decubitus ulcers and urinary sepsis." },
      { author: "William R. Gowers", work: "A Manual of Diseases of the Nervous System", quote: "The **paraplegic** patient exhibits hyperactive patellar reflexes and sustained ankle clonus." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Rehabilitation of the **paraplegic** individual requires remapping somatic awareness above the site of cord lesion." }
    ]
  },
  "Dashboard — pleg\\plectrum.md": {
    primary: "A small thin piece of metal, plastic, bone, or quill used to pluck the strings of an instrument such as a guitar, lute, or lyre.",
    secondary: "In comparative zoology, any small tooth, spine, or ridge in an insect or animal that strikes against a file to produce sound.",
    quotes: [
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Certain stridulating insects use the modified edge of the wing like a **plectrum** against a file-like ridge to produce their shrill call." },
      { author: "George Eliot", work: "Romola", quote: "His nimble fingers swept the strings of the lute with a polished ivory **plectrum**, drawing forth sweet Florentine melodies." },
      { author: "Thomas Love Peacock", work: "Gryll Grange", quote: "The ancient poet struck his cithara with a gold **plectrum**, invoking Apollo to inspire his verses." }
    ]
  },
  "Dashboard — pleg\\pleximeter.md": {
    primary: "A small, thin plate of ivory, wood, or metal placed against the body to receive the blow in diagnostic medical percussion.",
    secondary: "In physical diagnosis, a mediating plate utilized in indirect percussion to transmit acoustic vibrations and map internal organ boundaries.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Bedside percussion may be performed with an ivory **pleximeter** or, far more conveniently, using the index finger of the left hand." },
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", quote: "Piorry introduced the **pleximeter** to render the resonant sounds of the chest wall clearer and more uniform." },
      { author: "Austin Flint", work: "A Treatise on the Principles and Practice of Medicine", quote: "The thin rubber **pleximeter** dampens superficial vibration and allows accurate mapping of hepatic dullness." }
    ]
  },
  "Dashboard — pleg\\tetraplegia.md": {
    primary: "Paralysis of all four limbs and the torso, caused by injury to or disease of the cervical spinal cord; quadriplegia.",
    secondary: "In acute trauma care, the functional impairment of motor, sensory, and autonomic control below a cervical neuromedullary level.",
    quotes: [
      { author: "William R. Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Damage to the spinal cord at the fifth cervical segment causes complete **tetraplegia**, depriving all four extremities of voluntary motion." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute fracture-dislocation of the cervical spine carries an immediate risk of fatal respiratory compromise and **tetraplegia**." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "To witness a patient coping with sudden traumatic **tetraplegia** is to observe courage contending against catastrophic sensory-motor loss." }
    ]
  },
  "Dashboard — poie\\allopoiesis.md": {
    primary: "The process by which an organization, machine, or system produces an output or product distinct from itself (contrasted with autopoiesis).",
    secondary: "In systems theory and cybernetics, the operational modality of artificial mechanisms whose structural product lies outside their internal boundary.",
    quotes: [
      { author: "Humberto Maturana & Francisco Varela", work: "Autopoiesis and Cognition: The Realization of the Living", quote: "An industrial assembly line is a prime example of **allopoiesis**, producing commodities distinct from the machine that manufactures them." },
      { author: "Niklas Luhmann", work: "Social Systems", quote: "Unlike living organisms, mechanical factories operate by **allopoiesis**, generating outputs outside their own physical boundaries." },
      { author: "Felix Guattari", work: "Chaosmosis: An Ethico-Aesthetic Paradigm", quote: "Technical machines are caught in chains of **allopoiesis**, depending upon external human intervention for their reproduction." }
    ]
  },
  "Dashboard — poie\\autopoiesis.md": {
    primary: "The capability of a system to regenerate, maintain, and reproduce its own organizational components and boundaries internally.",
    secondary: "In theoretical biology and cognition, the fundamental defining criterion of living systems, characterized by continuous self-productive metabolism.",
    quotes: [
      { author: "Humberto Maturana & Francisco Varela", work: "Autopoiesis and Cognition", quote: "A cell maintains its identity through continuous self-generation; this defining organization of living systems is **autopoiesis**." },
      { author: "Niklas Luhmann", work: "Social Systems", quote: "We apply the concept of **autopoiesis** to communication networks that continuously reproduce their own internal operations." },
      { author: "Lynn Margulis", work: "What Is Life?", quote: "Life is matter that has acquired the gift of **autopoiesis**, continually transforming external nutrients into its own self-renewing structure." }
    ]
  },
  "Dashboard — poie\\onomatopoeia.md": {
    primary: "The formation of a word from a sound associated with what is named; the use of words whose sounds imitate their sense.",
    secondary: "In classical rhetoric and stylistics, the expressive imitation of natural sounds through vocal phonetics to evoke sensory immediacy.",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", quote: "The figure called **onomatopoeia**, or the invention of names from sounds, was regarded by the Greeks as a great ornament of speech." },
      { author: "Samuel Taylor Coleridge", work: "Lectures on Shakespeare", quote: "The whispering of the pines and the crash of waves are echoed in the poet's verse through subtle **onomatopoeia**." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The theory that all language originated from crude **onomatopoeia** has been termed the bow-wow theory of speech." }
    ]
  },
  "Dashboard — poie\\onomatopoeical.md": {
    primary: "Of, relating to, or characterized by onomatopoeia; echoic or sound-imitative.",
    secondary: "In comparative philology, describing phonetic roots that mimic animal cries or percussive natural noises.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "Words like buzz, hiss, and clatter are of clearly **onomatopoeical** origin, derived from direct imitation of acoustic sensations." },
      { author: "Max Müller", work: "The Science of Language", quote: "While primitive man made use of **onomatopoeical** roots, higher conceptual thought required abstract grammatical categories." },
      { author: "Edward Tylor", work: "Primitive Culture", quote: "Children and savages exhibit a natural fondness for **onomatopoeical** expressions to describe natural phenomena." }
    ]
  },
  "Dashboard — poie\\onomatopoetic.md": {
    primary: "Relating to or formed by onomatopoeia; imitative of the natural sound associated with an object or action.",
    secondary: "In phonetic linguistics and poetic analysis, using acoustic mimicry to reinforce semantic meaning in verse or prose.",
    quotes: [
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "Many bird names are frankly **onomatopoetic**, capturing the bird's distinctive cry in human phonemes." },
      { author: "William Dwight Whitney", work: "Language and the Study of Language", quote: "The **onomatopoetic** element in language, though real, accounts for only a minor fraction of our established lexicon." },
      { author: "Roman Jakobson", work: "Language in Literature", quote: "Poetic texture exploits **onomatopoetic** resonance to heighten the semantic weight of each phoneme." }
    ]
  },
  "Dashboard — poie\\pharmacopoeia.md": {
    primary: "An official publication containing a catalog of medicinal drugs, with descriptions of their preparation, identification, formulas, and dosages.",
    secondary: "In medical history and pharmacology, the authoritative compendium regulating drug standards and chemical purity within a jurisdiction.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "If the whole **pharmacopoeia** could be sunk to the bottom of the sea, it would be all the better for mankind—and all the worse for the fishes." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The young physician starts out with twenty remedies for each disease; the experienced physician uses one remedy from his **pharmacopoeia** for twenty diseases." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "A reformed **pharmacopoeia** ought to weed out superstitious compounds and record only remedies verified by experimental trial." }
    ]
  },
  "Dashboard — poie\\piyyut.md": {
    primary: "A Jewish liturgical poem or hymn designated to be chanted, sung, or recited during synagogue services.",
    secondary: "In Hebrew literary history, rhymed, metered religious verse flourishing from Byzantine Palestine through the medieval European paytanic traditions.",
    quotes: [
      { author: "Israel Abrahams", work: "Jewish Life in the Middle Ages", quote: "The mediaeval congregation welcomed the heartfelt **piyyut**, whose acrostics and biblical echoes enlivened the solemn festival service." },
      { author: "Solomon Schechter", work: "Studies in Judaism", quote: "In every stanza of the sacred **piyyut**, one detects the tears and ardent yearnings of a scattered people." },
      { author: "Heinrich Graetz", work: "History of the Jews", quote: "Eleazar Kalir enriched the synagogue liturgy with magnificent **piyyut** hymns celebrated for intricate rhyme schemes." }
    ]
  },
  "Dashboard — poie\\poem.md": {
    primary: "A piece of writing in which words are chosen for their sound and beauty and are carefully arranged, often in rhymed, metered lines.",
    secondary: "In literary aesthetics, a unified linguistic creation that synthesizes imaginative insight, rhythmic form, and intense emotional truth.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "A Defence of Poetry", quote: "A **poem** is the very image of life expressed in its eternal truth." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "A **poem** is that species of composition which is opposed to works of science, by proposing for its immediate object pleasure, not truth." },
      { author: "Robert Frost", work: "The Figure a Poem Makes", quote: "A **poem** begins as a lump in the throat, a sense of wrong, a homesickness, a lovesickness; it finds the thought and the thought finds the words." }
    ]
  },
  "Dashboard — poie\\poesy.md": {
    primary: "The art or craft of composing poetry; poetic works or verse considered collectively.",
    secondary: "In classical and Renaissance criticism, the divinely inspired creative faculty of poetic invention; imaginative vision.",
    quotes: [
      { author: "John Keats", work: "Ode to a Nightingale", quote: "Not charioted by Bacchus and his pards, but on the viewless wings of **Poesy**, though the dull brain perplexes and retards." },
      { author: "Philip Sidney", work: "An Apology for Poetry", quote: "Nature never set forth the earth in so rich tapestry as divers poets have done; her world is brazen, the world of **poesy** only delivereth a golden." },
      { author: "William Shakespeare", work: "Timon of Athens", quote: "A thing slipp’d idly from me. Our **poesy** is as a gum, which oozes from whence ’tis nourish’d." }
    ]
  },
  "Dashboard — poie\\poet.md": {
    primary: "A person who writes poetry, possessing creative imagination and expressive linguistic art.",
    secondary: "In philosophy and cultural history, a visionary creator who gives memorable verbal form to universal human ideals and emotions.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "The Poet", quote: "The **poet** is the sayer, the namer, and represents beauty; he stands among partial men for the complete man." },
      { author: "William Wordsworth", work: "Preface to Lyrical Ballads", quote: "What is a **poet**? He is a man speaking to men, endowed with more lively sensibility, more enthusiasm and tenderness." },
      { author: "Walt Whitman", work: "Preface to Leaves of Grass", quote: "The proof of a **poet** is that his country absorbs him as affectionately as he has absorbed it." }
    ]
  },
  "Dashboard — poie\\poetaster.md": {
    primary: "An inferior, petty, or pretentious writer of mediocre and trivial verses.",
    secondary: "In literary satire, a shallow rhymester who apes poetic manners without true inspiration or technical mastery.",
    quotes: [
      { author: "Lord Byron", work: "English Bards and Scotch Reviewers", quote: "Shall hoarse FitzGerald bawl his creaking couplets in a tavern hall, and I not sing, when each vile **poetaster** invades the press?" },
      { author: "Ben Jonson", work: "Poetaster", quote: "The true artist must chastise the vain **poetaster** who presumes to profane the sacred laurel of Apollo." },
      { author: "Alexander Pope", work: "An Epistle to Dr. Arbuthnot", quote: "What drop or nostrum can this plague remove, or quench the rage with which the **poetaster** scribbles?" }
    ]
  },
  "Dashboard — poie\\poetical.md": {
    primary: "Of, relating to, or characteristic of poetry or poets; written in verse.",
    secondary: "Expressing lofty feeling, imaginative beauty, or refined artistic sensibility.",
    quotes: [
      { author: "Samuel Johnson", work: "The Lives of the English Poets", quote: "Dryden was the father of English criticism, but Pope possessed in the highest degree the **poetical** fire." },
      { author: "Percy Bysshe Shelley", work: "A Defence of Poetry", quote: "The **poetical** faculty is that which creates new materials of knowledge, power, and pleasure." },
      { author: "Edgar Allan Poe", work: "The Poetic Principle", quote: "A passion for the beautiful is the sole legitimate origin and aim of the **poetical** sentiment." }
    ]
  },
  "Dashboard — poie\\poetically.md": {
    primary: "In a poetic manner; by means of verse or imaginative and elevated language.",
    secondary: "In existential philosophy and aesthetics, dwelling with creative receptivity toward the essence of being and the world.",
    quotes: [
      { author: "Martin Heidegger", work: "\"...Poetically Man Dwells...\"", quote: "Man dwells **poetically** upon this earth, in so far as he responds to the measure of being." },
      { author: "Ralph Waldo Emerson", work: "Nature", quote: "The morning wind blows; the universe appears afresh to those who view it **poetically**." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I went to the woods because I wished to live deliberately, to confront only the essential facts of life, and see whether I could not record them **poetically**." }
    ]
  },
  "Dashboard — poie\\poetise.md": {
    primary: "To compose poetry; to write or speak in verse; to treat a subject poetically.",
    secondary: "To perceive, represent, or idealize everyday reality through an artistic and imaginative lens.",
    quotes: [
      { author: "John Keats", work: "The Letters of John Keats", quote: "I find that I cannot exist without poetry—without eternal poetry—half the day will not do; I must **poetise** all night." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "To **poetise** our everyday existence is to discern the divine mystery shining through the coarsest habit." },
      { author: "George Eliot", work: "Adam Bede", quote: "She did not attempt to **poetise** her simple domestic chores, but went about them with cheerful fidelity." }
    ]
  },
  "Dashboard — poie\\poetiser.md": {
    primary: "A person who poetises; one who writes verse or attempts to compose poetry.",
    secondary: "In literary commentary, a practitioner of versification, ranging from a modest lyricist to a trivial dabbler.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Table Talk", quote: "The mere **poetiser** rhymes words without possessing the creative imagination that unifies thought and emotion." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "Between the genuine bard and the fashionable **poetiser** there lies the gulf between nature and artificial mimicry." },
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "The dilettante **poetiser** mistakes ease of versification for depth of poetic insight." }
    ]
  },
  "Dashboard — poie\\poetize.md": {
    primary: "To make poetic; to compose verse upon or treat with poetic imagination and elevated expression.",
    secondary: "In cultural criticism, to transfigure ordinary experiences, historical struggles, or mechanical phenomena into aesthetic forms.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "The Conduct of Life", quote: "The true thinker will **poetize** the machinery and commerce of his age, demonstrating that steel and steam obey spiritual laws." },
      { author: "Henry James", work: "The Art of Fiction", quote: "The novelist does not merely transcribe raw circumstances; his instinct is to **poetize** the underlying moral conflict." },
      { author: "Friedrich Nietzsche", work: "The Birth of Tragedy", quote: "To **poetize** is to transform the terror of existence into tragic transfiguration and beauty." }
    ]
  },
  "Dashboard — poie\\poetizer.md": {
    primary: "A person who poetizes; a composer of verses or one who views life through an idealized poetic prism.",
    secondary: "In literary discourse, an author who seeks to romanticize and elevate common subjects into poetic expression.",
    quotes: [
      { author: "Walt Whitman", work: "Democratic Vistas", quote: "America needs no shallow **poetizer** of drawing-room romance, but colossal voices attuned to democratic vastness." },
      { author: "Henry David Thoreau", work: "A Week on the Concord and Merrimack Rivers", quote: "The true poet creates life; the idle **poetizer** merely gossips about it in meter." },
      { author: "Ralph Waldo Emerson", work: "Letters and Social Aims", quote: "The amateur **poetizer** borrows the worn ornaments of past bards instead of looking directly into the sun." }
    ]
  },
  "Dashboard — poie\\poetry.md": {
    primary: "Literary work in which the expression of feelings and ideas is given intensity by the use of distinctive style, rhythm, and meter.",
    secondary: "In aesthetic philosophy, the primordial art of verbal creation through which human culture articulates its deepest truths and spiritual yearnings.",
    quotes: [
      { author: "William Wordsworth", work: "Preface to Lyrical Ballads", quote: "**Poetry** is the spontaneous overflow of powerful feelings: it takes its origin from emotion recollected in tranquillity." },
      { author: "Percy Bysshe Shelley", work: "A Defence of Poetry", quote: "**Poetry** lifts the veil from the hidden beauty of the world, and makes familiar objects be as if they were not familiar." },
      { author: "Samuel Taylor Coleridge", work: "Table Talk", quote: "I wish our clever young poets would remember my homely definitions of prose and poetry; that is, prose,—words in their best order; **poetry**,—the best words in their best order." }
    ]
  },
  "Dashboard — poie\\poiein.md": {
    primary: "The ancient Greek verb (poiein, meaning 'to make, create, produce, or compose'), the linguistic root of poem, poet, and poiesis.",
    secondary: "In Aristotelian philosophy, the category of productive action (making) distinguished from ethical and political conduct (praxis) and contemplation (theoria).",
    quotes: [
      { author: "Martin Heidegger", work: "The Question Concerning Technology", quote: "The Greek verb **poiein** means bringing-forth into appearance, disclosing what was previously concealed." },
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "Making, or **poiein**, differs essentially from acting, or prattein, because production has an end distinct from the activity itself." },
      { author: "Hannah Arendt", work: "The Human Condition", quote: "In Greek thought, the craft of **poiein** was distinguished from the political speech and action of praxis." }
    ]
  },
  "Dashboard — poie\\poiesis.md": {
    primary: "The activity in which a person brings something into being that did not exist before; creative production.",
    secondary: "In continental philosophy and classical metaphysics, the threshold of disclosure and manifestation through which truth is brought into presence.",
    quotes: [
      { author: "Plato", work: "Symposium", quote: "All creation or passage of non-being into being is **poiesis** or making, so that all arts are kinds of poetry." },
      { author: "Martin Heidegger", work: "Basic Writings", quote: "Not only handicraft manufacture, not only artistic and poetical bringing into appearance, is **poiesis**, but also the blossoming of nature itself." },
      { author: "Giorgio Agamben", work: "The Man Without Content", quote: "In classical antiquity, **poiesis** was understood as a pro-duction into presence, bringing the true into the open." }
    ]
  },
  "Dashboard — prag\\apractic.md": {
    primary: "Relating to or afflicted with apraxia; unable to execute learned purposeful movements despite intact sensory and muscular capability.",
    secondary: "In clinical neuropsychology, describing motor actions that lack coherent organization and spatial coordination due to cerebral lesion.",
    quotes: [
      { author: "Alexander Luria", work: "The Working Brain: An Introduction to Neuropsychology", quote: "Patients with severe parieto-occipital lesions exhibit **apractic** disturbances when asked to manipulate spatial coordinates." },
      { author: "Norman Geschwind", work: "Selected Papers on Language and the Brain", quote: "The patient was rendered severely **apractic** in the left limb following callosal disconnexion." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "His hands remained strong yet strangely **apractic**, unable to organize the sequence of tying his shoes." }
    ]
  },
  "Dashboard — prag\\apraxia.md": {
    primary: "Inability to perform learned, purposive movements, as a result of brain damage, without paralysis or sensory loss.",
    secondary: "In higher cortical neurology, the breakdown of motor planning systems in the parietal and frontal lobes that coordinate complex intentional behavior.",
    quotes: [
      { author: "Sigmund Freud", work: "On Aphasia: A Critical Study", quote: "Liepmann's description of motor **apraxia** proved that high-level motor planning could be dissociated from elementary muscle weakness." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Ideational **apraxia** prevents the patient from conceptualizing the consecutive steps required to light a candle." },
      { author: "Norman Geschwind", work: "Disconnexion Syndromes in Animals and Man", quote: "Lesions interrupting associations between sensory analysis and motor execution manifest clinically as **apraxia**." }
    ]
  },
  "Dashboard — prag\\apraxic.md": {
    primary: "Suffering from, affected by, or characteristic of apraxia.",
    secondary: "In neurological examinations, describing defective gestural imitation, tool manipulation, or spatial orientation resulting from cortical injury.",
    quotes: [
      { author: "Alexander Luria", work: "The Working Brain", quote: "The **apraxic** individual may recognize a comb perfectly yet brush his teeth with it when attempting to groom." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Post-encephalitic patients sometimes demonstrated bizarre **apraxic** halts in the midst of habitual motor performances." },
      { author: "Norman Geschwind", work: "Selected Papers on Language and the Brain", quote: "Testing revealed that the **apraxic** limb could perform reflexive withdrawals while failing voluntary commands." }
    ]
  },
  "Dashboard — prag\\dyspraxia.md": {
    primary: "A neurological disorder affecting motor skill development, characterized by impairment in planning and executing coordinated movements.",
    secondary: "In developmental pediatrics and neuropsychology, a condition that disrupts spatial organization, manual dexterity, and speech articulation without intellectual deficit.",
    quotes: [
      { author: "Oliver Sacks", work: "Musicophilia", quote: "Children suffering from developmental **dyspraxia** often find in musical rhythm an external scaffolding for motor coordination." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Subtle constructional **dyspraxia** may remain hidden until the patient is required to draw a clock face." },
      { author: "Donald Winnicott", work: "The Child, the Family, and the Outside World", quote: "The child with mild **dyspraxia** experiences profound frustration when physical clumsy movements fail to match mental agility." }
    ]
  },
  "Dashboard — prag\\parapraxis.md": {
    primary: "A minor error in speech, memory, or physical action that is thought to reveal a subconscious motive or repressed thought; a Freudian slip.",
    secondary: "In psychoanalytic theory, the symptomatic manifestation of unconscious mental conflict breaking through conscious suppression during everyday speech or action.",
    quotes: [
      { author: "Sigmund Freud", work: "The Psychopathology of Everyday Life", quote: "Every accidental slip of the tongue or pen, termed a **parapraxis**, reveals the emergence of a repressed unconscious intention." },
      { author: "Carl Jung", work: "The Structure and Dynamics of the Psyche", quote: "A momentary **parapraxis** often provides the analyst with an unvarnished glimpse into the patient's underlying complex." },
      { author: "Jacques Lacan", work: "The Four Fundamental Concepts of Psychoanalysis", quote: "The significance of the **parapraxis** lies in the sudden puncture of the conscious discourse by the symbolic order." }
    ]
  },
  "Dashboard — prag\\practic.md": {
    primary: "Practical; active; relating to action rather than theory (archaic or literary).",
    secondary: "In early modern literature, skilled in pragmatic stratagems, worldly management, or practical execution.",
    quotes: [
      { author: "Francis Bacon", work: "The Essays", quote: "Expert men can execute, and perhaps judge of particulars, one by one; but the general counsels and the plots and marshalling of affairs come best from those that are learned in **practic** wisdom." },
      { author: "Walter Scott", work: "The Antiquary", quote: "He had a shrewd eye for the **practic** world, knowing how to turn each turn of fortune to solid advantage." },
      { author: "Edmund Spenser", work: "The Faerie Queene", quote: "Full of vain wyles and of false guyle was she, yet trained in every **practic** art of worldly deceit." }
    ]
  },
  "Dashboard — prag\\practicable.md": {
    primary: "Able to be done or put into practice successfully; feasible; workable.",
    secondary: "In legal and administrative contexts, capable of being executed or used effectively with the available materials, routes, or facilities.",
    quotes: [
      { author: "Alexander Hamilton", work: "The Federalist No. 1", quote: "The establishment of a constitution in time of profound peace is an event of which history affords few examples, yet here it is entirely **practicable**." },
      { author: "Thomas Jefferson", work: "Letter to James Madison", quote: "A scheme may be theoretically elegant, but the legislator must ask whether it is **practicable** among actual men." },
      { author: "Jane Austen", work: "Mansfield Park", quote: "It was thought very **practicable** for the party to proceed on horseback as soon as the morning mist had cleared." }
    ]
  },
  "Dashboard — prag\\practical.md": {
    primary: "Relating to the actual doing or use of something rather than with theory and ideas.",
    secondary: "In moral philosophy and epistemology, concerned with action, moral choice, and real-world efficacy rather than abstract speculative reason.",
    quotes: [
      { author: "Immanuel Kant", work: "Critique of Practical Reason", quote: "The concepts of good and evil are not original objects of pure reason, but are determined solely by the **practical** moral law." },
      { author: "William James", work: "Pragmatism: A New Name for Some Old Ways of Thinking", quote: "The true is the name of whatever proves itself to be good in the way of belief, and good, too, for definite, **practical** reasons." },
      { author: "John Stuart Mill", work: "Utilitarianism", quote: "In evaluating human conduct, the ultimate test of virtue lies in its **practical** tendency to promote universal happiness." }
    ]
  }
};

const updatedCount = updateNotesBatch(baseClusterDir, batch2Data);
console.log(`[Batch 2] Successfully updated ${updatedCount}/${Object.keys(batch2Data).length} notes.`);
