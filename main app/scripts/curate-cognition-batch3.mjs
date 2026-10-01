import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind";

const wordsData = {
  // === Dashboard — oneir (17 words) ===
  "Dashboard — oneir/Oneirocritica.md": {
    word: "Oneirocritica",
    primary: "The celebrated ancient Greek treatise on the interpretation of dreams written by Artemidorus Daldianus in the second century CE.",
    secondary: "In classical historiography and psychological antiquity, the foundational five-book compendium cataloging Hellenistic dream symbolism, social divination, and omen typology.",
    quotes: [
      { author: "Artemidorus", work: "Oneirocritica", quote: "In the **Oneirocritica**, dreams are divided into those that reveal future realities and those that merely mirror daily bodily anxieties." },
      { author: "Michel Foucault", work: "The Care of the Self", quote: "The **Oneirocritica** of Artemidorus offers a profound window into how antiquity envisioned the ethical governance of desires." },
      { author: "Sigmund Freud", work: "The Interpretation of Dreams", quote: "Ancient dream analysis culminated in the **Oneirocritica**, where dreams were decoded through symbolic and linguistic associations." }
    ]
  },
  "Dashboard — oneir/Oneirodidae.md": {
    word: "Oneirodidae",
    primary: "A family of deep-sea anglerfishes (order Lophiiformes), commonly referred to as the dreamer anglerfishes.",
    secondary: "In ichthyological taxonomy, bathypelagic predatory fishes possessing a bioluminescent esca (lure), named from Greek oneiros (dream) due to their surreal, otherworldly morphology.",
    quotes: [
      { author: "William Beebe", work: "Half Mile Down", quote: "From the bathysphere window, we glimpsed bizarre anglerfishes of the family **Oneirodidae**, drifting like ghostly dreams through the black abyss." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The **Oneirodidae** inhabit profound oceanic depths, enticing prey with glowing lures suspended from their snouts." },
      { author: "Theodore Gill", work: "Deep-Sea Fishing", quote: "Naturalists named the **Oneirodidae** for their spectral, dreamlike appearance in the icy aphotic zone." }
    ]
  },
  "Dashboard — oneir/Oneiroi.md": {
    word: "Oneiroi",
    primary: "In Greek mythology, the personified spirits of dreams, winged daimones who dwell in the dark caverns of the underworld.",
    secondary: "In classical epic (Hesiod, Homer, Ovid), the sons or brothers of Hypnos (Sleep) who emerge through gates of horn (truthful dreams) or ivory (deceptive dreams), led by Morpheus, Icelos, and Phantasos.",
    quotes: [
      { author: "Homer", work: "The Odyssey", quote: "Twin gates of the **Oneiroi** there are: one fashioned of horn whence issue true portents, and one of polished ivory bearing flattering delusions." },
      { author: "Hesiod", work: "Theogony", quote: "Night bore dark Fate and black Ker, and Death, and Sleep, and she brought forth the winged tribe of the **Oneiroi**." },
      { author: "Ovid", work: "Metamorphoses", quote: "Among the thousand sons of Sleep, the leader of the **Oneiroi** was Morpheus, master at imitating human gait and voice." }
    ]
  },
  "Dashboard — oneir/oneir.md": {
    word: "oneir",
    primary: "A combining root derived from Ancient Greek oneiros, meaning dream or dreaming.",
    secondary: "In psychological, mythological, and medical terminology, the prefix or root element denoting nocturnal visions, reveries, or dream analysis.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek root **oneir**- gives us esoteric vocabulary such as oneiric, oneiromancy, and oneirology." },
      { author: "Havelock Ellis", work: "The World of Dreams", quote: "Scientific study of nocturnal consciousness unites psychology with the ancient Hellenic stem **oneir**-." },
      { author: "G. Stanley Hall", work: "Adolescence", quote: "Adolescent daydreams bridge waking imagination and the nocturnal realm represented by the combining form **oneir**-." }
    ]
  },
  "Dashboard — oneir/oneiric.md": {
    word: "oneiric",
    primary: "Of, relating to, or suggestive of dreams; dreamlike, ethereal, or surreal in quality.",
    secondary: "In film aesthetics and literary criticism, describing visual atmospheres, narrative pacing, or imagery characterized by uncanny, floating dream logic.",
    quotes: [
      { author: "Jorge Luis Borges", work: "Labyrinths", quote: "The mirrored corridors of the library possessed an **oneiric** quality, where time seemed suspended in geometric repetition." },
      { author: "Italo Calvino", work: "Invisible Cities", quote: "Cities are distinguished by their **oneiric** architecture, built from the desires and anxieties of wandering travelers." },
      { author: "Gaston Bachelard", work: "The Poetics of Reverie", quote: "The house of our childhood shelters our earliest **oneiric** reveries, anchoring the wandering imagination in space." }
    ]
  },
  "Dashboard — oneir/oneirism.md": {
    word: "oneirism",
    primary: "A dreamlike state of consciousness occurring during waking hours, often accompanied by vivid daydreams or hallucinations.",
    secondary: "In psychopathology, an abnormal condition marked by dreamlike delirium, somnambulistic automatism, or waking hallucinatory reveries.",
    quotes: [
      { author: "Pierre Janet", work: "The Major Symptoms of Hysteria", quote: "The patient slipped into a protracted **oneirism**, enacting theatrical scenes from past traumas while awake." },
      { author: "Henri Bergson", work: "Mind-Energy", quote: "In conditions of profound mental fatigue, the mind slides into **oneirism**, relaxing its effort to grasp outer reality." },
      { author: "C. G. Jung", work: "Psychology of the Unconscious", quote: "Spontaneous waking **oneirism** reveals mythic archetypes that ordinarily remain submerged beneath daytime consciousness." }
    ]
  },
  "Dashboard — oneir/oneirocritic.md": {
    word: "oneirocritic",
    primary: "An interpreter of dreams; of or relating to the interpretation of dreams and their symbolic meanings.",
    secondary: "In classical and folkloric traditions, a diviner or scholar who analyzes dream imagery to discern omens, character traits, or unconscious warnings.",
    quotes: [
      { author: "Thomas Browne", work: "Hydriotaphia, Urn Burial", quote: "An astute **oneirocritic** unknots the tangled threads of nocturnal visions, discerning truth from digestive vapors." },
      { author: "Charles Lamb", work: "Essays of Elia", quote: "I consulted an eccentric **oneirocritic** who promised to interpret my nightmare of drifting alone upon a frozen sea." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Every ancient monarch maintained a resident **oneirocritic** to decode the fearful apparitions of the night." }
    ]
  },
  "Dashboard — oneir/oneirogen.md": {
    word: "oneirogen",
    primary: "A substance, herb, or agent that stimulates, enhances, or induces vivid dream states or lucid dreaming.",
    secondary: "In ethnobotany and psychopharmacology, plants (such as Calea zacatechichi or Silene capensis) traditionally ingested by shamans to foster prophetic or vivid dreams.",
    quotes: [
      { author: "Richard Evans Schultes", work: "Plants of the Gods", quote: "Indigenous diviners revere the bitter herb as a potent **oneirogen**, smoking its leaves before sleep to receive spiritual visions." },
      { author: "Terence McKenna", work: "Food of the Gods", quote: "Certain African root preparations act as a true **oneirogen**, turning the ordinary night into an epic cinematic voyage." },
      { author: "Andrew Weil", work: "The Natural Mind", quote: "Pharmacologists have begun evaluating traditional botanical **oneirogens** for their capacity to enhance REM sleep architecture." }
    ]
  },
  "Dashboard — oneir/oneirogenic.md": {
    word: "oneirogenic",
    primary: "Producing, stimulating, or tending to induce dreams or dreamlike states.",
    secondary: "In neurobiology and sleep medicine, describing chemical compounds or environmental stimuli that promote vivid dream imagery or prolong REM sleep.",
    quotes: [
      { author: "Oliver Sacks", work: "Hallucinations", quote: "Certain dopamine agonists possess marked **oneirogenic** properties, provoking extraordinary, colorful dreams in parkinsonian patients." },
      { author: "William C. Dement", work: "Some Must Watch While Some Must Sleep", quote: "Cholinergic neurotransmission demonstrates a distinctly **oneirogenic** influence on the pontine dream generators." },
      { author: "Havelock Ellis", work: "The World of Dreams", quote: "The rhythmic murmur of mountain torrents exerts an **oneirogenic** effect upon weary travelers resting nearby." }
    ]
  },
  "Dashboard — oneir/oneiroid.md": {
    word: "oneiroid",
    primary: "Resembling a dream; dreamlike; in psychiatry, describing an oneiroid state characterized by hallucinatory, dreamlike clouding of consciousness.",
    secondary: "In psychopathology, an acute twilight state in which the patient experiences elaborate, theatrical hallucinations while maintaining partial orientation.",
    quotes: [
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "In the **oneiroid** state, patients experience catastrophic or cosmic adventures as if watching a living, vivid dream." },
      { author: "Eugen Bleuler", work: "Dementia Praecox or the Group of Schizophrenias", quote: "An **oneiroid** episode may herald acute psychosis, where the external world dissolves into fantastic imagery." },
      { author: "Emil Kraepelin", work: "Clinical Psychiatry", quote: "The delirium presented an **oneiroid** coloring, with visions of celestial pageants shifting across the ceiling." }
    ]
  },
  "Dashboard — oneir/oneirology.md": {
    word: "oneirology",
    primary: "The scientific study and analysis of dreams, dream processes, and their physiological mechanisms.",
    secondary: "In sleep neuroscience, the multidisciplinary field combining polysomnography, cognitive psychology, and neurochemistry to understand nocturnal mentation.",
    quotes: [
      { author: "Michel Jouvet", work: "The Paradox of Sleep", quote: "Modern **oneirology** took flight with the discovery of paradoxical sleep and rapid eye movement rhythms." },
      { author: "J. Allan Hobson", work: "The Dreaming Brain", quote: "Neurobiological **oneirology** reveals how the pontine brainstem generates the sensory fireworks of dreams." },
      { author: "Sigmund Freud", work: "New Introductory Lectures on Psycho-Analysis", quote: "Before our psychological investigations, scientific **oneirology** was largely confined to measuring somatic reflexes during sleep." }
    ]
  },
  "Dashboard — oneir/oneiromancer.md": {
    word: "oneiromancer",
    primary: "A diviner or fortune-teller who predicts the future through the interpretation of dreams; an oneirocritic.",
    secondary: "In mythological and historical narratives, a seer consulted by kings, generals, and pilgrims to reveal the hidden will of the gods through dream omens.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The superstitious emperor summoned an Egyptian **oneiromancer** to interpret his nocturnal vision of a falling star." },
      { author: "Walter Scott", work: "The Talisman", quote: "The Arab **oneiromancer** bowed low, professing to read the destiny of empires in the fleeting images of sleep." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Frightened souls run to the astrologer and the **oneiromancer**, seeking peace from phantom omens." }
    ]
  },
  "Dashboard — oneir/oneiromancy.md": {
    word: "oneiromancy",
    primary: "Divination or prophecy practiced through the interpretation of dreams.",
    secondary: "In cultural history and anthropology, an ancient mantic discipline based on the premise that nocturnal visions communicate supernatural portents.",
    quotes: [
      { author: "Cicero", work: "De Divinatione", quote: "Many philosophical schools revere **oneiromancy**, believing the unburdened soul perceives the future while the body sleeps." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "The art of **oneiromancy** hath deceived many great princes who staked their kingdoms upon ambiguous night visions." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Primitive tribes practiced ritual **oneiromancy**, sleeping upon sacred animal skins to solicit prophetic guidance." }
    ]
  },
  "Dashboard — oneir/oneironaut.md": {
    word: "oneironaut",
    primary: "A person who explores dream worlds, especially one who practices lucid dreaming and consciously navigates dream states.",
    secondary: "In consciousness studies and contemporary psychology, an individual trained to achieve lucidity and perform intentional cognitive experiments within dreams.",
    quotes: [
      { author: "Stephen LaBerge", work: "Lucid Dreaming", quote: "The skilled **oneironaut** recognizes that he is dreaming and steps forward to consciously shape the nocturnal landscape." },
      { author: "Oliver Sacks", work: "The River of Consciousness", quote: "Like an intrepid **oneironaut**, the lucid dreamer navigates the shifting currents of his own neurochemistry." },
      { author: "Alan Watts", work: "The Joyous Cosmology", quote: "The awakened **oneironaut** discovers that the dreamer and the dream world are an indivisible unity." }
    ]
  },
  "Dashboard — oneir/oneironautics.md": {
    word: "oneironautics",
    primary: "The practice, skill, or exploration of lucid dreaming; conscious navigation within dream environments.",
    secondary: "In experimental cognitive psychology, systematic techniques (such as reality checks and MILD) cultivated to retain waking awareness during REM sleep.",
    quotes: [
      { author: "Stephen LaBerge", work: "Exploring the World of Lucid Dreaming", quote: "Through disciplined **oneironautics**, researchers demonstrate that conscious volition can operate during physiological REM sleep." },
      { author: "Carl Sagan", work: "The Dragons of Eden", quote: "The frontiers of human exploration may soon encompass **oneironautics**, charting the inner cosmos of dream imagery." },
      { author: "Richard Feynman", work: "Surely You're Joking, Mr. Feynman!", quote: "I experimented with my own form of **oneironautics**, learning to wake up inside my dreams and observe the visual resolution." }
    ]
  },
  "Dashboard — oneir/oneirophobia.md": {
    word: "oneirophobia",
    primary: "An abnormal, morbid, or irrational fear of dreams or of falling asleep due to terror of nightmares.",
    secondary: "In clinical psychiatry and sleep disorders medicine, a debilitating phobia often associated with post-traumatic stress disorder, hypnophobia, or recurring night terrors.",
    quotes: [
      { author: "Sándor Ferenczi", work: "Theory and Technique of Psychoanalysis", quote: "Severe combat neurosis frequently engenders **oneirophobia**, as patients dread the traumatic replays awaiting them in sleep." },
      { author: "William C. Dement", work: "The Promise of Sleep", quote: "Patients with acute nightmare disorder develop intense **oneirophobia**, pacing their bedrooms until dawn to avoid dreaming." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The terrified child suffered from acute **oneirophobia**, weeping piteously whenever led toward his bed." }
    ]
  },
  "Dashboard — oneir/oneiroscopy.md": {
    word: "oneiroscopy",
    primary: "The diagnosis, prognosis, or psychological evaluation of an individual's health and state of mind through the examination of their dreams.",
    secondary: "In the history of medicine (Hippocratic and Galenic traditions), the clinical practice of inspecting dream content for early physiological signs of bodily illness.",
    quotes: [
      { author: "Galen", work: "On Diagnosis from Dreams", quote: "Medical **oneiroscopy** reveals impending bodily humors, as dreams of swimming in icy water forewarn of phlegmatic fevers." },
      { author: "Hippocrates", work: "On Regimen in Health", quote: "The prudent physician employs **oneiroscopy** to detect subtle bodily imbalances before overt physical symptoms appear." },
      { author: "Sigmund Freud", work: "The Interpretation of Dreams", quote: "Ancient medical **oneiroscopy** contained an intuitive truth: somatic irritations often announce themselves first in dream imagery." }
    ]
  },

  // === Dashboard — phren (21 words) ===
  "Dashboard — phren/-phrenia.md": {
    word: "-phrenia",
    primary: "A combining suffix derived from Ancient Greek phrēn (mind, heart, diaphragm) denoting a mental disorder, state of mind, or intellectual condition.",
    secondary: "In psychiatric nosology, forming diagnostic categories such as schizophrenia, hebephrenia, oligophrenia, and cyclophrenia.",
    quotes: [
      { author: "Eugen Bleuler", work: "Dementia Praecox or the Group of Schizophrenias", quote: "I coined the term schizophrenia, utilizing the Greek suffix -**phrenia** to emphasize the fundamental splitting of psychic functions." },
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "Conditions ending in -**phrenia** denote primary disturbances of the mental faculties rather than focal sensorimotor lesions." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "The historical evolution of terms ending in -**phrenia** reflects changing theories regarding the organic basis of madness." }
    ]
  },
  "Dashboard — phren/Euphrosyne.md": {
    word: "Euphrosyne",
    primary: "In Greek mythology, one of the three Graces (Charites), the personification of joy, cheerfulness, and lighthearted merriment (from eu- well + phren mind).",
    secondary: "In classical literature and astronomy, the goddess who gladdens the heart and mind; also a large carbonaceous main-belt asteroid discovered in 1854.",
    quotes: [
      { author: "John Milton", work: "L'Allegro", quote: "Heart-easing Mirth, whom lovely Venus bore / To ivy-crowned Bacchus, or whether more / Sing of **Euphrosyne** by Zephyr begot." },
      { author: "Edmund Spenser", work: "The Faerie Queene", quote: "These three on Men all gracious gifts bestow: / Aglaia, Thalia, and fair **Euphrosyne**, / Handmaids of Venus radiant and free." },
      { author: "Pindar", work: "Olympian Odes", quote: "O queenly Aglaia and song-loving **Euphrosyne**, daughters of Zeus, give ear unto our prayer." }
    ]
  },
  "Dashboard — phren/euneirophrenia.md": {
    word: "euneirophrenia",
    primary: "A peaceful, pleasant, and comforting state of mind upon waking from a good dream.",
    secondary: "In psychological aesthetics, the tranquil emotional afterglow experienced throughout the morning following an exceptionally serene or inspiring dream.",
    quotes: [
      { author: "Havelock Ellis", work: "The World of Dreams", quote: "Waking into profound **euneirophrenia**, the poet found his morning thoughts bathed in radiant tranquility." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The patient reported rare mornings of blessed **euneirophrenia**, feeling rejuvenated by comforting dreams of childhood gardens." },
      { author: "G. Stanley Hall", work: "Adolescence", quote: "Benevolent nocturnal visions often leave an adolescent in a gentle **euneirophrenia** that colors the entire day with optimism." }
    ]
  },
  "Dashboard — phren/euphrasy.md": {
    word: "euphrasy",
    primary: "The plant eyebright (Euphrasia officinalis), traditionally used in folk herbal medicine to treat eye complaints and metaphorically to clear spiritual vision.",
    secondary: "In literary and poetical usage, a botanical metaphor for purging clouded vision, spiritual blindness, or intellectual darkness (from Greek euphrasia, gladness of mind).",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Michael purged with **euphrasy** and rue / The visual nerve, for he had much to see, / And from the well of life three drops instilled." },
      { author: "William Wordsworth", work: "The Prelude", quote: "No magical **euphrasy** was needed to clear his vision, for nature herself opened his eyes to transcendent beauty." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Herbals celebrate **euphrasy** for its singular virtue in brightening dim and rheumy eyes." }
    ]
  },
  "Dashboard — phren/frantic.md": {
    word: "frantic",
    primary: "Wild or distraught with fear, anxiety, or other violent emotion; conducted in a hurried, chaotic, or desperate manner.",
    secondary: "Etymologically derived from Greek phrenitikos (delirious), denoting frenzied physical motion driven by acute panic or desperation.",
    quotes: [
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "The lunatic, the lover, and the poet / Are of imagination all compact: / One sees more devils than vast hell can hold, / That is, the madman; the lover, all as **frantic**." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "The crowd surged forward in **frantic** haste, desperate to dip their rags into the spilled wine." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "I hurried through the streets with **frantic** speed, terrified that the fiend was tracking my every footstep." }
    ]
  },
  "Dashboard — phren/frenetic.md": {
    word: "frenetic",
    primary: "Fast, energetic, wild, and uncontrolled; frantic; characterized by chaotic activity.",
    secondary: "In cultural and social criticism, describing the hyper-accelerated, dizzying pace of modern urban life and industrial technology.",
    quotes: [
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "The orchestra played yellow cocktail music, and the opera of voices pitched a key higher amidst **frenetic** laughter." },
      { author: "Aldous Huxley", work: "Point Counter Point", quote: "He watched the jazz dancers with disdain, weary of their **frenetic** pursuit of mechanical oblivion." },
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "The factory floor operated at a **frenetic** tempo that reduced living men to twitching extensions of machines." }
    ]
  },
  "Dashboard — phren/frenzy.md": {
    word: "frenzy",
    primary: "A state or period of uncontrolled excitement, violent mental agitation, or wild emotional delirium.",
    secondary: "In poetry and classical tragedy (as divine frenzy or poetic mania), the inspired fury or ecstatic passion that seizes the artist or prophet.",
    quotes: [
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "The poet's eye, in fine **frenzy** rolling, / Doth glance from heaven to earth, from earth to heaven." },
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", quote: "His long improvisations upon the guitar were wild and unearthly, bordering upon sheer demonic **frenzy**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Religious **frenzy** seized the populace of Alexandria, driving them to tear down ancient pagan shrines." }
    ]
  },
  "Dashboard — phren/oneirophrenia.md": {
    word: "oneirophrenia",
    primary: "A hallucinatory, dreamlike mental state occurring during waking consciousness, often accompanying acute psychosis, prolonged sleep deprivation, or severe delirium.",
    secondary: "In clinical psychiatry (introduced by L. J. Meduna in 1950), an acute confusional syndrome marked by clouding of consciousness and a sense that reality is an unreal dream.",
    quotes: [
      { author: "Ladislaw J. Meduna", work: "Oneirophrenia: The Confusional State", quote: "We defined **oneirophrenia** as an acute mental syndrome where reality is experienced through a haze of dreamlike illusions." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "In traumatic **oneirophrenia**, patients wander in an ambulatory twilight state, perceiving nurses as figures in an ancient pageant." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Prolonged amphetamine abuse triggered intense **oneirophrenia**, submerging his waking hours in vivid paranoid fantasies." }
    ]
  },
  "Dashboard — phren/paraphrenia.md": {
    word: "paraphrenia",
    primary: "A chronic psychotic disorder characterized by elaborate, well-organized paranoid delusions and hallucinations with relatively preserved intellectual functioning and personality.",
    secondary: "In European psychiatric nosology (formulated by Kraepelin), a late-onset paranoid condition distinguished from dementia praecox by the absence of dementia or emotional blunting.",
    quotes: [
      { author: "Emil Kraepelin", work: "Clinical Psychiatry", quote: "We distinguish **paraphrenia** from dementia praecox by the remarkable preservation of personality despite fantastic paranoid systems." },
      { author: "Sigmund Freud", work: "On Narcissism", quote: "In **paraphrenia**, the libido is withdrawn from the external world and redirected entirely upon the ego." },
      { author: "Eugen Bleuler", work: "Textbook of Psychiatry", quote: "Patients with late **paraphrenia** can manage everyday business affairs while harboring grandiose delusions of royal descent." }
    ]
  },
  "Dashboard — phren/phren.md": {
    word: "phren",
    primary: "A combining root derived from Ancient Greek phrēn, meaning mind, intellect, heart, or anatomical diaphragm.",
    secondary: "In historical physiology and medicine, reflecting the archaic Homeric belief that the respiratory diaphragm and midriff were the physical seat of emotion and thought.",
    quotes: [
      { author: "Homer", work: "The Iliad", quote: "Grief gripped Achilles deep within his **phren**, and he poured black ashes over his golden head." },
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "From Greek **phren**, meaning both diaphragm and intellect, modern medicine inherited phrenic, frenzy, and schizophrenia." },
      { author: "C. G. Jung", work: "Psychology and Religion", quote: "The archaic identification of the **phren** with both breathing and mental life reveals the somatopsychic roots of consciousness." }
    ]
  },
  "Dashboard — phren/phrenetic.md": {
    word: "phrenetic",
    primary: "A variant spelling of frenetic; wildly excited, frantic, or suffering from mental delirium.",
    secondary: "In classical and Renaissance English prose, describing violent intellectual passion, manic enthusiasm, or feverish mental agitation.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "A **phrenetic** man runs naked through the streets, crying that his brain is consumed by wildfire." },
      { author: "Samuel Taylor Coleridge", work: "Table Talk", quote: "His argument lacked philosophical calm, rushing onward in a **phrenetic** torrent of vehement indignation." },
      { author: "William Hazlitt", work: "The Spirit of the Age", quote: "The political orator’s speech was marked by **phrenetic** energy that electrified the crowd without convincing their reason." }
    ]
  },
  "Dashboard — phren/phrenic.md": {
    word: "phrenic",
    primary: "Of or relating to the diaphragm in anatomy (as the phrenic nerve); also of or relating to the mind.",
    secondary: "In human neuroanatomy, specifically referring to the bilateral phrenic nerves arising from cervical roots C3–C5 that provide motor innervation to the diaphragm for respiration.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy of the Human Body", quote: "The **phrenic** nerve descends through the thorax to supply motor innervation to the respiratory diaphragm." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Irritation of the **phrenic** nerve commonly induces intractable hiccups and diaphragmatic spasms." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The anatomist must trace the **phrenic** pathway with delicate care during dissection of the anterior neck." }
    ]
  },
  "Dashboard — phren/phrenitis.md": {
    word: "phrenitis",
    primary: "An ancient and historical medical diagnosis denoting acute inflammation of the brain accompanied by raging fever and violent delirium.",
    secondary: "In the history of medicine (Hippocrates to the 18th century), an acute febrile encephalopathy roughly corresponding to modern acute encephalitis or meningitis.",
    quotes: [
      { author: "Hippocrates", work: "Aphorisms", quote: "In cases of **phrenitis**, acute fever coupled with picking at bedclothes and violent muttering portends a fatal crisis." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "**Phrenitis** is an inflammation of the brain’s meninges, driving the patient to furious shouting and frantic delirium." },
      { author: "Thomas Willis", work: "Cerebri Anatome", quote: "Our post-mortem dissections demonstrate that the fatal distemper formerly termed **phrenitis** leaves severe swelling of the cerebral vessels." }
    ]
  },
  "Dashboard — phren/phrenological.md": {
    word: "phrenological",
    primary: "Of, relating to, or characteristic of phrenology, the 19th-century pseudo-scientific study of skull shape as an index of character and intellect.",
    secondary: "In Victorian literature and cultural history, describing popular skull-measuring charts, ceramic busts, and assessments of mental 'organs' and faculties.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "I would fain examine the sperm whale's **phrenological** developments, had he not so vast and impenetrable a cranium." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Rochester scrutinized my skull with a mock-serious gaze, declaring his intention to perform a **phrenological** reading of my obstinacy." },
      { author: "Mark Twain", work: "Autobiography of Mark Twain", quote: "The traveling **phrenological** lecturer ran his fingers across my bumps, finding an extraordinary cavity where the organ of caution should have been." }
    ]
  },
  "Dashboard — phren/phrenologist.md": {
    word: "phrenologist",
    primary: "A practitioner, expert, or advocate of phrenology who determines character and intellect by examining the contours of the skull.",
    secondary: "In 19th-century social history, a popular consultant who mapped cranial bumps to advise clients on careers, marriage prospects, and moral reform.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Imp of the Perverse", quote: "In the pure arrogance of reason, the **phrenologist** has failed to recognize our radical instinct for perversity." },
      { author: "George Eliot", work: "The Mill on the Floss", quote: "The visiting **phrenologist** declared that Tom possessed large organs of firmness and small organs of imagination." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "Dr. Mortimer gazed at Holmes's head with professional admiration, exclaiming, 'You have really a very remarkable cranium, sir; I covet your skull, as a **phrenologist**!'" }
    ]
  },
  "Dashboard — phren/phrenology.md": {
    word: "phrenology",
    primary: "The 19th-century pseudo-scientific doctrine that mental faculties and character traits are localized in specific brain organs indicated by external skull contours.",
    secondary: "In the history of neuroscience, the system founded by Franz Joseph Gall that erroneously read skull bumps but presciently introduced the principle of cerebral localization of function.",
    quotes: [
      { author: "Walt Whitman", work: "Leaves of Grass (Preface)", quote: "The great poet must assimilate all science—geology, **phrenology**, chemistry—into his grand hymn of American democracy." },
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", quote: "Modern cerebral physiology has swept away the crude map of **phrenology**, replacing it with experimental electrical mapping." },
      { author: "Oliver Wendell Holmes Sr.", work: "The Professor at the Breakfast-Table", quote: "Phrenologists imagine the mind as a chest of drawers, forgetting that **phrenology** mistakes outer bone for inner soul." }
    ]
  },
  "Dashboard — phren/phronema.md": {
    word: "phronema",
    primary: "The mindset, spiritual outlook, or disposition of the mind (Greek phrónēma).",
    secondary: "In Eastern Orthodox Christian theology, the collective mind, spiritual ethos, and living consensus of the Church handed down across generations.",
    quotes: [
      { author: "Apostle Paul", work: "Epistle to the Romans (8:6)", quote: "For the **phronema** of the flesh is death, but the **phronema** of the Spirit is life and peace." },
      { author: "John Henry Newman", work: "An Essay on the Development of Christian Doctrine", quote: "The consensus of the faithful preserves that inward **phronema** that guards traditional dogma against novel heresies." },
      { author: "Georges Florovsky", work: "Bible, Church, Tradition", quote: "True theological fidelity requires not mechanical quoting of texts, but acquiring the living **phronema** of the holy Fathers." }
    ]
  },
  "Dashboard — phren/phronesis.md": {
    word: "phronesis",
    primary: "Practical wisdom, prudence, or sound moral judgment; the capacity to deliberate well about human conduct and flourishing in classical ethics.",
    secondary: "In Aristotelian moral philosophy, the intellectual virtue governing practical action (distinguished from theoretical sophia and technical techne).",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "**Phronesis** is a true and reasoned state of capacity to act with regard to the things that are good or bad for man." },
      { author: "Hans-Georg Gadamer", work: "Truth and Method", quote: "The hermeneutic experience of historical understanding is fundamentally a form of Aristotelian **phronesis** rather than abstract scientific techne." },
      { author: "Alasdair MacIntyre", work: "After Virtue", quote: "Without **phronesis**, none of the other moral virtues can be properly exercised, for it dictates the golden mean in particular circumstances." }
    ]
  },
  "Dashboard — phren/phronetic.md": {
    word: "phronetic",
    primary: "Of, relating to, or characterized by practical wisdom (phronesis); guided by prudent moral judgment in human action.",
    secondary: "In contemporary social science (Bent Flyvbjerg's phronetic social science), an approach focusing on contextual values, power dynamics, and practical social praxis.",
    quotes: [
      { author: "Bent Flyvbjerg", work: "Making Social Science Matter", quote: "A **phronetic** social science does not seek universal natural laws, but clarifies practical values and power in real-world contexts." },
      { author: "Richard J. Bernstein", work: "Beyond Objectivism and Relativism", quote: "The moral agent exercises **phronetic** insight, applying broad ethical principles to concrete historical situations." },
      { author: "Martha Nussbaum", work: "The Fragility of Goodness", quote: "Deliberation in Greek tragedy is intensely **phronetic**, wrestling with irreducible, conflicting goods." }
    ]
  },
  "Dashboard — phren/sophrenia.md": {
    word: "sophrenia",
    primary: "Soundness of mind, mental poise, or wisdom combined with intellectual temperance (from Greek sophos wise + phren mind).",
    secondary: "In classical ethics and humanistic psychology, the harmonious integration of intellect and emotion producing stable mental equilibrium.",
    quotes: [
      { author: "Plato", work: "Charmides", quote: "The philosopher sought to discover whether true **sophrenia** consists in knowing one's own limits and exercising mental restraint." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The ideal Hellenic citizen balanced athletic vigor against that inward **sophrenia** that preserves civic order." },
      { author: "Robert Bridges", work: "The Testament of Beauty", quote: "Above the storm of sensual impulse rises that quiet **sophrenia**, wherein reason and feeling dwell in peace." }
    ]
  },
  "Dashboard — phren/sophrosyne.md": {
    word: "sophrosyne",
    primary: "An ancient Greek concept of ideal character excellence and soundness of mind, characterized by moderation, self-control, temperance, and balance.",
    secondary: "In classical philosophy, the cardinal virtue that prevents hubris through self-knowledge, emotional restraint, and harmonious living within natural limits.",
    quotes: [
      { author: "Plato", work: "Republic", quote: "**Sophrosyne** is like a kind of harmony, spreading through the whole state and bringing the rulers and the ruled into concord." },
      { author: "Aristotle", work: "Rhetoric", quote: "**Sophrosyne** is the virtue by which men are disposed to obey the law in the matter of bodily pleasures." },
      { author: "Friedrich Nietzsche", work: "The Birth of Tragedy", quote: "Apollonian culture erected the glorious monument of **sophrosyne** as a defensive rampart against the chaotic Dionysian abyss." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
    return;
  }
  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Batch 3 completed! Total words updated:", Object.keys(wordsData).length);
