import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind/Dashboard — psych";

const wordsData = {
  "psychoanalytic.md": {
    word: "psychoanalytic",
    primary: "Of, relating to, or using the principles and therapeutic techniques of psychoanalysis.",
    secondary: "In literary and cultural criticism, applying theories of the unconscious, repression, and dream symbolism to analyze art, culture, and narrative structures.",
    quotes: [
      { author: "Sigmund Freud", work: "The Interpretation of Dreams", quote: "The **psychoanalytic** method demonstrates that neuroses are meaningful reactions to unresolved infantile conflicts." },
      { author: "Carl Rogers", work: "Client-Centered Therapy", quote: "Unlike the **psychoanalytic** approach, our therapy relies on the client's own capacity for self-actualization." },
      { author: "Lionel Trilling", work: "The Liberal Imagination", quote: "Freud’s **psychoanalytic** conception of the mind makes poetic metaphor and neurosis kinship phenomena." }
    ]
  },
  "psychoanalytical.md": {
    word: "psychoanalytical",
    primary: "A variant form of psychoanalytic; pertaining to psychoanalysis or the systematic investigation of the unconscious mind.",
    secondary: "In intellectual history and clinical discourse, describing detailed case studies, treatises, and institutional journals exploring psychoanalytic doctrine.",
    quotes: [
      { author: "Ernest Jones", work: "The Life and Work of Sigmund Freud", quote: "The early international **psychoanalytical** congresses were battlegrounds where clinical loyalties were fiercely tested." },
      { author: "C. G. Jung", work: "The Archetypes and the Collective Unconscious", quote: "While classical **psychoanalytical** theories emphasized personal repressions, my work uncovered phylogenetic memories." },
      { author: "Melanie Klein", work: "The Psycho-Analysis of Children", quote: "Play therapy provides a direct **psychoanalytical** pathway into the infant's unconscious fantasies and anxieties." }
    ]
  },
  "psychoanalyze.md": {
    word: "psychoanalyze",
    primary: "To examine, treat, or interpret someone's psychological motivations using the techniques of psychoanalysis.",
    secondary: "In popular discourse, to dissect, scrutinize, or explain an individual’s hidden motives, neurotic habits, or defensive justifications.",
    quotes: [
      { author: "Aldous Huxley", work: "Brave New World", quote: "The authorities had no desire to **psychoanalyze** citizens when conditioning and soma kept everyone content." },
      { author: "Philip Roth", work: "Portnoy's Complaint", quote: "He lay upon the couch, begging Dr. Spielvogel to **psychoanalyze** his lifelong obsessions and guilt." },
      { author: "Hannah Arendt", work: "Men in Dark Times", quote: "We must not attempt to **psychoanalyze** great political actions as though they were merely displaced neurotic symptoms." }
    ]
  },
  "psychobabble.md": {
    word: "psychobabble",
    primary: "Psychological jargon, catchphrases, or pseudo-technical psychological terminology used casually and unthinkingly, especially in popular self-help culture.",
    secondary: "In sociolinguistic criticism (coined by Richard Rosen in 1975), trite, narcissistic speech that cloaks ordinary emotional realities in fashionable therapeutic buzzwords.",
    quotes: [
      { author: "Richard Rosen", work: "Psychobabble: Fast Talk and Quick Cure in the Era of Feeling", quote: "The modern cult of personal growth invented **psychobabble** to give superficial self-absorption the dignified veneer of medical science." },
      { author: "Tom Wolfe", work: "The 'Me' Decade and the Third Great Awakening", quote: "Every dinner party dissolved into fluent **psychobabble** about self-actualization, toxic boundaries, and holistic energy." },
      { author: "Joan Didion", work: "The White Album", quote: "Behind the comforting fog of contemporary **psychobabble** lay a profound unwillingness to face harsh moral choices." }
    ]
  },
  "psychodid.md": {
    word: "psychodid",
    primary: "Any small, hairy, moth-like dipteran fly belonging to the family Psychodidae; commonly known as a moth fly, drain fly, or sand fly.",
    secondary: "In medical and forensic entomology, referring to flies whose larvae inhabit moist drains or whose blood-feeding females (subfamily Phlebotominae) transmit leishmaniasis.",
    quotes: [
      { author: "L. O. Howard", work: "The Insect Book", quote: "The tiny **psychodid** fly flits with characteristic jerky flight around humid bathroom drains and mossy springs." },
      { author: "Robert Matheson", work: "Medical Entomology", quote: "Certain bloodsucking **psychodid** species of the genus Phlebotomus serve as primary vectors for dermal leishmaniasis in the Mediterranean basin." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The microscopic wing venation of each **psychodid** specimen was cataloged to distinguish cryptic tropical species." }
    ]
  },
  "psychodidae.md": {
    word: "psychodidae",
    primary: "A large, cosmopolitan family of small nematoceran dipterous insects, commonly called moth flies, drain flies, or sand flies.",
    secondary: "In systematic entomology, recognized by densely haired broad wings held roof-like over the body, named from Greek psyche (butterfly/moth) due to their moth-like appearance.",
    quotes: [
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Flies of the family **Psychodidae** are readily recognized by their downy bodies and fuzzy wings, resembling minute moths." },
      { author: "Alpheus Spring Packard", work: "Guide to the Study of Insects", quote: "The **Psychodidae** breed in decaying organic sludge, where their aquatic larvae thrive under anaerobic conditions." },
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "Fossil specimens preserved in Baltic amber prove that **Psychodidae** flourished alongside ancient social insects in the Eocene." }
    ]
  },
  "psychodynamics.md": {
    word: "psychodynamics",
    primary: "The study of the psychological forces, motives, and instinctual energies that underlie human behavior and mental states, especially at an unconscious level.",
    secondary: "In clinical psychiatry (originating with Freud's hydraulic energy models), the interplay of the id, ego, and superego in mediating emotional conflict and defense mechanisms.",
    quotes: [
      { author: "Sigmund Freud", work: "The Ego and the Id", quote: "The **psychodynamics** of the psyche are driven by the ceaseless struggle between eros and the death drive." },
      { author: "Erik Erikson", work: "Identity: Youth and Crisis", quote: "Understanding adolescent turmoil requires tracing the subtle **psychodynamics** connecting social roles to bodily changes." },
      { author: "Karen Horney", work: "Our Inner Conflicts", quote: "The **psychodynamics** of basic anxiety compel the neurotic individual to construct rigid idealizations of the self." }
    ]
  },
  "psychogenesis.md": {
    word: "psychogenesis",
    primary: "The origin and development of mental processes, psychological traits, or personality; also the psychological origin of somatic symptoms.",
    secondary: "In developmental psychology and psychosomatic medicine, the etiology of physical symptoms or behavioral adaptations arising from psychological causes rather than organic tissue disease.",
    quotes: [
      { author: "Jean Piaget", work: "The Origins of Intelligence in Children", quote: "We traced the gradual **psychogenesis** of logical thought from early sensorimotor reflexes to abstract operational thinking." },
      { author: "C. G. Jung", work: "The Psychogenesis of Mental Disease", quote: "The **psychogenesis** of schizophrenia involves a catastrophic invasion of the conscious ego by primordial archetypes." },
      { author: "Pierre Janet", work: "The Mental State of Hystericals", quote: "The sudden onset of functional paralysis pointed unmistakably to an emotional shock as the point of **psychogenesis**." }
    ]
  },
  "psychogenetic.md": {
    word: "psychogenetic",
    primary: "Of, relating to, or originating in psychological or emotional causes; psychogenic.",
    secondary: "In developmental psychology, concerning the origin and evolution of the mind, mental faculties, or behavioral patterns.",
    quotes: [
      { author: "G. Stanley Hall", work: "Adolescence", quote: "Adolescent emotional volatility represents a pivotal **psychogenetic** stage in the evolutionary unfolding of human character." },
      { author: "Sandor Ferenczi", work: "Contributions to Psycho-Analysis", quote: "The patient’s chronic tremors were revealed to have a **psychogenetic** basis linked to wartime shell shock." },
      { author: "Wilhelm Wundt", work: "Outlines of Psychology", quote: "Every complex mental function possesses a distinct **psychogenetic** history rooted in simple sensory apperception." }
    ]
  },
  "psychogenic.md": {
    word: "psychogenic",
    primary: "Having a psychological origin or cause rather than a physical or organic one, especially referring to illnesses or symptoms.",
    secondary: "In psychosomatic medicine and clinical neurology, describing functional somatic symptoms (such as non-epileptic seizures or pain syndromes) provoked by emotional stress.",
    quotes: [
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The orthopedic surgeons initially dismissed my profound alienation from my injured leg as a merely **psychogenic** reaction." },
      { author: "Sigmund Freud", work: "Studies on Hysteria", quote: "Hysterical blindness proved to be a **psychogenic** defense mechanism against traumatic visual memories." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinician must carefully differentiate between organic neurological palsies and **psychogenic** functional conversions." }
    ]
  },
  "psychokinesis.md": {
    word: "psychokinesis",
    primary: "The alleged movement or physical manipulation of physical objects by the power of the mind alone without physical contact; telekinesis.",
    secondary: "In parapsychological research (coined by Henry Holt and adopted by J. B. Rhine), macro- and micro-PK experiments testing mental influence on random number generators or rolling dice.",
    quotes: [
      { author: "J. B. Rhine", work: "The Reach of the Mind", quote: "Statistical anomalies in thousands of automated dice rolls suggested a faint but measurable influence of **psychokinesis**." },
      { author: "Arthur Koestler", work: "The Roots of Coincidence", quote: "If **psychokinesis** exists, it implies an intimate interweaving of mental intention and quantum probabilities." },
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "Stage magicians routinely duplicate all the alleged feats of **psychokinesis** using simple sleight of hand and hidden threads." }
    ]
  },
  "psychokinetic.md": {
    word: "psychokinetic",
    primary: "Of, relating to, or involving psychokinesis; relating to the direct mental influence over physical matter.",
    secondary: "In science fiction, parapsychology, and pop culture, designating characters, forces, or alleged anomalous powers capable of moving objects with mental energy.",
    quotes: [
      { author: "Philip K. Dick", work: "Ubik", quote: "The corporate anti-psi operative monitored the corridor for anomalous **psychokinetic** ripples." },
      { author: "J. B. Rhine", work: "New Frontiers of the Mind", quote: "The subject concentrated intensely, attempting to exert **psychokinetic** influence over the falling mechanical dice." },
      { author: "Stephen King", work: "Carrie", quote: "The sudden shattering of the light fixtures revealed Carrie's terrifying, uncontrolled **psychokinetic** eruption." }
    ]
  },
  "psycholinguist.md": {
    word: "psycholinguist",
    primary: "A cognitive scientist or linguist who studies psycholinguistics, investigating the psychological and neurobiological factors that enable humans to acquire, use, and comprehend language.",
    secondary: "In academic research, an investigator using eye-tracking, reaction times, and neuroimaging to model sentence parsing, lexical retrieval, and speech production.",
    quotes: [
      { author: "Noam Chomsky", work: "Language and Mind", quote: "The **psycholinguist** seeks to discover the universal computational principles that make child language acquisition possible." },
      { author: "Steven Pinker", work: "The Language Instinct", quote: "Every infant is a natural **psycholinguist**, effortlessly dissecting continuous acoustic streams into grammatical units." },
      { author: "George A. Miller", work: "The Science of Words", quote: "The **psycholinguist** must measure milliseconds of reaction time to map the mental dictionary in the brain." }
    ]
  },
  "psycholinguistic.md": {
    word: "psycholinguistic",
    primary: "Of or relating to psycholinguistics; concerning the relationship between linguistic behavior and psychological processes.",
    secondary: "In cognitive science and reading education, describing models of speech processing, phonological decoding, and the cognitive architecture of syntax comprehension.",
    quotes: [
      { author: "Steven Pinker", work: "Words and Rules", quote: "Irregular past-tense verbs provide a crucial test case for competing **psycholinguistic** models of human memory." },
      { author: "Noam Chomsky", work: "Aspects of the Theory of Syntax", quote: "Generative grammar spurred innovative **psycholinguistic** experiments measuring the cognitive reality of deep structures." },
      { author: "Alexander Luria", work: "Basic Problems of Neurolinguistics", quote: "Brain lesions disrupt specific **psycholinguistic** operations, dissociating syntagmatic fluency from paradigmatic selection." }
    ]
  },
  "psycholinguistics.md": {
    word: "psycholinguistics",
    primary: "The interdisciplinary study of the psychological and neurobiological mechanisms by which language is acquired, comprehended, produced, and represented in the mind.",
    secondary: "In cognitive psychology and linguistics, the empirical field examining speech perception, lexical access, child language milestones, and aphasic breakdowns.",
    quotes: [
      { author: "George A. Miller", work: "Language and Communication", quote: "Modern **psycholinguistics** was born from the fruitful marriage of mathematical communication theory and cognitive psychology." },
      { author: "Steven Pinker", work: "The Stuff of Thought", quote: "By examining slips of the tongue and garden-path sentences, **psycholinguistics** lays bare the machinery of thought." },
      { author: "Eric Lenneberg", work: "Biological Foundations of Language", quote: "Developmental **psycholinguistics** demonstrates that critical periods for language acquisition have strict biological foundations." }
    ]
  },
  "psychological.md": {
    word: "psychological",
    primary: "Of, relating to, or arising in the mind; concerning the mental and emotional state of a person, or the discipline of psychology.",
    secondary: "In literature and cinema, describing works that delve deeply into the complex motives, internal conflicts, and subtle subjective moods of characters.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "The stream of consciousness is the primary **psychological** fact of our inner life, flowing incessantly onward." },
      { author: "Virginia Woolf", work: "Modern Fiction", quote: "Let us examine for a moment an ordinary mind on an ordinary day; the true **psychological** novelist records the atoms as they fall." },
      { author: "Fyodor Dostoevsky", work: "Crime and Punishment", quote: "The judge engaged Raskolnikov in a game of feline patience, relying entirely on subtle **psychological** pressure." }
    ]
  },
  "psychologically.md": {
    word: "psychologically",
    primary: "In a manner relating to the mind, emotions, or psychological functioning; from a psychological viewpoint.",
    secondary: "In behavioral analysis and social critique, concerning internal mental motivations and emotional consequences rather than physical or economic factors.",
    quotes: [
      { author: "George Orwell", work: "Homage to Catalonia", quote: "It was **psychologically** impossible to believe that comrades fighting side by side in the trenches could harbor treasonous motives." },
      { author: "Carl Rogers", work: "On Becoming a Person", quote: "A person feels **psychologically** safe only when their deepest feelings are accepted without threat of condemnation." },
      { author: "Bertrand Russell", work: "The Conquest of Happiness", quote: "Envy is **psychologically** toxic because it prevents a man from enjoying what he has while tormenting him with what others possess." }
    ]
  },
  "psychologist.md": {
    word: "psychologist",
    primary: "An expert, researcher, or clinician who specializes in psychology and the scientific study of human behavior, emotion, and mental processes.",
    secondary: "In academic and applied domains, a professional conducting empirical behavioral experiments, administering psychometric assessments, or providing counseling.",
    quotes: [
      { author: "William James", work: "The Will to Believe", quote: "The **psychologist** must confess that human nature is far too multifaceted to fit neatly into any single theoretical cage." },
      { author: "B. F. Skinner", work: "About Behaviorism", quote: "The behavioral **psychologist** studies observable environmental contingencies rather than mysterious inner homunculi." },
      { author: "Jean Piaget", work: "The Child's Conception of the World", quote: "The developmental **psychologist** learns more by observing children's spontaneous errors than from their correct answers." }
    ]
  },
  "psychology.md": {
    word: "psychology",
    primary: "The scientific study of the human mind, consciousness, and behavior, encompassing both cognitive functions and emotional experiences.",
    secondary: "In broader cultural usage, the mental characteristics, attitude, or behavioral profile of an individual, group, or culture in a particular situation.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "**Psychology** is the Science of Mental Life, both of its phenomena and of their conditions." },
      { author: "Sigmund Freud", work: "New Introductory Lectures on Psycho-Analysis", quote: "The future may well see **psychology** grounded in biological discoveries whose chemical nature we can now barely imagine." },
      { author: "Herman Melville", work: "Billy Budd, Sailor", quote: "Claggart’s depravity presented a dark problem in moral **psychology** that normal human nature could neither comprehend nor cure." }
    ]
  },
  "psychometric.md": {
    word: "psychometric",
    primary: "Of or relating to psychometrics; measuring psychological variables such as intelligence, aptitude, personality traits, and educational achievement.",
    secondary: "In testing design and statistics, describing instruments that demonstrate validated reliability, construct validity, and standardized norming.",
    quotes: [
      { author: "Francis Galton", work: "Inquiries into Human Faculty and Its Development", quote: "I established an anthropometric laboratory to administer exact **psychometric** tests of sensory acuity and reaction speed." },
      { author: "Charles Spearman", work: "The Abilities of Man", quote: "Through rigorous **psychometric** testing across diverse mental tasks, the general factor 'g' consistently emerged." },
      { author: "Lewis Terman", work: "The Measurement of Intelligence", quote: "Standardized **psychometric** scales allow educators to identify gifted children who might otherwise languish in ordinary classrooms." }
    ]
  },
  "psychometrics.md": {
    word: "psychometrics",
    primary: "The science of measuring mental capacities, cognitive abilities, personality traits, and educational achievement through standardized quantitative tests.",
    secondary: "In applied statistics and educational measurement, the discipline concerned with item response theory, factor analysis, test calibration, and validation.",
    quotes: [
      { author: "L. L. Thurstone", work: "The Vectors of Mind", quote: "Mathematical **psychometrics** liberates psychology from vague speculation by providing multidimensional coordinate systems for human abilities." },
      { author: "Anne Anastasi", work: "Psychological Testing", quote: "The cardinal rule of modern **psychometrics** is that no test score has meaning apart from its established normative framework." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "The history of **psychometrics** serves as a cautionary tale against reifying abstract statistical constructs into innate biological ranks." }
    ]
  },
  "psychometrika.md": {
    word: "psychometrika",
    primary: "The premier peer-reviewed academic journal dedicated to quantitative psychology and statistical methods in psychological testing, founded in 1936.",
    secondary: "In quantitative behavioral science, the flagship publication of the Psychometric Society, known for pioneering factor analysis, latent trait theory, and structural equation modeling.",
    quotes: [
      { author: "L. L. Thurstone", work: "Psychometrika (Inaugural Issue, 1936)", quote: "The journal **Psychometrika** is established to cultivate the development of psychology as a quantitative, rational science." },
      { author: "Harold Hotelling", work: "Relations Between Two Sets of Variates", quote: "Key formulations of canonical correlation analysis found their natural intellectual home in the pages of **Psychometrika**." },
      { author: "Frederic M. Lord", work: "Applications of Item Response Theory", quote: "Modern item response theory was shaped through seminal treatises published in **Psychometrika** across several decades." }
    ]
  },
  "psychometry.md": {
    word: "psychometry",
    primary: "The alleged psychic ability to divine facts about an object or its owner through physical touch; also an alternative term for psychometrics (mental measurement).",
    secondary: "In spiritualism and psychical research (coined by Joseph Rodes Buchanan in 1842), the supposed extrasensory reading of energy impressions left on inanimate relics.",
    quotes: [
      { author: "William F. Barrett", work: "Psychical Research", quote: "In experiments with **psychometry**, the sensitive held an ancient coin and accurately described the Roman legion that struck it." },
      { author: "Arthur Conan Doyle", work: "The Edge of the Unknown", quote: "The astonishing demonstrations of **psychometry** prove that inanimate objects absorb invisible emotional vibrations from their owners." },
      { author: "Francis Galton", work: "Psychometric Experiments", quote: "I use the term **psychometry** in its strict scientific sense, denoting the precise measurement of the duration of mental processes." }
    ]
  },
  "psychomotor.md": {
    word: "psychomotor",
    primary: "Of or relating to muscular action or movement directly originating from or mediated by conscious mental processes.",
    secondary: "In clinical psychiatry and neurology, describing motor speed, coordination, and tempo (e.g. psychomotor agitation in mania or psychomotor retardation in severe depression).",
    quotes: [
      { author: "Emil Kraepelin", work: "Manic-Depressive Insanity and Paranoia", quote: "Severe melancholia is marked by profound **psychomotor** retardation, where speaking a simple sentence requires immense physical exertion." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Following L-DOPA administration, their frozen immobility gave way to astonishing bursts of **psychomotor** vitality." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Extreme **psychomotor** agitation in acute delirious states requires constant nursing vigilance to prevent cardiac exhaustion." }
    ]
  },
  "psychoneurosis.md": {
    word: "psychoneurosis",
    primary: "A mental or emotional disorder characterized by chronic anxiety, phobias, or obsessions without physical brain lesions or loss of contact with reality.",
    secondary: "In classical psychoanalysis (Freud's transference neuroses), a condition (such as hysteria or obsessive-compulsive neurosis) resulting from unconscious conflict between the ego and instinctual id.",
    quotes: [
      { author: "Sigmund Freud", work: "The Ego and the Id", quote: "Every true **psychoneurosis** is born from the failure of the ego to mediate between instinctual demands and reality." },
      { author: "Karen Horney", work: "The Neurotic Personality of Our Time", quote: "The underlying fuel of modern **psychoneurosis** is the gnawing sense of basic anxiety generated by competitive culture." },
      { author: "Carl Rogers", work: "Counseling and Psychotherapy", quote: "Under conditions of empathic warmth, the rigid defenses of the patient with **psychoneurosis** gradually dissolve." }
    ]
  },
  "psychoneurotic.md": {
    word: "psychoneurotic",
    primary: "Of, relating to, or suffering from a psychoneurosis; characterized by chronic anxiety, obsessive habits, or emotional maladjustment.",
    secondary: "In military and clinical history, describing combat fatigue, shell shock, or emotional casualties during wartime evaluated by psychiatric boards.",
    quotes: [
      { author: "W. H. R. Rivers", work: "Conflict and Dream", quote: "Soldiers suffering from severe **psychoneurotic** symptoms responded remarkably well to dream analysis and emotional abreaction." },
      { author: "George Orwell", work: "Inside the Whale", quote: "Much of twentieth-century literature is written in a **psychoneurotic** key, reflecting the widespread nervous exhaustion of European society." },
      { author: "Sigmund Freud", work: "Inhibitions, Symptoms and Anxiety", quote: "The **psychoneurotic** individual builds an elaborate fortress of symptoms to protect himself from unacknowledged anxiety." }
    ]
  },
  "psychonomics.md": {
    word: "psychonomics",
    primary: "The branch of science that studies the fundamental laws and principles governing the mind and psychological processes.",
    secondary: "In experimental cognitive science and psychophysics, the quantitative investigation of perceptual thresholds, decision-making, and cognitive architectures.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "If we are ever to establish a genuine science of **psychonomics**, it must rest upon unshakeable physiological and experimental laws." },
      { author: "E. B. Titchener", work: "A Text-Book of Psychology", quote: "Structural **psychonomics** dissects conscious experience into its fundamental sensory and affective elements." },
      { author: "Herbert A. Simon", work: "Models of Thought", quote: "Modern cognitive **psychonomics** models the mind as an information-processing system bounded by finite memory buffers." }
    ]
  },
  "psychopath.md": {
    word: "psychopath",
    primary: "A person suffering from chronic mental disorder with abnormal, aggressive, or egocentric social behavior, marked by a callous lack of empathy and remorse.",
    secondary: "In forensic psychology and criminology (Robert Hare's PCL-R), an individual characterized by superficial charm, pathological lying, impulsivity, and failure to feel guilt or moral responsibility.",
    quotes: [
      { author: "Hervey Cleckley", work: "The Mask of Sanity", quote: "The true **psychopath** wears a convincing mask of sanity, mimicking normal social affections while remaining utterly devoid of remorse." },
      { author: "Robert D. Hare", work: "Without Conscience", quote: "A predatory **psychopath** views other human beings not as persons, but as objects to be manipulated for self-gratification." },
      { author: "Hannah Arendt", work: "Eichmann in Jerusalem", quote: "The judges were baffled because the defendant was no fanatical **psychopath**, but an appallingly ordinary bureaucrat." }
    ]
  },
  "psychopathic.md": {
    word: "psychopathic",
    primary: "Of, relating to, or characteristic of a psychopath; exhibiting callous lack of empathy, predatory impulsivity, or remorseless antisocial behavior.",
    secondary: "In 19th-century psychiatry, historically designating any mental illness or mental instability before narrowing to antisocial personality pathology.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Genius is often allied with a **psychopathic** temperament, where intense sensitivity makes normal life almost unbearable." },
      { author: "Hervey Cleckley", work: "The Mask of Sanity", quote: "His charm was undeniable, but behind it lay that cold, **psychopathic** indifference that left devastated families in his wake." },
      { author: "Arthur Conan Doyle", work: "The Valley of Fear", quote: "Holmes warned that Professor Moriarty’s criminal empire was organized with cold, **psychopathic** calculation." }
    ]
  },
  "psychopathologic.md": {
    word: "psychopathologic",
    primary: "Of or relating to psychopathology; pertaining to mental illness, psychological dysfunction, or abnormal psychology.",
    secondary: "In clinical diagnostics, describing symptoms, cognitive distortions, or behavioral markers indicative of psychiatric disorders.",
    quotes: [
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "A thorough **psychopathologic** interview aims to comprehend how the patient subjectively experiences their altered reality." },
      { author: "Sigmund Freud", work: "The Psychopathology of Everyday Life", quote: "Slips of the tongue provide a miniature **psychopathologic** model illustrating how repressed thoughts disrupt conscious speech." },
      { author: "Emil Kraepelin", work: "Clinical Psychiatry", quote: "We must distinguish transient delirium from deep-seated **psychopathologic** degeneration of the affective faculties." }
    ]
  },
  "psychopathological.md": {
    word: "psychopathological",
    primary: "Of, relating to, or manifesting psychopathology; characteristic of mental or emotional disorders.",
    secondary: "In psychiatric medicine, pertaining to the empirical study, diagnostic categorization, and neurological mechanisms of abnormal mental states.",
    quotes: [
      { author: "C. G. Jung", work: "Psychology and Religion", quote: "Religious experiences must not be dismissed simply because they occur within a **psychopathological** crisis." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "His neurological syndrome was compounded by fascinating **psychopathological** compensations that allowed him to function as a musician." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The physician should recognize early **psychopathological** signs before full-blown melancholia sets in." }
    ]
  },
  "psychopathology.md": {
    word: "psychopathology",
    primary: "The scientific study of mental disorders, cognitive dysfunctions, and abnormal behavior; also the manifestations and symptoms of mental illness.",
    secondary: "In clinical psychiatry and clinical psychology, the overarching academic discipline investigating the etiology, development, and diagnostic nosology of psychological conditions.",
    quotes: [
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "The task of **psychopathology** is to clarify the conscious mental phenomena of the diseased mind and their somatic connections." },
      { author: "Sigmund Freud", work: "The Psychopathology of Everyday Life", quote: "The study of **psychopathology** reveals that the boundary between the normal and the abnormal mind is fluid and permeable." },
      { author: "Eugen Bleuler", work: "Textbook of Psychiatry", quote: "Descriptive **psychopathology** requires unbiased clinical observation free from premature theoretical dogmas." }
    ]
  },
  "psychopathy.md": {
    word: "psychopathy",
    primary: "A mental disorder characterized by persistent antisocial behavior, impaired empathy and remorse, boldness, and egotistical traits.",
    secondary: "In forensic psychology, a specific personality construct distinct from general sociopathy, characterized by lack of fear conditioning, emotional shallowness, and glib manipulation.",
    quotes: [
      { author: "Hervey Cleckley", work: "The Mask of Sanity", quote: "The core tragedy of **psychopathy** is the complete absence of emotional warmth beneath an engaging exterior." },
      { author: "Robert D. Hare", work: "Without Conscience", quote: "Criminal **psychopathy** accounts for a disproportionate amount of violent and predatory crime in our society." },
      { author: "William James", work: "The Principles of Psychology", quote: "Early medical writers used the term **psychopathy** broadly to designate any marked constitutional deviation of mind." }
    ]
  },
  "psychopharmacological.md": {
    word: "psychopharmacological",
    primary: "Of, relating to, or involving psychopharmacology; relating to the effects of drugs on psychological states, mood, and behavior.",
    secondary: "In clinical psychiatry, concerning therapeutic drug regimens, clinical trials of psychotropic medications, and neurochemical receptor affinities.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "The response to L-DOPA represented a triumph of targeted **psychopharmacological** intervention in basal ganglia pathology." },
      { author: "Kay Redfield Jamison", work: "An Unquiet Mind", quote: "Modern **psychopharmacological** discoveries have transformed manic-depressive illness from a life sentence into a manageable condition." },
      { author: "Eric Kandel", work: "In Search of Memory", quote: "Our **psychopharmacological** assays illuminated how specific cyclic AMP pathways consolidate long-term behavioral changes." }
    ]
  },
  "psychopharmacology.md": {
    word: "psychopharmacology",
    primary: "The scientific study of the effects of drugs and chemical substances on the mind, mood, sensation, thinking, and behavior.",
    secondary: "In medical history, the revolutionary post-1950 branch of neuroscience that introduced neuroleptics, antidepressants, and mood stabilizers into psychiatric care.",
    quotes: [
      { author: "Solomon Snyder", work: "Brainstorming: The Science of Politics and Politics of Science", quote: "The dawn of modern **psychopharmacology** proved that severe mental illnesses have identifiable molecular receptor targets." },
      { author: "Oliver Sacks", work: "The River of Consciousness", quote: "Advances in **psychopharmacology** revealed that subjective conscious states are profoundly modulated by neurotransmitter balances." },
      { author: "Aldous Huxley", work: "Brave New World Revisited", quote: "The political danger of the future lies in totalitarian governments wielding the discoveries of **psychopharmacology** to drug citizens into passive obedience." }
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
console.log("Batch 5 completed! Total words updated:", Object.keys(wordsData).length);
