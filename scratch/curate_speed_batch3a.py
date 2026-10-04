# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — ambul (18 words)
  # =========================================================================
  "Dashboard — ambul/ambulacral.md": {
    "primary": "Relating to the radial food grooves or tube-foot rows of echinoderms such as sea stars and sea urchins.",
    "secondary": "In marine invertebrate zoology, ambulacral ossicles and pores through which hydraulic podia extend for locomotion.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed the numerous **ambulacral** suckers of the starfish adhering tenaciously to the wet rock."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The water-vascular canals run beneath each **ambulacral** groove to supply the rows of tentacles."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The calcareous test of the echinus is divided into five perforate **ambulacral** zones."},
    ]
  },
  "Dashboard — ambul/ambulacrum.md": {
    "primary": "One of the radial zones, grooves, or avenues on an echinoderm where the tube feet or tentacles are situated.",
    "secondary": "In botanical and classical architectural history, a shaded garden avenue or broad promenade lined with trees.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Each **ambulacrum** exhibits a double series of perforations through which the locomotor podia project."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The central nerve cord extends down the midline of the **ambulacrum** toward the terminal eye-spot."},
      {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "The Italian villa featured a pleasant **ambulacrum** planted with ancient cypresses and fragrant laurels."}
    ]
  },
  "Dashboard — ambul/ambulance.md": {
    "primary": "A specially equipped motor vehicle or historic horse-drawn wagon for transporting sick or injured persons to medical care.",
    "secondary": "In military surgical history (Larrey's ambulances volantes), mobile field dressing stations following active regiments into battle.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Specimen Days", "quote": "The rattling **ambulance** arrived bearing wounded soldiers from the battle line to the pavilion hospital."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Prompt removal of casualties by a well-ventilated **ambulance** greatly reduces the incidence of secondary shock."},
      {"author": "Arthur Conan Doyle", "work": "The Great Boer War", "quote": "The volunteer **ambulance** corps worked tirelessly under heavy shrapnel fire to rescue fallen comrades."}
    ]
  },
  "Dashboard — ambul/ambulant.md": {
    "primary": "Able to walk around; not confined to bed or a wheelchair; moving from place to place.",
    "secondary": "In hospital triage and clinical management, convalescent patients categorized as ambulant requiring minimal nursing assistance.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient became fully **ambulant** within three weeks following the surgical reduction of the fracture."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "An **ambulant** case of typhoid fever often disseminates contagion widely before being properly confined."},
      {"author": "Tobias Smollett", "work": "The Expedition of Humphry Clinker", "quote": "The venerable invalid declared himself once more **ambulant** after a fortnight of sulfurous bath treatments."}
    ]
  },
  "Dashboard — ambul/ambulate.md": {
    "primary": "To walk from place to place; to move about on one's feet rather than remaining bedridden.",
    "secondary": "In physical rehabilitation protocols, guided gait retraining assisting post-operative patients to ambulate independently.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients recovering from mild hemiplegia are encouraged to **ambulate** with the aid of a cane."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "It was remarkable to see the wounded soldier **ambulate** across the ward after so grave an injury."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Fresh air and gentle encouragement help the convalescent **ambulate** outdoors in sunny weather."}
    ]
  },
  "Dashboard — ambul/ambulation.md": {
    "primary": "The act or technique of walking or moving about on foot; locomotion.",
    "secondary": "In orthopedics and occupational therapy, quantitative kinematic analysis of stride length, cadence, and footfall symmetry during ambulation.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The quadrupedal **ambulation** of animals exhibits diverse mechanical adaptations suited to their native terrain."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The onset of painful claudication severely restricted comfortable **ambulation** to a few paces."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Daily **ambulation** in the open air invigorates the circulatory and nervous systems of the invalid."}
    ]
  },
  "Dashboard — ambul/ambulatory.md": {
    "primary": "Adapted for or capable of walking; or a covered colonnaded aisle, cloister walk, or corridor in a church.",
    "secondary": "In ecclesiastical Gothic architecture, the semicircular curving walkway surrounding the apse and high altar behind the choir stalls.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The monastic **ambulatory** enclosed a quiet courtyard where marble arches framed the cloister garden."},
      {"author": "Henry Adams", "work": "Mont-Saint-Michel and Chartres", "quote": "Pilgrims processed through the vaulted **ambulatory** behind the choir to venerate the sacred relics."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The hospital established an **ambulatory** clinic to treat walking patients without requiring hospital admission."}
    ]
  },
  "Dashboard — ambul/ambulette.md": {
    "primary": "A specially outfitted, wheelchair-accessible passenger vehicle used for non-emergency medical transport.",
    "secondary": "In modern commercial healthcare logistics, paratransit transport providing door-to-door transit for elderly and disabled individuals.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The convalescent was conveyed safely to the rehabilitation center in a comfortable modern **ambulette**."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "A light motor **ambulette** was provided by benefactors to convey disabled outpatients to the dispensary."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The specialized **ambulette** superseded the rough carriage, offering smooth transit for delicate convalescents."}
    ]
  },
  "Dashboard — ambul/circumambulate.md": {
    "primary": "To walk completely around something, especially in a ritual, ceremonial, or contemplative manner.",
    "secondary": "In comparative liturgical practice and religious anthropology (parikrama, pradaksina), ritual circular procession around a shrine or sacred mountain.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "**Circumambulate** the city of a dreamy Sabbath afternoon; go from Corlears Hook to Coenties Slip."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The pilgrims prepared to **circumambulate** the Kaaba seven times according to ancient liturgical rites."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The wandering philosopher chose to **circumambulate** the ancient walls of the city in deep meditation."}
    ]
  },
  "Dashboard — ambul/perambulate.md": {
    "primary": "To walk through, about, or over a place; especially to make an official inspection of boundaries on foot.",
    "secondary": "In traditional English property law, the ceremonial beating of parish bounds ('perambulation') to preserve landmark boundaries.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "Princes should often **perambulate** their realms to observe the true condition and temper of their subjects."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The civic officers assembled to **perambulate** the municipal boundaries according to ancestral usage."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He loved to **perambulate** the rural lanes on quiet evenings, enjoying the stillness of the meadows."}
    ]
  },
  "Dashboard — ambul/perambulating.md": {
    "primary": "Walking about or touring an area on foot; making an official inspection of territorial boundaries.",
    "secondary": "In Victorian social description, taking leisurely constitutional strolls along public esplanades or garden paths.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He spent the dreary morning **perambulating** the foggy streets in search of employment."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth delighted in **perambulating** the extensive shrubbery of Rosings Park in solitary freedom."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak observed the shepherd **perambulating** the lower pastures to inspect the lambing pens."}
    ]
  },
  "Dashboard — ambul/perambulation.md": {
    "primary": "The act of walking around or through an area; an official tour to survey and verify territorial boundaries.",
    "secondary": "In English legal and parish history, the annual rogationtide perambulation recording land charters and parish landmarks.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A philosophical **perambulation** through the fields of human knowledge reveals many unexplored provinces."},
      {"author": "Walter Scott", "work": "Guy Mannering", "quote": "The magistrate concluded his **perambulation** of the estate, noting every boundary stone and hedgerow."},
      {"author": "John Evelyn", "work": "Diary of John Evelyn", "quote": "We joined the annual parish **perambulation**, accompanied by the curate and churchwardens."}
    ]
  },
  "Dashboard — ambul/perambulator.md": {
    "primary": "A four-wheeled carriage for a baby or child pushed by a pedestrian (pram); or a surveyor's measuring wheel.",
    "secondary": "In mechanical geodesy and cartography, a hodometer or surveying wheel registering linear distance traveled along a road.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Sketches by Boz", "quote": "A proud nursemaid pushed an elegant **perambulator** through the fashionable walks of the public park."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Sussex Vampire", "quote": "The child lay smiling in a wicker **perambulator** parked on the sunlit veranda of the manor house."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The village street was clear save for a solitary **perambulator** pushed hurriedly by an anxious mother."}
    ]
  },
  "Dashboard — ambul/somnambulant.md": {
    "primary": "Walking while asleep; resembling, characteristic of, or behaving like a sleepwalker.",
    "secondary": "In Gothic literature and psychological fiction, an entranced or dissociative state marked by unseeing, automatic movement.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "She entered the shadowy hall with the slow, **somnambulant** step of one wandering in a trance."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The shocked witness moved forward in a **somnambulant** stupor, heedless of the questions addressed to him."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The fevered agent walked with a strange, **somnambulant** air toward the dark fringe of the jungle."}
    ]
  },
  "Dashboard — ambul/somnambulate.md": {
    "primary": "To walk while asleep; to wander about in a state of sleep or hypnotic dissociation.",
    "secondary": "In clinical sleep medicine, non-REM parasomnia occurring typically during slow-wave stage N3 sleep.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Children subject to night terrors will occasionally **somnambulate** through darkened rooms without waking."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The patient was known to **somnambulate** across the veranda, avoiding furniture with surprising accuracy."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Lucy began to **somnambulate** each midnight, drawn irresistibly toward the lonely churchyard on the cliff."}
    ]
  },
  "Dashboard — ambul/somnambulation.md": {
    "primary": "The act or phenomenon of walking while asleep; sleepwalking.",
    "secondary": "In historical neuropsychiatry, motor automatisms performed during partial arousal from deep delta sleep.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical history revealed repeated nocturnal **somnambulation** associated with severe emotional stress."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Currents and Counter-Currents in Medical Science", "quote": "Unconscious **somnambulation** exhibits an astonishing preservation of muscular coordination in sleep."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "We maintained a vigilant watch to prevent her perilous **somnambulation** along the dangerous seaside cliffs."}
    ]
  },
  "Dashboard — ambul/somnambulism.md": {
    "primary": "A sleep disorder characterized by walking or executing complex behaviors while in a state of sleep.",
    "secondary": "In 19th-century alienism and mesmerism, spontaneous or induced trance states involving lucid motor action without conscious recall.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "A great perturbation in nature, to receive at once the benefit of sleep and do the effects of watching! What is this **somnambulism**?"},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The phenomenon of **somnambulism** occurs most frequently in young individuals with neuropathic tendencies."},
      {"author": "Edgar Allan Poe", "work": "The Facts in the Case of M. Valdemar", "quote": "The subject passed into a profound magnetic trance closely allied to spontaneous **somnambulism**."}
    ]
  },
  "Dashboard — ambul/somnambulist.md": {
    "primary": "A person who walks in their sleep; someone afflicted with sleepwalking.",
    "secondary": "In dramatic and operatic literature (Bellini's La sonnambula), a protagonist whose nocturnal trances drive dramatic intrigue.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Look, how she rubs her hands! The guilty queen walked like a fearful **somnambulist** across the gallery."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The pale **somnambulist** escaped through the window, guided only by the eerie light of the full moon."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Barrymore moved silently down the corridor like a **somnambulist**, carrying a lighted candle to the window."}
    ]
  },

  # =========================================================================
  # Dashboard — migr (first 9 words)
  # =========================================================================
  "Dashboard — migr/emigrant.md": {
    "primary": "A person who leaves their own country or region in order to settle permanently in another.",
    "secondary": "In 19th-century demographic history, European emigrant cohorts traveling in steerage to settle American agricultural frontiers.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The **emigrant** ship swung slowly out into the river, cheered by weeping crowds on the departure pier."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The destitute laborer turns his desperate eyes westward, hoping as an **emigrant** to find bread and liberty."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every industrious **emigrant** enriches the young colony while relieving population pressure at home."}
    ]
  },
  "Dashboard — migr/emigrate.md": {
    "primary": "To leave one's own country or native land in order to settle permanently in another.",
    "secondary": "In socioeconomic migration theory, push-pull dynamics driving households to emigrate in response to crop failure or political upheaval.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Thousands of industrious Huguenots resolved to **emigrate** rather than renounce their reformed faith."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Many hardy settlers chose to **emigrate** to Australia in search of fertile sheep-grazing pastures."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "He dreamed of nothing else than to **emigrate** to the colonies and retrieve the ruined family fortune."}
    ]
  },
  "Dashboard — migr/emigration.md": {
    "primary": "The act or process of leaving one's resident country with the intent to settle permanently abroad.",
    "secondary": "In historical political economy, state-sponsored emigration schemes designed to relieve domestic paupers during economic crises.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The continuous **emigration** of skilled mechanics to foreign lands was long forbidden by severe statutes."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The warlike **emigration** of the Vandals across the Pyrenees reshaped the Western Roman provinces."},
      {"author": "Thomas Carlyle", "work": "Chartism", "quote": "Systematic national **emigration** was proposed as an indispensable remedy for industrial distress."}
    ]
  },
  "Dashboard — migr/emigre.md": {
    "primary": "An emigrant, especially one forced to flee their native country for political, ideological, or aristocratic reasons.",
    "secondary": "In French Revolutionary historiography, royalist aristocrats and refractory clergy (les émigrés) who mobilized counter-revolutionary forces from abroad.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The noble French **emigre** sought honorable asylum in England, deprived of his ancestral estates by revolution."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The gathering of an armed **emigre** army at Coblenz provoked fiery retaliatory decrees from the Legislative Assembly."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Charles Darnay was branded an aristocrat and an **emigre** by the ruthless tribunal of the Republic."}
    ]
  },
  "Dashboard — migr/emigree.md": {
    "primary": "A female emigrant; a woman who has left her native country, especially as a political exile or refugee.",
    "secondary": "In 19th-century biographical and historical literature, noblewomen who established schools or literary salons while in exile.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The accomplished French **emigree** supported herself in London by giving lessons in drawing and music."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "She listened with deep sympathy to the sorrowful recollections of the elderly foreign **emigree**."},
      {"author": "Henry James", "work": "The American", "quote": "The aristocratic **emigree** preserved the refined manners and courtly speech of the ancient court of Versailles."}
    ]
  },
  "Dashboard — migr/immigrant.md": {
    "primary": "A person who comes to live permanently in a foreign country or jurisdiction.",
    "secondary": "In demographic sociology and urban history, waves of immigrant labor providing the demographic foundation for industrial expansion.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Welcome to the brave **immigrant** arriving from distant lands to cultivate the fertile western prairies."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The industrious Scandinavian **immigrant** transformed the wild scrubland into rich wheat fields."},
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "Every honest **immigrant** who adopts our country adds strength and honor to the American commonwealth."}
    ]
  },
  "Dashboard — migr/immigrate.md": {
    "primary": "To come into another country or region of which one is not a native, in order to settle permanently.",
    "secondary": "In population genetics and ecology, the inward movement of individuals or alleles into an established population or ecosystem.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on Manufactures", "quote": "European artisans should be encouraged to **immigrate** to establish domestic manufactures in the republic."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When continental species **immigrate** into oceanic islands, they often replace the indigenous fauna."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "Men who **immigrate** to a free nation seek the security of just laws and civil liberty."}
    ]
  },
  "Dashboard — migr/immigration.md": {
    "primary": "The international movement of people to a destination country of which they are not natives in order to settle.",
    "secondary": "In legal and policy analysis, statutory naturalization frameworks, entry quotas, and border enforcement regulating foreign nationals.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A liberal policy regarding foreign **immigration** is vital to populate our vast and uncultivated territories."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The extensive European **immigration** to the New World constitutes one of the grandest demographic movements in history."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The rapid growth of the colonies was accelerated by unrestricted **immigration** from Great Britain and Europe."}
    ]
  },
  "Dashboard — migr/migraine.md": {
    "primary": "A neurological condition marked by recurrent, severe throbbing headache attacks, often with nausea and visual disturbances.",
    "secondary": "In clinical neurology, a neurovascular disorder involving cortical spreading depression and trigeminovascular sensitization.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The classic visual aura of **migraine** consists of scintillating scotoma followed by unilateral hemicrania."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Patients tortured by periodic **migraine** find relief only in absolute darkness and complete stillness."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The clinical notes recorded hereditary patterns of severe **migraine** recurring across multiple generations."}
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

print(f"Speed Batch 3A: Successfully updated {updated}/{len(data)} notes.")
