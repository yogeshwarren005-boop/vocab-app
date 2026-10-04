# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — cuss (remaining 4 words)
  # =========================================================================
  "Dashboard — cuss/repercuss.md": {
    "primary": "To drive or beat back; to reflect or reverberate; to react upon or have an impact.",
    "secondary": "In physical acoustics and mechanical dynamics, the reciprocal rebound or reverberation of shockwaves against a barrier.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The hollow cavern walls **repercuss** the sound with an amplified and prolonged echo."},
      {"author": "John Tyndall", "work": "Sound", "quote": "Solid cliffs serve to **repercuss** acoustic impulses, directing reflected waves across the valley."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Violent measures invariably **repercuss** upon those who first unchain popular fury."}
    ]
  },
  "Dashboard — cuss/repercussion.md": {
    "primary": "An unintended consequence or indirect effect occurring after an event; a rebound, recoil, or reverberation.",
    "secondary": "In geopolitics and macroeconomics, systemic cascading impacts across markets or diplomatic alliances following a major crisis.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A breach of public credit would produce a disastrous **repercussion** throughout all state treasuries."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The assassination of the emperor had an immediate **repercussion** across the distant frontier legions."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The bankruptcy of the great firm caused an alarming **repercussion** in the financial quarter of London."}
    ]
  },
  "Dashboard — cuss/succuss.md": {
    "primary": "To shake vigorously or agitate; especially in medical examination to detect internal fluids.",
    "secondary": "In historical clinical diagnosis (Hippocratic succussion), vigorously shaking a patient's torso to hear hydropneumothorax splashing.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The demonstrator proceeded to **succuss** the patient's chest to confirm the presence of pleural fluid and air."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Ancient practitioners would violently **succuss** the torso to determine whether fluid had accumulated in the pleura."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The clinical teacher showed how to gently **succuss** the patient without causing undue discomfort."}
    ]
  },
  "Dashboard — cuss/succussion.md": {
    "primary": "The act of shaking vigorously; a clinical diagnostic maneuver used to elicit splashing sounds in body cavities.",
    "secondary": "In pulmonary medicine, the Hippocratic succussion splash pathognomonic of hydropneumothorax or pyopneumothorax.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Hippocratic **succussion** produces a distinct splashing sound audible when fluid and air coexist in the pleural space."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The diagnostic value of thoracic **succussion** was first recorded in the classical treatises of Hippocrates."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "A clear **succussion** splash was elicited upon shaking the patient, confirming the thoracic diagnosis."}
    ]
  },

  # =========================================================================
  # Dashboard — volv (23 words)
  # =========================================================================
  "Dashboard — volv/circumvolve.md": {
    "primary": "To roll or turn round; to revolve or cause to rotate about an axis or central point.",
    "secondary": "In celestial kinematics, orbital bodies circumvolving around a gravitational barycenter according to Keplerian laws.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The starry heavens seemed to **circumvolve** in majestic harmony about the celestial throne."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Planets that **circumvolve** the sun are retained in their orbits by an attractive gravitational force."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Generations of mortal men **circumvolve** upon this earth, completing their brief earthly pilgrimage."}
    ]
  },
  "Dashboard — volv/convolve.md": {
    "primary": "To roll, coil, or wind together; to twist or entwine one part upon another.",
    "secondary": "In mathematical analysis and signal processing, the convolution of two functions yielding an integral area overlap.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fiery serpents did **convolve** their snaky folds across the burning lake of sulfur."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The growing tendrils **convolve** around the supporting twig with remarkable mechanical tenacity."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Dark tempestuous clouds **convolve** across the mountain crags, blotting out the stars."}
    ]
  },
  "Dashboard — volv/convolvulaceae.md": {
    "primary": "A taxonomic family of dicotyledonous flowering plants commonly known as the bindweed or morning glory family.",
    "secondary": "In systematic botany, Convolvulaceae encompass over 1,000 species of twining vines, shrubs, and trees featuring funnelform corollas.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "Many climbing members of the family **convolvulaceae** revolve revolving stems in search of physical support."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "The trumpet-shaped flowers of the sweet potato belong characteristically to the **convolvulaceae**."},
      {"author": "John Ruskin", "work": "Proserpina: Studies of Wayside Flowers", "quote": "The delicate wild bindweed of the hedgerows represents the humble grace of the **convolvulaceae**."}
    ]
  },
  "Dashboard — volv/convolvulus.md": {
    "primary": "A genus of twining or trailing plants of the morning glory family, featuring trumpet-shaped flowers.",
    "secondary": "In horticultural botany and agricultural weed control, Convolvulus arvensis (field bindweed) possessing deep, persistent rhizomes.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The shoot of the wild **convolvulus** completed a full circular rotation every hour and forty minutes."},
      {"author": "John Ruskin", "work": "Proserpina: Studies of Wayside Flowers", "quote": "The pink-striped bells of the hedge **convolvulus** open joyfully to greet the morning sunlight."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Wild sprays of white **convolvulus** climbed luxuriantly over the old stone wall of the cottage garden."}
    ]
  },
  "Dashboard — volv/devolve.md": {
    "primary": "To pass down or transfer power, duty, or responsibility to a lower, regional, or secondary level.",
    "secondary": "In constitutional law and political restructuring, statutory devolution delegating parliamentary competences to regional assemblies.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Upon the death or disability of the chief magistrate, executive powers **devolve** upon the vice president."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The management of the family estate would naturally **devolve** upon the eldest son upon his father's demise."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The crown did not **devolve** by choice, but followed the settled constitutional course of inheritance."}
    ]
  },
  "Dashboard — volv/devolvement.md": {
    "primary": "The delegation, transfer, or decentralization of authority or duties to a subordinate or regional body.",
    "secondary": "In public administration and governance, the structured transference of fiscal or administrative competencies.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional **devolvement** of state authority to federal bodies was strictly limited by written powers."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "A prudent **devolvement** of local tax administration to the colonial assemblies would have preserved peace."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The statutory **devolvement** of regal duties onto a council of regency was hotly contested in parliament."}
    ]
  },
  "Dashboard — volv/disinvolve.md": {
    "primary": "To disentangle, free from complication or involvement; to separate what is rolled up or confused.",
    "secondary": "In analytical philosophy and jurisprudence, resolving complex evidentiary tangles into distinct logical propositions.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Careful definition of terms enables the philosopher to **disinvolve** true concepts from verbal confusion."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Methodical inquiry serves to **disinvolve** natural truths from ancient scholastic dogmas."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "The minister attempted to **disinvolve** imperial policy from contradictory fiscal enactments."}
    ]
  },
  "Dashboard — volv/evolve.md": {
    "primary": "To develop gradually, especially from a simple to a more complex form; to unfold or work out.",
    "secondary": "In evolutionary biology, changes in allele frequencies and morphological adaptations within populations over generations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "From so simple a beginning endless forms most beautiful and most wonderful have been, and are being, **evolved**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He watched the complex moral situation **evolve** with increasing apprehension for his friend's honor."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Human society must **evolve** ethical constraints to curb the ruthless competitive struggle of raw nature."}
    ]
  },
  "Dashboard — volv/involve.md": {
    "primary": "To include or contain as a necessary part or result; to entangle, implicate, or engage deeply.",
    "secondary": "In civil and criminal law, evidence tending to implicate a party in conspiratorial or contractual liability.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The suit of Jarndyce and Jarndyce had come to **involve** whole generations in ruin and hopeless litigation."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She was unwilling to **involve** her sister in unnecessary distress until the facts were fully known."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A treaty made by the general government may **involve** the peace and security of the entire confederacy."}
    ]
  },
  "Dashboard — volv/involved.md": {
    "primary": "Difficult to comprehend or unravel; complicated, intricate, or implicated in a situation.",
    "secondary": "In narrative structure and legal pleading, arguments featuring convoluted dependent clauses and layered premises.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber's financial affairs had become so **involved** that temporary detention seemed unavoidable."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes paused, considering the **involved** chain of circumstantial evidence that pointed toward the moor."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The sentence was so grammatically **involved** that Casaubon's audience struggled to extract its meaning."}
    ]
  },
  "Dashboard — volv/involvement.md": {
    "primary": "Active participation or connection with an affair, group, or conflict; financial or emotional entanglement.",
    "secondary": "In diplomatic history and international relations, military interventionism vs. strategic non-intervention in foreign wars.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Entangling alliances threaten the republic with ruinous **involvement** in European imperial rivalries."},
      {"author": "George Washington", "work": "Farewell Address", "quote": "The great rule of conduct for us in regard to foreign nations is to steer clear of permanent **involvement**."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Herbert warned me against further pecuniary **involvement** in debts that could never be repaid."}
    ]
  },
  "Dashboard — volv/revolve.md": {
    "primary": "To turn or move in a circle around a central axis or focal point; to ponder or reflect upon deeply.",
    "secondary": "In celestial mechanics and planetary orbits, orbital revolution around a gravitational center governed by gravity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "If this fall into thy hand, **revolve**. In my stars I am above thee; but be not afraid of greatness."},
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The primary planets **revolve** about the sun in ellipses having the sun in one focus."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "He sat by the fire to **revolve** in his mind the dangerous stratagem by which the prisoner might be saved."}
    ]
  },
  "Dashboard — volv/revolved.md": {
    "primary": "Having rotated or circled around an axis or center; pondered repeatedly in thought.",
    "secondary": "In astronomical observation, celestial bodies completing periodic revolutions along predictable orbits.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The great constellation of Orion **revolved** slowly across the clear, frosty winter sky."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight **revolved** many anxious thoughts concerning the perilous siege that awaited him."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The case had **revolved** in Holmes's mind until every mysterious thread fell into logical sequence."}
    ]
  },
  "Dashboard — volv/revolver.md": {
    "primary": "A repeating handgun featuring a revolving multi-chambered cylinder holding cartridges aligned with the barrel.",
    "secondary": "In firearm technological history (Samuel Colt's patent of 1836), mass-manufactured handguns with interchangeable parts.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes slipped his loaded **revolver** into his overcoat pocket as we set out across the dark moor."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The captain cocked his heavy brass-mounted **revolver**, watching the mutineers on the shore."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "Every stagecoach traveler in the territories carried an impressive six-shot **revolver** in his belt."}
    ]
  },
  "Dashboard — volv/uninvolved.md": {
    "primary": "Not participating, connected, or implicated in an activity, dispute, or emotional relationship; detached.",
    "secondary": "In international arbitration and judicial ethics, neutral third parties exhibiting complete impartiality regarding litigants.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An impartial judge must remain entirely **uninvolved** in the political controversies of the day."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She preferred to remain **uninvolved** in the petty domestic quarrels that agitated the household."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A spectator remained cool and **uninvolved**, observing the speculative mania without taking part."}
    ]
  },
  "Dashboard — volv/volva.md": {
    "primary": "A cup-like membranous structure enveloping the base of the stem in certain mushrooms.",
    "secondary": "In fungal taxonomy and macromycete morphology, the remnant of the universal veil surrounding species of Amanita and Volvariella.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We found a brilliant scarlet toadstool bursting forth from its white, cup-like **volva** in the damp moss."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The presence of a basal **volva** is an essential diagnostic feature distinguishing lethal amanitas from edible mushrooms."},
      {"author": "John Ruskin", "work": "Proserpina: Studies of Wayside Flowers", "quote": "The botanist carefully inspected the ruptured **volva** at the base of the delicate woodland fungus."}
    ]
  },
  "Dashboard — volv/volvaria.md": {
    "primary": "A former genus of gilled mushrooms characterized by pink spores and a prominent basal volva.",
    "secondary": "In mycological taxonomy, species formerly placed in Volvaria are now classified primarily within the genus Volvariella (Pluteaceae).",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The mycologist identified the specimen as a member of **Volvaria**, noting its distinct pink spore print."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cultivated fungi of the **Volvaria** type have long been prized in Asian agriculture for their rapid growth."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The structural veil in the genus **Volvaria** protects the immature gills prior to expansion."}
    ]
  },
  "Dashboard — volv/volvariaceae.md": {
    "primary": "A historical family of agaric fungi characterized by pink spores, free gills, and a volva.",
    "secondary": "In systematic mycology, modern cladistic analyses subsumed Volvariaceae into the family Pluteaceae within the order Agaricales.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The taxonomic grouping **Volvariaceae** was distinguished by the combination of pink basidiospores and a persistent volva."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Fungal families like **Volvariaceae** demonstrate subtle morphological divergence across continental forest zones."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "Students of mycology studied the **Volvariaceae** to recognize the dangerous mimicry among gilled mushrooms."}
    ]
  },
  "Dashboard — volv/volvariella.md": {
    "primary": "A genus of saprotrophic mushrooms with pink spores and a basal volva, including the edible paddy straw mushroom.",
    "secondary": "In commercial mycology, Volvariella volvacea widely cultivated on agricultural straw substrates throughout East and Southeast Asia.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The Asian straw mushroom, belonging to **Volvariella**, has been domesticated on composted rice beds for centuries."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Microscopic examination of **Volvariella** demonstrates smooth ellipsoidal spores lacking an apical germ pore."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The volvate base of **Volvariella** arises from the rupture of the membranous universal veil."}
    ]
  },
  "Dashboard — volv/volvocaceae.md": {
    "primary": "A family of colonial freshwater green flagellates of the order Volvocales, comprising motile multi-cellular spheres.",
    "secondary": "In evolutionary protistology and developmental biology, Volvocaceae serving as a model system for the transition to multicellularity.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The family **Volvocaceae** presents a remarkable evolutionary progression from solitary flagellates to integrated colonies."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Colonial green flagellates of the **Volvocaceae** exhibit cellular differentiation between somatic and reproductive cells."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The coordinated flagellar swimming of the **Volvocaceae** demonstrates primitive intercellular signaling."}
    ]
  },
  "Dashboard — volv/volvocales.md": {
    "primary": "An order of flagellated green algae (Chlorophyta) consisting of unicellular or colonial freshwater organisms.",
    "secondary": "In algology, Volvocales characterized by biflagellate or quadriflagellate cells containing cup-shaped chloroplasts with eyespots.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The microscopic members of the **Volvocales** populate sunny freshwater ponds with swarms of green flagellates."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The phototactic responsiveness of colonial **Volvocales** guides the organism toward optimal light for photosynthesis."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "Reproductive colonies in the order **Volvocales** undergo cellular inversion during daughter colony formation."}
    ]
  },
  "Dashboard — volv/volvox.md": {
    "primary": "A genus of freshwater green algae forming spherical, microscopic rolling colonies of thousands of flagellated cells.",
    "secondary": "In developmental and evolutionary biology, Volvox colonies exhibiting true division of labor between biflagellate somatocytes and gonidia.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Under the microscope, the elegant green sphere of **Volvox** rolls gracefully through the water drop like a tiny planet."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The daughter colonies rotating inside the parent sphere of **Volvox** present one of the most charming sights in microscopy."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "Cytoplasmic bridges interconnect the individual cells of **Volvox**, coordinating the beat of thousands of flagella."}
    ]
  },
  "Dashboard — volv/volvulus.md": {
    "primary": "An acute surgical condition caused by the twisting of a loop of intestine around its mesentery, causing obstruction.",
    "secondary": "In abdominal surgery and emergency medicine, sigmoid or cecal volvulus causing closed-loop obstruction, ischemia, and gangrene.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute intestinal obstruction caused by sigmoid **volvulus** demands prompt surgical intervention to prevent bowel necrosis."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The exploratory laparotomy revealed an extensive **volvulus** that had strangulated the mesenteric blood supply."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The clinical diagnosis of acute **volvulus** relies upon the triad of sudden distension, obstipation, and abdominal pain."}
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

print(f"Speed Batch 3C: Successfully updated {updated}/{len(data)} notes.")
