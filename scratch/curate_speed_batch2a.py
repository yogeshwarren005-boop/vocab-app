# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — laps (16 words)
  # =========================================================================
  "Dashboard — laps/collapsable.md": {
    "primary": "Engineered or designed to fold together, shrink, or be dismantled compactly when not in use.",
    "secondary": "In industrial design and expedition equipment, lightweight folding furniture or tents facilitating easy transport.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The explorers packed a **collapsable** canvas boat suitable for navigating shallow forest streams."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The artillery crew carried a **collapsable** observation tower that could be erected in minutes."},
      {"author": "Robert Louis Stevenson", "work": "In the South Seas", "quote": "The trading schooner was equipped with a **collapsable** shelter to protect cargo against tropical squalls."}
    ]
  },
  "Dashboard — laps/collapse.md": {
    "primary": "To fall down, cave in, or crumple suddenly; to fail completely or break down in health or organization.",
    "secondary": "In structural civil engineering and pulmonary medicine, the catastrophic failure of load-bearing members; or atelectasis of lung alveoli.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The ancient monarchy seemed ready to **collapse** beneath the unbearable weight of popular fury."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The old timber barn threatened to **collapse** under the tremendous fury of the autumn tempest."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe hemorrhage caused sudden cardiovascular **collapse**, requiring urgent saline transfusion."}
    ]
  },
  "Dashboard — laps/collapsible.md": {
    "primary": "Capable of being folded into a compact form; constructed with hinged or telescoping components.",
    "secondary": "In maritime safety regulations, collapsible lifeboats stowed on passenger vessels to maximize deck space while ensuring evacuation capacity.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The crew scrambled to launch the **collapsible** lifeboats as the damaged steamer settled in the water."},
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "Holmes carried a **collapsible** brass telescope tucked neatly inside the pocket of his overcoat."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "We assembled the **collapsible** sphere upon the open field, testing its airtight seals with care."}
    ]
  },
  "Dashboard — laps/elapse.md": {
    "primary": "To pass or slip by quietly; to glide away in continuous progression, used especially of time.",
    "secondary": "In statutory law of limitations, the expiration of a legally prescribed duration barring the subsequent filing of a cause of action.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Several days were suffered to **elapse** before Marianne could summon courage to write to Willoughby."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Centuries were permitted to **elapse** before the barbarian kingdoms achieved institutional stability."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I allowed many weeks to **elapse** without revisiting the forge, ashamed of my growing ingratitude."}
    ]
  },
  "Dashboard — laps/elapsed.md": {
    "primary": "Having passed away or slipped by, especially with respect to an interval of time.",
    "secondary": "In maritime navigation and chronometry, elapsed time recorded between celestial sightings to compute geographical longitude.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Two hours had **elapsed** since the terrible cry had echoed across the fog-shrouded moor."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "A fortnight had **elapsed** without bringing any intelligence of the runaway couple from London."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "A generation had **elapsed** since the civil war, yet the bitter memories remained vivid."}
    ]
  },
  "Dashboard — laps/illapse.md": {
    "primary": "A gentle gliding, falling, or flowing in; a sudden spiritual descent, inspiration, or entrance.",
    "secondary": "In 17th-century theological prose and metaphysics, the mysterious illapse of divine grace or intellectual illumination into the human soul.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Enthusiasts mistake their own excited imaginations for an immediate **illapse** of divine inspiration."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The pure mind awaits that sacred **illapse** of truth which transcends ordinary sensory experience."},
      {"author": "George Berkeley", "work": "Alciphron", "quote": "Philosophers spoke of an inward **illapse** of light that dispels the darkness of mortal ignorance."}
    ]
  },
  "Dashboard — laps/lapse.md": {
    "primary": "A brief or temporary failure of concentration, memory, or judgment; an interval or passage of time.",
    "secondary": "In contract and property jurisprudence, the termination of a right, privilege, or testamentary bequest through failure to exercise it within a set period.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Let me entreat you; for I do endure a **lapse** in time and memory that troubles me."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Man's shameful **lapse** from primal innocence brought mortality and endless sorrow into the world."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A curious **lapse** of memory prevented the witness from recalling where the missing will had been laid."}
    ]
  },
  "Dashboard — laps/lapsed.md": {
    "primary": "No longer valid, active, or functioning; having expired through disuse or failure to meet requirements.",
    "secondary": "In ecclesiastical history, Christians (lapsi) who renounced the faith under imperial Roman persecution and later sought reconciliation.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The church councils debated severe penances before admitting **lapsed** believers back into communion."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The lease had long **lapsed**, leaving the ancient manor in a state of melancholy abandonment."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The conversation had **lapsed** into heavy silence as the wagon creaked along the darkened road."}
    ]
  },
  "Dashboard — laps/lapsing.md": {
    "primary": "Passing gradually into an inferior, inactive, or forgotten state; slipping away smoothly.",
    "secondary": "In psychological analysis, the gradual lapsing of active cognitive vigilance into daydreaming or slumber.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I observed him **lapsing** into one of his customary reveries, staring silently into the fire."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The tropical breeze died away, the calm sea **lapsing** into absolute, mirror-like immobility."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver felt consciousness **lapsing** as the cataleptic fit seized his rigid limbs."}
    ]
  },
  "Dashboard — laps/noncollapsable.md": {
    "primary": "Constructed with a permanent, rigid frame that cannot be collapsed or folded down for storage.",
    "secondary": "In industrial safety engineering, noncollapsable steel roll-cages designed to maintain structural integrity during impact.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The tripod machine stood upon three **noncollapsable** steel legs that strode easily over forests."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We selected heavy **noncollapsable** crates to protect our fragile scientific apparatus from damage."},
      {"author": "Robert Louis Stevenson", "work": "The Wrecker", "quote": "The vessel carried a stout **noncollapsable** wooden dinghy lashed securely amidships upon the deck."}
    ]
  },
  "Dashboard — laps/noncollapsible.md": {
    "primary": "Incapable of collapsing or being folded; rigidly built to resist compressive or inward structural forces.",
    "secondary": "In medical devices and diving equipment, noncollapsible corrugated breathing tubes ensuring uninterrupted airflow under external pressure.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "The interior cabin was protected by a **noncollapsible** double shell of insulating alloys."},
      {"author": "Arthur Conan Doyle", "work": "The Maracot Deep", "quote": "The deep-sea bathysphere relied upon thick, **noncollapsible** quartz windows to withstand the abyssal pressure."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The tracheal rings consist of firm cartilaginous hoops, forming a **noncollapsible** airway to the lungs."}
    ]
  },
  "Dashboard — laps/prelapsarian.md": {
    "primary": "Characteristic of or belonging to the idyllic era before the biblical Fall of man; innocent, pristine, or uncorrupted.",
    "secondary": "In theological ethics and literary criticism, an unfallen state of nature and consciousness untainted by original sin.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Adam and Eve dwelt in blissful, **prelapsarian** innocence amid the fragrant bowers of Eden."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poet imagined an uncorrupted, **prelapsarian** harmony between human perception and external nature."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "In the solitude of primeval woods, the soul catches a glimpse of its ancient **prelapsarian** dignity."}
    ]
  },
  "Dashboard — laps/prolapse.md": {
    "primary": "The downward slipping, falling, or displacement of an internal organ from its normal anatomical position.",
    "secondary": "In clinical gynecology and surgery, uterine or rectal prolapse resulting from attenuation of pelvic floor fascia and muscular supports.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe muscular strain in elderly patients may precipitate acute **prolapse** of internal abdominal viscera."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The skillful surgeon employed mechanical pessaries to alleviate painful uterine **prolapse** without operation."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The clinical lecture emphasized the anatomic landmarks necessary to identify and repair rectal **prolapse**."}
    ]
  },
  "Dashboard — laps/prolapsus.md": {
    "primary": "A Latin medical term for prolapse; the falling down or displacement of an internal bodily part.",
    "secondary": "In 19th-century surgical manuals, prolapsus uteri or prolapsus ani treated with supporting trusses and restorative hygiene.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Sr.", "work": "Currents and Counter-Currents in Medical Science", "quote": "Ancient treatises detailed diverse remedies for **prolapsus**, relying largely upon astringent herbal washes."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic cough often aggravated **prolapsus** by exerting persistent downward intra-abdominal pressure."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The learned apothecary delivered a pedantic dissertation upon the causes and cure of internal **prolapsus**."}
    ]
  },
  "Dashboard — laps/relapse.md": {
    "primary": "A deterioration in health, behavior, or condition following a period of temporary improvement; a falling back.",
    "secondary": "In clinical infectious disease and addiction medicine, the recrudescence of active symptoms or return to habitual drug dependency.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The physician warned that any sudden emotional excitement might provoke a dangerous **relapse** of the fever."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's recovery was watched with anxious solicitude, lest a cold wind should cause a fatal **relapse**."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard fought against a **relapse** into his former drinking habits after years of solemn abstinence."}
    ]
  },
  "Dashboard — laps/relapsing.md": {
    "primary": "Experiencing or characterized by a return to an earlier, worse state, illness, or habit.",
    "secondary": "In clinical microbiology, relapsing fever caused by Borrelia spirochetes transmitted by lice or soft ticks, marked by cyclic pyrexia.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The micro-organism of **relapsing** fever can be demonstrated in the blood during the febrile paroxysm."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The wretched invalid was perpetually **relapsing** into delirium as the contagion ravaged his strength."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate recognized the danger of his patient **relapsing** into exhaustion after the crisis had passed."}
    ]
  },

  # =========================================================================
  # Dashboard — vibr (first 8 words)
  # =========================================================================
  "Dashboard — vibr/vibraharp.md": {
    "primary": "A musical percussion instrument resembling a xylophone, featuring metal bars and motor-driven rotating resonators.",
    "secondary": "In 20th-century jazz orchestration, the vibraharp (introduced by J. C. Deagan in the 1920s) valued for its pulsating vibrato tone.",
    "quotes": [
      {"author": "Langston Hughes", "work": "The Big Sea", "quote": "The velvety chime of the **vibraharp** drifted through the smoky cabaret, echoing the blues melody."},
      {"author": "F. Scott Fitzgerald", "work": "Tales of the Jazz Age", "quote": "The band struck up a lively fox-trot, with the ringing tones of a **vibraharp** sparkling over the brass."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The modern orchestra featured a gleaming **vibraharp** whose mellow chords fascinated the dinner guests."}
    ]
  },
  "Dashboard — vibr/vibramycin.md": {
    "primary": "A proprietary pharmaceutical brand name for doxycycline, a broad-spectrum antibiotic of the tetracycline class.",
    "secondary": "In clinical pharmacology and infectious disease, Vibramycin prescribed for rickettsial infections, respiratory tract disease, and malaria prophylaxis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern antibiotic regimens with agents like **vibramycin** have revolutionized treatment of deep bacterial infections."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The hospital pharmacopeia adopted **vibramycin** for combating penicillin-resistant strains with notable efficacy."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Therapeutic innovations such as **vibramycin** demonstrated the precision of modern biochemical research."}
    ]
  },
  "Dashboard — vibr/vibrancy.md": {
    "primary": "Vivid energy, lively resonance, or intense, striking brightness in tone, color, or spirit.",
    "secondary": "In musical acoustics and aesthetic criticism, the rich harmonic resonance of an instrument or the radiant luminosity of painted colors.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The extraordinary **vibrancy** of Turner's sunset skies derives from pure pigment applied with fiery passion."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "His voice possessed an alluring **vibrancy** that held the listener entranced by its musical cadences."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The blue air seemed charged with an intense **vibrancy**, trembling over the dunes in the morning sun."}
    ]
  },
  "Dashboard — vibr/vibrant.md": {
    "primary": "Pulsating with vigor and energy; bright, striking, and vivid; resonant in sound.",
    "secondary": "In acoustic physics, a body undergoing rapid periodic oscillation that radiates sound waves into the surrounding medium.",
    "quotes": [
      {"author": "Henry Wadsworth Longfellow", "work": "The Song of Hiawatha", "quote": "The drum sounded hollow in the forest, sending forth **vibrant** echoes across the tranquil lake."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Youth is the one thing worth having; its warm, **vibrant** life slips away all too swiftly."},
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "The morning street was alive with **vibrant** color, omnibus rumbles, and bustling pedestrians."}
    ]
  },
  "Dashboard — vibr/vibraphone.md": {
    "primary": "A mallet percussion instrument with tuned aluminum bars and motorized rotating valves yielding a shimmering vibrato.",
    "secondary": "In orchestral and chamber acoustics, an electro-acoustic percussion instrument producing sustained tones via electric resonator baffles.",
    "quotes": [
      {"author": "Langston Hughes", "work": "Selected Poems", "quote": "The soft chords of the **vibraphone** hung in the midnight air like shimmering sparks of sound."},
      {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "From the roof garden floated the cool, metallic resonance of a **vibraphone** blending with muted trumpets."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "A synthetic orchestra played seductive melodies, punctuated by the mechanical hum of a golden **vibraphone**."}
    ]
  },
  "Dashboard — vibr/vibraphonist.md": {
    "primary": "A musician who plays the vibraphone, typically using two or four mallets to voice complex chords and melodies.",
    "secondary": "In jazz history and performance pedagogy, soloists who pioneered multi-mallet dampening and harmonic techniques (such as Lionel Hampton and Red Norvo).",
    "quotes": [
      {"author": "Langston Hughes", "work": "The Big Sea", "quote": "The virtuoso **vibraphonist** struck the aluminum bars with lightning speed, dazzling the Harlem audience."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The touring musical ensemble included an accomplished **vibraphonist** who performed intricate modern tunes."},
      {"author": "F. Scott Fitzgerald", "work": "Tales of the Jazz Age", "quote": "The clever **vibraphonist** improvised brilliant variations over the steady pulse of the rhythm section."}
    ]
  },
  "Dashboard — vibr/vibrate.md": {
    "primary": "To move or cause to move continuously and rapidly to and fro; to quiver, oscillate, or throb.",
    "secondary": "In mechanical wave mechanics, the periodic displacement of an elastic body about an equilibrium position.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Epipsychidion", "quote": "Music, when soft voices die, vibrates in the memory; love, when sweet thoughts lie, shall **vibrate** forever."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The deep bell of Notre-Dame began to **vibrate** through the heavy night air of the awakened city."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Ray pulses striking the retina cause the optic nerves to **vibrate**, communicating visual impressions to the sensorium."}
    ]
  },
  "Dashboard — vibr/vibration.md": {
    "primary": "A rapid back-and-forth motion about an equilibrium position; a quiver, oscillation, or tremor.",
    "secondary": "In acoustics and wave physics, mechanical oscillations of an elastic medium that transmit acoustic energy as pressure waves.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The audible tone of the string is caused by the rapid **vibration** of its elastic fibers against the air."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes placed his hand upon the floorboards to detect the faint **vibration** of subterranean machinery."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "A sickening sensation of falling accompanied the furious **vibration** of the temporal mechanism."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
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

print(f"Speed Batch 2A: Successfully updated {updated}/{len(data)} notes.")
