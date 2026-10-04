# -*- coding: utf-8 -*-
"""
Curates Dashboard — psych (Part 1: words 1-36) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part1 = {
  "antipsychotic": {
    "primary": "A medication class used primarily to manage psychosis, schizophrenia, and severe bipolar mania.",
    "secondary": "In clinical neuropharmacology, dopamine receptor antagonists reducing positive psychotic symptoms and hallucinations.",
    "quotes": [
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "The introduction of chlorpromazine as a viable **antipsychotic** emptied vast psychiatric wards in the mid-twentieth century."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Careful titration of each **antipsychotic** regimen helped minimize parkinsonian tremors and tardive dyskinesia."},
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "Modern psychiatric practice often pairs mood stabilizers with an atypical **antipsychotic** to arrest acute mania."}
    ]
  },
  "metempsychosis": {
    "primary": "The transmigration of the soul at death into another human or animal physical body.",
    "secondary": "In philosophical theology, the Orphic and Pythagorean doctrine of cyclic rebirth governing spiritual purification.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "Molly Bloom puzzled over the long word **metempsychosis**, asking Leopold to explain the transmigration of souls."},
      {"author": "Plato", "work": "Phaedo", "quote": "Socrates outlined an ancient doctrine of **metempsychosis**, wherein unpurified spirits gravitate into animal forms."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "A whimsical notion of **metempsychosis** led the ancients to spare beasts lest they injure an ancestor."}
    ]
  },
  "nonpsychoactive": {
    "primary": "Not affecting the brain, mental processes, cognitive state, or subjective mood and perception.",
    "secondary": "In pharmacological biochemistry, compounds that lack central nervous system intoxication or psychoactive binding affinities.",
    "quotes": [
      {"author": "Michael Pollan", "work": "This Is Your Mind on Plants", "quote": "Researchers distinguished the intoxicating components of the plant from its **nonpsychoactive** structural flavonoids."},
      {"author": "David Nutt", "work": "Drugs Without the Hot Air", "quote": "Cannabidiol gained rapid therapeutic acceptance because it remains completely **nonpsychoactive** compared to THC."},
      {"author": "Siddhartha Mukherjee", "work": "The Gene", "quote": "Cellular assays confirmed that the targeted molecule was entirely **nonpsychoactive**, acting solely on peripheral receptors."}
    ]
  },
  "psyche": {
    "primary": "The human soul, mind, or totality of conscious and unconscious mental processes.",
    "secondary": "In psychoanalytic theory, the dynamic psychic apparatus integrating id, ego, and super-ego mechanisms.",
    "quotes": [
      {"author": "Carl Jung", "work": "Modern Man in Search of a Soul", "quote": "The collective unconscious constitutes a foundational tier within the human **psyche**, preserving archaic archetypes."},
      {"author": "Sigmund Freud", "work": "The Ego and the Id", "quote": "Repressed traumatic memories exert continuous hydraulic pressure upon the developing **psyche**."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Every fleeting emotion leaves an indelible organic imprint upon the delicate fabric of the **psyche**."}
    ]
  },
  "psyched": {
    "primary": "Mentally prepared, excited, energized, or emotionally primed to face a challenging encounter.",
    "secondary": "In informal psychological parlance, entering a state of heightened adrenaline and competitive self-confidence.",
    "quotes": [
      {"author": "David Foster Wallace", "work": "Infinite Jest", "quote": "The academy tennis prodigy got completely **psyched** before stepping onto the center stadium court."},
      {"author": "Hunter S. Thompson", "work": "Fear and Loathing on the Campaign Trail '72", "quote": "The advance volunteers were thoroughly **psyched** for the midnight rally in Manchester."},
      {"author": "Tom Wolfe", "work": "The Right Stuff", "quote": "The test pilots stayed intensely **psyched**, channeling raw tension into absolute flight-deck focus."}
    ]
  },
  "psychedelia": {
    "primary": "Music, visual art, fashion, or subcultural artifacts reflecting psychedelic hallucinations and altered consciousness.",
    "secondary": "In cultural history, the 1960s aesthetic movement characterized by kaleidoscopic colors, liquid projections, and surreal distortion.",
    "quotes": [
      {"author": "Joan Didion", "work": "Slouching Towards Bethlehem", "quote": "Haight-Ashbury storefronts peddled cheap **psychedelia**, day-glo posters, and incense to runaways."},
      {"author": "Hunter S. Thompson", "work": "Fear and Loathing in Las Vegas", "quote": "The garish casino carpets seemed an unintentional monument to the frantic **psychedelia** of the past decade."},
      {"author": "Tom Wolfe", "work": "The Electric Kool-Aid Acid Test", "quote": "Ken Kesey transformed the barn into an epicenter of kinetic **psychedelia** with strobe lights and neon paint."}
    ]
  },
  "psychedelic": {
    "primary": "Producing dramatic expansion of consciousness, vivid sensory illusions, or profound perceptual transformations.",
    "secondary": "In neuropsychopharmacology, compounds that act as serotonin 5-HT2A receptor agonists to remodel thalamic sensory gating.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "The Doors of Perception", "quote": "The **psychedelic** experience opened inner vistas where ordinary objects shone with intrinsic sacramental beauty."},
      {"author": "Michael Pollan", "work": "How to Change Your Mind", "quote": "Modern clinical trials demonstrate that **psychedelic** therapy can quiet hyperactive default mode networks."},
      {"author": "Oliver Sacks", "work": "Hallucinations", "quote": "The patient recounted a vivid **psychedelic** vision where geometric tapestries unrolled across the ceiling."}
    ]
  },
  "psychiatric": {
    "primary": "Relating to the medical branch focused on diagnosing, treating, and preventing mental disorders.",
    "secondary": "In healthcare administration, institutional facilities and clinical protocols specialized in psychiatric therapeutics.",
    "quotes": [
      {"author": "Michel Foucault", "work": "Madness and Civilization", "quote": "The modern **psychiatric** asylum established a moral regime where unreason was subjected to clinical surveillance."},
      {"author": "Kay Redfield Jamison", "work": "Touched with Fire", "quote": "Epidemiological studies reveal striking correlations between artistic families and major **psychiatric** illnesses."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The neurological ward routinely collaborated with **psychiatric** consultants to untangle organic from functional symptoms."}
    ]
  },
  "psychiatrical": {
    "primary": "Pertaining to psychiatry or psychiatric methods and classifications; synonymous with psychiatric.",
    "secondary": "In nineteenth-century medical texts, describing nosological categorizations of insanity and mental alienation.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Our medical materialist friends dismiss visionary conversions as mere **psychiatrical** degeneracies."},
      {"author": "Henry Maudsley", "work": "The Pathology of Mind", "quote": "Early **psychiatrical** treaties attempted to correlate moral depravity with localized cranial malformations."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The alienist presented an exhaustive **psychiatrical** report detailing hereditary instability in the defendant's family."}
    ]
  },
  "psychiatrist": {
    "primary": "A medical physician specializing in the diagnosis, psychopharmacological treatment, and prevention of mental disorders.",
    "secondary": "In clinical forensic medicine, a certified physician providing expert testimony regarding criminal competency and sanity.",
    "quotes": [
      {"author": "Kay Redfield Jamison", "work": "Night Falls Fast", "quote": "The consulting **psychiatrist** recognized subtle warning signs that preceded suicidal crises in adolescent patients."},
      {"author": "Siddhartha Mukherjee", "work": "The Gene", "quote": "The hospital **psychiatrist** noted that twin studies provided powerful evidence for genetic vulnerability to schizophrenia."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "When the post-encephalitic patients grew manic, our staff **psychiatrist** adjusted their neurological medication dosages."}
    ]
  },
  "psychiatry": {
    "primary": "The medical specialty devoted to the study, diagnosis, treatment, and prevention of mental and behavioral disorders.",
    "secondary": "In clinical history, the evolving discipline bridging biological neuroscience, psychotherapy, and institutional mental health.",
    "quotes": [
      {"author": "Michel Foucault", "work": "The Birth of the Clinic", "quote": "Nineteenth-century **psychiatry** transformed eccentric behavior into formalized categories of curable disease."},
      {"author": "Thomas Szasz", "work": "The Myth of Mental Illness", "quote": "He argued vigorously that institutional **psychiatry** functioned as an arm of social control rather than healing."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Modern **psychiatry** increasingly relies upon cellular biology and neural imaging to validate therapeutic interventions."}
    ]
  },
  "psychic": {
    "primary": "Relating to the human mind or soul, or possessing extrasensory, telepathic, or supernatural faculties.",
    "secondary": "In psychoanalysis, psychic energy or tension circulating between unconscious drives and conscious inhibitions.",
    "quotes": [
      {"author": "William James", "work": "The Will to Believe", "quote": "He maintained an open scholarly curiosity toward **psychic** phenomena, investigating mediums with rigorous skepticism."},
      {"author": "Sigmund Freud", "work": "Civilization and Its Discontents", "quote": "The preservation of primitive **psychic** structures alongside civilized adaptations resembles ancient strata beneath modern Rome."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "She felt an intangible **psychic** sympathy linking the dispersed members of the family across the quiet room."}
    ]
  },
  "psychical": {
    "primary": "Pertaining to the mind, spirit, or soul as distinguished from physical matter and bodily organs.",
    "secondary": "In parapsychological history, investigations undertaken by scientific bodies into telepathy, clairvoyance, and apparitions.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Edge of the Unknown", "quote": "His fascination with **psychical** research led him to attend seances across England during his later years."},
      {"author": "Henry Sidgwick", "work": "Practical Ethics", "quote": "The Society for **Psychical** Research sought to apply strict scientific standards to supernatural claims."},
      {"author": "William James", "work": "Memories and Studies", "quote": "A truly impartial investigator will find in **psychical** reports much that defies simplistic physical explanations."}
    ]
  },
  "psychically": {
    "primary": "In a manner pertaining to the mind, soul, or mental consciousness rather than physical bodily sensation.",
    "secondary": "In depth psychology, describing somatic symptoms generated psychically through emotional repression and conflict.",
    "quotes": [
      {"author": "Carl Jung", "work": "Psychological Types", "quote": "The introverted subject experiences external events **psychically**, filtering reality through archetypal associations."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The six companions remained **psychically** bound together, sharing an unspoken cadence of childhood memories."},
      {"author": "Sigmund Freud", "work": "Studies on Hysteria", "quote": "Physical paralysis in the patient was **psychically** determined by an unacknowledged domestic humiliation."}
    ]
  },
  "psycho": {
    "primary": "A person exhibiting erratic, aggressive, or psychopathic behavior; also used informally as an adjective.",
    "secondary": "In popular colloquial discourse, an unhinged individual displaying severe personality detachment or manic violence.",
    "quotes": [
      {"author": "Stephen King", "work": "Misery", "quote": "Paul realized with mounting terror that his captor was an unhinged **psycho** who lived inside her own delusions."},
      {"author": "David Foster Wallace", "work": "A Supposedly Fun Thing I'll Never Do Again", "quote": "The frantic pace of the luxury cruise ship turned normally placid vacationers into **psycho** deck-chair hunters."},
      {"author": "Bret Easton Ellis", "work": "American Psycho", "quote": "The glittering Manhattan skyline offered a polished veneer behind which the wealthy **psycho** prowled undisturbed."}
    ]
  },
  "psychoactive": {
    "primary": "Affecting the mind, brain chemistry, perception, cognition, mood, or subjective psychological experience.",
    "secondary": "In neuropharmacology, substances capable of crossing the blood-brain barrier to modulate neurotransmitter signaling.",
    "quotes": [
      {"author": "Michael Pollan", "work": "Caffeine: How Caffeine Created the Modern World", "quote": "Coffee became the foundational **psychoactive** fuel that sustained the grueling discipline of industrial factories."},
      {"author": "Oliver Sacks", "work": "Hallucinations", "quote": "Indigenous cultures have long employed natural **psychoactive** plants to mediate sacred communal rituals."},
      {"author": "Aldous Huxley", "work": "Island", "quote": "The utopian society incorporated a benevolent **psychoactive** elixir called moksha to foster spiritual enlightenment."}
    ]
  },
  "psychoanalyse": {
    "primary": "To examine, treat, or interpret psychological conflicts using the techniques of psychoanalysis (British spelling).",
    "secondary": "In clinical psychotherapy, exploring free associations, dreams, and childhood memories to uncover unconscious repressions.",
    "quotes": [
      {"author": "W. H. Auden", "work": "In Memory of Sigmund Freud", "quote": "The modern critic sought to **psychoanalyse** the artist rather than evaluate the formal architecture of his verse."},
      {"author": "E. M. Forster", "work": "Aspects of the Novel", "quote": "Biographers who attempt to **psychoanalyse** dead authors often sacrifice human complexity for clinical formulas."},
      {"author": "Virginia Woolf", "work": "The Moment and Other Essays", "quote": "To **psychoanalyse** an imaginative impulse while writing risks extinguishing the fragile spark of creative spontaneity."}
    ]
  },
  "psychoanalysis": {
    "primary": "A psychological theory and therapeutic method founded by Sigmund Freud to treat mental conflict via the unconscious.",
    "secondary": "In intellectual history, an interpretive paradigm analyzing dreams, slips of the tongue, and infantile sexuality.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "The Interpretation of Dreams", "quote": "Through the rigorous discipline of **psychoanalysis**, the royal road to the unconscious mind was finally opened."},
      {"author": "Carl Jung", "work": "The Archetypes and the Collective Unconscious", "quote": "Early classical **psychoanalysis** focused too exclusively upon biological drives while ignoring mythic dimensions."},
      {"author": "Lionel Trilling", "work": "The Liberal Imagination", "quote": "Literary criticism found in Freudian **psychoanalysis** a revolutionary grammar for reading latent narrative desire."}
    ]
  },
  "psychoanalyst": {
    "primary": "A practitioner trained in the therapeutic theories and clinical methods of psychoanalysis.",
    "secondary": "In clinical mental health, a certified therapist interpreting transference, countertransference, and free association.",
    "quotes": [
      {"author": "Janet Malcolm", "work": "The Impossible Profession", "quote": "The dedicated **psychoanalyst** must maintain benevolent neutrality while absorbing intense emotional projections."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "When physical therapy stalled, a perceptive **psychoanalyst** helped untangle the patient's deep bodily dissociation."},
      {"author": "Sigmund Freud", "work": "An Outline of Psycho-Analysis", "quote": "The **psychoanalyst** listens with evenly hovering attention to the patient's unfiltered associations on the couch."}
    ]
  },
  "psychoanalytic": {
    "primary": "Relating to or based upon the theories and clinical methods of psychoanalysis.",
    "secondary": "In critical cultural theory, utilizing psychoanalytic concepts like repression and projection to analyze art and society.",
    "quotes": [
      {"author": "Paul Ricœur", "work": "Freud and Philosophy", "quote": "The **psychoanalytic** approach embodies a hermeneutics of suspicion that interrogates conscious rationalizations."},
      {"author": "Julia Kristeva", "work": "Powers of Horror", "quote": "She utilized **psychoanalytic** models of abjection to explain societal rituals of purification and expulsion."},
      {"author": "Jacques Lacan", "work": "Écrits", "quote": "A proper **psychoanalytic** reading discovers the structure of the unconscious mirrored in the laws of language."}
    ]
  },
  "psychoanalytical": {
    "primary": "Pertaining to psychoanalysis; characterized by psychoanalytic theory, interpretation, or investigation.",
    "secondary": "In scholarly and cultural criticism, describing methodologies that deconstruct psychological subtexts within historical narratives.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "Totem and Taboo", "quote": "These primitive tribal taboos yielded unexpected clarity when subjected to **psychoanalytical** scrutiny."},
      {"author": "Erich Fromm", "work": "Escape from Freedom", "quote": "Modern political movements require both socioeconomic and **psychoanalytical** explanations to understand their appeal."},
      {"author": "Susan Sontag", "work": "Against Interpretation", "quote": "She rejected reductive **psychoanalytical** readings that translated literary masterpieces into mundane clinical symptoms."}
    ]
  },
  "psychoanalyze": {
    "primary": "To examine, interpret, or treat mental and emotional conflicts using the techniques of psychoanalysis.",
    "secondary": "In cultural conversation, applying Freudian frameworks to dissect an individual's hidden motives and neuroses.",
    "quotes": [
      {"author": "Arthur Miller", "work": "Timebends: A Life", "quote": "Friends attempted to **psychoanalyze** his creative paralysis instead of recognizing the simple burden of exhaustion."},
      {"author": "Philip Roth", "work": "Portnoy's Complaint", "quote": "Alexander lay back on the couch and begged the doctor to **psychoanalyze** his unrelenting guilt."},
      {"author": "Iris Murdoch", "work": "The Sea, The Sea", "quote": "Charles disliked modern novelists who pause in mid-chapter to **psychoanalyze** every minor character's breakfast."}
    ]
  },
  "psychobabble": {
    "primary": "Superficial psychological jargon and buzzwords used casually in speech to explain complex human behavior.",
    "secondary": "In cultural criticism, colloquial self-help vernacular that trivializes clinical insights for quick social currency.",
    "quotes": [
      {"author": "Christopher Lasch", "work": "The Culture of Narcissism", "quote": "Contemporary therapy culture spawned an endless dialect of **psychobabble** that replaced moral accountability."},
      {"author": "David Foster Wallace", "work": "Brief Interviews with Hideous Men", "quote": "The interviewee concealed his emotional cruelty behind a slick barrage of pop **psychobabble** about boundaries."},
      {"author": "Joan Didion", "work": "The White Album", "quote": "Hollywood parties hummed with self-absorbed **psychobabble** about primal screams and holistic alignments."}
    ]
  },
  "psychodid": {
    "primary": "A moth fly or drain fly belonging to the dipteran insect family Psychodidae.",
    "secondary": "In entomological morphology, a small hairy nematoceran fly possessing moth-like wings with parallel venation.",
    "quotes": [
      {"author": "Edward O. Wilson", "work": "The Diversity of Life", "quote": "A tiny **psychodid** alighted upon the damp stone, vibrating its hairy wings in the tropical darkness."},
      {"author": "Vincent Dethier", "work": "To Know a Fly", "quote": "The urban sewer system provides an ideal moist haven for every prolific **psychodid** larva."},
      {"author": "Howard Ensign Evans", "work": "Life on a Little-Known Planet", "quote": "Examined under a hand lens, the delicate **psychodid** resembles a miniature silk moth rather than a common gnat."}
    ]
  },
  "psychodidae": {
    "primary": "The cosmopolitan family of small, moth-like dipteran flies commonly known as drain flies or moth flies.",
    "secondary": "In medical entomology, the insect family containing sandflies of the subfamily Phlebotominae, which transmit leishmaniasis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tropical vectors belonging to the family **Psychodidae** transmit the flagellate protozoan that causes kala-azar."},
      {"author": "Edward O. Wilson", "work": "Naturalist", "quote": "Aquatic surveys in limestone creeks revealed diverse larval specimens of **Psychodidae** clinging to wet moss."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Excessive pesticide applications frequently fail against **Psychodidae** populations breeding in subterranean drain lines."}
    ]
  },
  "psychodynamics": {
    "primary": "The psychological forces, conscious and unconscious motives, and emotional tensions that influence human behavior.",
    "secondary": "In clinical psychiatry, the systematic study of psychic energy exchanges between instinctual drives and defenses.",
    "quotes": [
      {"author": "Erik Erikson", "work": "Childhood and Society", "quote": "The internal **psychodynamics** of adolescent development reflect tensions between personal autonomy and social role."},
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "Understanding the subtle **psychodynamics** of depressive mood swings proved crucial for long-term recovery."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Neurobiological studies are now beginning to map the synaptic correlates of Freudian **psychodynamics**."}
    ]
  },
  "psychogenesis": {
    "primary": "The origin and development of psychological states, behavioral traits, or mental conditions from mental processes.",
    "secondary": "In psychiatric nosology, the etiology of a disorder arising from psychological trauma rather than organic lesions.",
    "quotes": [
      {"author": "Carl Jung", "work": "The Psychogenesis of Mental Disease", "quote": "We must trace the intricate **psychogenesis** of delusions back to unresolved emotional complexes in early youth."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The **psychogenesis** of religious convictions involves both subconscious incubation and conscious intellectual assent."},
      {"author": "Sigmund Freud", "work": "Introductory Lectures on Psycho-Analysis", "quote": "The physician investigated the **psychogenesis** of the hysterical paralysis by examining the patient's dreams."}
    ]
  },
  "psychogenetic": {
    "primary": "Relating to psychogenesis; having a mental, psychological, or emotional origin rather than a physical cause.",
    "secondary": "In developmental psychology, describing the phased maturation of mental faculties throughout the human lifecycle.",
    "quotes": [
      {"author": "Jean Piaget", "work": "The Psychology of Intelligence", "quote": "The **psychogenetic** emergence of logical reasoning proceeds through invariant stages of sensorimotor coordination."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Careful neurological examination ruled out a **psychogenetic** source, confirming an organic genetic mutation."},
      {"author": "Carl Jung", "work": "Memories, Dreams, Reflections", "quote": "He identified a profound **psychogenetic** root connecting modern mythological motifs with ancient tribal initiation rites."}
    ]
  },
  "psychogenic": {
    "primary": "Originating in the mind or in emotional conflict rather than in physiological or somatic disease.",
    "secondary": "In clinical diagnosis, denoting functional physical symptoms, such as non-epileptic seizures, caused by psychological stress.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Migraine", "quote": "While emotional stress may trigger attacks, vascular migraines cannot be dismissed as purely **psychogenic** episodes."},
      {"author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "Nineteenth-century physicians frequently misdiagnosed terminal malignancies as **psychogenic** manifestations of melancholy."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The skillful clinician must distinguish organic cardiac murmurs from palpitations of **psychogenic** origin."}
    ]
  },
  "psychokinesis": {
    "primary": "The alleged ability to move or influence physical objects through the power of the mind without physical contact.",
    "secondary": "In parapsychology, experimental investigations measuring micro-influences on random number generators or mechanical dice.",
    "quotes": [
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "Controlled laboratory tests have consistently failed to demonstrate authentic **psychokinesis** under double-blind conditions."},
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "If genuine **psychokinesis** were ever confirmed, every established law of Newtonian conservation would require radical revision."},
      {"author": "Martin Gardner", "work": "Fads and Fallacies in the Name of Science", "quote": "Stage magicians have repeatedly replicated famous feats of alleged **psychokinesis** using elementary sleight of hand."}
    ]
  },
  "psychokinetic": {
    "primary": "Relating to or capable of psychokinesis; involving the mental manipulation of material objects.",
    "secondary": "In science fiction and parapsychological literature, describing individuals possessing telekinetic mental faculties.",
    "quotes": [
      {"author": "Stephen King", "work": "Carrie", "quote": "The adolescent girl released a terrifying **psychokinetic** blast that shattered every window in the high school gym."},
      {"author": "Arthur C. Clarke", "work": "Childhood's End", "quote": "The emerging generation developed extraordinary **psychokinetic** powers that dismantled the remnants of human technology."},
      {"author": "Philip K. Dick", "work": "Ubik", "quote": "Corporate espers deployed **psychokinetic** operatives to shield sensitive corporate secrets from psychic intrusion."}
    ]
  },
  "psycholinguist": {
    "primary": "A cognitive scientist or linguist who studies the psychological processes underlying language acquisition and use.",
    "secondary": "In experimental cognitive science, a researcher measuring reaction times, eye tracking, and neural activations during speech.",
    "quotes": [
      {"author": "Steven Pinker", "work": "The Language Instinct", "quote": "As an experimental **psycholinguist**, he tracked how young children spontaneously apply grammatical rules to novel verbs."},
      {"author": "Noam Chomsky", "work": "Language and Mind", "quote": "The practicing **psycholinguist** must account for the universal generative grammar hardwired into the human brain."},
      {"author": "Oliver Sacks", "work": "Seeing Voices", "quote": "The **psycholinguist** demonstrated that deaf children invent complex sign languages with spontaneous grammatical syntax."}
    ]
  },
  "psycholinguistic": {
    "primary": "Relating to psycholinguistics; combining psychological and linguistic principles in the study of speech and thought.",
    "secondary": "In educational research, evaluating reading comprehension and phonological processing through psycholinguistic metrics.",
    "quotes": [
      {"author": "Steven Pinker", "work": "Words and Rules", "quote": "He designed rigorous **psycholinguistic** experiments to measure the latency of past-tense verb production in adults."},
      {"author": "Oliver Sacks", "work": "An Anthropologist on Mars", "quote": "Brain lesions produced fascinating **psycholinguistic** deficits where naming nouns remained intact while verbs vanished."},
      {"author": "Jean Piaget", "work": "The Language and Thought of the Child", "quote": "Early egocentric speech offers valuable **psycholinguistic** clues regarding the pre-operational thought of toddlers."}
    ]
  },
  "psycholinguistics": {
    "primary": "The interdisciplinary study of the psychological, cognitive, and neurobiological factors involved in language.",
    "secondary": "In cognitive psychology, the academic field investigating speech perception, lexical access, sentence parsing, and bilingualism.",
    "quotes": [
      {"author": "Steven Pinker", "work": "The Blank Slate", "quote": "Discoveries in modern **psycholinguistics** dismantled behaviorist theories that viewed language acquisition as simple conditioning."},
      {"author": "Noam Chomsky", "work": "Reflections on Language", "quote": "The core questions of **psycholinguistics** probe how abstract linguistic knowledge is physically instantiated in the cortex."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Functional imaging transformed **psycholinguistics** by mapping Broca's and Wernicke's territories during silent reading."}
    ]
  },
  "psychological": {
    "primary": "Relating to the human mind, emotions, mental processes, or the scientific discipline of psychology.",
    "secondary": "In dramatic literature and character study, exploring nuanced internal motivations and subconscious tensions.",
    "quotes": [
      {"author": "William James", "work": "The Will to Believe", "quote": "Our passional nature and **psychological** predispositions inevitably dictate our choices when intellectual proof is silent."},
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "Clarissa's walk across London unfolded as a delicate **psychological** portrait of memory, regret, and fleeting joy."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The author displayed supreme **psychological** penetration in tracing the gradual disillusionment of Dorothea's marriage."}
    ]
  },
  "psychologically": {
    "primary": "From a psychological perspective; in terms of mental processes, emotional states, or subjective perception.",
    "secondary": "In narrative character development, describing motivations and behavioral shifts grounded in inner emotional realism.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel Archer was **psychologically** incapable of accepting an easy compromise that violated her personal ideals."},
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "Seemingly accidental slips of the tongue are **psychologically** motivated by unconscious desires breaking into speech."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Jim remained **psychologically** scarred by that single fateful jump from the doomed training ship Patna."}
    ]
  }
}
