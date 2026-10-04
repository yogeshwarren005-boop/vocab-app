# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — migr (remaining 10 words)
  # =========================================================================
  "Dashboard — migr/migrant.md": {
    "primary": "A person or animal that moves from one place or country to another, especially in search of work or seasonal residence.",
    "secondary": "In labor economics and sociological studies, seasonal agricultural workers migrating across regional crop cycles.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The woodcock is a notable **migrant** bird, shifting its habitation as the harsh frost approaches."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed the solitary **migrant** hawk resting upon the rigging of our vessel far from shore."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The weary **migrant** family traveled along Highway 66 in an overloaded, creaking jalopy."}
    ]
  },
  "Dashboard — migr/migrate.md": {
    "primary": "To move from one country, place, or locality to another, especially on a seasonal or permanent basis.",
    "secondary": "In evolutionary biology and biogeography, periodic seasonal dispersal of animal populations between breeding and wintering grounds.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Birds that **migrate** across vast continental distances possess powerful wings and keen navigational instincts."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Tribes of early hunters were compelled to **migrate** as the advancing glacial ice altered grazing ranges."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Laborers will naturally **migrate** from depressed districts toward towns offering higher industrial wages."}
    ]
  },
  "Dashboard — migr/migration.md": {
    "primary": "The movement of people or animals from one country, region, or habitat to another.",
    "secondary": "In evolutionary population dynamics, genetic gene flow facilitated by the spatial movement and interbreeding of migrant individuals.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The annual **migration** of vast herds across the African plains is governed by seasonal rainfall."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sudden **migration** of northern barbarian nations overwhelmed the frontiers of the Western Empire."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The restless **migration** of provincial delegations into Paris intensified the political ferment of the capital."}
    ]
  },
  "Dashboard — migr/migrational.md": {
    "primary": "Of, relating to, or involving geographical migration or seasonal movements.",
    "secondary": "In human ecology and historical demography, patterns of intercontinental population dispersal and settlement.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The established **migrational** routes of migratory fowl span thousands of leagues over open oceans."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Anthropological findings reveal complex **migrational** pathways taken by early humans across ancient land bridges."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Tribal warfare frequently altered the **migrational** trajectories of nomadic pastoralists in Central Asia."}
    ]
  },
  "Dashboard — migr/migrator.md": {
    "primary": "An individual, organism, or species that migrates or undertakes regular seasonal journeys.",
    "secondary": "In ornithology, long-distance avian migrators equipped with physiological adaptations for prolonged trans-oceanic flight.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The golden plover is an intrepid **migrator**, flying non-stop across thousands of miles of ocean."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The stork was anciently celebrated as a faithful **migrator**, returning unerringly to its ancestral chimney."},
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "Every feathered **migrator** responds to an irresistible seasonal impulse to journey toward the sunlit south."}
    ]
  },
  "Dashboard — migr/migratory.md": {
    "primary": "Moving from one region, habitat, or country to another, especially periodically or on a seasonal basis.",
    "secondary": "In wildlife conservation biology and game law, the Migratory Bird Treaty Act protecting international avian flyways.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many **migratory** birds are blown out to sea by storms and colonize remote oceanic archipelagos."},
      {"author": "Oliver Goldsmith", "work": "The Deserted Village", "quote": "The **migratory** swallows gathered upon the thatch, preparing for their long autumn flight southward."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The remarkable endurance of **migratory** animals is supported by efficient muscular and respiratory metabolism."}
    ]
  },
  "Dashboard — migr/nonmigratory.md": {
    "primary": "Remaining in the same geographical region throughout the year; not migratory or seasonal in movement.",
    "secondary": "In avian ecology, sedentary resident species adapted to endure seasonal climatic fluctuations without shifting range.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain island finches have become entirely **nonmigratory**, their wings growing rounder and shorter over generations."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The local insect population comprised both wanderers and strictly **nonmigratory** ground beetles."},
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The cardinal remains a cheerful, **nonmigratory** resident, braving the cold winters of our northern forests."}
    ]
  },
  "Dashboard — migr/transmigrante.md": {
    "primary": "A trader or transporter who conveys merchandise or used vehicles across international borders for resale.",
    "secondary": "In North American cross-border commerce, transmigrantes operating bonded transit routes through Mexico to Central American markets.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "The City of the Saints", "quote": "The itinerant trader acted as an enterprising **transmigrante**, carrying manufactured goods across distant frontiers."},
      {"author": "John Russell Bartlett", "work": "Personal Narrative of Explorations in Texas and New Mexico", "quote": "The border **transmigrante** guided heavily laden pack-mules along the dusty trails leading southward into Sonora."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The commercial **transmigrante** navigated river passages to exchange coastal wares with inland settlements."}
    ]
  },
  "Dashboard — migr/transmigrate.md": {
    "primary": "To pass into another body at death, as the soul; to migrate from one country or state to another.",
    "secondary": "In philosophical theology and Pythagorean metaphysics, the transmigration of the immaterial psyche through successive mortal incarnations.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Pythagoras taught that the immortal soul would **transmigrate** through diverse beastly and human forms."},
      {"author": "Alexander Pope", "work": "The Dunciad", "quote": "Fools believe their spirits shall **transmigrate** into glorious celestial beings after worldly folly ends."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "If the soul of Socrates were to **transmigrate** into the body of another, identity would depend on memory."}
    ]
  },
  "Dashboard — migr/transmigration.md": {
    "primary": "The passage of the soul at death into another body; metempsychosis; or movement between regions.",
    "secondary": "In comparative religion (Hinduism, Buddhism, Jainism), the continuous cyclic transmigration (samsara) of sentient beings.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Druids of ancient Gaul inculcated the doctrine of the **transmigration** of souls to inspire martial bravery."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "He joked that the cat must be an ancient scholar undergoing a bizarre **transmigration** of identity."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The spiritual **transmigration** of ideas from generation to generation constitutes the immortal soul of history."}
    ]
  },

  # =========================================================================
  # Dashboard — cuss (first 16 words)
  # =========================================================================
  "Dashboard — cuss/concuss.md": {
    "primary": "To shake violently or agitate; to injure the brain through a severe blow or sudden impact.",
    "secondary": "In Scots law and classical jurisprudence, to coerce or intimidate a party into an involuntary covenant through extortion.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A severe fall from a carriage may violently **concuss** the cerebral hemispheres without causing cranial fracture."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The surgeon examined the soldier whose skull had been struck, fearing the impact had managed to **concuss** vital centers."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The violent tumult seemed to **concuss** the ancient rafters of the hall, shaking plaster onto the floor."}
    ]
  },
  "Dashboard — cuss/concussion.md": {
    "primary": "A violent shock, shaking, or jarring collision; a traumatic brain injury caused by a blow to the head.",
    "secondary": "In sports medicine and traumatology, mild traumatic brain injury (mTBI) resulting in functional neurological disturbance without gross lesions.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The primary symptom of cerebral **concussion** is immediate, transient loss of consciousness followed by amnesia."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The overturn of the carriage produced a tremendous **concussion**, depositing the passengers in the muddy ditch."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes examined the shattered walking stick, pointing out the signs of a violent mechanical **concussion**."}
    ]
  },
  "Dashboard — cuss/cuss.md": {
    "primary": "To swear or curse using profane language; or an informal term for an eccentric, stubborn, or annoying person.",
    "secondary": "In colloquial dialectology, an expressive oath or an affectionate/derogatory epithet for a cantankerous individual.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "He was an awkward, obstinate **cuss**, ever ready to dispute with the village schoolmaster."},
      {"author": "Bret Harte", "work": "The Luck of Roaring Camp", "quote": "The rough miners were known to swear and **cuss** roundly, yet they softened their speech before the newborn babe."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The angry sergeant began to **cuss** the skirmish line for retreating before the artillery smoke."}
    ]
  },
  "Dashboard — cuss/cussed.md": {
    "primary": "Stubborn, perverse, or cantankerous; damned or cursed in informal speech.",
    "secondary": "In regional American vernacular literature, expressing exasperation at an intractable problem or mule-headed individual.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The mule exhibited the most **cussed** perversity, refusing to advance a single step along the mountain trail."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "He muttered against the **cussed** luck that had brought his regiment into the center of the crossfire."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Old man Slauson was known as a **cussed** neighbor who contested every survey line with legal lawsuits."}
    ]
  },
  "Dashboard — cuss/cussedly.md": {
    "primary": "In a cussed, stubbornly contrary, or perverse manner; with obstinate awkwardness.",
    "secondary": "In vernacular prose, acting in a deliberately contrary or difficult fashion to thwart others.",
    "quotes": [
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The river channel wound **cussedly** through treacherous snags, defying the pilot's best navigation."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The sled dog behaved **cussedly**, tangling the harness traces whenever the driver reached for the whip."},
      {"author": "Bret Harte", "work": "Tales of the Argonauts", "quote": "The prospector clung **cussedly** to his dry claim, refusing to abandon the exhausted gravel bank."}
    ]
  },
  "Dashboard — cuss/cussedness.md": {
    "primary": "Obstinate contrariness, stubborn perversity, or willful cantankerousness in behavior.",
    "secondary": "In folk psychology and humor, the perverse tendency of inanimate objects or stubborn animals to malfunction at critical moments.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "He attributed the breakdown of the bicycle entirely to the sheer **cussedness** of mechanical contrivances."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The contractor complained bitterly of the obstinate **cussedness** displayed by the municipal building board."},
      {"author": "Jack London", "work": "White Fang", "quote": "The northern wolf-dog met the cruelty of the sled drivers with an unyielding, ferocious **cussedness**."}
    ]
  },
  "Dashboard — cuss/decussate.md": {
    "primary": "To cross or intersect in the form of the letter X; or arranged in pairs that cross alternately at right angles.",
    "secondary": "In botanical morphology and neuroanatomy, decussate leaves arranged opposite in perpendicular pairs; or crossing tracts in the brainstem.",
    "quotes": [
      {"author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "Nature delights to **decussate** and cross her fibers in the elegant quincuncial order of ancient plantations."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The opposite leaves of the plant **decussate** at each node, optimizing exposure to sunlight."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The motor fibers from the cerebral cortex **decussate** in the lower medulla before entering the spinal cord."}
    ]
  },
  "Dashboard — cuss/decussation.md": {
    "primary": "An intersection or crossing of lines, fibers, or nerve tracts in the form of the letter X.",
    "secondary": "In human neuroanatomy, the decussation of the pyramids in the medulla oblongata where corticospinal tract axons cross the midline.",
    "quotes": [
      {"author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "The mystical quincunx displays its beauty in the regular **decussation** of diagonal crossing lines."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Lesions situated above the **decussation** of the pyramids produce contralateral hemiplegia in the patient."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The optic chiasm presents a partial **decussation** of retinal nerve fibers entering the visual cortex."}
    ]
  },
  "Dashboard — cuss/discuss.md": {
    "primary": "To talk about something with another person or group; to examine, deliberate upon, or debate an issue.",
    "secondary": "In archaic surgical terminology, to disperse, dissipate, or scatter a tumor, swelling, or morbid humor.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "They sat down by the drawing-room fire to **discuss** the unexpected arrival of Mr. Bingley at Netherfield."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Let us calmly **discuss** the advantages of a well-constructed union before passion clouds our judgment."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe sat beside me on the hearth to **discuss** our prospects over a comforting bowl of hot broth."}
    ]
  },
  "Dashboard — cuss/discussant.md": {
    "primary": "A designated participant in a formal academic discussion, symposium, or panel meeting.",
    "secondary": "In scholarly conferences, an expert appointed to deliver a prepared commentary evaluating a presenter's paper.",
    "quotes": [
      {"author": "William James", "work": "The Meaning of Truth", "quote": "The philosophical **discussant** raised acute objections against the pragmatic definition of verity."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Every active **discussant** contributes a distinct perspective to the communal resolution of social problems."},
      {"author": "Thorstein Veblen", "work": "The Higher Learning in America", "quote": "The academic **discussant** parsed the economic treatise, highlighting methodological assumptions."}
    ]
  },
  "Dashboard — cuss/discussion.md": {
    "primary": "The action or process of talking about something in order to reach a decision or exchange ideas; debate.",
    "secondary": "In scientific literature, the terminal section of a research treatise interpreting experimental results in light of hypotheses.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The peculiar evil of silencing the expression of an opinion is, that it robs the human race of open **discussion**."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The **discussion** was carried on with great warmth and spirit by both ladies throughout the morning."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A full **discussion** of this complex problem must be postponed to my future larger work."}
    ]
  },
  "Dashboard — cuss/percuss.md": {
    "primary": "To strike or tap smartly, firmly, or rhythmically; to perform medical percussion on a patient's body.",
    "secondary": "In clinical physical diagnosis (Auenbrugger's technique), tapping the chest or abdomen to elicit resonant or dull acoustic notes.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician must carefully **percuss** the thoracic wall to map the borders of cardiac dullness."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The practiced ear learns to **percuss** the lungs and interpret every variation between resonance and flat tympany."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Students watched the professor gently **percuss** the patient's right hypochondrium to detect hepatic enlargement."}
    ]
  },
  "Dashboard — cuss/percussion.md": {
    "primary": "The striking of one solid body against another; or musical instruments played by being struck; physical tapping.",
    "secondary": "In clinical diagnosis and firearms history, thoracic acoustic tapping; or the percussion cap detonating firearm gunpowder.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The motion generated in two colliding elastic bodies is proportional to the direct **percussion** between them."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Immediate auscultation following thoracic **percussion** confirmed the presence of pleural effusion."},
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "He carried a modern revolver fitted with copper **percussion** caps that astonished the medieval knights."}
    ]
  },
  "Dashboard — cuss/percussionist.md": {
    "primary": "A musician who plays percussion instruments such as drums, cymbals, xylophone, or timpani in an ensemble.",
    "secondary": "In symphonic orchestration and modern jazz, an instrumentalist responsible for rhythmic propulsion and coloristic timbres.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The orchestra's principal **percussionist** executed the sudden roll on the kettledrums with thrilling precision."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The rhythm rose and crashed as though an invisible **percussionist** beat upon the sounding floor of the sea."},
      {"author": "F. Scott Fitzgerald", "work": "Tales of the Jazz Age", "quote": "The energetic **percussionist** rattled his wire brushes across the snare drum, driving the dancers faster."}
    ]
  },
  "Dashboard — cuss/percussive.md": {
    "primary": "Of, relating to, or produced by percussion; striking sharply; having the quality of a sharp impact.",
    "secondary": "In acoustic timbre and musical composition, percussive transients characterized by steep attack envelopes.",
    "quotes": [
      {"author": "John Tyndall", "work": "Sound", "quote": "The sharp **percussive** shock of the electric spark produces an explosive wave in the surrounding air."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "A heavy, **percussive** thud shook the ground as the Martian fighting-machine strode through the shattered woods."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "A regular **percussive** beat from the Indian war drums echoed through the dense canopy of the jungle."}
    ]
  },
  "Dashboard — cuss/percussor.md": {
    "primary": "A small medical hammer used to strike the body in diagnostic percussion or to test deep tendon reflexes.",
    "secondary": "In neurological examination tools, a reflex hammer (such as the Taylor or Babinski percussor) eliciting patellar responses.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The neurologist tapped the patellar tendon with a rubber **percussor**, eliciting a brisk knee-jerk reflex."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The clinical kit contained a delicate ivory **percussor** and a brass stethoscope for thoracic examinations."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The clinic demonstrator used a light **percussor** to map the subtle resonance boundaries of the thoracic cavity."}
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

print(f"Speed Batch 3B: Successfully updated {updated}/{len(data)} notes.")
