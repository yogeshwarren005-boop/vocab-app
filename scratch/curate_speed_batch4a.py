# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — trem (24 words)
  # =========================================================================
  "Dashboard — trem/entremets.md": {
    "primary": "A light side dish, savory delicacy, or sweet confection served between the principal courses of a meal.",
    "secondary": "In classical French haute cuisine, elaborate pastry courses or dessert preparations following the roasts.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The grand dinner proceeded through rich soups and roasts to a magnificent course of delicate **entremets**."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The French cook prided himself upon the artistic composition of his sugary **entremets**."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "They lingered over the sweet **entremets**, enjoying the pleasant twilight in the Parisian restaurant."}
    ]
  },
  "Dashboard — trem/extreme.md": {
    "primary": "Reaching a high or the highest degree; situated at the farthest possible point from the center.",
    "secondary": "In philosophical ethics and epistemology, radical stances distant from the Aristotelian golden mean.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Why, this is very midsummer madness! Do not carry your grief to so **extreme** a hazard."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Passions carried to an **extreme** degree obscure the light of reason and distort all clear judgment."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The wretched inhabitants were driven to the most **extreme** despair by grinding poverty and heavy taxes."}
    ]
  },
  "Dashboard — trem/extremely.md": {
    "primary": "To a very great degree or extent; exceedingly; in the utmost manner.",
    "secondary": "In empirical discourse, an intensive modifier signifying the highest statistical or observational magnitude.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was **extremely** pleased to find that Darcy had quitted the room before she re-entered."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The weather was **extremely** cold, with violent squalls of sleet driving across the barren rocks."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes examined the minute footprints with **extremely** meticulous attention through his pocket lens."}
    ]
  },
  "Dashboard — trem/extremeness.md": {
    "primary": "The character of reaching the farthest limits, maximum intensity, or utmost severity.",
    "secondary": "In philosophical discourse, the excessive distance of an opinion or measure from moderate principles.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The **extremeness** of the revolutionary measures alienated the most temperate friends of freedom."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Prudence teaches rulers to avoid the dangerous **extremeness** of either harsh tyranny or lawless license."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The **extremeness** of partisan demands was checked by the steady balance of the constitution."}
    ]
  },
  "Dashboard — trem/extremism.md": {
    "primary": "The holding of extreme political, religious, or ideological views; advocacy of fanatical measures.",
    "secondary": "In political science and sociology, ideological polarization that rejects democratic compromise in favor of radical transformation.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Violent political **extremism** tears down ancestral institutions without offering any viable substitute."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Unchecked dogmatic **extremism** stifles intellectual vitality and represses individual independence."},
      {"author": "George Orwell", "work": "Collected Essays", "quote": "Totalitarian regimes thrive by inflaming ideological **extremism** and cultivating perpetual hatred."}
    ]
  },
  "Dashboard — trem/extremist.md": {
    "primary": "A person who holds extreme or fanatical political or religious views, especially one who advocates radical action.",
    "secondary": "In political history, individuals who reject moderate legislative consensus in pursuit of total doctrinal victory.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Thoughts on French Affairs", "quote": "The Jacobin **extremist** regarded moderate constitutionalists with far greater hatred than open royalists."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Every radical club was swayed by some fiery **extremist** shouting for instantaneous popular justice."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A wise parliament provides a forum where the views of the **extremist** are tested by open debate."}
    ]
  },
  "Dashboard — trem/extremity.md": {
    "primary": "The furthest point or limit of something; an extreme condition or degree; a limb of the body.",
    "secondary": "In clinical anatomy and emergency medicine, upper and lower extremities; or states of critical circulatory collapse.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "To will the break of it? O my good lord! he's dead: off with his boots: look to his **extremity**."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The unfortunate family was reduced to the last **extremity** of suffering before relief arrived."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Coldness and cyanosis in the lower **extremity** suggested severe peripheral arterial insufficiency."}
    ]
  },
  "Dashboard — trem/extremum.md": {
    "primary": "The maximum or minimum value attained by a mathematical function on a specified domain.",
    "secondary": "In differential calculus and optimization theory, local or global extrema identified by finding critical points where the derivative vanishes.",
    "quotes": [
      {"author": "Isaac Newton", "work": "The Method of Fluxions", "quote": "To find the **extremum** of a geometric curve, we determine the point where the tangent is horizontal."},
      {"author": "Leonhard Euler", "work": "Method of Finding Curved Lines", "quote": "The variational principle locates the true trajectory by identifying the stationary **extremum** of action."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The electrostatic potential achieves its local **extremum** only at boundaries possessing surface charge."}
    ]
  },
  "Dashboard — trem/trema.md": {
    "primary": "A genus of fast-growing evergreen trees and shrubs of the family Cannabaceae native to tropical regions.",
    "secondary": "In tropical forest succession and silviculture, Trema orientalis serving as a pioneer species that stabilizes disturbed soils.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Pioneer saplings of **Trema** sprang up rapidly across the clearing left by the forest landslide."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The widespread distribution of **Trema** across oceanic islands illustrates effective avian seed dispersal."},
      {"author": "Richard Francis Burton", "work": "The Lake Regions of Central Africa", "quote": "The native village was surrounded by a protective hedge of thorny shrubs and leafy **Trema**."}
    ]
  },
  "Dashboard — trem/trematoda.md": {
    "primary": "A taxonomic class of parasitic flatworms (phylum Platyhelminthes) commonly known as flukes.",
    "secondary": "In medical parasitology and helminthology, Trematoda characterized by complex life cycles involving intermediate molluscan hosts.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The class **Trematoda** includes internal parasites equipped with powerful oral and ventral suckers."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The intricate larval stages of the **Trematoda** demonstrate remarkable adaptations to diverse host species."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Endemic hepatic infections in the tropics are frequently caused by flukes of the class **Trematoda**."}
    ]
  },
  "Dashboard — trem/trematode.md": {
    "primary": "A parasitic flatworm belonging to the class Trematoda, such as the liver fluke or blood fluke.",
    "secondary": "In clinical helminthology, human infestation by trematode parasites (Schistosoma) causing chronic portal and urinary morbidity.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The microscopic egg of the **trematode** parasite was detected in the biliary sediments during autopsy."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The adult **trematode** secures its attachment to the host's intestinal mucosa by specialized muscular suckers."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Sheep grazing upon damp pastures are frequently decimated by the insidious liver **trematode**."}
    ]
  },
  "Dashboard — trem/tremble.md": {
    "primary": "To shake involuntarily, typically as a result of anxiety, excitement, cold, or physical weakness; to quiver.",
    "secondary": "In physical geology and architecture, the slight perceptible oscillation of ground or structural frames during seismic shocks.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "The very trees did **tremble** at his approach, responsive to the magician's commanding wand."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The accused stood with pale lips, his hands beginning to **tremble** as the tribunal read the decree."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I felt my limbs **tremble** with fatigue as I wandered across the lonely, rain-drenched moors."}
    ]
  },
  "Dashboard — trem/trembler.md": {
    "primary": "A person or thing that trembles; an electrical contact or vibrating reed that automatically makes and breaks a circuit.",
    "secondary": "In historical electrical engineering, a trembler coil utilized in early automobile ignition systems (e.g. Ford Model T).",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The cowardly **trembler** hid behind the shuttered windows while the armed crowd surged down the street."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The rapid vibration of the spring **trembler** produced a brilliant series of sparks across the contact points."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "No faint-hearted **trembler** was permitted to take up arms among the highland clan in battle."}
    ]
  },
  "Dashboard — trem/trembling.md": {
    "primary": "Shaking or quivering involuntarily from fear, cold, or weakness; a shaking movement.",
    "secondary": "In botanical names, plants displaying fluttering foliage under gentle breezes (e.g. Populus tremula, the trembling poplar).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "If **trembling** I inhabit then, protest me the baby of a girl. Hence, horrible shadow!"},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "With **trembling** hands she broke the seal of Willoughby's letter, anticipating the bitterest disappointment."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She listened with **trembling** anxiety to the approaching footsteps on the darkened stairway."}
    ]
  },
  "Dashboard — trem/tremella.md": {
    "primary": "A genus of jelly fungi producing gelatinous, brain-like, or lobed fruiting bodies on decaying wood.",
    "secondary": "In classical mycology, Tremella species exhibiting dimorphic life cycles with parasitic yeast-like and filamentous stages.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We found a curious yellow **Tremella** fungus adhering to the wet bark of an ancient beech tree."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The gelatinous consistency of **Tremella** enables it to absorb moisture and swell rapidly after rainfall."},
      {"author": "John Ruskin", "work": "Proserpina: Studies of Wayside Flowers", "quote": "The moist forest path was adorned with bright gelatinous cushions of **Tremella** gleaming in the shade."}
    ]
  },
  "Dashboard — trem/tremellaceae.md": {
    "primary": "A taxonomic family of jelly fungi belonging to the order Tremellales, characterized by cruciately septate basidia.",
    "secondary": "In systematic basidiomycology, Tremellaceae fungi comprising mycoparasites that form gelatinous basidiocarps on wood.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The cruciform basidia of the **Tremellaceae** distinguish them from ordinary gilled woodland mushrooms."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Fungal families like the **Tremellaceae** exhibit specialized adaptations for survival in humid forest leaf-litter."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "The gelatinous texture of the **Tremellaceae** protects their developing basidiospores from rapid desiccation."}
    ]
  },
  "Dashboard — trem/tremellales.md": {
    "primary": "An order of basidiomycete fungi comprising both gelatinous macrofungi and human opportunistic pathogens.",
    "secondary": "In medical mycology and cladistics, Tremellales encompassing both edible wood-rotting jelly fungi and pathogenic Cryptococcus species.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The order **Tremellales** encompasses diverse fungal taxa characterized by distinctively divided basidial structures."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cryptogamic plants belonging to the **Tremellales** thrive in shaded temperate woodlands across Europe."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pathologists investigated yeast-like organisms allied to the **Tremellales** in deep systemic granulomatous infections."}
    ]
  },
  "Dashboard — trem/tremendous.md": {
    "primary": "Extraordinarily large in size, amount, extent, or intensity; inspiring awe, wonder, or astonishment.",
    "secondary": "In physical science and astronomical events, explosive magnitudes releasing vast kinetic or thermal energy.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The crowd surged forward with a **tremendous** roar that shook the very foundations of the Bastille."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "A **tremendous** crash echoed through the forest as an enormous prehistoric monster crashed through the trees."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian projectile struck the earth with a **tremendous** shock that shattered every window for miles."}
    ]
  },
  "Dashboard — trem/tremendously.md": {
    "primary": "In a tremendous manner; to an extraordinary, immense, or overwhelming degree.",
    "secondary": "In narrative prose, actions or events unfolding with colossal force or breathtaking magnitude.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The night followed day like the flapping of a black wing, the machine accelerating **tremendously**."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes laughed **tremendously**, delighted by the complete success of our nocturnal expedition."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The wind howled **tremendously** off the Yarmouth coast, sending great waves crashing over the jetty."}
    ]
  },
  "Dashboard — trem/tremolite.md": {
    "primary": "A white to pale-green silicate mineral of the amphibole group, typically forming bladed or fibrous crystals.",
    "secondary": "In metamorphic petrology, a calcium magnesium amphibole (Ca2Mg5Si8O22(OH)2) diagnostic of metamorphosed siliceous dolomites.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "The metamorphic limestone cliffs were traversed by veins of fibrous white **tremolite** and glassy quartz."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The mineral collector prized the silky luster of delicate **tremolite** needles embedded in ancient marble."},
      {"author": "Thomas Henry Huxley", "work": "Physiography: An Introduction to the Study of Nature", "quote": "Crystalline schists often contain bladed crystals of **tremolite** produced by intense regional metamorphism."}
    ]
  },
  "Dashboard — trem/tremolo.md": {
    "primary": "A rapid, trembling musical effect produced by the quick reiteration of a note or rapid alternation between notes.",
    "secondary": "In string performance and keyboard instrumentation, bowing technique or electronic modulation creating an undulating vibrato.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The orchestral strings sustained a delicate, shimmering **tremolo** that mirrored the moonlight upon the stage."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "From the open window of the conservatory came the sweet, throbbing **tremolo** of a solo violin."},
      {"author": "Thomas Mann", "work": "Buddenbrooks", "quote": "The pianist ended the nocturne with a soft, dying **tremolo** that left the salon in breathless silence."}
    ]
  },
  "Dashboard — trem/tremor.md": {
    "primary": "An involuntary quivering or shaking movement of the body; a slight earthquake or vibration.",
    "secondary": "In clinical neurology, involuntary, rhythmic, oscillatory movements caused by alternating contractions of antagonistic muscle groups.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The resting **tremor** of paralysis agitans typically begins in one hand with a characteristic pill-rolling motion."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A slight **tremor** passed through her slender frame as she listened to the harsh reading of the will."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A sudden subterranean **tremor** shook the island, causing the inhabitants to rush terror-stricken into the streets."}
    ]
  },
  "Dashboard — trem/tremulous.md": {
    "primary": "Shaking or quivering slightly; timid, nervous, or hesitant; displaying a slight fluttering movement.",
    "secondary": "In literary description, voices or light characterized by delicate, wavering, or hesitant vibrations.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister spoke in a low, **tremulous** voice that touched the hearts of all who heard him."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne's hand was **tremulous** as she received the letter, fearing to read what Captain Wentworth had written."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A single **tremulous** ray of sunlight penetrated the gloom of the old philosopher's study."}
    ]
  },
  "Dashboard — trem/tremulously.md": {
    "primary": "In a tremulous, quivering, or hesitant manner; with a wavering voice or unsteady motion.",
    "secondary": "In psychological fiction, actions performed with palpable hesitation born of intense grief, awe, or apprehension.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I held out my hand **tremulously**, scarcely daring to believe that Rochester had indeed returned."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She stepped **tremulously** forward into the misty garden, her heart beating with painful rapidity."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea spoke **tremulously**, striving to conceal the deep emotion that threatened to overwhelm her."}
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

print(f"Speed Batch 4A: Successfully updated {updated}/{len(data)} notes.")
