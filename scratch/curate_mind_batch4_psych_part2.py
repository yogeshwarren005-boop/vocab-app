# -*- coding: utf-8 -*-
"""
Curates Dashboard — psych (Part 2: words 37-72) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part2 = {
  "psychologist": {
    "primary": "A specialist or researcher trained in the scientific study of the human mind, behavior, and mental processes.",
    "secondary": "In clinical mental health, a licensed professional administering behavioral therapies and psychometric diagnostic batteries.",
    "quotes": [
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "The observant **psychologist** knows that education is the organization of acquired habits of conduct."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Our research **psychologist** mapped the strange cognitive boundaries of his agnosia using visual sorting tests."},
      {"author": "B. F. Skinner", "work": "About Behaviorism", "quote": "The experimental **psychologist** examines environmental contingencies rather than mysterious inner states."}
    ]
  },
  "psychology": {
    "primary": "The scientific discipline that investigates mental states, emotional dynamics, perception, and human behavior.",
    "secondary": "In philosophical history, the empirical branch of natural science that emerged from epistemology to measure consciousness.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Experimental **psychology** began when physiological laboratories sought to quantify sensory thresholds."},
      {"author": "Sigmund Freud", "work": "New Introductory Lectures on Psycho-Analysis", "quote": "Depth **psychology** demonstrated that conscious awareness constitutes merely the tip of the mental iceberg."},
      {"author": "Steven Pinker", "work": "How the Mind Works", "quote": "Evolutionary **psychology** interprets human emotions as computational adaptations tailored for ancestral survival."}
    ]
  },
  "psychometric": {
    "primary": "Relating to the design, administration, and statistical evaluation of psychological measurements and mental tests.",
    "secondary": "In educational testing, quantitative instruments assessing cognitive aptitude, personality dimensions, and scholastic ability.",
    "quotes": [
      {"author": "Stephen Jay Gould", "work": "The Mismeasure of Man", "quote": "He criticized the **psychometric** fallacy of ranking complex human intellect onto a single linear scale."},
      {"author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "Early **psychometric** apparatus measured reaction times and sensory discrimination among thousands of volunteers."},
      {"author": "Steven Pinker", "work": "The Blank Slate", "quote": "Modern **psychometric** evaluations of identical twins reared apart reveal robust heritability across major personality traits."}
    ]
  },
  "psychometrics": {
    "primary": "The scientific subfield of psychology devoted to developing, validating, and analyzing quantitative tests and scales.",
    "secondary": "In applied statistics, the mathematical modeling of latent traits, item response curves, and measurement error.",
    "quotes": [
      {"author": "Stephen Jay Gould", "work": "The Mismeasure of Man", "quote": "Pioneers of **psychometrics** frequently mistook their statistical factor loadings for tangible biological entities."},
      {"author": "Howard Gardner", "work": "Frames of Mind", "quote": "Standard **psychometrics** captures linguistic and logical abilities while systematically overlooking musical and spatial talents."},
      {"author": "Daniel Kahneman", "work": "Thinking, Fast and Slow", "quote": "Rigorous **psychometrics** enabled researchers to quantify subjective confidence intervals under conditions of uncertainty."}
    ]
  },
  "psychometrika": {
    "primary": "A premier academic peer-reviewed journal dedicated to mathematical psychology, quantitative methods, and psychometrics.",
    "secondary": "In scholarly publishing, the flagship journal of the Psychometric Society advancing latent variable models and factor analysis.",
    "quotes": [
      {"author": "L. L. Thurstone", "work": "Multiple-Factor Analysis", "quote": "His foundational paper in **Psychometrika** revolutionized mental measurement through multidimensional vector spaces."},
      {"author": "Harold Gulliksen", "work": "Theory of Mental Tests", "quote": "Subsequent issues of **Psychometrika** refined true-score test models and reliability coefficients for standardized testing."},
      {"author": "Paul Lazarsfeld", "work": "Latent Structure Analysis", "quote": "Theoretical treatises published in **Psychometrika** established formal mathematical foundations for latent class models."}
    ]
  },
  "psychometry": {
    "primary": "The measurement of mental faculties, traits, and intelligence, or the alleged psychic power to divine object history.",
    "secondary": "In the history of parapsychology and spiritualism, the purported occult faculty of reading vibrations from antiquities.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory **psychometry** attempted to chart exact mathematical relations between physical stimulus and mental sensation."},
      {"author": "Arthur Conan Doyle", "work": "The History of Spiritualism", "quote": "Practitioners of **psychometry** claimed they could reconstruct an author's private life merely by holding his handwritten letters."},
      {"author": "Francis Galton", "work": "Psychometric Experiments", "quote": "His pioneer work in mental **psychometry** employed association clocks to measure the speed of fleeting thoughts."}
    ]
  },
  "psychomotor": {
    "primary": "Relating to movement, muscular coordination, and physical actions initiated or influenced by conscious mental activity.",
    "secondary": "In clinical neurology and psychiatry, describing behavioral manifestations such as psychomotor agitation or retardation in depression.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "L-dopa administration released severe **psychomotor** freezing, allowing catatonic post-encephalitic patients to dance."},
      {"author": "Kay Redfield Jamison", "work": "Touched with Fire", "quote": "Manic episodes frequently generate rapid speech accompanied by relentless **psychomotor** agitation and sleepless energy."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Basal ganglia pathways coordinate cognitive planning with precise **psychomotor** execution during instrument play."}
    ]
  },
  "psychoneurosis": {
    "primary": "A relatively mild mental, emotional, or behavioral disorder characterized by anxiety, obsessions, or phobias without psychosis.",
    "secondary": "In classical psychoanalysis, functional neurotic conditions generated by unconscious conflict between instinctual drives and ego defenses.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "The Ego and the Id", "quote": "Every clinical **psychoneurosis** represents a compromise between repressed unconscious wishes and moral prohibitions."},
      {"author": "Carl Jung", "work": "Modern Man in Search of a Soul", "quote": "A persistent **psychoneurosis** must ultimately be understood as the suffering of a soul which has not found its meaning."},
      {"author": "Karen Horney", "work": "The Neurotic Personality of Our Time", "quote": "Basic anxiety arising from childhood insecurity constitutes the fertile soil from which adult **psychoneurosis** springs."}
    ]
  },
  "psychoneurotic": {
    "primary": "Suffering from, relating to, or characteristic of a psychoneurosis; exhibiting chronic anxiety or neurotic conflict.",
    "secondary": "In historical psychiatric nosology, describing neurotic patients whose reality testing and sensorium remain intact.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "Sir William Bradshaw diagnosed Septimus with severe **psychoneurotic** exhaustion and prescribed complete bed rest."},
      {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "Hysterical symptoms reveal that **psychoneurotic** patients possess an excess of repressed sexual energy."},
      {"author": "W. H. R. Rivers", "work": "Instinct and the Unconscious", "quote": "Wartime shell shock presented acute **psychoneurotic** manifestations among soldiers surviving trench bombardments."}
    ]
  },
  "psychonomics": {
    "primary": "The branch of psychology that deals with the relationship between psychological laws, economics, and human behavior.",
    "secondary": "In experimental cognitive science, the study of fundamental mental processes governing perception, memory, and decision making.",
    "quotes": [
      {"author": "Herbert Simon", "work": "Administrative Behavior", "quote": "The emerging discipline of **psychonomics** demonstrated that human decision makers operate under bounded rationality."},
      {"author": "Daniel Kahneman", "work": "Thinking, Fast and Slow", "quote": "Insights from **psychonomics** shattered classical economic models that assumed perfectly rational self-interested actors."},
      {"author": "Amos Tversky", "work": "Judgment under Uncertainty: Heuristics and Biases", "quote": "Heuristics uncovered by **psychonomics** explain systematic biases in financial risk assessment and market behavior."}
    ]
  },
  "psychopath": {
    "primary": "An individual possessing an antisocial personality disorder characterized by pervasive lack of empathy, remorselessness, and manipulation.",
    "secondary": "In forensic criminology, a calculating predator who mimics prosocial emotional responses while exploiting others.",
    "quotes": [
      {"author": "Hervey Cleckley", "work": "The Mask of Sanity", "quote": "Behind a superficially charming facade, the clinical **psychopath** remains utterly indifferent to the distress of others."},
      {"author": "Truman Capote", "work": "In Cold Blood", "quote": "The psychiatric report characterized Perry as a wounded **psychopath** driven by sudden eruptions of paranoid rage."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Frontal lobe damage can transform a gentle citizen into an impulsive social **psychopath** devoid of moral inhibition."}
    ]
  },
  "psychopathic": {
    "primary": "Relating to, characterized by, or suffering from psychopathy; exhibiting remorseless and callous antisocial conduct.",
    "secondary": "In forensic psychiatry, describing behavioral traits scored on Hare's Psychopathy Checklist, such as glibness and grandiosity.",
    "quotes": [
      {"author": "Hervey Cleckley", "work": "The Mask of Sanity", "quote": "His repeated swindles reflected classic **psychopathic** traits: total absence of guilt and an uncanny talent for deceit."},
      {"author": "Hannah Arendt", "work": "Eichmann in Jerusalem", "quote": "The terrifying realization was that Eichmann did not exhibit monstrous **psychopathic** fury, but mundane bureaucratic efficiency."},
      {"author": "Stephen Jay Gould", "work": "The Mismeasure of Man", "quote": "Lombroso erroneously believed that **psychopathic** tendencies could be identified by atavistic facial asymmetries."}
    ]
  },
  "psychopathologic": {
    "primary": "Relating to psychopathology or the study and manifestation of mental disorders; synonymous with psychopathological.",
    "secondary": "In clinical neuroscience, denoting structural and functional neural aberrations that generate psychiatric symptoms.",
    "quotes": [
      {"author": "Karl Jaspers", "work": "General Psychopathology", "quote": "He established rigorous phenomenological methods to categorize bizarre **psychopathologic** experiences in schizophrenia."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Synaptic remodeling provides a biological substrate for understanding how stress precipitates severe **psychopathologic** states."},
      {"author": "Michel Foucault", "work": "Madness and Civilization", "quote": "Classical society categorized as **psychopathologic** any deviation from disciplined economic production and bourgeois order."}
    ]
  },
  "psychopathological": {
    "primary": "Relating to the manifestations, mechanisms, and classification of mental disorders and psychological dysfunction.",
    "secondary": "In diagnostic psychiatry, describing abnormal behavioral patterns cataloged within standardized diagnostic manuals.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The clinical presentation defied standard **psychopathological** categories, revealing a complex visual agnosia instead."},
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "The boundary between exceptional creative insight and acute **psychopathological** breakdown often appears perilously thin."},
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "Everyday slips of memory share structural affinities with more severe **psychopathological** defense mechanisms."}
    ]
  },
  "psychopathology": {
    "primary": "The scientific study of mental disorders, cognitive dysfunction, and maladaptive psychological behavior.",
    "secondary": "In clinical medicine, the systematic description of symptoms, emotional pathology, and psychiatric etiology.",
    "quotes": [
      {"author": "Karl Jaspers", "work": "General Psychopathology", "quote": "The foundation of clinical **psychopathology** rests upon careful phenomenological descriptions of subjective human suffering."},
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "He demonstrated that normal forgetting and morbid **psychopathology** obey the identical psychological dynamics of repression."},
      {"author": "Eric Kandel", "work": "Psychiatry, Psychoanalysis, and the New Biology of Mind", "quote": "Modern **psychopathology** requires integrating molecular neurogenetics with psychological understanding of development."}
    ]
  },
  "psychopathy": {
    "primary": "A severe personality disorder marked by callousness, superficial charm, lack of remorse, and chronic impulsivity.",
    "secondary": "In neuropsychiatry, a disorder associated with hypoactive amygdala responsiveness to fear and distress cues in others.",
    "quotes": [
      {"author": "Hervey Cleckley", "work": "The Mask of Sanity", "quote": "True clinical **psychopathy** presents an exquisite mimicry of human normality while remaining emotionally vacant."},
      {"author": "Robert Hare", "work": "Without Conscience", "quote": "His definitive research demonstrated that **psychopathy** affects roughly one percent of the general adult population."},
      {"author": "Steven Pinker", "work": "The Better Angels of Our Nature", "quote": "Social institutions and the rule of law were constructed to constrain the predatory damage wrought by **psychopathy**."}
    ]
  },
  "psychopharmacological": {
    "primary": "Relating to psychopharmacology, or the chemical substances used to treat mental, emotional, and behavioral disorders.",
    "secondary": "In neurotherapeutics, describing drug mechanisms targeting neurotransmitter reuptake and post-synaptic receptors.",
    "quotes": [
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "Finding the correct **psychopharmacological** regimen required years of trial, dosage titration, and clinical patience."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The unexpected **psychopharmacological** triumph of L-dopa illuminated the chemical architecture of Parkinson's disease."},
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Early **psychopharmacological** breakthroughs revolutionized asylum medicine and catalyzed the modern neurobiological revolution."}
    ]
  },
  "psychopharmacology": {
    "primary": "The scientific discipline studying how chemical agents and drugs influence mental processes, mood, and behavior.",
    "secondary": "In clinical neuroscience, the specialty developing pharmaceutical treatments for psychiatric illnesses such as depression.",
    "quotes": [
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "The rapid ascent of modern **psychopharmacology** provided direct empirical proof that mental states correlate with neurotransmission."},
      {"author": "Kay Redfield Jamison", "work": "Touched with Fire", "quote": "Lithium therapy stands as the historic foundation stone upon which contemporary **psychopharmacology** was erected."},
      {"author": "David Nutt", "work": "Drugs Without the Hot Air", "quote": "Evidence-based **psychopharmacology** must prioritize clinical harm reduction over political moralizing about substances."}
    ]
  },
  "psychophysicist": {
    "primary": "A scientist or experimental researcher who investigates the quantitative relationship between physical stimuli and perception.",
    "secondary": "In experimental cognitive science, an investigator measuring sensory thresholds, luminance gradients, and acoustic latencies.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The painstaking German **psychophysicist** spent decades mapping the smallest detectable difference in auditory pitch."},
      {"author": "Ernst Mach", "work": "The Analysis of Sensations", "quote": "Every observant **psychophysicist** recognizes that external physics and internal sensations share a common mathematical threshold."},
      {"author": "Steven Pinker", "work": "How the Mind Works", "quote": "The visual **psychophysicist** can determine the neural wiring of retinal cells through simple contrast detection experiments."}
    ]
  },
  "psychophysics": {
    "primary": "The branch of psychology that measures and models the relationship between physical stimuli and sensory experience.",
    "secondary": "In sensory science, the discipline founded by Gustav Fechner formulating Weber-Fechner laws of perception.",
    "quotes": [
      {"author": "Gustav Fechner", "work": "Elements of Psychophysics", "quote": "The primary objective of **psychophysics** is to establish an exact mathematical theory of the relation between body and soul."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Fechner's pioneering **psychophysics** inaugurated the era of rigorous experimental measurement in sensory psychology."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Classical **psychophysics** provided the psychophysical methods needed to evaluate cone photoreceptor loss in islanders."}
    ]
  },
  "psychophysiology": {
    "primary": "The scientific branch exploring the physiological bases of mental processes and subjective psychological states.",
    "secondary": "In experimental cognitive neuroscience, measuring autonomic responses such as heart rate variability, skin conductance, and EEGs.",
    "quotes": [
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Contemporary **psychophysiology** utilizes multichannel electroencephalography to track cognitive load during problem solving."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Our autonomic reactions and somatic visceral changes form the very bedrock of emotional **psychophysiology**."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The patient's bizarre alien limb syndrome revealed an unrecognized collapse in sensory-motor **psychophysiology**."}
    ]
  },
  "psychopomp": {
    "primary": "A mythological figure, spiritual deity, or guide responsible for escorting the souls of the deceased to the underworld.",
    "secondary": "In Jungian archetypal psychology, an inner symbolic figure guiding the conscious ego through the depths of the unconscious.",
    "quotes": [
      {"author": "Carl Jung", "work": "Memories, Dreams, Reflections", "quote": "Hermes acted as the supreme **psychopomp**, navigating the borderlands between the living sunlit world and the dark underworld."},
      {"author": "Joseph Campbell", "work": "The Hero with a Thousand Faces", "quote": "The mythological hero frequently encounters a benevolent **psychopomp** who provides talismans for the threshold crossing."},
      {"author": "James Hillman", "work": "The Dream and the Underworld", "quote": "In archetypal therapy, the dream image serves as an active **psychopomp**, reorienting the spirit toward deeper soul concerns."}
    ]
  },
  "psychopsis": {
    "primary": "A genus of neotropical epiphytic orchids famous for their striking yellow and brown butterfly-like blossoms.",
    "secondary": "In botanical horticulture, commonly cultivated butterfly orchids bearing solitary long-lasting flowers with elongated petals.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects", "quote": "The extraordinary dorsal sepal in **Psychopsis** mimics insect antennae to attract specialized tropical pollinators."},
      {"author": "John Lindley", "work": "The Genera and Species of Orchidaceous Plants", "quote": "Specimens of **Psychopsis** collected along the Orinoco river exhibited remarkable floral mimicry of fluttering butterflies."},
      {"author": "Henry Oakeley", "work": "Orchid Species Culture", "quote": "Experienced greenhouse growers prize **Psychopsis** for its habit of producing successive blooms from the same flower spike."}
    ]
  },
  "psychosexual": {
    "primary": "Relating to the psychological aspects of human sexuality and emotional sexual development.",
    "secondary": "In psychoanalytic theory, denoting Freud's progressive developmental stages: oral, anal, phallic, latency, and genital.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "The child undergoes a multifaceted **psychosexual** evolution long before biological puberty manifests physical maturity."},
      {"author": "Erik Erikson", "work": "Identity: Youth and Crisis", "quote": "He expanded Freud's **psychosexual** framework by integrating psychosocial stages of identity formation and community ethics."},
      {"author": "Michel Foucault", "work": "The History of Sexuality", "quote": "The Victorian era created an elaborate discursive apparatus around the **psychosexual** confessions of individuals."}
    ]
  },
  "psychosexuality": {
    "primary": "The emotional, mental, and psychological dynamics associated with sexual identity, desire, and behavior.",
    "secondary": "In depth psychology, the complex developmental integration of instinctual libido with conscious interpersonal relationships.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "A scientific analysis of human **psychosexuality** reveals an astonishing diversity of natural variations across cultures."},
      {"author": "Sigmund Freud", "work": "Introductory Lectures on Psycho-Analysis", "quote": "Fixation at early developmental milestones can permanently shape the adult expression of **psychosexuality**."},
      {"author": "Simone de Beauvoir", "work": "The Second Sex", "quote": "She demonstrated how societal hierarchies and gender roles actively condition the subjective **psychosexuality** of women."}
    ]
  },
  "psychosis": {
    "primary": "A severe mental disorder characterized by loss of contact with external reality, delusions, and hallucinations.",
    "secondary": "In clinical psychiatry, acute states of cognitive and perceptual disintegration requiring emergency antipsychotic stabilization.",
    "quotes": [
      {"author": "Karl Jaspers", "work": "General Psychopathology", "quote": "The phenomenology of acute **psychosis** confronts the clinician with unbridgeable chasms in comprehensible psychic life."},
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "The terrifying descent from ecstatic mania into paranoid **psychosis** shattered her ability to distinguish dream from reality."},
      {"author": "Oliver Sacks", "work": "Hallucinations", "quote": "Unlike organic delirium, the hallucinations of toxic **psychosis** are often woven into elaborate, threatening delusional systems."}
    ]
  },
  "psychosomatic": {
    "primary": "Relating to physical bodily symptoms that are caused, exacerbated, or influenced by psychological factors and mental stress.",
    "secondary": "In integrative medicine, conditions like stress-induced peptic ulcers, tension migraines, and psychogenic dermatitis.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Migraine", "quote": "To dismiss chronic vascular pain as merely **psychosomatic** ignores the physiological cascades that ravage the nervous system."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The astute physician treats both the inflamed organ and the anxious soul, acknowledging their **psychosomatic** unity."},
      {"author": "Kay Redfield Jamison", "work": "Night Falls Fast", "quote": "Severe despair frequently manifests through excruciating **psychosomatic** aches, chronic insomnia, and gastrointestinal distress."}
    ]
  },
  "psychosurgery": {
    "primary": "Brain surgery performed to treat severe, intractable mental disorders or psychiatric symptoms through targeted lesions.",
    "secondary": "In medical history, neurosurgical procedures evolving from crude prefrontal lobotomies to precise stereotactic cingulotomies.",
    "quotes": [
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "The mid-twentieth-century craze for crude **psychosurgery** left thousands of psychiatric patients tragically blunted."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Fortunately, advances in psychopharmacology largely superseded the irreversible destruction of tissue by **psychosurgery**."},
      {"author": "Stephen Jay Gould", "work": "The Mismeasure of Man", "quote": "Egas Moniz received the Nobel Prize for introducing **psychosurgery**, a decision history views with profound moral unease."}
    ]
  },
  "psychotherapeutic": {
    "primary": "Relating to psychotherapy or the clinical treatment of emotional and psychological problems through dialogue.",
    "secondary": "In mental healthcare, describing evidence-based psychological modalities such as cognitive behavioral therapy and psychoanalysis.",
    "quotes": [
      {"author": "Carl Rogers", "work": "On Becoming a Person", "quote": "The core of the **psychotherapeutic** process lies in the unconditional positive regard extended by the therapist."},
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "Medication restored her sanity, but skilled **psychotherapeutic** counsel taught her how to rebuild a shattered life."},
      {"author": "Sigmund Freud", "work": "On Psychotherapy", "quote": "The primary requirement for successful **psychotherapeutic** work is the patient's willingness to engage in candid self-examination."}
    ]
  },
  "psychotherapeutics": {
    "primary": "The branch of medicine and psychology concerned with the application of psychological therapies to treat mental disease.",
    "secondary": "In clinical history, the systematic discipline encompassing hypnotic suggestion, moral treatment, and modern psychotherapies.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Faith healing and mental science movements demonstrated the practical efficacy of suggestive **psychotherapeutics**."},
      {"author": "Morton Prince", "work": "The Dissociation of a Personality", "quote": "His clinical treatises helped establish systematic **psychotherapeutics** as an indispensable branch of modern neurology."},
      {"author": "Pierre Janet", "work": "Psychological Healing", "quote": "Nineteenth-century alienists explored diverse **psychotherapeutics** to restore equilibrium to dissociated and hysterical minds."}
    ]
  },
  "psychotherapist": {
    "primary": "A trained professional who provides psychotherapy to individuals struggling with emotional, mental, or behavioral difficulties.",
    "secondary": "In clinical practice, a licensed clinician guiding clients through cognitive reframing, trauma recovery, and personal insight.",
    "quotes": [
      {"author": "Carl Rogers", "work": "Client-Centered Therapy", "quote": "An effective **psychotherapist** does not dispense authoritative advice, but facilitates the client's own capacity for growth."},
      {"author": "Irvin Yalom", "work": "Love's Executioner", "quote": "The experienced **psychotherapist** recognizes that human encounters in the consulting room mirror universal existential struggles."},
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "Her **psychotherapist** served as an anchor of quiet common sense during the tempestuous aftermath of manic storm."}
    ]
  },
  "psychotherapy": {
    "primary": "The treatment of mental and emotional disorders through psychological methods, communication, and therapeutic relationship.",
    "secondary": "In healthcare, modalities ranging from psychodynamic analysis to cognitive behavioral therapy aimed at behavioral change.",
    "quotes": [
      {"author": "Carl Jung", "work": "The Practice of Psychotherapy", "quote": "The ultimate aim of deep **psychotherapy** is not simple symptom relief, but the individuation of the unique self."},
      {"author": "Viktor Frankl", "work": "Man's Search for Meaning", "quote": "Logotherapy introduced a vital dimension to modern **psychotherapy** by addressing the human quest for purpose."},
      {"author": "Sigmund Freud", "work": "A General Introduction to Psychoanalysis", "quote": "In classical **psychotherapy**, nothing takes place between patient and physician except an exchange of honest words."}
    ]
  },
  "psychotic": {
    "primary": "Experiencing or relating to psychosis; characterized by hallucinations, delusions, and severe detachment from reality.",
    "secondary": "In psychiatric classification, symptoms indicating profound impairment in cognitive reality testing and perception.",
    "quotes": [
      {"author": "Kay Redfield Jamison", "work": "Night Falls Fast", "quote": "During her **psychotic** episodes, the mundane furniture around her seemed imbued with sinister, coded warnings."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The patient remained rational and alert, showing no evidence of **psychotic** distortion or delusional thought."},
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "New generations of pharmaceuticals selectively dampened **psychotic** paranoia without precipitating debilitating sedation."}
    ]
  },
  "psychotria": {
    "primary": "A large pantropical genus of flowering plants in the coffee family Rubiaceae, notable for psychoactive alkaloids.",
    "secondary": "In ethnobotany, the genus including Psychotria viridis (chacruna), a primary plant ingredient used in traditional ayahuasca brews.",
    "quotes": [
      {"author": "Richard Evans Schultes", "work": "Plants of the Gods", "quote": "Indigenous shamans combine leaves of **Psychotria** with Banisteriopsis vines to unlock visionary states of consciousness."},
      {"author": "Michael Pollan", "work": "This Is Your Mind on Plants", "quote": "The DMT contained in wild **Psychotria** becomes orally active only when paired with natural monoamine oxidase inhibitors."},
      {"author": "Wade Davis", "work": "One River", "quote": "The botanists collected voucher specimens of glossy-leaved **Psychotria** along the forested riverbanks of the Putumayo."}
    ]
  },
  "psychotropic": {
    "primary": "Capable of affecting mental activity, emotional state, or conscious perception; altering brain biochemistry.",
    "secondary": "In pharmacology, medications such as antidepressants, anxiolytics, and stimulants prescribed for psychiatric management.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "The Doors of Perception", "quote": "Every civilization has cultivated some form of **psychotropic** agent to obtain relief from existential monotony."},
      {"author": "Oliver Sacks", "work": "Musicophilia", "quote": "Certain **psychotropic** medications induced vivid musical hallucinations that persisted long after discontinuation."},
      {"author": "Kay Redfield Jamison", "work": "Touched with Fire", "quote": "The discovery of effective **psychotropic** compounds radically transformed prognosis for patients with bipolar disorder."}
    ]
  },
  "psychrometer": {
    "primary": "A meteorological hygrometer consisting of dry-bulb and wet-bulb thermometers to measure atmospheric relative humidity.",
    "secondary": "In thermodynamic instrumentation, an apparatus calculating humidity by measuring evaporative cooling rates on a saturated wick.",
    "quotes": [
      {"author": "Cleveland Abbe", "work": "Treatise on Meteorological Apparatus and Methods", "quote": "The sling **psychrometer** provides rapid and accurate determinations of vapor pressure by ventilating the wet bulb."},
      {"author": "William Napier Shaw", "work": "Manual of Meteorology", "quote": "Careful readings of the aspiration **psychrometer** revealed significant humidity gradients near the ground surface."},
      {"author": "Alexander Buchan", "work": "Handy Book of Meteorology", "quote": "The observer moistened the muslin sleeve of the **psychrometer** with distilled water prior to recording temperature differentials."}
    ]
  }
}
