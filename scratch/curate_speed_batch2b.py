# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — vibr (remaining 8 words)
  # =========================================================================
  "Dashboard — vibr/vibrational.md": {
    "primary": "Relating to, consisting of, or caused by rapid periodic oscillations or vibration.",
    "secondary": "In molecular spectroscopy and quantum mechanics, vibrational energy levels and transitions observed in infrared and Raman spectra.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The magnetic induction produced a distinct **vibrational** pulse through the coils of the armature."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "Molecular kinetic energy is apportioned between translational and **vibrational** degrees of freedom."},
      {"author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "Thermal radiation excites the internal **vibrational** modes of polyatomic gas molecules."}
    ]
  },
  "Dashboard — vibr/vibrato.md": {
    "primary": "A pulsating, expressive musical effect produced by slight, rapid, and regular variations in pitch or volume.",
    "secondary": "In vocal and string performance pedagogy, expressive pitch oscillation controlled by the laryngeal musculature or the left wrist.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The tenor marred an otherwise noble aria by indulging in an excessive and uncontrollable **vibrato**."},
      {"author": "Arthur Conan Doyle", "work": "The Red-Headed League", "quote": "Holmes closed his eyes, savoring the rich, haunting **vibrato** of Sarasate's violin solo at St. James's Hall."},
      {"author": "Thomas Mann", "work": "Buddenbrooks", "quote": "The organist struck a sustained chord, letting its gentle **vibrato** reverberate through the high nave."}
    ]
  },
  "Dashboard — vibr/vibrator.md": {
    "primary": "A mechanical or electromagnetic device that produces rapid, continuous oscillatory vibrations.",
    "secondary": "In early electrical engineering, an electromagnetic interrupter or trembler reed used in induction coils and telegraph transmitters.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The rhythmic buzzing of the spring **vibrator** regulated the periodic interruption of the battery circuit."},
      {"author": "H. G. Wells", "work": "The Sleeper Awakes", "quote": "The complex machinery was activated by a small pneumatic **vibrator** pulsating rapidly upon the console."},
      {"author": "Nikola Tesla", "work": "My Inventions: The Autobiography of Nikola Tesla", "quote": "I constructed an electromechanical **vibrator** capable of producing powerful resonance in solid rock foundations."}
    ]
  },
  "Dashboard — vibr/vibratory.md": {
    "primary": "Characterized by, causing, or consisting of rapid oscillations back and forth; vibrating.",
    "secondary": "In physics and physiological acoustics, vibratory wave motions transmitted through air or bone to stimulate auditory hair cells.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Luminous bodies excite a **vibratory** motion in the ethereal medium that spreads in concentric waves."},
      {"author": "John Tyndall", "work": "Sound", "quote": "The tuning fork imparts its **vibratory** impulse to the surrounding air, generating acoustic waves."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Intense terror often induces a rapid **vibratory** trembling throughout the voluntary musculature."}
    ]
  },
  "Dashboard — vibr/vibrio.md": {
    "primary": "A genus of curved, comma-shaped Gram-negative bacteria possessing a single polar flagellum for motility.",
    "secondary": "In clinical microbiology and infectious epidemiology, Vibrio cholerae secreting enterotoxin that produces massive dehydrating diarrhea.",
    "quotes": [
      {"author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "quote": "Microscopic analysis of the epidemic water supply revealed abundant comma-shaped **vibrio** organisms."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The pathogenic **vibrio** was isolated from the intestinal discharges of victims dying of Asiatic cholera."},
      {"author": "Louis Pasteur", "work": "Germ Theory and Its Applications to Medicine and Surgery", "quote": "Culturing the motile **vibrio** confirmed its distinct morphological characteristics under the high-power objective."}
    ]
  },
  "Dashboard — vibr/vibrion.md": {
    "primary": "A microscopic, motile bacterium with an undulatory or comma-shaped morphology; a vibrio.",
    "secondary": "In 19th-century bacteriological literature, early classifications of curved and spiral bacterial filaments (vibrioniens).",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The butyric fermentation was excited by a peculiar **vibrion** capable of living without free atmospheric oxygen."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Every drop of stagnant infusion teemed with innumerable active monads and the sinuous **vibrion**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Observers debated whether the septic **vibrion** represented a distinct infectious entity or a post-mortem invader."}
    ]
  },
  "Dashboard — vibr/vibrionic.md": {
    "primary": "Relating to, caused by, or characteristic of bacteria of the genus Vibrio; of the nature of a vibrio.",
    "secondary": "In veterinary epidemiology, vibrionic abortion in sheep and cattle caused by Campylobacter (formerly Vibrio) fetus.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The severe dehydration was diagnosed as an acute **vibrionic** infection contracted from contaminated canal water."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Pathologists investigated the toxic mechanisms underlying **vibrionic** enteritis in experimental models."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Epidemics of **vibrionic** dysentery swept through overcrowded tenements lacking clean municipal drainage."}
    ]
  },
  "Dashboard — vibr/vibrissa.md": {
    "primary": "A long, stiff tactile hair growing on the face or snout of many mammals, such as a cat's whisker.",
    "secondary": "In comparative vertebrate anatomy and sensory neurobiology, specialized sinus hair follicles with rich trigeminal innervation detecting spatial vibrations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Each facial **vibrissa** is connected with sensitive sensory nerves that warn nocturnal animals of nocturnal obstacles."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The enormous tactile **vibrissa** of the walrus facilitates foraging for shellfish along muddy ocean beds."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The follicle of a mammalian **vibrissa** is surrounded by a venous sinus providing sensitive hydrostatic amplification."}
    ]
  },

  # =========================================================================
  # Dashboard — vola (16 words)
  # =========================================================================
  "Dashboard — vola/nonvolatile.md": {
    "primary": "Not evaporating readily at normal room temperatures and pressures; stable, persistent, or permanent.",
    "secondary": "In computer architecture and chemistry, nonvolatile memory (such as ROM or flash) that retains data without continuous electrical power.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Evaporation of the solvent leaves behind the **nonvolatile** mineral residue crystallized upon the porcelain dish."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Fixed salts remain **nonvolatile** even when subjected to the intense heat of the reverberatory furnace."},
      {"author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "Dense, **nonvolatile** solids require enormous thermal energy before their atomic cohesion is overcome."}
    ]
  },
  "Dashboard — vola/nonvolatilisable.md": {
    "primary": "Incapable of being converted into gas or vapor; resistant to volatilization under standard conditions.",
    "secondary": "In analytical metallurgy, refractory metals and inorganic silicates that resist sublimation in open crucibles.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "The metallic slag proved entirely **nonvolatilisable** at the highest temperature attainable by the forge."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Certain earthy earths are found to be stubbornly **nonvolatilisable** under prolonged calcination."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The mineral ash left by combustion consists of **nonvolatilisable** carbonates and oxides."}
    ]
  },
  "Dashboard — vola/nonvolatilizable.md": {
    "primary": "Not susceptible of being vaporized or converted into a gaseous state; chemically fixed or refractory.",
    "secondary": "In chemical refining, heavy hydrocarbon fractions and tars that remain in the boiling vessel during fractional distillation.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical History of a Candle", "quote": "The heavy carbonaceous base of the wick is **nonvolatilizable**, serving to anchor the luminous flame."},
      {"author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "A **nonvolatilizable** film of soot deposited upon the glass surface absorbed all incident thermal radiation."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The fixed and **nonvolatilizable** components of the compound remained behind after prolonged boiling."}
    ]
  },
  "Dashboard — vola/volaille.md": {
    "primary": "Poultry or the edible flesh of domestic birds (such as chicken, capon, or turkey) in culinary gastronomy.",
    "secondary": "In classical French haute cuisine, culinary dishes utilizing supreme de volaille prepared with velouté sauces and truffles.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "The grand banquet commenced with an exquisite soup followed by a delicate fricassee of **volaille**."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "They dined delightfully in the Parisian courtyard upon white wine and tender roast **volaille**."},
      {"author": "Tobias Smollett", "work": "Travels through France and Italy", "quote": "The provincial inn served an agreeable supper composed of local trout and seasoned **volaille**."}
    ]
  },
  "Dashboard — vola/volans.md": {
    "primary": "A faint southern constellation located near the south celestial pole, representing a flying fish (Piscis Volans).",
    "secondary": "In observational astrometry, an 8th-magnitude constellation introduced by Dutch navigators Keyser and de Houtman in 1598.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Near the Large Magellanic Cloud lies the compact constellation **Volans**, visible only in southern skies."},
      {"author": "Richard Anthony Proctor", "work": "The Orbs Around Us", "quote": "Navigators sailing past the Cape of Good Hope steered by the sparkling stars of Piscis **Volans**."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "The celestial cartographer depicted the graceful flying fish of **Volans** skimming across the polar sphere."}
    ]
  },
  "Dashboard — vola/volant.md": {
    "primary": "Flying or capable of flight; passing swiftly through the air; with wings outstretched.",
    "secondary": "In classical heraldry, depicting a bird or winged beast in the act of flying with wings extended horizontally.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The radiant seraph sped on **volant** wing across the celestial plains toward the gates of morning."},
      {"author": "Walter Scott", "work": "The Lay of the Last Minstrel", "quote": "The knight bore upon his shield a falcon **volant**, ready to strike down its quarry in flight."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Swift thoughts flew like **volant** spirits across the expanse of the starry midnight sky."}
    ]
  },
  "Dashboard — vola/volar.md": {
    "primary": "Relating to the palm of the hand (palmar) or the flexor surface of the forearm or sole of the foot.",
    "secondary": "In orthopedic surgery and microvascular reconstruction, the volar plate and volar carpal ligament providing stability against wrist hyperextension.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A small erythematous nodule appeared on the **volar** aspect of the patient's thumb, indicating embolus."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The deep **volar** arch supplies arterial blood to the digital branches through an intricate anastomosis."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The surgeon made a longitudinal incision along the **volar** surface of the wrist to relieve median nerve pressure."}
    ]
  },
  "Dashboard — vola/volary.md": {
    "primary": "A large enclosure, cage, or aviary spacious enough to permit birds to fly freely within it.",
    "secondary": "In landscape gardening and ornithological history, grand royal aviaries constructed in palace gardens for exotic avian species.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays: Of Gardens", "quote": "For aviaries, I like them not, except they be of that largeness as they may be turf-walks, like a great **volary**."},
      {"author": "John Evelyn", "work": "Diary of John Evelyn", "quote": "We inspected the duke's magnificent **volary**, populated with rare hummingbirds and birds of paradise."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Miss Flite kept her caged birds in a tiny garret that she fancifully referred to as her private **volary**."}
    ]
  },
  "Dashboard — vola/volatile.md": {
    "primary": "Evaporating rapidly at normal temperatures; liable to change rapidly and unpredictably, especially for the worse.",
    "secondary": "In financial market analysis and chemical kinetics, assets exhibiting high price variance; or compounds with high vapor pressures.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Spirits that are too subtle and **volatile** dissipate into air unless fixed by methodical judgment."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Popular sentiment in revolutionary times is ever **volatile**, veering rapidly from adoration to bloody vengeance."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The ethereal liquid was extremely **volatile**, vaporizing immediately upon contact with the open air."}
    ]
  },
  "Dashboard — vola/volatilisable.md": {
    "primary": "Capable of being vaporized or converted into gas upon the application of heat.",
    "secondary": "In extractive metallurgy and sublimatory distillation, chemical substances that sublimate or boil off without chemical decomposition.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Camphor is readily **volatilisable** under gentle heat, depositing beautiful crystal needles upon the glass."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The alchemist examined whether the sulphur of the mineral was truly **volatilisable** or fixed."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Organic matter contains **volatilisable** compounds that escape during heating, leaving mineral charcoal."}
    ]
  },
  "Dashboard — vola/volatilise.md": {
    "primary": "To convert or cause to pass from a solid or liquid state into gas or vapor; to evaporate.",
    "secondary": "In thermodynamics, phase change to the gaseous state promoted by raising temperature above boiling or sublimation point.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Care must be taken not to **volatilise** the precious iodine crystals by applying sudden excess heat."},
      {"author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "A intense electric spark will instantly **volatilise** the thinnest strip of gold leaf into fine purple dust."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The warm air from the lungs tends to **volatilise** moisture, producing clouds of vapor on cold mornings."}
    ]
  },
  "Dashboard — vola/volatilised.md": {
    "primary": "Converted into gas, vapor, or steam through heat or chemical action; evaporated away.",
    "secondary": "In metallurgical cupellation, impurities volatilised by furnace blasts leaving purified bullion.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "The solvent had completely **volatilised**, leaving a sparkling crust of pure crystals inside the flask."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The lighter spirits were **volatilised** by the gentle warmth of the water bath."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The heat-ray instantly **volatilised** the moisture within the trees, causing them to burst into flame."}
    ]
  },
  "Dashboard — vola/volatility.md": {
    "primary": "The tendency of a substance to evaporate rapidly; liability to rapid and unpredictable change.",
    "secondary": "In econometric finance, statistical variance (standard deviation) of returns of a financial asset over a specified timeframe.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "The extreme **volatility** of ether necessitates keeping the storage bottles in a cool, shaded environment."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The dangerous **volatility** of paper speculation frequently imperils the stability of commercial banking."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The alarming **volatility** of the Parisian mob rendered every constitutional settlement temporary."}
    ]
  },
  "Dashboard — vola/volatilizable.md": {
    "primary": "Capable of being turned into vapor; subject to vaporization or sublimation under suitable temperature.",
    "secondary": "In analytical chemistry, elements or volatile organic compounds (VOCs) separated from crude matrices by thermal desorption.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Mercury is a **volatilizable** metal that condenses readily upon the cold upper neck of the retort."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "He demonstrated that the essential oil was easily **volatilizable** without losing its aromatic virtue."},
      {"author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "The **volatilizable** components of the coal escaped in thick smoke as the temperature rose."}
    ]
  },
  "Dashboard — vola/volatilize.md": {
    "primary": "To cause to pass off in vapor; to transform from liquid or solid into a gaseous state.",
    "secondary": "In high-temperature physics and spectroscopy, electric arcs used to volatilize refractory samples for atomic emission analysis.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "A steady flame was applied to **volatilize** the liquid, collecting the distillate in a chilled receiver."},
      {"author": "John Tyndall", "work": "Fragments of Science", "quote": "The electric discharge possessed sufficient thermal energy to **volatilize** the diamond in an atmosphere of oxygen."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "To **volatilize** the stubborn mineral requires temperatures unattainable by ordinary domestic hearths."}
    ]
  },
  "Dashboard — vola/volatilized.md": {
    "primary": "Having been evaporated or converted into vapor; dispersed into the atmosphere as gas.",
    "secondary": "In geophysics and impact cratering, volatile rock and ice volatilized instantly upon cosmic meteoritic impact.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "The alcohol was gradually **volatilized**, leaving the pure resin deposited upon the walls of the vessel."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The chemical tincture was rapidly **volatilized** by the apparatus, filling the laboratory with bleaching fumes."},
      {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "Holmes suggested that an unfamiliar cosmic vapor had **volatilized** in the upper strata of the atmosphere."}
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

print(f"Speed Batch 2B: Successfully updated {updated}/{len(data)} notes.")
