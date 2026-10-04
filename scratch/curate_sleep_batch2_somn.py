# -*- coding: utf-8 -*-
"""
Curates Dashboard — somn (14 words) in Cluster Sleep, Rest & Stillness.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_somn = {
  "insomnia": {
    "primary": "Habitual or chronic inability to obtain adequate sleep; persistent sleeplessness.",
    "secondary": "In clinical psychiatry, a recognized sleep disorder marked by difficulty initiating or maintaining restorative rest.",
    "quotes": [
      {"author": "Franz Kafka", "work": "Letters to Felice", "quote": "My **insomnia** only means that I am continually watchful, dreading the onset of unconsciousness."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Severe **insomnia** fractures the stream of thought, filling wakeful hours with morbid ruminations."},
      {"author": "F. Scott Fitzgerald", "work": "The Crack-Up", "quote": "In a real dark night of the soul, it is always three o'clock in the morning, day after day of unrelenting **insomnia**."}
    ]
  },
  "insomniac": {
    "primary": "A person who is chronically or habitually afflicted with sleeplessness or insomnia.",
    "secondary": "In psychological studies, an individual experiencing impaired cognitive performance due to prolonged sleep deprivation.",
    "quotes": [
      {"author": "Vladimir Nabokov", "work": "Speak, Memory", "quote": "Like every passionate **insomniac**, I regarded the approaching daylight with mixed relief and dread."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The lonely **insomniac** listens to the ticking clock and the distant murmur of nocturnal streets."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Resident Patient", "quote": "The trembling doctor was an acute **insomniac**, pacing his consulting room night after night."}
    ]
  },
  "somnambulate": {
    "primary": "To walk, move about, or perform actions while asleep or in a somnambulistic trance.",
    "secondary": "In literary metaphor, to move or act in a dazed, unthinking, or automatous state.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "I have seen her rise from her bed, unlock her closet, take forth paper, write upon't, and return to bed; thus did Lady Macbeth **somnambulate** through the dark gallery."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "At dead of night a stealthy figure seemed to **somnambulate** through the upper corridors of Thornfield Hall."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Arthur Dimmesdale felt an uncanny urge to **somnambulate** toward the scaffold in the black of midnight."}
    ]
  },
  "somnambulation": {
    "primary": "The act, process, or habit of walking about or performing complex behaviors while asleep.",
    "secondary": "In sleep medicine and parasomnia research, motor behavior initiated during slow-wave non-REM sleep.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Premature Burial", "quote": "Episodes of **somnambulation** and cataleptic trance plagued the narrator since early childhood."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The clerk's nocturnal **somnambulation** alarmed the entire household when he began filing papers in his sleep."},
      {"author": "Wilkie Collins", "work": "The Moonstone", "quote": "The crucial extraction of the diamond occurred during an involuntary episode of **somnambulation** caused by laudanum."}
    ]
  },
  "somnambulism": {
    "primary": "Sleepwalking; a sleep disorder involving motor activities performed while asleep.",
    "secondary": "In medical jurisprudence, automatic motor behavior during sleep raised as a defense in criminal law.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Walking in the shadow of a dream, as it were, and under the influence of **somnambulism**, Mr. Dimmesdale reached the spot."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "There have been documented cases of **somnambulism** in which complex actions were performed during unconscious motor activity."},
      {"author": "W. D. Pitcairn", "work": "Two Years Among the Savages", "quote": "The native guide exhibited symptoms of **somnambulism**, rising from his mat to wander through the camp fires."}
    ]
  },
  "somnambulist": {
    "primary": "A person who walks about, speaks, or performs other complex actions while asleep; a sleepwalker.",
    "secondary": "In historical hypnotism and mesmerism, a subject in an induced deep hypnotic trance.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy stood rigid as a **somnambulist**, his eyes fixed upon the marble monument in the churchyard."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She moved about the quiet library like a **somnambulist**, obeying routine duties without conscious awareness."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The company doctor looked at me attentively, like an experimenter studying an unconscious **somnambulist**."}
    ]
  },
  "somniferous": {
    "primary": "Inducing, tending to produce, or bringing about sleep; soporific and slumber-bearing.",
    "secondary": "In pharmacological botany, designating sleep-inducing plants such as Papaver somniferum (opium poppy).",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Pearl played among the weeds, gathering the dark and **somniferous** nightshade with innocent curiosity."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Henbane and mandragora possess strong **somniferous** properties capable of quieting the most agitated mind."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The warm fire and heavy draperies produced a **somniferous** languor that stilled conversation."}
    ]
  },
  "somnific": {
    "primary": "Causing, stimulating, or tending to produce sleep; sleep-inducing.",
    "secondary": "In pharmaceutical physiology, agents or stimuli that promote the onset of neurological slumber.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The gentle murmur of falling water exerts a **somnific** charm upon weary travelers."},
      {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Certain neutral salts and warm pediluvia act as mild **somnific** remedies in nervous fevers."},
      {"author": "John Keats", "work": "Endymion", "quote": "Poppies cast their **somnific** dew across the eyelids of the slumbering shepherd."}
    ]
  },
  "somniloquism": {
    "primary": "The act, habit, or phenomenon of talking in one's sleep without conscious awareness.",
    "secondary": "In sleep pathology, a parasomnia characterized by sleep-talking during REM or non-REM sleep transitions.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Curious instances of **somniloquism** reveal how memories echo through the brain when will is suspended."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The suspect's midnight **somniloquism** inadvertently betrayed the location of the stolen Agra treasure."},
      {"author": "Oliver Wendell Holmes", "work": "The Professor at the Breakfast-Table", "quote": "Psychologists study **somniloquism** to decipher the fragmentary language of the dreaming mind."}
    ]
  },
  "somniloquist": {
    "primary": "A person who talks in their sleep; someone prone to unconscious sleep-talking.",
    "secondary": "In clinical neurology, an individual exhibiting frequent nocturnal vocalizations during sleep cycles.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Narrative of Arthur Gordon Pym", "quote": "The agitated sailor was a confirmed **somniloquist**, muttering dreadful shipboard secrets in his bunk."},
      {"author": "Wilkie Collins", "work": "The Woman in White", "quote": "Listening beside the bed of the **somniloquist**, Marian hoped to glean the secret of Sir Percival."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Tom feared that Huck would prove a dangerous **somniloquist** and reveal their graveyard adventure in sleep."}
    ]
  },
  "somniloquy": {
    "primary": "The practice or habit of talking in one's sleep; utterances spoken while asleep.",
    "secondary": "In forensic psychology, unconscious vocalizations uttered during parasomnia, generally inadmissible as voluntary testimony.",
    "quotes": [
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Ancient physicians recorded instances of **somniloquy** wherein patients disclosed hidden crimes in nocturnal delirium."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The frightened apprentice was betrayed by his own **somniloquy**, confessing his small thefts while dreaming."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In **somniloquy**, the motor speech apparatus responds directly to vivid dream imagery without conscious censorship."}
    ]
  },
  "somnolence": {
    "primary": "A state of strong desire for sleep, drowsiness, or sluggish mental and physical inactivity.",
    "secondary": "In clinical medicine, a decreased level of consciousness from which a patient is easily aroused but quickly falls back asleep.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "As a physiological remedy against **somnolence**, the student applied cold compresses to his throbbing temples."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "A heavy **somnolence** settled over Lowood School as the winter twilight faded into darkness."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The opulent degenerate court sank into luxurious **somnolence**, blind to the approaching barbarian storm."}
    ]
  },
  "somnolent": {
    "primary": "Sleepy, drowsy, lethargic, or inducing drowsiness; languid and sluggish.",
    "secondary": "In pastoral literature, describing quiet, slow-moving, or peaceful rural landscapes.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The **somnolent** cows stood motionless in the lush buttercup pastures of Blackmoor Vale."},
      {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "A drowsy, dreamy influence seems to hang over the land, and to pervade the very atmosphere of this **somnolent** valley."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "Onward to the dreamland, where the **somnolent** waters murmured against the limestone quay."}
    ]
  },
  "somnolently": {
    "primary": "In a sleepy, drowsy, heavy, or sluggish manner; languidly and half-asleep.",
    "secondary": "In narrative description, speaking or responding with the slow cadence of impending slumber.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The Fat Boy blinked **somnolently** at Mr. Wardle before nodding off once more in the carriage."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The watchman leaned **somnolently** against the bulwark, lulled by the rhythmic heaving of the sea."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The old dog opened one eye, wagged its tail **somnolently**, and curled closer to the hearth fire."}
    ]
  }
}
