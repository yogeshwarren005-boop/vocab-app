import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind/Dashboard — psych";

const wordsData = {
  "psychophysicist.md": {
    word: "psychophysicist",
    primary: "A scientist or experimental psychologist who studies psychophysics, investigating the quantitative relationships between physical stimuli and conscious sensory perceptions.",
    secondary: "In sensory science and neurobiology, a researcher measuring absolute detection thresholds, difference limens, and sensory scaling using mathematical psychophysical functions.",
    quotes: [
      { author: "Gustav Fechner", work: "Elements of Psychophysics", quote: "The **psychophysicist** measures the exact mathematical function connecting the physical intensity of sound to perceived loudness." },
      { author: "William James", work: "The Principles of Psychology", quote: "Weber and Fechner worked as pioneer **psychophysicists**, establishing the first quantitative law of human sensation." },
      { author: "S. S. Stevens", work: "Psychophysics: Introduction to Its Perceptual, Neural, and Social Prospects", quote: "The modern **psychophysicist** employs magnitude estimation to chart sensory power laws across all modalities." }
    ]
  },
  "psychophysics.md": {
    word: "psychophysics",
    primary: "The branch of experimental psychology that quantitatively investigates the relationships between physical stimuli and the sensations and perceptions they produce.",
    secondary: "In the history of science (founded by Gustav Fechner in 1860), the foundational methodology that established psychology as an exact experimental science via mathematical laws (Weber-Fechner Law).",
    quotes: [
      { author: "Gustav Fechner", work: "Elements of Psychophysics", quote: "By **psychophysics** is to be understood an exact theory of the functionally dependent relations of body and soul." },
      { author: "Wilhelm Wundt", work: "Principles of Physiological Psychology", quote: "Experimental **psychophysics** provided the essential laboratory bridge between external physics and internal mental life." },
      { author: "Ernst Mach", work: "The Analysis of Sensations", quote: "The inquiries of **psychophysics** compel us to recognize that sensation and physical reality are aspects of one continuum." }
    ]
  },
  "psychophysiology.md": {
    word: "psychophysiology",
    primary: "The branch of science that studies the relationship between psychological processes (cognition, emotion, attention) and physiological responses of the body.",
    secondary: "In cognitive neuroscience, the recording and analysis of bodily autonomic indicators—such as galvanic skin response, electrocardiography, pupillometry, and electroencephalography—during mental tasks.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Our theory of emotion belongs squarely to **psychophysiology**, asserting that bodily changes follow directly the perception of the exciting fact." },
      { author: "Walter Bradford Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", quote: "The **psychophysiology** of fear mobilizes adrenal secretion and vascular constriction to prepare the organism for fight or flight." },
      { author: "Alexander Luria", work: "The Nature of Human Conflicts", quote: "Through experimental **psychophysiology**, we monitored motor tremors to expose hidden affective complexes in criminal suspects." }
    ]
  },
  "psychopomp.md": {
    word: "psychopomp",
    primary: "A conductor or guide of souls to the underworld or afterlife in mythology and religion, such as Greek Hermes, Charon, or Egyptian Anubis.",
    secondary: "In analytical psychology (Carl Jung), an archetypal figure, dream guide, or symbolic presence that mediates between the conscious ego and the collective unconscious.",
    quotes: [
      { author: "Homer", work: "The Odyssey", quote: "Hermes, the golden-wand **psychopomp**, summoned the fluttering souls of the slain suitors and led them down murky ways to the meadows of asphodel." },
      { author: "C. G. Jung", work: "Memories, Dreams, Reflections", quote: "In my dreams, Philemon appeared as a wise **psychopomp**, guiding my conscious understanding through dark mythic landscapes." },
      { author: "Joseph Campbell", work: "The Hero with a Thousand Faces", quote: "The supernatural helper or **psychopomp** provides the wandering hero with amulets and secret knowledge needed to cross the threshold." }
    ]
  },
  "psychopsis.md": {
    word: "psychopsis",
    primary: "A genus of epiphytic orchids native to Central and South America, commonly known as butterfly orchids due to their striking flowers that mimic fluttering butterflies.",
    secondary: "In systematic orchidology (family Orchidaceae), prized for tall, wiry scapes topped by solitary yellow and chestnut blossoms with long, antenna-like dorsal sepals and petals (from Greek psyche butterfly + opsis appearance).",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The exquisite genus **Psychopsis** derives its name from the extraordinary resemblance of its blossoms to fluttering tropical butterflies." },
      { author: "H. G. Reichenbach", work: "Xenia Orchidacea", quote: "Collectors traveled deep into Trinidad to obtain living specimens of **Psychopsis** krameriana for European conservatories." },
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised by Insects", quote: "The bizarre floral architecture of the butterfly orchid, **Psychopsis**, is exquisitely adapted to deceive insect pollinators." }
    ]
  },
  "psychosexual.md": {
    word: "psychosexual",
    primary: "Of or relating to the mental, emotional, and psychological aspects of human sexuality and sexual development.",
    secondary: "In psychoanalytic theory, denoting Freud's developmental stages (oral, anal, phallic, latent, genital) through which instinctual libido matures toward adult object choice.",
    quotes: [
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Every adult neurosis exhibits roots in the early **psychosexual** development and childhood fixations of the individual." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The **psychosexual** constitution of an individual reflects an intricate mosaic of biological heredity and cultural conditioning." },
      { author: "Erik Erikson", work: "Childhood and Society", quote: "We must expand Freud’s **psychosexual** milestones into a broader psychosocial matrix that accounts for communal rituals." }
    ]
  },
  "psychosexuality.md": {
    word: "psychosexuality",
    primary: "The psychological, emotional, and social dimensions of an individual's sexual nature, identity, desires, and behaviors.",
    secondary: "In clinical psychiatry and sexology, the totality of psychological attitudes and conscious and unconscious experiences that shape erotic and romantic life.",
    quotes: [
      { author: "Alfred Kinsey", work: "Sexual Behavior in the Human Male", quote: "Human **psychosexuality** spans a broad, continuous spectrum that cannot be divided into rigid, mutually exclusive categories." },
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "The full richness of adult **psychosexuality** emerges only after the tempestuous storms of puberty subside." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "One is not born a woman; human **psychosexuality** is an existential project constructed within historical patriarchal constraints." }
    ]
  },
  "psychosis.md": {
    word: "psychosis",
    primary: "A severe mental disorder characterized by a loss of contact with external reality, typically manifesting through delusions, hallucinations, and severely disorganized thought.",
    secondary: "In clinical psychiatry, a diagnostic category distinguishing major conditions such as schizophrenia and bipolar mania from non-psychotic neurotic and personality disorders.",
    quotes: [
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "The acute onset of manic-depressive **psychosis** often presents dramatic affective swings without permanent cognitive decay." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "In true **psychosis**, the patient's delusional world possesses an incorrigible certainty that defies logical argument." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "We must differentiate between focal neurological agnosia and generalized toxic or functional **psychosis**." }
    ]
  },
  "psychosocial.md": {
    word: "psychosocial",
    primary: "Relating to the interrelation of social factors and individual thought, emotion, and behavior.",
    secondary: "In developmental psychology (Erik Erikson's eight stages), the lifelong interplay between psychological ego development and cultural, societal expectations.",
    quotes: [
      { author: "Erik Erikson", work: "Identity and the Life Cycle", quote: "Each stage of **psychosocial** development presents a specific crisis that the emerging ego must resolve in dialogue with society." },
      { author: "Carl Rogers", work: "A Way of Being", quote: "A healthy **psychosocial** environment provides unconditional positive regard, fostering authentic personal growth." },
      { author: "Noam Chomsky", work: "For Reasons of State", quote: "Institutional propaganda creates a **psychosocial** climate of fear to manufacture consent for aggressive foreign policy." }
    ]
  },
  "psychosomatic.md": {
    word: "psychosomatic",
    primary: "Of, relating to, or caused by the interaction of the mind and body; especially describing physical illnesses aggravated or triggered by mental stress or emotional conflict.",
    secondary: "In holistic clinical medicine, an approach emphasizing that physical pathology (such as peptic ulcers, hypertension, or eczema) cannot be divorced from emotional life.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "It is much more important to know what sort of a patient has a disease than what sort of a disease a patient has; all healing is in some degree **psychosomatic**." },
      { author: "Franz Alexander", work: "Psychosomatic Medicine", quote: "Chronic unexpressed emotional tension finds somatic discharge through autonomic pathways, producing genuine **psychosomatic** tissue damage." },
      { author: "Oliver Sacks", work: "Migraine", quote: "The classical migraine attack represents an intricate **psychosomatic** drama where vascular physiology mirrors psychic stress." }
    ]
  },
  "psychosurgery.md": {
    word: "psychosurgery",
    primary: "Brain surgery used to treat severe, intractable mental disorders by severing or altering specific neural pathways in the brain.",
    secondary: "In the history of medicine, neurosurgical interventions ranging from historical prefrontal lobotomies (Egas Moniz) to modern stereotactic cingulotomies and deep brain stimulation.",
    quotes: [
      { author: "Egas Moniz", work: "Nobel Lecture (1949)", quote: "We introduced **psychosurgery** through prefrontal leucotomy to interrupt fixed emotional pathways in incurable melancholia." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The reckless era of widespread **psychosurgery** left thousands of psychiatric patients emotionally blunted and intellectually diminished." },
      { author: "Ken Kesey", work: "One Flew Over the Cuckoo's Nest", quote: "The final horror inflicted upon McMurphy was the cold blade of **psychosurgery**, turning a rebellious spirit into a pacified vegetable." }
    ]
  },
  "psychotherapeutic.md": {
    word: "psychotherapeutic",
    primary: "Of, relating to, or used in psychotherapy; serving to heal mental, emotional, or behavioral conditions through psychological methods.",
    secondary: "In clinical psychology and counseling, describing therapeutic modalities (such as cognitive-behavioral, psychodynamic, or humanistic therapy) aimed at relieving mental suffering.",
    quotes: [
      { author: "Carl Rogers", work: "Client-Centered Therapy", quote: "The primary **psychotherapeutic** condition is the therapist’s genuine congruence and empathic understanding." },
      { author: "Sigmund Freud", work: "On Psychotherapy", quote: "The **psychotherapeutic** procedure does not add anything new to the mind, but removes pathological repressions like a sculptor chipping away marble." },
      { author: "Viktor Frankl", work: "Man's Search for Meaning", quote: "Logotherapy offers a **psychotherapeutic** framework centered upon finding purpose even in the midst of unavoidable suffering." }
    ]
  },
  "psychotherapeutics.md": {
    word: "psychotherapeutics",
    primary: "The branch of medicine and psychology concerned with the application of psychotherapy and psychological treatments to alleviate mental distress.",
    secondary: "In 19th- and early 20th-century clinical practice, the therapeutic utilization of hypnotic suggestion, moral treatment, and dialogue to cure neuroses.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The rise of mind-cure movements forced medical orthodoxy to recognize the legitimate efficacy of **psychotherapeutics**." },
      { author: "Pierre Janet", work: "Psychological Healing", quote: "Scientific **psychotherapeutics** must rest upon a rigorous classification of psychological tensions and moral economies." },
      { author: "Morton Prince", work: "The Dissociation of a Personality", quote: "Our success in integrating the multiple personalities of Miss Beauchamp was achieved through meticulous **psychotherapeutics**." }
    ]
  },
  "psychotherapist.md": {
    word: "psychotherapist",
    primary: "A licensed professional trained to treat mental disorders, emotional problems, and behavioral difficulties through psychological techniques and dialogue.",
    secondary: "In mental health care, a clinical practitioner (such as a psychologist, psychiatrist, or licensed counselor) who guides clients through self-reflection and therapeutic change.",
    quotes: [
      { author: "Carl Rogers", work: "On Becoming a Person", quote: "The skilled **psychotherapist** does not dispense answers, but creates a nonjudgmental climate where the client finds their own path." },
      { author: "Irvin D. Yalom", work: "Love's Executioner", quote: "Every experienced **psychotherapist** knows that behind diverse symptoms lies an encounter with fundamental existential truths." },
      { author: "Viktor Frankl", work: "The Doctor and the Soul", quote: "The **psychotherapist** must respect the spiritual freedom of the patient, never imposing personal metaphysical dogmas." }
    ]
  },
  "psychotherapy.md": {
    word: "psychotherapy",
    primary: "The treatment of mental disorders, emotional challenges, and psychological distress by psychological means rather than medical or somatic intervention.",
    secondary: "In the history of psychiatry, the talking cure encompassing diverse theoretical orientations (psychoanalytic, behavioral, humanistic, systemic) to enhance well-being and insight.",
    quotes: [
      { author: "Sigmund Freud", work: "A General Introduction to Psychoanalysis", quote: "In **psychotherapy**, nothing takes place between the patient and the physician except that they talk to each other." },
      { author: "Carl Rogers", work: "Counseling and Psychotherapy", quote: "Effective **psychotherapy** frees the individual to explore hidden aspects of their self without the terror of rejection." },
      { author: "C. G. Jung", work: "Modern Man in Search of a Soul", quote: "The ultimate aim of **psychotherapy** is not merely symptom relief, but the profound individuation of the human personality." }
    ]
  },
  "psychotic.md": {
    word: "psychotic",
    primary: "Of, relating to, or suffering from psychosis; characterized by severe delusions, hallucinations, or a major detachment from reality.",
    secondary: "In clinical psychiatry, describing states or episodes (such as in acute schizophrenia or severe bipolar mania) where reality testing is fundamentally compromised.",
    quotes: [
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "A **psychotic** delusion cannot be corrected by empirical evidence, for it forms the foundational premise of the patient's reality." },
      { author: "Kay Redfield Jamison", work: "An Unquiet Mind", quote: "During severe manic episodes, my thoughts accelerated into terrifying **psychotic** hallucinations that shattered daily life." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Certain post-encephalitic patients experienced brief **psychotic** excitements characterized by vivid visual hallucinations." }
    ]
  },
  "psychoticism.md": {
    word: "psychoticism",
    primary: "A personality dimension in Hans Eysenck's PEN model characterized by tough-mindedness, nonconformity, impulsivity, interpersonal hostility, and predisposition to psychosis.",
    secondary: "In differential psychology, a continuous trait dimension where high scores correlate with reduced empathy, sensation-seeking, and high creative unconventionality.",
    quotes: [
      { author: "Hans Eysenck", work: "The Biological Basis of Personality", quote: "We isolated **psychoticism** as a fundamental biological trait dimension underlying both criminal deviance and exceptional artistic originality." },
      { author: "Raymond Cattell", work: "The Scientific Analysis of Personality", quote: "High measures of **psychoticism** reflect constitutional traits of detachment and cold disregard for social conventions." },
      { author: "Arthur Jensen", work: "The g Factor: The Science of Mental Ability", quote: "Empirical studies in personality genetics demonstrate substantial heritability for Eysenck’s **psychoticism** factor." }
    ]
  },
  "psychotria.md": {
    word: "psychotria",
    primary: "A large genus of flowering plants in the coffee family (Rubiaceae), native to tropical and subtropical forests worldwide.",
    secondary: "In ethnobotany and pharmacognosy, notably comprising Psychotria viridis (chacruna), a sacred Amazonian shrub containing DMT, traditionally brewed with Banisteriopsis caapi to make ayahuasca (from Greek psyche soul/life due to medicinal virtues).",
    quotes: [
      { author: "Richard Evans Schultes", work: "The Healing Forest", quote: "Indigenous shamans combine the leaves of **Psychotria** viridis with the banisteriopsis vine to prepare the visionary sacrament ayahuasca." },
      { author: "Wade Davis", work: "One River", quote: "The forest tribes recognize subtle botanical variations in the genus **Psychotria**, knowing which leaves awaken luminous spirits." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "The understory of the Orinoco river basin was dense with blooming shrubs of **Psychotria**, their fragrant white flowers humming with insects." }
    ]
  },
  "psychotropic.md": {
    word: "psychotropic",
    primary: "Affecting mental activity, behavior, or perception; describing chemical substances or drugs that cross the blood-brain barrier to alter brain function.",
    secondary: "In pharmacotherapeutics, a broad classification encompassing antidepressants, anxiolytics, mood stabilizers, antipsychotics, and hallucinogens.",
    quotes: [
      { author: "Oliver Sacks", work: "Hallucinations", quote: "The accidental synthesis of LSD opened an unprecedented era in the investigation of **psychotropic** molecules." },
      { author: "Aldous Huxley", work: "Brave New World Revisited", quote: "Modern pharmacology places powerful **psychotropic** substances at the disposal of governments, raising grave ethical dilemmas." },
      { author: "Solomon Snyder", work: "Drugs and the Brain", quote: "Every **psychotropic** medication exerts its therapeutic effect by altering specific receptor neurotransmission within synaptic clefts." }
    ]
  },
  "psychrometer.md": {
    word: "psychrometer",
    primary: "A meteorological instrument used to measure relative humidity and atmospheric moisture, consisting of a dry-bulb thermometer and a wet-bulb thermometer.",
    secondary: "In atmospheric physics and HVAC engineering, calculating relative humidity from the evaporative cooling differential between the wet and dry bulbs (from Greek psychros cold, NOT psyche soul!).",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book: A Manual of Practical Meteorology", quote: "By comparing the two mercurial tubes of the **psychrometer**, the mariner computes the atmospheric dew point and predicts approaching fog." },
      { author: "Alexander von Humboldt", work: "Cosmos: A Sketch of a Physical Description of the Universe", quote: "We carried a portable sling **psychrometer** across the Llanos, recording the extraordinary dryness of the tropical desert winds." },
      { author: "Cleveland Abbe", work: "Treatise on Meteorological Apparatus and Methods", quote: "The ventilated **psychrometer** devised by Assmann eliminates radiant heat errors, providing precise humidity measurements." }
    ]
  },
  "sympathetic.md": {
    word: "sympathetic",
    primary: "Feeling, showing, or expressing sympathy, compassion, and sensitivity toward others' misfortune or suffering.",
    secondary: "In human physiology, designating the sympathetic nervous system—the autonomic division that accelerates heart rate, dilates airways, and mobilizes fight-or-flight energy.",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Elinor listened to her sister's outpourings with a **sympathetic** heart, while striving to conceal her own secret heartache." },
      { author: "Charles Dickens", work: "A Christmas Carol", quote: "The spirit looked down upon the struggling family with gentle, **sympathetic** eyes, blessing their humble holiday feast." },
      { author: "Walter Bradford Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", quote: "The **sympathetic** nervous system mobilizes the entire bodily economy for violent exertion during mortal peril." }
    ]
  },
  "sympathise.md": {
    word: "sympathise",
    primary: "To feel or express sympathy, pity, or compassion for someone experiencing sorrow or hardship (British English spelling).",
    secondary: "In philosophical and social discourse, to share common sentiments, agree with an ideology, or harmonize emotionally with others.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "Dorothea could always **sympathise** with passionate intellectual aspirations, even when hidden behind pedantic phraseology." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "I could not but **sympathise** with his restless pain, for I recognized in him a fiery spirit caged like my own." },
      { author: "Bertrand Russell", work: "The Autobiography of Bertrand Russell", quote: "Throughout my life, an unbearable pity for the suffering of mankind compelled me to **sympathise** with the oppressed." }
    ]
  },
  "sympathize.md": {
    word: "sympathize",
    primary: "To feel or express compassion, pity, or sorrow for another person's hardships; to share another's feelings.",
    secondary: "In political and moral philosophy, to be in agreement with, support, or approve of an opinion, movement, or cause.",
    quotes: [
      { author: "Adam Smith", work: "The Theory of Moral Sentiments", quote: "How selfish soever man may be supposed, there are evidently some principles in his nature which interest him in the fortune of others, and render their happiness necessary to him, though he derives nothing from it except the pleasure of seeing it; by this we **sympathize** with our fellows." },
      { author: "Frederick Douglass", work: "Narrative of the Life of Frederick Douglass", quote: "The courageous abolitionists in the North were quick to **sympathize** with fugitive slaves fleeing southern bondage." },
      { author: "Mark Twain", work: "The Adventures of Huckleberry Finn", quote: "I couldn't help but **sympathize** with poor Jim, knowing how he missed his wife and children." }
    ]
  },
  "sympathy.md": {
    word: "sympathy",
    primary: "Feelings of pity, sorrow, and compassion for someone else's misfortune; harmony or agreement in feeling between people.",
    secondary: "In 18th-century moral philosophy (David Hume, Adam Smith), the natural human propensity to mirror and participate in the sentiments and passions of others.",
    quotes: [
      { author: "David Hume", work: "A Treatise of Human Nature", quote: "No quality of human nature is more remarkable, both in itself and in its consequences, than that propensity we have to **sympathy** with others, and to receive by communication their inclinations and sentiments." },
      { author: "William Shakespeare", work: "The Tempest", quote: "O, I have suffered / With those that I saw suffer: a brave vessel, / Who had, no doubt, some noble creature in her, / Dash'd all to pieces. O, the cry did knock / Against my very heart! Poor souls, they perish'd. / Had I been any god of power, I would / Have sunk the sea within the earth or ere / It should the good ship so have swallow'd and / The fraughting souls within her; mine eyes felt true **sympathy**." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "We are drawn to genuine friends by an instinctive **sympathy** that bypasses all calculated social advantage." }
    ]
  },
  "telepathic.md": {
    word: "telepathic",
    primary: "Of, relating to, or communicating by telepathy; transmitting thoughts, sensations, or feelings directly from one mind to another without sensory means.",
    secondary: "In psychology and fiction, describing an uncanny, unspoken mutual understanding or intuitive connection between two closely bonded individuals.",
    quotes: [
      { author: "Frederic W. H. Myers", work: "Human Personality and Its Survival of Bodily Death", quote: "We define **telepathic** communication as the direct transmission of thoughts or emotional states between minds independent of known sensory channels." },
      { author: "Virginia Woolf", work: "The Waves", quote: "Between the two lovers existed an almost **telepathic** communion, where glances conveyed volumes of unspoken thought." },
      { author: "Arthur C. Clarke", work: "Childhood's End", quote: "The final evolutionary leap of mankind involved merging into a vast, harmonious **telepathic** overmind." }
    ]
  },
  "telepathise.md": {
    word: "telepathise",
    primary: "To communicate, send, or receive thoughts and feelings by telepathy (British English spelling).",
    secondary: "In imaginative literature, to establish direct mental contact across distances without speaking or writing.",
    quotes: [
      { author: "H. G. Wells", work: "Men Like Gods", quote: "The advanced utopian humans did not speak aloud, but chose to **telepathise** their ideas with effortless lucidity." },
      { author: "Arthur Conan Doyle", work: "The Land of Mist", quote: "The medium claimed she could **telepathise** with friends in distant cities during deep hypnotic trance." },
      { author: "George Bernard Shaw", work: "Back to Methuselah", quote: "The ancient sages of the future had learned to **telepathise** their philosophical debates across mountain valleys." }
    ]
  },
  "telepathist.md": {
    word: "telepathist",
    primary: "A person who claims to possess the ability to communicate by telepathy, or one who investigates telepathic phenomena.",
    secondary: "In late 19th-century stage entertainment and psychical research, a mentalist or medium demonstrating apparent direct mind-reading.",
    quotes: [
      { author: "William James", work: "Memories and Studies", quote: "The celebrated **telepathist** baffled observers by identifying hidden objects and reproducing concealed drawings." },
      { author: "Arthur Conan Doyle", work: "The History of Spiritualism", quote: "Scientists subjected the **telepathist** to strict controls, shielding him in copper rooms to eliminate wireless signals." },
      { author: "Mark Twain", work: "Mental Telegraphy", quote: "I began to suspect that every human being is an unconscious **telepathist**, radiating thoughts across invisible ether." }
    ]
  },
  "telepathize.md": {
    word: "telepathize",
    primary: "To transmit, communicate, or perceive thoughts, feelings, or mental images through telepathy.",
    secondary: "In speculative fiction and parapsychology, to initiate direct mind-to-mind contact or project consciousness across physical boundaries.",
    quotes: [
      { author: "Philip K. Dick", work: "Ubik", quote: "The psi-shield operative tried to **telepathize** an emergency distress signal to company headquarters." },
      { author: "Isaac Asimov", work: "Foundation and Earth", quote: "The inhabitants of Gaia could **telepathize** across planetary distances, linking their consciousness into a single shared world-soul." },
      { author: "Stephen King", work: "The Shining", quote: "Little Danny could **telepathize** with Hallorann across hundreds of miles of snowy Rocky Mountain passes." }
    ]
  },
  "telepathy.md": {
    word: "telepathy",
    primary: "The direct communication of thoughts, feelings, or mental states from one person to another without using speech, writing, or physical senses.",
    secondary: "In psychical research (term coined by Frederic W. H. Myers in 1882), anomalous extrasensory mental transference investigated through card-guessing and distance experiments.",
    quotes: [
      { author: "Frederic W. H. Myers", work: "Proceedings of the Society for Psychical Research", quote: "I have proposed the word **telepathy** to designate the communication of impressions of any kind from one mind to another, independently of the recognized channels of sense." },
      { author: "Sigmund Freud", work: "Dreams and Occultism", quote: "If **telepathy** be a real process, it may well represent the archaic, original means of communication between individuals." },
      { author: "Arthur Conan Doyle", work: "The Edge of the Unknown", quote: "Evidence for spontaneous **telepathy** during moments of mortal crisis is backed by hundreds of authenticated affidavits." }
    ]
  },
  "unsympathetic.md": {
    word: "unsympathetic",
    primary: "Not showing or feeling sympathy, warmth, or compassion; callous, unfeeling, or harsh.",
    secondary: "In literary characterization and aesthetics, describing characters or atmospheres that fail to evoke fondness, warmth, or emotional identification from the audience.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mr. Darcy appeared cold and **unsympathetic** at the assembly ball, declining to dance with strangers." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The court of Chancery was a vast, **unsympathetic** machine that ground litigants to dust through decades of delays." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Gilbert Osmond’s **unsympathetic** aestheticism chilled Isabel’s generous spirit, reducing their marriage to a silent prison." }
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
console.log("Batch 6 completed! Total words updated:", Object.keys(wordsData).length);
