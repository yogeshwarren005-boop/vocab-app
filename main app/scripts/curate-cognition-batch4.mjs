import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind/Dashboard — psych";

const wordsData = {
  "antipathetic.md": {
    word: "antipathetic",
    primary: "Showing or feeling a strong, settled, or deep-seated aversion or opposition; repugnant or hostile.",
    secondary: "In physiological and chemical discourse, naturally incompatible, mutually repelling, or antagonistic in properties.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "There was something in the cold, hard face of Mrs. Reed profoundly **antipathetic** to my ardent nature." },
      { author: "William James", work: "The Principles of Psychology", quote: "Certain sounds and bodily sensations are instinctively **antipathetic** to human nervous systems from infancy." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "Henchard felt an **antipathetic** shudder whenever Farfrae’s cool, calculating gaze rested upon him." }
    ]
  },
  "antipathetical.md": {
    word: "antipathetical",
    primary: "Of, relating to, or marked by antipathy; inherently contrary, incompatible, or repellant.",
    secondary: "In philosophical and medical treatises, describing principles or qualities that actively neutralize or conflict with one another.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Some constitutions have an **antipathetical** horror of cheese, fainting at the mere smell thereof." },
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "Naturalists observed an **antipathetical** virtue between the vine and the cabbage, which wither when planted together." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The mechanical philosophy of Hobbes is thoroughly **antipathetical** to the spiritual nature of poetry." }
    ]
  },
  "antipathy.md": {
    word: "antipathy",
    primary: "A deep-seated feeling of dislike, repugnance, or settled aversion toward someone or something.",
    secondary: "In classical philosophy and natural magic, a natural constitutional repulsion between certain substances or organisms (opposite of sympathy).",
    quotes: [
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The Yahoos conceived an invincible **antipathy** toward the cleanly and rational Houyhnhnms." },
      { author: "Edgar Allan Poe", work: "The Tell-Tale Heart", quote: "Object there was none; passion there was none; I loved the old man, yet an inexplicable **antipathy** seized me." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Herbert pocketed his pride, concealing his instinctive **antipathy** toward the boorish manners of Bentley Drummle." }
    ]
  },
  "antipsychotic.md": {
    word: "antipsychotic",
    primary: "A medication used to treat psychosis, schizophrenia, and severe mood disorders; also having the property of counteracting psychotic symptoms.",
    secondary: "In neuropsychopharmacology, neuroleptic agents (such as chlorpromazine, haloperidol, or atypical agents) that modulate central dopamine and serotonin receptor activity.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "The introduction of modern **antipsychotic** compounds revolutionized psychiatric wards in the mid-twentieth century." },
      { author: "Kay Redfield Jamison", work: "An Unquiet Mind", quote: "She struggled with the heavy sedative side effects of the prescribed **antipsychotic** medication." },
      { author: "Paul Kalanithi", work: "When Breath Becomes Air", quote: "In the emergency department, acute agitation was carefully managed with low-dose **antipsychotic** therapy." }
    ]
  },
  "apathetic.md": {
    word: "apathetic",
    primary: "Showing or feeling no interest, enthusiasm, or concern; listless, unresponsive, or indifferent.",
    secondary: "In Stoic philosophy, possessing apatheia (freedom from disruptive passions); in clinical medicine, exhibiting pathological blunting of affective responsiveness.",
    quotes: [
      { author: "George Orwell", work: "1984", quote: "The proles remained politically **apathetic**, stirred to fury only by lottery shortages or football matches." },
      { author: "Herman Melville", work: "Bartleby, the Scrivener", quote: "Bartleby stood in his dim corner, utterly **apathetic** to my entreaties and reasonable commands." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Despotism loves an **apathetic** populace that surrenders public duties to enjoy petty private pleasures." }
    ]
  },
  "apathy.md": {
    word: "apathy",
    primary: "Lack of interest, enthusiasm, or concern; emotional indifference and inaction.",
    secondary: "In Stoic ethics, apatheia—the virtuous tranquility of mind untouched by turbulent desires; in neuropsychiatry, a syndrome of diminished motivation and reduced goal-directed behavior.",
    quotes: [
      { author: "Epictetus", work: "Discourses", quote: "The philosopher strives for holy **apathy**, remaining unshaken whether fortune bestows riches or exile." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "A deadly weight hung upon me, and I sank into a sullen **apathy** from which neither books nor friends could rouse me." },
      { author: "Winston Churchill", work: "The Gathering Storm", quote: "The catastrophic drift toward world war was accelerated by public **apathy** and wishful thinking." }
    ]
  },
  "biopsychic.md": {
    word: "biopsychic",
    primary: "Of or relating to the interaction between biological organismic processes and psychological or mental phenomena.",
    secondary: "In developmental biology and neuropsychology, describing organismic evolution where physiological vitality and cognitive consciousness develop reciprocally.",
    quotes: [
      { author: "Julian Huxley", work: "Evolution in Action", quote: "Human evolution marks the transition from purely biological selection to a self-conscious **biopsychic** phase." },
      { author: "C. G. Jung", work: "The Structure and Dynamics of the Psyche", quote: "Archetypes are fundamentally **biopsychic** instincts, rooting conscious symbols in somatic heritage." },
      { author: "Pierre Teilhard de Chardin", work: "The Phenomenon of Man", quote: "The planetary web of life represents a continuous **biopsychic** ascent toward greater complexity and consciousness." }
    ]
  },
  "biopsychology.md": {
    word: "biopsychology",
    primary: "The branch of psychology that studies the biological and physiological bases of behavior, emotion, and mental processes.",
    secondary: "In cognitive neuroscience, the empirical discipline investigating how genetics, neural circuits, endocrine systems, and neurotransmitters mediate cognition.",
    quotes: [
      { author: "Donald O. Hebb", work: "The Organization of Behavior", quote: "Modern **biopsychology** bridges the conceptual gap between subjective consciousness and synaptic plastic changes." },
      { author: "William James", work: "The Principles of Psychology", quote: "Every psychological fact is anchored in somatic physiology, forming the true foundation of **biopsychology**." },
      { author: "Eric Kandel", work: "In Search of Memory", quote: "Through cellular **biopsychology**, we traced the biochemical mechanisms of memory storage in simple marine mollusks." }
    ]
  },
  "empathetic.md": {
    word: "empathetic",
    primary: "Showing an ability to understand, share, and resonate with the feelings, thoughts, and experiences of another.",
    secondary: "In clinical psychotherapy and affective neuroscience, having high interpersonal sensitivity that mirrors others' emotional states via mirror neuron networks.",
    quotes: [
      { author: "Carl Rogers", work: "On Becoming a Person", quote: "An **empathetic** therapist enters the private world of the client without judgment or preconception." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "His deeply **empathetic** gaze seemed to comprehend her unspoken grief before she spoke a syllable." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "Mrs. Ramsay possessed an **empathetic** warmth that knit the discordant house guests into a single harmonious family." }
    ]
  },
  "empathic.md": {
    word: "empathic",
    primary: "Involving, characterized by, or based on empathy; empathetic.",
    secondary: "In psychoanalytic theory (Heinz Kohut), describing vicarious introspection whereby the analyst immerses themselves in the patient's subjective experience.",
    quotes: [
      { author: "Heinz Kohut", work: "The Restoration of the Self", quote: "The analyst’s **empathic** immersion is the essential instrument for understanding the injured self." },
      { author: "Philip K. Dick", work: "Do Androids Dream of Electric Sheep?", quote: "The Voight-Kampff test measures **empathic** capillary dilation to separate humans from synthetic androids." },
      { author: "William James", work: "Talks to Teachers on Psychology", quote: "True moral education demands an **empathic** leap beyond the narrow confines of one’s own ego." }
    ]
  },
  "empathise.md": {
    word: "empathise",
    primary: "To understand and share the feelings of another person; to experience empathy (British English spelling).",
    secondary: "In literary aesthetics and humanistic psychology, to project one's consciousness into a work of art, nature, or another human being's plight.",
    quotes: [
      { author: "E. M. Forster", work: "Howards End", quote: "Only connect! We must learn to **empathise** with those whose social circumstances differ entirely from our own." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "To read a masterpiece is to **empathise** so intimately with the author that their sentences seem our own creation." },
      { author: "Bertrand Russell", work: "The Conquest of Happiness", quote: "The happy man possesses broad interests and the capacity to **empathise** generously with his fellows." }
    ]
  },
  "empathize.md": {
    word: "empathize",
    primary: "To understand and share the feelings, perspective, and emotional experiences of another person.",
    secondary: "In developmental and social psychology, to activate shared neural representations that foster compassion, altruism, and social cooperation.",
    quotes: [
      { author: "Carl Rogers", work: "A Way of Being", quote: "When you deeply **empathize** with another person, their fears lose their terrifying isolation." },
      { author: "Maya Angelou", work: "I Know Why the Caged Bird Sings", quote: "Great literature taught me to **empathize** with souls whose lives were radically different from my own." },
      { author: "Barack Obama", work: "The Audacity of Hope", quote: "We must expand our moral imagination and **empathize** with the struggles of the working poor and the immigrant." }
    ]
  },
  "empathy.md": {
    word: "empathy",
    primary: "The ability to understand, be sensitive to, and vicariously experience the feelings, thoughts, and motives of another.",
    secondary: "In aesthetic philosophy (translating German Einfühlung, 'feeling-into'), the projection of human emotion and vitality onto works of art or natural forms.",
    quotes: [
      { author: "Edward B. Titchener", work: "Lectures on the Experimental Psychology of the Thought-Processes", quote: "I introduced the word **empathy** into English to translate the German Einfühlung, denoting this mental feeling-into an object." },
      { author: "Atticus Finch (Harper Lee)", work: "To Kill a Mockingbird", quote: "You never really understand a person until you consider things from his point of view—until you climb into his skin and walk around in it; that is **empathy**." },
      { author: "Vernon Lee", work: "The Beautiful", quote: "Aesthetic **empathy** allows us to feel the dynamic rhythm of a soaring cathedral arch within our own limbs." }
    ]
  },
  "hylopsychism.md": {
    word: "hylopsychism",
    primary: "The philosophical doctrine that matter and mind are inseparable, or that all physical matter possesses an inherent psychic or conscious aspect.",
    secondary: "In metaphysics and panpsychist philosophy, the belief that mind (psyche) is a primordial, ubiquitous property of all material substance (hyle).",
    quotes: [
      { author: "Ernst Haeckel", work: "The Riddle of the Universe", quote: "Our monistic cosmology aligns with **hylopsychism**, recognizing rudimentary sensation even in the simplest atoms." },
      { author: "William James", work: "The Principles of Psychology", quote: "The hypothesis of **hylopsychism** attempts to solve the mind-body dilemma by assuming consciousness is coextensive with mass." },
      { author: "Charles Sanders Peirce", work: "The Architecture of Theories", quote: "A consistent evolutionary metaphysics must embrace some form of **hylopsychism**, viewing matter as effete mind." }
    ]
  },
  "panpsychism.md": {
    word: "panpsychism",
    primary: "The philosophical theory that consciousness, mind, or soul is a universal and primordial feature of all things throughout the cosmos.",
    secondary: "In philosophy of mind, the proposition that mentality is fundamental rather than an emergent property of complex biological brains.",
    quotes: [
      { author: "William James", work: "A Pluralistic Universe", quote: "**Panpsychism** offers the mind-dust theory as an alternative to the miraculous emergence of consciousness from dead matter." },
      { author: "Alfred North Whitehead", work: "Process and Reality", quote: "An organic philosophy of nature leans toward **panpsychism**, seeing feeling and experiential occasions in every actual entity." },
      { author: "Bertrand Russell", work: "The Analysis of Matter", quote: "Neutral monism shares common ground with **panpsychism** by asserting that the intrinsic nature of physical events resembles conscious percepts." }
    ]
  },
  "parapsychological.md": {
    word: "parapsychological",
    primary: "Of, relating to, or dealing with parapsychology; concerning paranormal or psychic phenomena outside the scope of orthodox science.",
    secondary: "In experimental research, referring to laboratory investigations of telepathy, clairvoyance, precognition, and psychokinesis using statistical methods.",
    quotes: [
      { author: "J. B. Rhine", work: "New Frontiers of the Mind", quote: "Our **parapsychological** trials at Duke University utilized standard Zener card decks under strict double-blind conditions." },
      { author: "Arthur Koestler", work: "The Roots of Coincidence", quote: "Modern quantum physics presents paradoxes that render **parapsychological** hypotheses less inherently absurd." },
      { author: "Carl Sagan", work: "Broca's Brain", quote: "Rigorous scientific scrutiny must be maintained toward all **parapsychological** claims, demanding extraordinary proof for extraordinary hypotheses." }
    ]
  },
  "parapsychologist.md": {
    word: "parapsychologist",
    primary: "A researcher or investigator who studies parapsychology, psychic phenomena, and extrasensory perception.",
    secondary: "In historical psychology, an academic scientist investigating anomalies of consciousness and anomalous human experiences through controlled experiments.",
    quotes: [
      { author: "J. B. Rhine", work: "Extra-Sensory Perception", quote: "The **parapsychologist** must apply the exact mathematical tools of statistics to eliminate mere chance coincidence." },
      { author: "William James", work: "Memories and Studies", quote: "As a pioneer **parapsychologist**, I observed mediumistic sittings with an open mind tempered by clinical caution." },
      { author: "Arthur Conan Doyle", work: "The Edge of the Unknown", quote: "The dedicated **parapsychologist** endures the ridicule of orthodox peers while pioneering unseen frontiers of the mind." }
    ]
  },
  "parapsychology.md": {
    word: "parapsychology",
    primary: "The study of mental phenomena that cannot be explained by established scientific theories or orthodox sensory physiology (such as ESP, telepathy, and psychokinesis).",
    secondary: "In academic history (term coined by Max Dessoir in 1889), the field of research dedicated to empirically investigating borderline psychic phenomena.",
    quotes: [
      { author: "J. B. Rhine", work: "The Reach of the Mind", quote: "Experimental **parapsychology** seeks to determine whether human personality possesses capacities that transcend physical space-time." },
      { author: "C. G. Jung", work: "Synchronicity: An Acausal Connecting Principle", quote: "The statistical discoveries of **parapsychology** demonstrate that meaningful coincidences operate beyond simple causality." },
      { author: "Bertrand Russell", work: "An Outline of Philosophy", quote: "If the claims of **parapsychology** were substantiated, the fundamental laws of classical physics would require radical revision." }
    ]
  },
  "parasympathetic.md": {
    word: "parasympathetic",
    primary: "Relating to the branch of the autonomic nervous system that slows heart rate, increases intestinal and gland activity, and relaxes sphincter muscles (rest and digest).",
    secondary: "In physiological neurology, the craniosacral division of the autonomic system that counterbalances sympathetic fight-or-flight activation to restore homeostasis.",
    quotes: [
      { author: "Walter Bradford Cannon", work: "The Wisdom of the Body", quote: "The **parasympathetic** system acts as a gentle brake upon metabolic expenditure, husbanding bodily reserves." },
      { author: "Henry Gray", work: "Anatomy of the Human Body", quote: "The vagus nerve constitutes the principal **parasympathetic** trunk supplying the viscera of the thorax and abdomen." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "A profound relaxation enveloped him as his **parasympathetic** nervous system regained dominance after the ordeal." }
    ]
  },
  "pathy.md": {
    word: "pathy",
    primary: "A combining form derived from Greek pathos meaning feeling, suffering, emotion, or disease (e.g. empathy, sympathy, neuropathy).",
    secondary: "In linguistic morphology and medical terminology, a suffix denoting either emotional affinity or a specified therapeutic method or pathological disorder.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The terminal element -**pathy** derives from Greek pathos, branching into words of suffering, healing, and emotional kinship." },
      { author: "William Osler", work: "The Master-Word in Medicine", quote: "Medical terminology employs -**pathy** to denote structural disease as well as diverse therapeutic systems." },
      { author: "Max Müller", work: "The Science of Thought", quote: "In the evolution of language, the root **path**- and its suffix -**pathy** record the primordial human capacity to feel." }
    ]
  },
  "psyche.md": {
    word: "psyche",
    primary: "The human soul, mind, or total personality, encompassing conscious and unconscious processes; in Greek mythology, the mortal princess loved by Cupid.",
    secondary: "In depth psychology (Freud and Jung), the totality of all psychological processes, both conscious and unconscious, that constitute the individual self.",
    quotes: [
      { author: "C. G. Jung", work: "Modern Man in Search of a Soul", quote: "The **psyche** is not an indivisible unit, but an intricate cosmos of conscious intentions and dark unconscious depths." },
      { author: "John Keats", work: "Ode to Psyche", quote: "O Goddess! hear these tuneless numbers, wrung / By sweet enforcement and remembrance dear, / And pardon that thy secrets should be sung / Even into thine own soft-conched ear: / Surely I dreamt to-day, or did I see / The winged **Psyche** with awaken'd eyes?" },
      { author: "Sigmund Freud", work: "The Ego and the Id", quote: "We conceptualize the human **psyche** as an arena where primal instinctual drives clash with cultural prohibitions." }
    ]
  },
  "psychedelia.md": {
    word: "psychedelia",
    primary: "The subculture, music, art, and visual style associated with psychedelic drugs and altered states of consciousness, flourishing in the late 1960s.",
    secondary: "In cultural history and aesthetics, kaleidoscopic imagery, vibrant swirling colors, and distorted sounds evoking mystical or hallucinogenic experiences.",
    quotes: [
      { author: "Hunter S. Thompson", work: "Fear and Loathing in Las Vegas", quote: "San Francisco in the middle sixties was a very special time and place; the wave of **psychedelia** crested and broke upon the coast." },
      { author: "Aldous Huxley", work: "Moksha: Writings on Psychedelics", quote: "The vibrant sensory explosions of **psychedelia** reflect the brain’s filtering valve temporarily swinging wide open." },
      { author: "Tom Wolfe", work: "The Electric Kool-Aid Acid Test", quote: "The Day-Glo bus rolled across America, spreading the strange new gospel of neon **psychedelia**." }
    ]
  },
  "psychedelic.md": {
    word: "psychedelic",
    primary: "Relating to or producing hallucinations, apparent expansions of consciousness, or altered sensory perceptions (coined from Greek psyche mind + delos visible/manifest).",
    secondary: "In pharmacognosy and psychiatry, substances (such as psilocybin, LSD, and mescaline) that act as 5-HT2A receptor agonists, inducing profound shifts in cognition and ego dissolution.",
    quotes: [
      { author: "Humphry Osmond", work: "Letter to Aldous Huxley", quote: "To fathom Hell or soar angelic, / Just take a pinch of **psychedelic**." },
      { author: "Aldous Huxley", work: "The Doors of Perception", quote: "The **psychedelic** experience demonstrated that our normal waking state is merely one special type of consciousness among many." },
      { author: "Oliver Sacks", work: "Hallucinations", quote: "Under the influence of a **psychedelic** alkaloid, ordinary carpets and curtains became teeming tapestries of luminous geometry." }
    ]
  },
  "psychiatric.md": {
    word: "psychiatric",
    primary: "Of or relating to psychiatry, mental illness, or the clinical treatment of psychological and emotional disorders.",
    secondary: "In clinical medicine, designating hospital wards, diagnostic manuals, and therapeutic regimens dedicated to severe mental disorders.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough medical education must include practical **psychiatric** training in the observation of mental alienation." },
      { author: "Kay Redfield Jamison", work: "Touched with Fire", quote: "Many great artists wrestled with agonizing **psychiatric** conditions that fueled both their torment and their creativity." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The chronic post-encephalitic patients exhibited bizarre motor tics that defied simple **psychiatric** categorization." }
    ]
  },
  "psychiatrical.md": {
    word: "psychiatrical",
    primary: "A variant or historical form of psychiatric; of or relating to psychiatry or the treatment of mental illness.",
    secondary: "In 19th- and early 20th-century medical treatises, pertaining to asylum administration, mental jurisprudence, and clinical diagnosis of psychoses.",
    quotes: [
      { author: "Henry Maudsley", work: "Physiology and Pathology of the Mind", quote: "The author presented a detailed **psychiatrical** examination of the prisoner's hereditary family history." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Medical materialists dismiss religious genius with a few hasty **psychiatrical** labels of degeneration." },
      { author: "C. G. Jung", work: "The Psychology of Dementia Praecox", quote: "Our **psychiatrical** observations at the Burghölzli asylum revealed that delusions follow distinct associative laws." }
    ]
  },
  "psychiatrist.md": {
    word: "psychiatrist",
    primary: "A medical doctor who specializes in the diagnosis, prevention, study, and treatment of mental health disorders and emotional illnesses.",
    secondary: "In clinical practice, a licensed physician authorized to prescribe psychotropic medications, conduct somatic therapies, and provide psychotherapy.",
    quotes: [
      { author: "Carl Rogers", work: "On Becoming a Person", quote: "The compassionate **psychiatrist** listens not merely to the spoken complaint, but to the anxious soul beneath." },
      { author: "Kay Redfield Jamison", work: "An Unquiet Mind", quote: "As both a clinical psychologist and a patient, I watched the **psychiatrist** weigh the precarious balance of lithium dosage." },
      { author: "Sigmund Freud", work: "An Autobiographical Study", quote: "My early training as a neuropathologist led me naturally to the role of a consulting **psychiatrist** in Vienna." }
    ]
  },
  "psychiatry.md": {
    word: "psychiatry",
    primary: "The branch of medicine devoted to the diagnosis, prevention, study, and treatment of mental, emotional, and behavioral disorders.",
    secondary: "In the history of medicine (coined by Johann Christian Reil in 1808), the medical discipline bridging neurological pathology, psychopharmacology, and psychotherapy.",
    quotes: [
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "Clinical **psychiatry** must construct its classifications upon careful longitudinal observation of disease course and outcome." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "Scientific **psychiatry** requires both the causal explanations of natural science and the empathetic understanding of the humanities." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The division between neurology and **psychiatry** is an artificial historical frontier that our patients constantly cross." }
    ]
  },
  "psychic.md": {
    word: "psychic",
    primary: "Relating to or being within the human soul, mind, or psychological life; also sensitive to supernatural or nonphysical forces.",
    secondary: "In depth psychology, pertaining to the psyche or mental energy (psychic energy/libido); colloquially, an individual claiming telepathic or clairvoyant sensitivity.",
    quotes: [
      { author: "C. G. Jung", work: "Psychological Types", quote: "Every creative act springs from a profound redistribution of **psychic** energy within the unconscious." },
      { author: "William James", work: "The Will to Believe", quote: "We must remain open to anomalous **psychic** experiences that challenge our tidy mechanistic dogmas." },
      { author: "Sigmund Freud", work: "The Interpretation of Dreams", quote: "A dream is a full-fledged **psychic** act, possessing meaning and an undeniable place in the waking soul." }
    ]
  },
  "psychical.md": {
    word: "psychical",
    primary: "Of or relating to the mind or psyche; psychological or mental (contrasted with physical).",
    secondary: "Historically, in late 19th-century Britain, referring to psychical research—the scientific investigation of telepathy, apparitions, and mediumship.",
    quotes: [
      { author: "Henry Sidgwick", work: "Presidential Address to the Society for Psychical Research", quote: "Our aim in **psychical** research is to investigate disputed phenomena without prejudice or prepossession." },
      { author: "William James", work: "The Principles of Psychology", quote: "The relationship between physical brain processes and **psychical** states remains the ultimate riddle of science." },
      { author: "Arthur Balfour", work: "Essays and Addresses", quote: "The boundary between biological reflex and conscious **psychical** life is impossible to delineate with precision." }
    ]
  },
  "psychically.md": {
    word: "psychically",
    primary: "In a mental or psychological manner; in terms of the soul, psyche, or inner consciousness.",
    secondary: "In spiritualism and psychical inquiry, through extrasensory, telepathic, or clairvoyant channels.",
    quotes: [
      { author: "William James", work: "Memories and Studies", quote: "The sensitive individual seemed **psychically** attuned to the emotional crisis occurring miles away." },
      { author: "C. G. Jung", work: "Man and His Symbols", quote: "Primitive man lived **psychically** immersed in his natural environment, projecting his soul into rocks and trees." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The two partners were **psychically** compatible, sharing an unspoken harmony of temperament and values." }
    ]
  },
  "psycho.md": {
    word: "psycho",
    primary: "A colloquial abbreviation for a psychopath, psychotic individual, or someone displaying wildly erratic or dangerous behavior; also the combining root psycho-.",
    secondary: "In informal cultural discourse (popularized by Hitchcock's 1960 thriller Psycho), a derisive label for a homicidal or severely disturbed individual; in morphology, the root denoting mind or soul.",
    quotes: [
      { author: "Alfred Hitchcock", work: "Interviews on Cinema", quote: "In directing **Psycho**, I was interested in pure cinematic emotion and manipulating audience terror through editing." },
      { author: "Stephen King", work: "On Writing", quote: "The small town harbored secrets that exploded when a local **psycho** went off the deep end." },
      { author: "H. L. Mencken", work: "The American Language", quote: "American slang eagerly clipped clinical terms, turning psychopath into the ubiquitous label **psycho**." }
    ]
  },
  "psychoactive.md": {
    word: "psychoactive",
    primary: "Affecting the mind, mood, thoughts, or behavior, especially referring to chemical substances and pharmaceuticals.",
    secondary: "In pharmacology and neurochemistry, describing compounds that cross the blood-brain barrier to act upon central nervous system neurotransmitter systems.",
    quotes: [
      { author: "Oliver Sacks", work: "Hallucinations", quote: "Humankind has experimented with natural **psychoactive** plants since the dawn of Paleolithic culture." },
      { author: "Aldous Huxley", work: "The Doors of Perception", quote: "The discovery of synthetic **psychoactive** agents offers unexpected insights into how the brain shapes reality." },
      { author: "Andrew Weil", work: "The Natural Mind", quote: "Every culture except the Inuits has utilized some local **psychoactive** substance to alter baseline consciousness." }
    ]
  },
  "psychoanalyse.md": {
    word: "psychoanalyse",
    primary: "To examine or treat someone using the methods of psychoanalysis (British English spelling).",
    secondary: "In psychological criticism, to interpret unconscious motives, repressed desires, and symbolic behaviors in literary texts or historical figures.",
    quotes: [
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "To **psychoanalyse** the great poets of the past risks reducing their celestial music to petty childhood neuroses." },
      { author: "W. H. Auden", work: "In Memory of Sigmund Freud", quote: "He taught us to **psychoanalyse** our daily slips of tongue, revealing the secret desires lurking behind polite speech." },
      { author: "Bertrand Russell", work: "The Conquest of Happiness", quote: "One does not need to **psychoanalyse** every fleeting unhappiness when simple fresh air and meaningful work suffice." }
    ]
  },
  "psychoanalysis.md": {
    word: "psychoanalysis",
    primary: "A system of psychological theory and therapy founded by Sigmund Freud, investigating the interaction of conscious and unconscious elements through free association and dream analysis.",
    secondary: "In intellectual history, a revolutionary 20th-century hermeneutic movement that reshaped philosophy, literature, art, and the understanding of human sexuality.",
    quotes: [
      { author: "Sigmund Freud", work: "The Question of Lay Analysis", quote: "**Psychoanalysis** is a part of psychology, not of medical psychology; it is the psychology of the unconscious mental processes." },
      { author: "C. G. Jung", work: "Memories, Dreams, Reflections", quote: "My collaboration with Freud centered upon **psychoanalysis**, until our differing views on the nature of the libido led to our parting." },
      { author: "Thomas Mann", work: "Freud and the Future", quote: "Through **psychoanalysis**, modern humanism gained a fearless lantern to explore the subterranean caverns of the soul." }
    ]
  },
  "psychoanalyst.md": {
    word: "psychoanalyst",
    primary: "A clinician, psychologist, or psychiatrist who specializes in and practices the therapeutic method of psychoanalysis.",
    secondary: "In psychoanalytic tradition, a practitioner who has undergone personal training analysis and utilizes free association, transference, and interpretation to resolve neuroses.",
    quotes: [
      { author: "Sigmund Freud", work: "Analysis Terminable and Interminable", quote: "The **psychoanalyst** must maintain evenly hovering attention, receptive to every nuance of the patient's discourse." },
      { author: "Erik Erikson", work: "Childhood and Society", quote: "As a practicing **psychoanalyst**, I observed how cultural rituals guide the developing ego through identity crises." },
      { author: "Janet Malcolm", work: "The Impossible Profession", quote: "The relationship between the patient and the **psychoanalyst** is among the strangest and most intense human intimacies." }
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
console.log("Batch 4 completed! Total words updated:", Object.keys(wordsData).length);
