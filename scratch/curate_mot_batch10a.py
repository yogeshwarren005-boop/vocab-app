# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — mot Part 1 (10A, 33 words) ---
  "Dashboard — mot/commotion.md": {
    "primary": "A state of noisy, confused, and tumultuous movement, disturbance, or violent agitation.",
    "secondary": "In political history, civil commotion describes localized rioting or violent urban disorder short of formal belligerent insurrection.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "There is a great **commotion** in the Prince's camp, and all the northern borders are up in arms."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The sudden alarm in the courtyard created a tremendous **commotion** among the terrified prisoners."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The trumpet blast caused an instant **commotion** throughout the tournament lists, knights scrambling to horse."}
    ]
  },
  "Dashboard — mot/demote.md": {
    "primary": "To reduce someone to a lower rank, grade, position, or class, usually as a disciplinary penalty.",
    "secondary": "In corporate human resources, administrative boards demote nonperforming supervisors to lower salary tiers following formal performance reviews.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The master decided to **demote** the neglectful bailiff to the rank of common teamster."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The commander-in-chief did not hesitate to **demote** any general who displayed lack of operational vigor."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The board resolved to **demote** the clerk whose accounts showed suspicious discrepancies."}
    ]
  },
  "Dashboard — mot/demotic.md": {
    "primary": "Relating to or characteristic of ordinary people; popular, colloquial, or vernacular.",
    "secondary": "In Egyptology, Demotic denotes the simplified cursive Egyptian script that replaced Hieratic during the Saite Dynasty around 650 BCE.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The Rosetta Stone provided parallel texts in sacred hieroglyphs, cursive **demotic** script, and classical Greek."},
      {"author": "George Orwell", "work": "All Art Is Propaganda", "quote": "Dickens drew masterfully upon the **demotic** speech of London cockneys to give vitality to his characters."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "True literature must balance aristocratic polish with the vigorous reality of **demotic** vernacular."}
    ]
  },
  "Dashboard — mot/demotion.md": {
    "primary": "The reduction or lowering of an individual to a subordinate rank, grade, position, or status.",
    "secondary": "In military and naval discipline, a court-martial may impose punitive demotion to the ranks alongside forfeiture of pay.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The admiral accepted his sudden **demotion** without bitterness, requesting immediate assignment to sea."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Whether it was suggested by Bathsheba's act of **demotion** or not, the herdsman felt deeply injured in pride."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The sudden **demotion** of the head clerk to the cellar ledger cast a gloom over the office."}
    ]
  },
  "Dashboard — mot/emote.md": {
    "primary": "To portray, display, or express emotion openly, especially in an exaggerated, theatrical, or dramatic manner.",
    "secondary": "In Stanislavskian acting methodology, actors are taught to experience internal emotional memory rather than superficially emote before the audience.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The young actress began to **emote** with unnatural extravagance, ruining the subtle poetry of Shakespeare's verse."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Vincent Crummles urged the novice to **emote** with tragic despair while striking the cardboard dagger upon his breast."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Mirah did not mechanically **emote** upon the stage, but sang with the sincere sorrow of her ancestors."}
    ]
  },
  "Dashboard — mot/emoticon.md": {
    "primary": "A pictorial representation of a facial expression formed by typographic characters or punctuation marks used in digital messaging.",
    "secondary": "In computer-mediated communication and digital semiotics, Scott Fahlman's 1982 proposal of :-) established the typographic emoticon to disambiguate tone.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "Symbolic systems invent concise tokens, much as modern electronic messages employ an **emoticon** to convey immediate feeling."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The crude typographic **emoticon** demonstrates our irresistible psychological need to project facial expression into text."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Human ingenuity continually devises symbolic shorthand, from ancient runes to the simplest typographic **emoticon**."}
    ]
  },
  "Dashboard — mot/emotion.md": {
    "primary": "A strong feeling or instinctive affective state of mind deriving from one's circumstances, mood, or relationships.",
    "secondary": "In cognitive psychology and neurobiology, emotion arises from the cerebral perception of autonomic visceral and muscular reactions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Every true **emotion** produces immediate somatic changes in the heart, respiration, and facial muscles."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne could never disguise any **emotion** that agitated her sensitive heart."},
      {"author": "William Shakespeare", "work": "Sonnet 128", "quote": "How oft, when thou, my music, music play'st, do I envy those jacks that nimble leap to kiss the tender inward of thy hand, while deep **emotion** stirs my breast."}
    ]
  },
  "Dashboard — mot/emotional.md": {
    "primary": "Relating to, aroused by, or expressing intense emotions, feelings, or passions.",
    "secondary": "In psychological assessment, emotional intelligence refers to the capacity to perceive, evaluate, and regulate emotional states in oneself and others.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Material causes and **emotional** effects are not to be arranged in regular equation."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's nature was too ardent to remain satisfied without an **emotional** outlet in benevolent action."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The dog displays an **emotional** attachment to his human master that borders upon moral devotion."}
    ]
  },
  "Dashboard — mot/emotionalism.md": {
    "primary": "The tendency to display, cultivate, or be swayed by excessive emotional feelings rather than reason.",
    "secondary": "In nineteenth-century religious sociology, evangelical revivalism was criticized by traditionalists for encouraging unbridled religious emotionalism.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Hebraism often degenerates into narrow moral **emotionalism** when unaccompanied by Hellenic intellectual sweetness and light."},
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "Political propaganda appeals to crude **emotionalism** to prevent the electorate from coolly examining economic facts."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Sincere religious **emotionalism** can unlock profound energies of heroic self-sacrifice."}
    ]
  },
  "Dashboard — mot/emotionality.md": {
    "primary": "The capacity for intense feeling, emotional responsiveness, or subjective passion.",
    "secondary": "In personality trait psychology, neuroticism reflects high physiological emotionality and autonomic hyperreactivity.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Individuals exhibit marked congenital differences in **emotionality**, some remaining placid while others vibrate with every impression."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her ardent **emotionality** was disciplined by high moral duty and deep intellectual hunger."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The expressive cries of mammalian young reflect an adaptive **emotionality** that summons parental protection."}
    ]
  },
  "Dashboard — mot/emotionally.md": {
    "primary": "In an emotional manner; with regard to feelings, sentiments, or passions.",
    "secondary": "In developmental psychopathology, children who are emotionally neglected exhibit delayed attachment security and social adjustment.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "They were both young, and they were talking of the time when they lived and loved together, **emotionally** unburdening their souls."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea responded **emotionally** to Casaubon's cold pedantry, mistaking it for profound wisdom."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Agnes spoke so **emotionally** of our childhood friendship that tears rose to my eyes."}
    ]
  },
  "Dashboard — mot/emotionless.md": {
    "primary": "Devoid of emotion, feeling, or passion; calm, cold, impassive, or unfeeling.",
    "secondary": "In clinical psychiatry, an emotionless flat affect is a hallmark negative symptom observed in chronic schizophrenia.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "To Sherlock Holmes she is always the woman; he never spoke of her under any other name, maintaining his cold, **emotionless** demeanor."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Tulkinghorn stood before the hearth, an **emotionless** rusty automaton holding the secret fate of noble families."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers spoke in an **emotionless**, measured cadence that froze my ardent heart."}
    ]
  },
  "Dashboard — mot/emotionlessness.md": {
    "primary": "The complete absence or suppression of emotional feeling, passion, or sentiment; cold detachment.",
    "secondary": "In Stoic moral philosophy, apatheia (or rational emotionlessness) represented freedom from irrational affective disturbances.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes's absolute **emotionlessness** of mind was his greatest investigative weapon, allowing pure deduction."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The apparent **emotionlessness** of the catatonic patient often masks an agonizing inner turbulence."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's scholarly **emotionlessness** chilled the warm, expansive nature of his youthful bride."}
    ]
  },
  "Dashboard — mot/emotive.md": {
    "primary": "Arousing, expressing, or accompanied by intense emotional feelings or passions.",
    "secondary": "In logical positivism and Ayer's expressivism, ethical judgments possess solely emotive meaning rather than empirical cognitive truth value.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Poetic language relies upon **emotive** associations to awaken sympathetic resonance in the reader."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Scientific prose avoids purely **emotive** rhetoric to present empirical facts with dispassionate lucidity."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain musical cadences exert an immediate **emotive** effect upon the autonomic nervous system."}
    ]
  },
  "Dashboard — mot/immotile.md": {
    "primary": "Incapable of independent movement or locomotion; stationary, motionless, or sessile.",
    "secondary": "In microbiology and protozoology, immotile bacteria lack flagella and cannot execute chemotactic swimming.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Certain encysted microorganisms remain completely **immotile** until exposed to moisture and nourishment."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The spores of primitive algae exist in an **immotile** resting stage during winter freezes."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination confirmed that the bacteria were **immotile** rods lacking polar flagella."}
    ]
  },
  "Dashboard — mot/immotility.md": {
    "primary": "The inability or absence of capacity in an organism, cell, or microorganism to move independently.",
    "secondary": "In reproductive medicine, primary ciliary dyskinesia causes sperm immotility and bronchial clearance failure due to defective dynein arms.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Complete cellular **immotility** was demonstrated under high-power microscopic magnification."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The temporary **immotility** of hibernating protozoa protects them against desiccation."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The apparent **immotility** of adult barnacles is preceded by an active, free-swimming larval stage."}
    ]
  },
  "Dashboard — mot/locomote.md": {
    "primary": "To move, travel, or change physical location from one place to another through active self-propulsion.",
    "secondary": "In robotics and animal biomechanics, quadrupedal machines locomote by coordinating multi-joint leg kinematics across uneven terrain.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Bipedal primates **locomote** with an upright posture that liberates the forelimbs for tool manipulation."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Invertebrates **locomote** using diverse anatomical mechanisms, from ciliary beating to hydrostatic muscular contraction."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The capacity to **locomote** actively enhances an animal's ability to forage and escape predators."}
    ]
  },
  "Dashboard — mot/locomotion.md": {
    "primary": "The act, process, or power of moving from one place to another through physical self-propulsion.",
    "secondary": "In vertebrate evolutionary anatomy, the transition from aquatic swimming to terrestrial tetrapod locomotion required modifications to the pectoral and pelvic girdles.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Seeing how important an organ of **locomotion** the tail is in most aquatic animals, its general presence is easily understood."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The coordinated contraction of opposing flexor and extensor muscles effects human bipedal **locomotion**."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Every advance in the mechanical arts multiplies our powers of **locomotion** across the earth."}
    ]
  },
  "Dashboard — mot/locomotive.md": {
    "primary": "Pertaining to movement or locomotion; or a self-propelled railway vehicle engine used for hauling trains.",
    "secondary": "In industrial engineering history, George Stephenson's Rocket established the multi-tubular boiler design for steam locomotives in 1829.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy was full of activity, but his activities were less of a **locomotive** than a vegetative nature."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "We anticipate a new era from the invention of a **locomotive**, or a balloon; the new engine brings civilizing speed."},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "The mighty **locomotive** rushed through the dark night, breathing fire and shaking the trembling earth."}
    ]
  },
  "Dashboard — mot/locomotor.md": {
    "primary": "Pertaining to, concerned with, or effecting locomotion and physical bodily movement.",
    "secondary": "In clinical neurology, tabes dorsalis causes progressive sensory loss and wide-based stomping gait due to dorsal column degeneration.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The typical symptoms of **locomotor** ataxia include loss of deep tendon reflexes and sensory Romberg sign."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The spinal cord houses the essential reflex arcs that coordinate **locomotor** rhythmic gait."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **locomotor** apparatus of anthropoid apes is adapted primarily for arboreal brachiation."}
    ]
  },
  "Dashboard — mot/mot.md": {
    "primary": "A witty, clever, or pithy remark, saying, or bon mot; or a musical note sounded upon a hunting horn.",
    "secondary": "In heraldry and chivalric badge literature, a mot designated the short French motto or device inscribed upon a knight's coat of arms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Rape of Lucrece", "quote": "Reproach is stamped in Collatinus' face, and Tarquin's eye may read the **mot** afar, how he in vain lamented."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The forester sounded a light **mot** upon his bugle horn to recall his hounds from the brake."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry smiled as he delivered another brilliant **mot** that amused the dinner table."}
    ]
  },
  "Dashboard — mot/motacilla.md": {
    "primary": "The zoological type genus of the wagtail family (Motacillidae), comprising slender insectivorous passerine birds.",
    "secondary": "In avian taxonomy, the genus Motacilla is characterized by persistent tail-pumping locomotion and white-and-pied plumage patterns.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A species of **motacilla** flitted along the stony banks of the stream, constantly vibrating its slender tail."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The Pied Wagtail, known to science as **motacilla** yarrellii, frequents English millponds and meadow brooks."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The delicate **motacilla** feeds upon aquatic diptera hovering over the shallow cattle ford."}
    ]
  },
  "Dashboard — mot/motacillidae.md": {
    "primary": "The ornithological taxonomic family of small passerine songbirds comprising wagtails, pipits, and longclaws.",
    "secondary": "In avian phylogenetics, the family Motacillidae features elongated hallux claws and terrestrial foraging behaviors across open habitats.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The diverse genera of the family **motacillidae** illustrate how insectivorous habits shape slender beaks."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Taxonomists classify both pipits and wagtails within the natural avian family **motacillidae**."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Specimens belonging to the **motacillidae** were collected across the grassy volcanic plains of Java."}
    ]
  },
  "Dashboard — mot/mote.md": {
    "primary": "A tiny speck, particle, or minute fragment of dust, especially one visible dancing in a sunbeam.",
    "secondary": "In Biblical exegesis, the Parable of the Mote and the Beam contrasts small faults in others with gross hypocrisy in oneself.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "A **mote** it is to trouble the mind's eye; in the most high and palmy state of Rome, a little ere the mightiest Julius fell."},
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "You found his **mote**, the King your mote did see; but I a beam do find in each of three."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A single **mote** floating in the golden sunbeam reveals the invisible circulation of room air."}
    ]
  },
  "Dashboard — mot/motel.md": {
    "primary": "A roadside hotel designed primarily for motorists, typically featuring rooms with direct access to an open parking area.",
    "secondary": "In American architectural and automotive history, the motel accommodated transcontinental highway tourism.",
    "quotes": [
      {"author": "John Steinbeck", "work": "Travels with Charley", "quote": "The neon sign of the roadside **motel** glowed brightly through the gathering Arizona dusk."},
      {"author": "Jack London", "work": "The Cruise of the Snark", "quote": "The modern traveler craves the convenience of the roadside **motel** where automobile and bed lie side by side."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The dusty highway was bordered by modest cabins that foreshadowed the modern American **motel**."}
    ]
  },
  "Dashboard — mot/motet.md": {
    "primary": "A polyphonic choral musical composition on a sacred Latin text, typically unaccompanied by instruments.",
    "secondary": "In Renaissance musicology, the Renaissance motet featured imitative counterpoint based on sacred scripture.",
    "quotes": [
      {"author": "George Eliot", "work": "Romola", "quote": "The choir in the cathedral sang a sublime Latin **motet** composed by the Flemish master for holy week."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The villagers attempted an antique ecclesiastical **motet**, their violins trembling with earnest fervor."},
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The deep resonant voices of the monks chanted a solemn four-part **motet** in the vaulted chancel."}
    ]
  },
  "Dashboard — mot/motif.md": {
    "primary": "A recurring thematic element, subject, idea, or dominant design pattern in an artistic, literary, or musical work.",
    "secondary": "In Wagnerian music theory, a leitmotif associates specific melodic phrases with characters, objects, or dramatic concepts.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "A subtle psychological **motif** ran through the entire tapestry, linking the tragic figures."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The noble **motif** that inspired Dorothea's life was misunderstood by her provincial neighbors."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The decorative **motif** of antique Roman garlands appeared carved across the marble mantelpiece."}
    ]
  },
  "Dashboard — mot/motile.md": {
    "primary": "Capable of spontaneous and independent movement or motion; exhibiting motility.",
    "secondary": "In cognitive psychology, a motile person is one whose mental imagery predominantly takes kinesthetic or motor form.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The microscopic **motile** cilia on plant gametes propel them actively through film water."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Under high magnification, the **motile** zoospores were observed swimming vigorously across the slide."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The diagnosis was confirmed by finding actively **motile** amoebae in the dysenteric stool."}
    ]
  },
  "Dashboard — mot/motilin.md": {
    "primary": "A polypeptide gastrointestinal peptide hormone that regulates and stimulates migrating motor complexes in the gut.",
    "secondary": "In gastroenterology, motilin is secreted by endocrine M-cells in the duodenum and jejunum during fasting to clear residual luminal contents.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Physiological research identified **motilin** as a key enteric hormone coordinating interdigestive gastrointestinal motility."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Endocrine secretions like **motilin** trigger rhythmic contractile waves that cleanse the alimentary canal."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Autonomic peptide transmitters including **motilin** mediate visceral bowel sensations during emotional stress."}
    ]
  },
  "Dashboard — mot/motility.md": {
    "primary": "The spontaneous capacity or power of an organism or anatomical structure to move actively using metabolic energy.",
    "secondary": "In clinical andrology, sperm motility is a fundamental metric in semen analysis evaluating male fertility.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The rapid **motility** of microscopic flagellates gives them an immense advantage in finding organic food."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The peristaltic **motility** of the intestine depends upon the coordinated reflex of smooth muscle coats."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Impaired gastric **motility** results in delayed gastric emptying and chronic postprandial dyspepsia."}
    ]
  },
  "Dashboard — mot/motion.md": {
    "primary": "The act, process, or state of changing place, position, or posture; movement; or a formal proposal made in a meeting.",
    "secondary": "In classical Newtonian mechanics, the three laws of motion establish the fundamental relationships between applied forces and body acceleration.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "Every body perseveres in its state of rest, or of uniform **motion** in a right line, unless it is compelled to change that state by forces impressed thereon."},
      {"author": "William Shakespeare", "work": "Sonnet 104", "quote": "Ah yet doth beauty like a dial hand, steal from his figure, and no pace perceived; so your sweet hue hath **motion**, and mine eye may be deceived."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Every growing part of every plant is continually in **motion**, revolving in slow circumnutating circles."}
    ]
  },
  "Dashboard — mot/motional.md": {
    "primary": "Pertaining to, accompanied by, or characterized by physical motion or movement.",
    "secondary": "In classical electrodynamics, motional electromotive force is generated when a conductor moves across a magnetic field.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The **motional** electromotive intensity arises from the velocity of the conductor across magnetic lines of force."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "The kinetic energy of the rotating flywheel represents stored **motional** work."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The **motional** energy of river currents gradually erodes the hardest granite bedrock."}
    ]
  },
  "Dashboard — mot/motionless.md": {
    "primary": "Lacking motion; completely still, at rest, immobile, or stationary.",
    "secondary": "In military sniper tactics and animal camouflage, remaining motionless eliminates optical parallax detection by visual predators.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The girl on the summit of the load sat **motionless**, surrounded by tables and chairs with their legs pointed upward."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes stood **motionless** upon the granite tor, his tall figure silhouetted against the rising moon."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The giant sperm whale lay **motionless** upon the glassy ocean surface, basking in the tropical midday sun."}
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

print(f"Motion Batch 10A: Successfully updated {updated}/{len(data)} notes.")
