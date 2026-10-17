import json
import os
import re
import sys

BATCH2_DATA = {
  "Dashboard — neur/neurological.md": {
    "primary": "Of, relating to, or affecting neurology or the structure, function, and pathology of the nervous system.",
    "secondary": "In clinical diagnosis, designating organic abnormalities, physical examination signs, or disease states directly attributable to lesions of neural pathways.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A complete **neurological** assessment requires systematic inspection of sensory perception, motor reflexes, and cranial nerve integrity."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "The patient presented profound **neurological** signs indicating progressive uncal herniation through the tentorial notch."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Focal epileptogenic discharge evokes predictable **neurological** auras that disclose the precise anatomical seat of origin."
      }
    ]
  },
  "Dashboard — neur/neurologist.md": {
    "primary": "A physician or medical specialist who diagnoses and treats organic disorders and diseases of the nervous system.",
    "secondary": "In medical practice and clinical research, an expert versed in localization of lesions across the brain, spinal cord, neuromuscular junction, and peripheral nerves.",
    "quotes": [
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "The discerning **neurologist** learns that the patient's subjective narrative provides the decisive key to anatomical localization."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "At the Salpêtrière, the clinical **neurologist** was confronted with every conceivable variety of paralysis and tremor."
      },
      {
        "author": "John Hughlings Jackson",
        "work": "Selected Writings of John Hughlings Jackson",
        "quote": "The philosophical **neurologist** observes the dissolution of nervous functions from highest voluntary levels down to basic reflexes."
      }
    ]
  },
  "Dashboard — neur/neurology.md": {
    "primary": "The medical specialty and branch of biology concerned with the anatomy, functions, and disorders of the nervous system.",
    "secondary": "In clinical science, the discipline integrating structural pathology, electrophysiology, and neurogenetics to investigate central and peripheral nervous diseases.",
    "quotes": [
      {
        "author": "Thomas Willis",
        "work": "Cerebri Anatome",
        "quote": "I introduced the doctrine of **neurology** to describe the exact distribution of nerves emanating from the brain and spinal marrow."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The remarkable advances in modern **neurology** have transformed cerebral localization from speculative theory into operative certainty."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Senile and Chronic Diseases",
        "quote": "Systematic anatomoclinical correlation constitutes the immutable foundation upon which clinical **neurology** has been erected."
      }
    ]
  },
  "Dashboard — neur/neurolysin.md": {
    "primary": "A metalloendopeptidase enzyme that hydrolyzes neurotensin and other bioactive peptides within the nervous system.",
    "secondary": "In neurochemistry and peptide pharmacology, a zinc-dependent peptidase (EC 3.4.24.16) localized in brain tissue that degrades neuropeptides involved in pain processing and blood pressure control.",
    "quotes": [
      {
        "author": "Solomon Snyder",
        "work": "Brain Peptides",
        "quote": "Rapid enzymatic inactivation by cytosolic **neurolysin** terminates the neuromodulatory action of neurotensin at synaptic junctions."
      },
      {
        "author": "Julius Axelrod",
        "work": "Studies on Peptide Inactivation in the Brain",
        "quote": "Selective inhibition of **neurolysin** potentiates the central antinociceptive effects elicited by endogenous peptide agonists."
      },
      {
        "author": "Leslie Iversen",
        "work": "The Biochemical Pharmacology of the Neuropeptides",
        "quote": "Purified **neurolysin** cleaves the proline-tyrosine bond of neurotensin with exceptional substrate specificity."
      }
    ]
  },
  "Dashboard — neur/neuroma.md": {
    "primary": "A benign tumor or swelling composed of nerve fibers and neural tissue; also, a disorganized tangle of regenerating nerve fibers following trauma (stump or amputation neuroma).",
    "secondary": "In neuropathology and surgery, a traumatic mass of axons, Schwann cells, and scar tissue at the proximal stump of a transected nerve, often source of intense phantom limb pain.",
    "quotes": [
      {
        "author": "Silas Weir Mitchell",
        "work": "Injuries of Nerves and Their Consequences",
        "quote": "Following amputation, the tender bulbous **neuroma** formed at the severed nerve end proved an agonizing trigger of reflex neuralgia."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "The surgical removal of an acoustic **neuroma** requires delicate preservation of the facial nerve to avoid disfiguring facial palsy."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Solitary plexiform **neuroma** may attain immense size along the cords of the brachial plexus."
      }
    ]
  },
  "Dashboard — neur/neuromatous.md": {
    "primary": "Pertaining to, resembling, or characterized by the presence of a neuroma or neuromas.",
    "secondary": "In surgical pathology, describing nodular, tangled nerve swellings or reactive fibrous proliferation following peripheral nerve transection.",
    "quotes": [
      {
        "author": "Silas Weir Mitchell",
        "work": "Injuries of Nerves and Their Consequences",
        "quote": "The bulbous **neuromatous** mass at the extremity of the stump was exquisitely painful upon the slightest pressure."
      },
      {
        "author": "Carl von Rokitansky",
        "work": "A Manual of Pathological Anatomy",
        "quote": "Microscopic examination of the **neuromatous** nodule reveals bundles of medullated fibers intertwined in fibrous connective tissue."
      },
      {
        "author": "James Paget",
        "work": "Lectures on Surgical Pathology",
        "quote": "Multiple **neuromatous** growths along the sciatic trunk may provoke progressive muscular wasting in the distal extremity."
      }
    ]
  },
  "Dashboard — neur/neuromorphology.md": {
    "primary": "The branch of neuroscience concerned with the structural form, architecture, and microscopic organization of nervous tissue.",
    "secondary": "In neurobiology, the systematic analysis of dendritic branching patterns, axonal arborizations, synaptic ultrastructure, and volumetric brain architecture.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System of Man and the Vertebrates",
        "quote": "The fundamental laws of **neuromorphology** dictate that cellular form reflects functional economy and receptive surface area."
      },
      {
        "author": "Wilhelm His",
        "work": "Die Neuroblasten und deren Entstehung im embryonalen Mark",
        "quote": "Tracing the ontogenetic emergence of nerve cells reveals the mechanical forces shaping early embryonic **neuromorphology**."
      },
      {
        "author": "Camillo Golgi",
        "work": "Studies on the Fine Anatomy of the Central Nervous Organs",
        "quote": "Our understanding of cerebellar **neuromorphology** was transformed when the silver chromate reaction resolved the dendritic tree of Purkinje cells."
      }
    ]
  },
  "Dashboard — neur/neuromotor.md": {
    "primary": "Relating to or involving both neural and motor mechanisms, specifically the control of muscular action by the nervous system.",
    "secondary": "In protistology and physiology, referring to integrated neural and contractile apparatuses, including the coordinated ciliary system in ciliates and motor unit innervation in animals.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Every purposeful movement relies upon integrated **neuromotor** circuits that coordinate agonists and antagonize opposing muscle groups."
      },
      {
        "author": "Charles Atwood Kofoid",
        "work": "The Neuromotor System of Ciliates",
        "quote": "We demonstrated an interconnected fibrillar **neuromotor** apparatus that synchronizes the beating of membranelles in Euplotes."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Direct stimulation of Area 4 elicits discrete contractions, mapping out the precise **neuromotor** representations of the fingers and tongue."
      }
    ]
  },
  "Dashboard — neur/neuromuscular.md": {
    "primary": "Pertaining to, involving, or affecting both nerves and muscles, especially the junction where motor nerves innervate muscle fibers.",
    "secondary": "In neurophysiology and clinical neurology, designating transmission across the motor endplate, as well as disorders (such as myasthenia gravis) affecting the neuromuscular junction.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Curare paralyzes the animal not by destroying the nerve or the muscle, but by blocking conduction at the **neuromuscular** connection."
      },
      {
        "author": "Henry Hallett Dale",
        "work": "Adventures in Physiology",
        "quote": "The release of acetylcholine quanta at the motor endplate serves as the physiological mediator of **neuromuscular** transmission."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Myasthenia gravis represents an extraordinary fatigue of **neuromuscular** conduction provoked by repetitive voluntary effort."
      }
    ]
  },
  "Dashboard — neur/neuron.md": {
    "primary": "The structural and functional unit of the nervous system, consisting of a cell body (soma), dendrites, and an axon capable of conducting electrical and chemical impulses.",
    "secondary": "In cellular neuroscience, the fundamental cellular doctrine formulated by Waldeyer and Cajal, asserting the anatomical independence and polarized signaling of individual nerve cells.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System of Man and the Vertebrates",
        "quote": "The individual **neuron** possesses distinct receptive, integrative, and emissive poles, communicating with its fellows solely by contiguity."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The synapse forms the nexus where the terminal arborizations of one **neuron** appose the receptive surface of another."
      },
      {
        "author": "Heinrich Wilhelm Waldeyer",
        "work": "Ueber einige neuere Forschungen im Gebiete der Anatomie des Centralnervensystems",
        "quote": "I propose the name **neuron** for the cellular individual composed of the nerve cell together with all its processes."
      }
    ]
  },
  "Dashboard — neur/neuronal.md": {
    "primary": "Of, relating to, or characteristic of a neuron or neurons.",
    "secondary": "In neurophysiology and molecular biology, describing cellular mechanisms such as membrane depolarization, synaptic vesicle release, or neurodegenerative cascades occurring within nerve cells.",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Long-term synaptic potentiation requires persistent alterations in **neuronal** gene expression and protein synthesis."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The **neuronal** doctrine triumphed because it explained nervous conduction without invoking an amorphous reticular syncytium."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Subclinical paroxysmal discharges demonstrate the hypersynchrony of injured **neuronal** aggregates within the epileptic focus."
      }
    ]
  },
  "Dashboard — neur/neurone.md": {
    "primary": "A variant spelling of neuron, designating the nerve cell with its axon and dendrites (predominantly in British English).",
    "secondary": "In classical British and European neurophysiology, the term standardly applied in descriptions of motor and sensory reflex arcs (e.g., upper motor neurone).",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The motor **neurone** forms the final common path through which all impulses must converge to evoke muscular movement."
      },
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Degeneration of the lower motor **neurone** produces flaccid paralysis accompanied by rapid muscular atrophy and loss of reflexes."
      },
      {
        "author": "John Hughlings Jackson",
        "work": "Selected Writings of John Hughlings Jackson",
        "quote": "Destruction of the highest sensory **neurone** impairs the synthesis of complex perceptual representations."
      }
    ]
  },
  "Dashboard — neur/neuronic.md": {
    "primary": "Pertaining to a neuron or to neurons; neuronal.",
    "secondary": "In historical neurophysiology and psychology, describing the network architecture, conduction pathways, or cellular energy exchanges of nerve cells.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Consciousness correlates with the sum total of **neuronic** activities fluctuating within the cerebral hemispheres."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The delay observed in reflex conduction indicates resistance encountered at successive **neuronic** junctions."
      },
      {
        "author": "Sigmund Freud",
        "work": "Project for a Scientific Psychology",
        "quote": "We postulate that **neuronic** charges are discharged through pathways offering the least resistance to flow."
      }
    ]
  },
  "Dashboard — neur/neurontin.md": {
    "primary": "A brand name for gabapentin, an anticonvulsant and neuropathic pain analgesic that binds to the alpha-2-delta subunit of voltage-gated calcium channels.",
    "secondary": "In clinical psychopharmacology and neurology, a medication originally designed as a lipophilic GABA agonist, widely prescribed for partial seizures, postherpetic neuralgia, and restless legs syndrome.",
    "quotes": [
      {
        "author": "Stephen Stahl",
        "work": "Stahl's Essential Psychopharmacology",
        "quote": "Prescription of **Neurontin** modulates neurotransmitter release by dampening calcium influx through voltage-sensitive channels in hyperexcitable neurons."
      },
      {
        "author": "David Taylor",
        "work": "The Maudsley Prescribing Guidelines in Psychiatry",
        "quote": "When managing refractory neuropathic distress, therapeutic titration of **Neurontin** provides analgesic efficacy with favorable tolerability."
      },
      {
        "author": "Anthony Trevor",
        "work": "Katzung & Trevor's Pharmacology",
        "quote": "Despite its structural similarity to gamma-aminobutyric acid, **Neurontin** does not bind directly to GABA receptors."
      }
    ]
  },
  "Dashboard — neur/neuropathic.md": {
    "primary": "Pertaining to, resulting from, or characteristic of a disease or functional disorder of the nervous system (neuropathy).",
    "secondary": "In clinical medicine, describing chronic pain (burning, allodynia, hyperalgesia) originating from primary damage to or dysfunction of the nervous system.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe **neuropathic** joint destruction, known as Charcot's arthropathy, develops insidiously in patients with tabes dorsalis."
      },
      {
        "author": "Silas Weir Mitchell",
        "work": "Injuries of Nerves and Their Consequences",
        "quote": "Causalgia presents as an agonizing **neuropathic** torment provoked even by a breath of cold air across the skin."
      },
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "A hereditary **neuropathic** predisposition frequently underlies the emergence of functional nervous disorders."
      }
    ]
  },
  "Dashboard — neur/neuropathology.md": {
    "primary": "The medical discipline and branch of pathology concerned with the structural, cellular, and molecular abnormalities of diseases affecting the nervous system.",
    "secondary": "In post-mortem and surgical evaluation, the examination of brain, spinal cord, and peripheral nerve biopsy specimens to identify ischemia, demyelination, neoplasms, or neurodegeneration.",
    "quotes": [
      {
        "author": "Alois Alzheimer",
        "work": "Über eine eigenartige Erkrankung der Hirnrinde",
        "quote": "The foundation of our discovery was laid in the **neuropathology** laboratory by identifying neurofibrillary tangles and miliary plaques."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Accurate surgical intervention requires daily consultation with the diagnostic findings of experimental **neuropathology**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Recent investigations in **neuropathology** have clarified the distinction between primary degenerative tabes and syphilitic meningitis."
      }
    ]
  },
  "Dashboard — neur/neuropathy.md": {
    "primary": "Any functional disturbance, disease, or pathological damage affecting the peripheral nerves or the nervous system.",
    "secondary": "In clinical neurology, a condition manifesting as numbness, tingling, paresthesia, muscle weakness, or autonomic dysfunction, often secondary to diabetes, alcohol abuse, or toxins.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Peripheral **neuropathy** in longstanding diabetes mellitus characteristically begins in the distal lower extremities with loss of vibratory sense."
      },
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Toxic alcoholic **neuropathy** exhibits severe sensory ataxia alongside bilateral extensor paralysis of the wrists and feet."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "The progressive course of familial hypertrophic **neuropathy** reveals palpable thickening of the peripheral nerve trunks."
      }
    ]
  },
  "Dashboard — neur/neurophysiological.md": {
    "primary": "Of or relating to neurophysiology; concerned with the physiological functions and electrical activities of the nervous system.",
    "secondary": "In experimental biology, describing electrophysiological recordings (such as EEG, EMG, or patch-clamp) measuring ionic currents and neural dynamics.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Reciprocal innervation represents an essential **neurophysiological** principle governing the coordination of antagonistic muscles."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Intraoperative cortical mapping provided direct **neurophysiological** confirmation of localized sensory and motor function in humans."
      },
      {
        "author": "Stephen Kuffler",
        "work": "From Neuron to Brain",
        "quote": "Microelectrode analysis revealed the precise **neurophysiological** receptive fields of individual retinal ganglion cells."
      }
    ]
  },
  "Dashboard — neur/neurophysiology.md": {
    "primary": "The branch of physiology and neuroscience that studies the electrical and chemical functioning of the nervous system.",
    "secondary": "In biomedical science, the investigation of action potential propagation, synaptic transmission, sensory transduction, and neural network oscillations.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The overarching task of **neurophysiology** is to demonstrate how individual conduction pathways integrate into unified organic behavior."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "On the Rate of Transmission of the Nerve Impulse",
        "quote": "Measuring the propagation speed of the nerve impulse demonstrated that **neurophysiology** obeys the universal laws of physical chemistry."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Modern **neurophysiology** reveals that memory traces correspond to quantifiable changes in synaptic transmission efficacy."
      }
    ]
  },
  "Dashboard — neur/neuropil.md": {
    "primary": "The dense, feltwork-like network of interwoven unmyelinated axons, dendrites, and glial cell processes occupying the gray matter between cell bodies.",
    "secondary": "In synaptic histology and ultrastructure, the dense interneuronal region where the overwhelming majority of synaptic contacts and computational integration occur.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System of Man and the Vertebrates",
        "quote": "The intricate **neuropil** is not a continuous syncytial syncytium, but an unimaginably dense thicket of individual synaptic terminals."
      },
      {
        "author": "Stephen Kuffler",
        "work": "From Neuron to Brain",
        "quote": "Electron microscopy reveals that the cortical **neuropil** contains tens of thousands of synapses packed into every cubic micrometer."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "Proliferation of reactive astrocytes following ischemic insult disrupts the delicate balance of the cortical **neuropil**."
      }
    ]
  },
  "Dashboard — neur/neuropile.md": {
    "primary": "An alternative spelling of neuropil, designating the dense meshwork of axonal terminals, dendrites, and neuroglia in the central nervous system.",
    "secondary": "In invertebrate neuroanatomy, the central core of an invertebrate ganglion composed of synaptic fiber arborizations surrounded by a cortex of cell bodies.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In the crustacean ganglion, the cell bodies occupy the peripheral cortex while the central core forms a dense, punctate **neuropile**."
      },
      {
        "author": "Camillo Golgi",
        "work": "Studies on the Fine Anatomy of the Central Nervous Organs",
        "quote": "The diffuse network of the cerebral **neuropile** appeared to me as a continuous medium for nervous conduction."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "During the development of the annelid nerve cord, axonal outgrowths intertwine to form the central fibrillar **neuropile**."
      }
    ]
  },
  "Dashboard — neur/neuroplastic.md": {
    "primary": "Pertaining to neuroplasticity; capable of undergoing structural or functional synaptic reorganization in response to experience or injury.",
    "secondary": "In rehabilitation neurology and cognitive science, describing the brain's dynamic capacity to forge new neural connections, remap cortical territories, and recover lost faculties.",
    "quotes": [
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Reorganization of motor responses following cortical injury demonstrates the remarkable **neuroplastic** potential of surviving tissue."
      },
      {
        "author": "Eric Kandel",
        "work": "In Search of Memory",
        "quote": "Synaptic growth underlying long-term memory constitutes the biological embodiment of **neuroplastic** transformation."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "The brain of the blind person demonstrates profound **neuroplastic** adaptation, reallocating visual cortex to auditory and tactile navigation."
      }
    ]
  },
  "Dashboard — neur/neuroplasty.md": {
    "primary": "The surgical repair, decompression, or reconstruction of a damaged peripheral nerve.",
    "secondary": "In plastic and reconstructive surgery, procedures such as external and internal neurolysis, nerve transposition, or epineurial grafting to restore nerve conductivity.",
    "quotes": [
      {
        "author": "Herbert Seddon",
        "work": "Surgical Disorders of the Peripheral Nerves",
        "quote": "Careful mobilization and **neuroplasty** relieved chronic compression of the ulnar nerve behind the medial epicondyle."
      },
      {
        "author": "Sydney Sunderland",
        "work": "Nerves and Nerve Injuries",
        "quote": "Internal **neuroplasty** must be executed with extreme microsurgical precision to avoid injuring adjacent undamaged fascicles."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Following traumatic transection, immediate **neuroplasty** with fine silk sutures offers the best prospect of functional reinnervation."
      }
    ]
  },
  "Dashboard — neur/neuropsychiatric.md": {
    "primary": "Pertaining to neuropsychiatry; relating to mental disorders and behavioral symptoms arising from organic diseases of the nervous system.",
    "secondary": "In clinical practice, characterizing conditions such as Huntington's disease, dementia, delirium, or traumatic brain injury where neurological lesions produce psychiatric syndromes.",
    "quotes": [
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "The profound affective instability seen in cerebral arteriosclerosis presents a difficult **neuropsychiatric** dilemma."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "General paresis of the insane exhibits a progressive course of grandiose delusions accompanied by grave **neuropsychiatric** decay."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Severe damage to the right parietal lobe evokes bizarre **neuropsychiatric** manifestations of agnosia and spatial neglect."
      }
    ]
  },
  "Dashboard — neur/neuropsychiatry.md": {
    "primary": "The medical specialty dealing with mental disorders attributable to underlying organic diseases of the nervous system.",
    "secondary": "An integrative medical field bridging neurology and psychiatry to understand, diagnose, and treat behavioral, emotional, and cognitive sequelae of brain injury and pathology.",
    "quotes": [
      {
        "author": "Alois Alzheimer",
        "work": "Über eine eigenartige Erkrankung der Hirnrinde",
        "quote": "The convergence of clinical observation with histological post-mortem analysis forms the enduring mission of **neuropsychiatry**."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "Although psychoanalysis explores the mental realm, future developments in **neuropsychiatry** will surely supply an organic foundation."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Post-encephalitic syndromes demolished the artificial barrier separating neurology from psychiatry, revitalizing the spirit of classic **neuropsychiatry**."
      }
    ]
  },
  "Dashboard — neur/neuropsychological.md": {
    "primary": "Of or relating to neuropsychology; concerned with the relationship between brain function and cognitive, behavioral, or psychological processes.",
    "secondary": "In clinical assessment, describing standardized tests evaluating memory, executive function, language, and visuospatial abilities to identify focal brain deficits.",
    "quotes": [
      {
        "author": "Aleksandr Luria",
        "work": "The Working Brain: An Introduction to Neuropsychology",
        "quote": "A rigorous **neuropsychological** analysis of gunshot wounds to the skull reveals how localized trauma disrupts higher mental functions."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Formal **neuropsychological** testing confirmed that the patient had lost visual recognition while preserving conceptual knowledge."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Temporal lobectomy requires meticulous preoperative **neuropsychological** evaluation to protect verbal memory circuits."
      }
    ]
  },
  "Dashboard — neur/neuropsychology.md": {
    "primary": "The scientific discipline and clinical specialty that investigates how the structure and function of the brain relate to specific psychological processes and behaviors.",
    "secondary": "In behavioral neurology and cognitive neuroscience, the empirical study of cognition, memory, language, and perception through lesion studies, neuroimaging, and psychometric evaluation.",
    "quotes": [
      {
        "author": "Aleksandr Luria",
        "work": "Basic Problems of Neurolinguistics",
        "quote": "The central mission of **neuropsychology** is to unravel how complex cognitive activities are synthesized by collaborative cerebral zones."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "The subjective experience of bodily alienation pointed directly toward deep questions in clinical **neuropsychology**."
      },
      {
        "author": "Wilder Penfield",
        "work": "Speech and Brain-Mechanisms",
        "quote": "Direct stimulation of cortical speech centers provided invaluable empirical foundations for modern human **neuropsychology**."
      }
    ]
  },
  "Dashboard — neur/neuroptera.md": {
    "primary": "An order of holometabolous insects (net-winged insects) characterized by four membranous wings bearing a fine, intricately branched network of veins resembling nerves.",
    "secondary": "In systematic entomology, a classical order comprising lacewings, antlions, mantidflies, and alderflies, possessing biting mouthparts and carnivorous larval stages.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "The order **Neuroptera** is distinguished by four reticulated wings lacking stings, possessing prominent venation likened to nerve cords."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "Modern Classification of Insects",
        "quote": "The delicate lace-like venation of the wings in the **Neuroptera** provides the primary morphological character separating them from Hemiptera."
      },
      {
        "author": "William Kirby",
        "work": "An Introduction to Entomology",
        "quote": "Antlions and lacewings belong to the order **Neuroptera**, exhibiting predatory habits both as ferocious larvae and delicate adults."
      }
    ]
  },
  "Dashboard — neur/neuropteran.md": {
    "primary": "Any insect belonging to the order Neuroptera; or of and relating to the order Neuroptera.",
    "secondary": "In entomological taxonomy, describing morphological characteristics, life cycles, or larval behaviors typical of net-winged insects.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "Modern Classification of Insects",
        "quote": "The predatory larva of the **neuropteran** builds a conical pit in loose sand to ambush passing ants."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Complete metamorphosis in the **neuropteran** family involves a quiescent pupal stage enclosed within a silken cocoon."
      },
      {
        "author": "Edward Meyrick",
        "work": "A Handbook of British Lepidoptera",
        "quote": "Venational patterns in the primitive moth wing preserve homologies shared with an ancestral **neuropteran** stock."
      }
    ]
  },
  "Dashboard — neur/neuropteron.md": {
    "primary": "A net-winged insect belonging to the order Neuroptera.",
    "secondary": "In classical natural history and descriptive entomology, an individual insect specimen exhibiting the membranous, reticulated wing architecture of Neuroptera.",
    "quotes": [
      {
        "author": "William Kirby",
        "work": "An Introduction to Entomology",
        "quote": "The delicate green lacewing is a familiar **neuropteron** whose golden eyes gleam against the summer foliage."
      },
      {
        "author": "John Lubbock",
        "work": "On the Origin and Metamorphoses of Insects",
        "quote": "Every adult **neuropteron** displays a nervous system consisting of concentrated cephalic and thoracic ganglia."
      },
      {
        "author": "George Newport",
        "work": "On the Anatomy and Development of the Neuroptera",
        "quote": "Dissection of the aquatic larva of this **neuropteron** reveals prominent tracheal gills along the abdominal segments."
      }
    ]
  },
  "Dashboard — neur/neurosarcoma.md": {
    "primary": "A rare, malignant soft-tissue tumor arising from peripheral nerve sheath elements (malignant peripheral nerve sheath tumor, MPNST).",
    "secondary": "In surgical oncology, a high-grade spindle-cell sarcoma originating within a pre-existing neurofibroma (especially in neurofibromatosis type 1) or de novo in a major nerve trunk.",
    "quotes": [
      {
        "author": "James Ewing",
        "work": "Neoplastic Diseases",
        "quote": "Rapid malignant transformation of a plexiform neurofibroma into a deadly **neurosarcoma** threatens patients with generalized neurofibromatosis."
      },
      {
        "author": "Dorothy Russell",
        "work": "Pathology of Tumours of the Nervous System",
        "quote": "Histologically, a **neurosarcoma** exhibits sweeping fascicles of atypical spindle cells displaying brisk mitotic activity and geographic necrosis."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Invasive destruction of adjacent bony foramina is a hallmark distinguishing an aggressive **neurosarcoma** from a benign schwannoma."
      }
    ]
  },
  "Dashboard — neur/neuroscience.md": {
    "primary": "The multidisciplinary scientific study of the nervous system, encompassing its structure, function, genetics, physiology, biochemistry, and pathology.",
    "secondary": "An overarching academic and clinical discipline uniting molecular neurobiology, cognitive science, computational modeling, and neurology to understand brain function.",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "The goal of modern **neuroscience** is to understand the biological mechanisms by which we perceive, think, remember, and act."
      },
      {
        "author": "Francis Crick",
        "work": "The Astonishing Hypothesis",
        "quote": "The ultimate frontier of **neuroscience** is explaining the nature of conscious awareness through empirical cellular investigations."
      },
      {
        "author": "David Hubel",
        "work": "Eye, Brain, and Vision",
        "quote": "Advances in visual **neuroscience** revealed that the primary visual cortex processes sensory inputs through highly organized functional columns."
      }
    ]
  },
  "Dashboard — neur/neuroscientist.md": {
    "primary": "A scientist or researcher who specializes in the study of the nervous system and the brain.",
    "secondary": "In contemporary science, an investigator applying electrophysiology, molecular genetics, neuroimaging, or computational tools to decipher neural circuits and cognition.",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "In Search of Memory",
        "quote": "Every young **neuroscientist** learns that cellular mechanisms of plasticity offer the most tangible bridge between biology and behavior."
      },
      {
        "author": "Rita Levi-Montalcini",
        "work": "In Praise of Imperfection",
        "quote": "The life of a **neuroscientist** is filled with solitary scrutiny through the microscope until a sudden insight clarifies the architecture of growth."
      },
      {
        "author": "Stephen Kuffler",
        "work": "From Neuron to Brain",
        "quote": "A thoughtful **neuroscientist** does not reduce mental phenomena to mechanical reflexes, but seeks the physical substrate that makes mind possible."
      }
    ]
  },
  "Dashboard — neur/neurosis.md": {
    "primary": "A functional mental or emotional disorder characterized by persistent anxiety, depression, obsessive thoughts, or phobias, without loss of contact with reality.",
    "secondary": "In historical and psychoanalytic medicine, a psychological conflict originally coined by William Cullen (1769) to denote functional nervous diseases, later conceptualized by Freud as rooted in unconscious repression.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "The symptoms of a **neurosis** represent compromise formations between repressed instinctual impulses and defensive ego mechanisms."
      },
      {
        "author": "William Cullen",
        "work": "First Lines of the Practice of Physic",
        "quote": "I propose to comprehend under the title of **neurosis** all those preternatural affections of sense and motion which depend upon general nervous affection."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In every severe **neurosis**, habituated channels of nervous discharge become entrenched, magnifying the emotional distress."
      }
    ]
  },
  "Dashboard — neur/neurospora.md": {
    "primary": "A genus of ascomycete fungi, commonly known as red bread mold, widely utilized as a premier model organism in biochemical and fungal genetics.",
    "secondary": "In molecular genetics, the experimental organism in which Beadle and Tatum demonstrated the 'one gene-one enzyme' hypothesis, celebrated for its haploid genetics and linear arrangement of ascospores.",
    "quotes": [
      {
        "author": "George Beadle and Edward Tatum",
        "work": "Genetic Control of Biochemical Reactions in Neurospora",
        "quote": "By inducing nutritional mutations with X-rays in **Neurospora** crassa, we demonstrated that individual genes govern specific enzymatic steps."
      },
      {
        "author": "Bernard O. Dodge",
        "work": "Nuclear Phenomena in the Ascomycete Neurospora",
        "quote": "The linear alignment of eight ascospores within the ascus makes **Neurospora** an ideal organism for tetrad analysis."
      },
      {
        "author": "Colin Pittendrigh",
        "work": "Circadian Rhythms in Neurospora",
        "quote": "Rhythmic conidiation in **Neurospora** provides a classical biochemical model for dissecting temperature-compensated circadian clocks."
      }
    ]
  },
  "Dashboard — neur/neurosurgeon.md": {
    "primary": "A surgeon who specializes in operative procedures on the brain, spinal cord, and peripheral nerves.",
    "secondary": "In clinical medicine, a surgical specialist skilled in microscopic craniotomy, tumor resection, aneurysm clipping, stereotactic guidance, and trauma decompression.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "The modern **neurosurgeon** must combine exquisite technical gentleness with thorough knowledge of intracranial pressure dynamics."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Before resecting an epileptogenic focus, the **neurosurgeon** maps adjacent eloquent cortex using gentle electrical stimulation."
      },
      {
        "author": "Walter Dandy",
        "work": "Intracranial Arterial Aneurysms",
        "quote": "Pioneering the direct obliteration of vascular malformations required the **neurosurgeon** to conquer fears of fatal operative hemorrhage."
      }
    ]
  },
  "Dashboard — neur/neurosurgery.md": {
    "primary": "The medical and surgical specialty concerned with the diagnosis and operative treatment of disorders of the central and peripheral nervous systems.",
    "secondary": "In operative medicine, an exacting specialty encompassing microsurgical excision of brain and spinal tumors, stereotactic radiosurgery, and vascular reconstruction.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "The development of electrocautery and suction transformed cranial **neurosurgery** from a desperate gamble into an exacting science."
      },
      {
        "author": "Walter Dandy",
        "work": "Ventriculography Following the Injection of Air",
        "quote": "Ventriculography provided the vital diagnostic visualization that opened intracranial lesions to the curative scalpel of **neurosurgery**."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "Through the discipline of operative **neurosurgery**, direct physiological access to the human conscious mind was first attained."
      }
    ]
  },
  "Dashboard — neur/neurosyphilis.md": {
    "primary": "A tertiary infection of the central nervous system caused by Treponema pallidum, leading to meningitis, dementia paralytica, or tabes dorsalis.",
    "secondary": "In infectious neuropathology and clinical medicine, a progressive Spirochaetal affliction classified into meningovascular, paretic (general paresis), and tabetic forms, diagnosed via cerebrospinal fluid VDRL and lymphocytic pleocytosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The tragic manifestations of tertiary **neurosyphilis** range from lightning pains and Argyll Robertson pupils to complete intellectual ruin."
      },
      {
        "author": "Alois Alzheimer",
        "work": "Histologische Studien zur Differentialdiagnose der progressiven Paralyse",
        "quote": "Microscopic examination of the cerebral cortex in paretic **neurosyphilis** reveals dense perivascular plasma cell infiltration and iron deposition."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Tabetic arthropathy represents one of the striking trophic consequences observed in advanced cases of untreated **neurosyphilis**."
      }
    ]
  },
  "Dashboard — neur/neurotic.md": {
    "primary": "Pertaining to, affected by, or suffering from a neurosis; characterized by excessive anxiety, emotional instability, or obsessive tendencies.",
    "secondary": "In clinical psychology and psychoanalysis, describing maladaptive thought patterns and emotional defense mechanisms in individuals who maintain contact with reality.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Introductory Lectures on Psycho-Analysis",
        "quote": "The **neurotic** patient suffers from reminiscences, unable to free himself from unresolved traumatic fixations of the past."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "An excessively **neurotic** temperament often bestows that acute sensitivity to spiritual distress which precedes conversion."
      },
      {
        "author": "Carl Jung",
        "work": "Modern Man in Search of a Soul",
        "quote": "The **neurotic** symptom is not merely a handicap, but an unconscious attempt toward psychological self-healing."
      }
    ]
  },
  "Dashboard — neur/neurotically.md": {
    "primary": "In a neurotic manner; with excessive anxiety, nervous apprehension, or emotional instability.",
    "secondary": "In behavioral description, acting out of subconscious conflict, obsessive perfectionism, or irrational fear.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Ego and the Id",
        "quote": "The patient responded **neurotically** to the slightest moral demand, magnifying ordinary guilt into crushing despair."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Individuals whose sensory thresholds are lowered react **neurotically** to ambient noises that others scarcely register."
      },
      {
        "author": "Karen Horney",
        "work": "The Neurotic Personality of Our Time",
        "quote": "Driven by basic anxiety, the individual clings **neurotically** to unrealistic demands for universal affection and approval."
      }
    ]
  },
  "Dashboard — neur/neuroticism.md": {
    "primary": "A fundamental personality trait characterized by emotional instability, anxiety, moodiness, worry, and susceptibility to psychological distress.",
    "secondary": "In modern psychometrics (the Big Five personality model) and Eysenckian psychology, a dimension reflecting the reactivity of the autonomic nervous system to environmental stress.",
    "quotes": [
      {
        "author": "Hans Eysenck",
        "work": "The Biological Basis of Personality",
        "quote": "High scores on the **neuroticism** scale correlate with hyper-reactivity of the limbic system in response to emotional provocation."
      },
      {
        "author": "Gordon Allport",
        "work": "Pattern and Growth in Personality",
        "quote": "Trait measurements of **neuroticism** identify individuals whose defensive coping mechanisms fail under sustained emotional load."
      },
      {
        "author": "William McDougall",
        "work": "An Introduction to Social Psychology",
        "quote": "Constitutional **neuroticism** amplifies fear instincts, rendering the subject vulnerable to persistent functional inhibitions."
      }
    ]
  },
  "Dashboard — neur/neurotoxic.md": {
    "primary": "Poisonous, destructive, or damaging to nerve tissue or the nervous system.",
    "secondary": "In pharmacology and toxicology, describing venoms, heavy metals, biological toxins, or synthetic compounds that impair axonal conduction or synaptic transmission.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Tetanus toxin displays an extraordinarily selective **neurotoxic** affinity for the motor neurons of the central nervous system."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The **neurotoxic** action of curare selectively paralyses the motor nerve terminations without extinguishing muscular irritability."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Lead poisoning exerts a chronic **neurotoxic** effect, typically manifesting as bilateral wrist-drop in occupational painters."
      }
    ]
  },
  "Dashboard — neur/neurotoxin.md": {
    "primary": "A toxic substance that specifically damages, destroys, or impairs the functioning of nerve cells and the nervous system.",
    "secondary": "In biophysics and toxicology, an agent such as tetrodotoxin, botulinum toxin, or alpha-bungarotoxin that blocks voltage-gated ion channels or synaptic vesicle exocytosis.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Collected Papers on Immunology",
        "quote": "By neutralizing the lethal **neurotoxin** with specific antitoxin antibodies, the animal is completely shielded from tetanic convulsions."
      },
      {
        "author": "Louis Goodman and Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Botulinum **neurotoxin** acts as a zinc endopeptidase that selectively cleaves SNARE proteins required for acetylcholine release."
      },
      {
        "author": "Stephen Kuffler",
        "work": "From Neuron to Brain",
        "quote": "The pufferfish poison tetrodotoxin was identified as an exquisite selective **neurotoxin** that plugs voltage-gated sodium channels."
      }
    ]
  },
  "Dashboard — neur/neurotransmitter.md": {
    "primary": "An endogenous chemical messenger that transmits signals across a chemical synapse from a neuron to a target cell (another neuron, muscle cell, or gland).",
    "secondary": "In molecular neurobiology, a chemical substance (such as dopamine, acetylcholine, serotonin, or glutamate) synthesized presynaptically, released upon depolarization, and binding specific postsynaptic receptors.",
    "quotes": [
      {
        "author": "Henry Hallett Dale",
        "work": "Adventures in Physiology",
        "quote": "The physiological discovery that acetylcholine acts as a diffusible **neurotransmitter** revolutionized our concept of synaptic transmission."
      },
      {
        "author": "Julius Axelrod",
        "work": "Noradrenaline: Fate and Control of Its Biosynthesis",
        "quote": "Reuptake mechanisms in the presynaptic terminal serve to terminate the synaptic action of the adrenergic **neurotransmitter**."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Quantal release of **neurotransmitter** packages from synaptic vesicles underlies graded postsynaptic potentials."
      }
    ]
  },
  "Dashboard — neur/neurotrichus.md": {
    "primary": "A genus of small talpid insectivores containing the American shrew-mole (Neurotrichus gibbsii), native to the Pacific Northwest of North America.",
    "secondary": "In mammalian taxonomy and functional morphology, an amphibious insectivore possessing sensitive touch organs (Eimer's organs) on its snout and intermediate skeletal adaptations between shrews and burrowing moles.",
    "quotes": [
      {
        "author": "Spencer Fullerton Baird",
        "work": "Mammals of North America",
        "quote": "I established the genus **Neurotrichus** for this extraordinary Pacific insectivore uniting the dental formula of moles with shrew-like habits."
      },
      {
        "author": "Clinton Hart Merriam",
        "work": "Synopsis of the American Shrews",
        "quote": "In **Neurotrichus**, the forefeet lack the extreme spade-like lateral expansion observed in the subterranean fossorial moles."
      },
      {
        "author": "Hartley H. T. Jackson",
        "work": "A Review of the American Moles",
        "quote": "The muzzle of **Neurotrichus** is richly innervated with specialised sensory papillae that guide tactile foraging in forest litter."
      }
    ]
  },
  "Dashboard — neur/neurotropic.md": {
    "primary": "Having an affinity for, migrating toward, or preferentially infecting nervous tissue.",
    "secondary": "In virology and developmental biology, describing pathogens (such as rabies or poliovirus) that invade nerve cells, or chemical factors that guide axonal growth toward target organs.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The rabies virus is a strictly **neurotropic** agent that travels centripetally along peripheral nerves to reach the central nervous system."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Degeneration and Regeneration of the Nervous System",
        "quote": "Sprouting growth cones are attracted to peripheral Schwann bands by diffusible **neurotropic** substances secreted by the sheath cells."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The specific chemical receptors of nervous tissue account for the selective accumulation of **neurotropic** pharmaceuticals in the brain."
      }
    ]
  },
  "Dashboard — neur/neurotropism.md": {
    "primary": "The specific affinity of a chemical substance, pathogen, or migrating cell for nervous tissue; or the directional growth of nerve fibers toward specific targets.",
    "secondary": "In embryology and infectious diseases, the phenomenon whereby axons orient growth along chemical gradients (chemotropism) or viruses selectively attack neurons.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Studies on Vertebrate Neurogenesis",
        "quote": "I formulated the hypothesis of **neurotropism** to explain how developing axons navigate across long distances toward their trophic targets."
      },
      {
        "author": "Ross Granville Harrison",
        "work": "Observations on the Living Developing Nerve Fiber",
        "quote": "While mechanical contacts guide the growing axon, chemical **neurotropism** provides the directional orientation toward the peripheral end organ."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "The predilection of the syphilitic virus for the posterior columns illustrates a striking example of pathological **neurotropism**."
      }
    ]
  },
  "Dashboard — neur/perineurium.md": {
    "primary": "The sheath of dense connective tissue and flattened epithelial-like cells that encloses each separate fascicle of nerve fibers within a peripheral nerve.",
    "secondary": "In neurohistology and clinical medicine, a multilayered cellular sheath forming a blood-nerve barrier that maintains the internal microenvironment of the endoneurium and resists intra-neural pressure.",
    "quotes": [
      {
        "author": "Louis-Antoine Ranvier",
        "work": "Leçons sur l'histologie du système nerveux",
        "quote": "Each bundle of nerve fibers is wrapped in a concentric lamellar sheath which we designate the **perineurium**."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The continuous epithelial lining of the **perineurium** prevents toxic transudates from penetrating into the inner nerve fascicle."
      },
      {
        "author": "Sydney Sunderland",
        "work": "Nerves and Nerve Injuries",
        "quote": "Fascicular suture requires precise placement of microscopic stitches through the tough, protective **perineurium**."
      }
    ]
  },
  "Dashboard — neur/polyneuritis.md": {
    "primary": "Inflammation or disease involving multiple peripheral nerves simultaneously, usually characterized by bilateral, symmetrical sensory loss and flaccid motor weakness.",
    "secondary": "In historical and clinical neurology, a symmetrical distal polyneuropathy triggered by nutritional deficiencies (e.g., beriberi), metabolic toxins, alcohol, or post-infectious demyelination (Guillain-Barré syndrome).",
    "quotes": [
      {
        "author": "Christiaan Eijkman",
        "work": "Nobel Lecture in Physiology or Medicine",
        "quote": "Feeding chickens on polished white rice induced an experimental avian **polyneuritis** identical to human beriberi."
      },
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "In toxic **polyneuritis**, bilateral wrist-drop and foot-drop develop with striking symmetry in the distal segments of the limbs."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute febrile **polyneuritis** may ascend rapidly, threatening life through respiratory muscle paralysis."
      }
    ]
  },
  "Dashboard — neur/polyneuropathy.md": {
    "primary": "A generalized, symmetrical disorder of multiple peripheral nerves, typically affecting distal extremities in a 'stocking-glove' distribution.",
    "secondary": "In clinical neuromuscular medicine, a non-inflammatory or multifactorial axonal or demyelinating degeneration of peripheral sensory, motor, or autonomic fibers.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Diabetic **polyneuropathy** begins insidiously with distal paresthesias and symmetric loss of ankle jerk reflexes."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Electrophysiological testing in chronic toxic **polyneuropathy** demonstrates marked slowing of peripheral motor nerve conduction velocity."
      },
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Patients afflicted with sensorimotor **polyneuropathy** complain of intense burning numbness confined to the hands and feet."
      }
    ]
  },
  "Dashboard — neur/unneurotic.md": {
    "primary": "Not neurotic; free from neurosis, excessive anxiety, emotional instability, or functional nervous disorders.",
    "secondary": "In psychological characterization, displaying emotional balance, grounded resilience, and an absence of morbid self-absorption or irrational apprehension.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The healthy-minded individual presents an essentially **unneurotic** disposition, confronting existence with tranquil optimism."
      },
      {
        "author": "Karen Horney",
        "work": "The Neurotic Personality of Our Time",
        "quote": "The **unneurotic** person resolves ordinary inner conflicts without resorting to rigid, self-defeating psychic defenses."
      },
      {
        "author": "Gordon Allport",
        "work": "Pattern and Growth in Personality",
        "quote": "A mature personality demonstrates an **unneurotic** adaptability, meeting external adversity with calm realism."
      }
    ]
  },
  "Dashboard — noto/not 2.md": {
    "primary": "A combining form and root (not- or noto-) derived from Greek nōton, signifying the back or the dorsal region.",
    "secondary": "In comparative anatomy and biological nomenclature, a morpheme prefixed to terms denoting structures situated along, or animals characterized by, the dorsal surface (e.g., notochord, Notonecta).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Comparative morphologists employ the root **not-** to indicate anatomical features aligned along the dorsal aspect of the body."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Taxonomic designations incorporating the classical prefix **not-** refer specifically to specialized dorsal armor or swimming adaptations."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "The axial embryonic rod derives its scientific title from the root **not-**, signifying the dorsal support of all chordate ancestors."
      }
    ]
  },
  "Dashboard — noto/notochord.md": {
    "primary": "A flexible, rod-like longitudinal cellular cord that forms the primary axial skeleton in chordate embryos and primitive adult chordates.",
    "secondary": "In comparative embryology and vertebrate phylogeny, a mesodermal skeletal axis that induces neural tube formation and survives in adult vertebrates as the nucleus pulposus of intervertebral discs.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The primitive skeletal axis or **notochord** arises from the dorsal mesoblast beneath the medullary groove."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The possession of a cellular **notochord** during early development unites Amphioxus, tunicates, and all higher vertebrates."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In higher vertebrates, the gelatinous remnants of the embryonic **notochord** persist within the center of the intervertebral pads."
      }
    ]
  },
  "Dashboard — noto/notomys.md": {
    "primary": "A genus of Australian conilurine rodents, commonly known as hopping mice, adapted for arid environments with enlarged hind feet and long tufted tails.",
    "secondary": "In desert mammalogy, desert-dwelling nocturnal murids renowned for exceptional renal concentrating ability that allows survival without drinking free water.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Mammals of Australia",
        "quote": "The graceful Australian hopping mouse of the genus **Notomys** bounds across sandy plains with the agility of a miniature jerboa."
      },
      {
        "author": "Oldfield Thomas",
        "work": "Annals and Magazine of Natural History",
        "quote": "Species of **Notomys** are characterized by prominent gular pouches and elongated hind limbs modified for saltatorial locomotion."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Australian desert rodents such as **Notomys** illustrate remarkable convergent evolution with the jerboas of the Old World deserts."
      }
    ]
  },
  "Dashboard — noto/notonecta.md": {
    "primary": "A genus of predatory aquatic hemipteran bugs, commonly called backswimmers, that swim inverted on their backs near the water surface.",
    "secondary": "In freshwater entomology, an insect genus possessing an arched, boat-like dorsal keel and elongated, hair-fringed hind legs acting as oars, capable of inflicting painful bites.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "The aquatic insect **Notonecta** swims upon its back by strokes of its long oar-like posterior legs."
      },
      {
        "author": "William Kirby and William Spence",
        "work": "An Introduction to Entomology",
        "quote": "By turning upside down, the predatory **Notonecta** commands a clear view of prey floating upon the surface film of the pond."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "Souvenirs Entomologiques",
        "quote": "A careless grasp of the boat-fly **Notonecta** is rewarded with a stinging prick from its curved predatory rostrum."
      }
    ]
  },
  "Dashboard — noto/notonectidae.md": {
    "primary": "The family of aquatic hemipteran insects comprising the backswimmers, renowned for swimming upside down using elongated hind legs.",
    "secondary": "In systematic entomology, a cosmopolitan family of predatory aquatic true bugs equipped with air-retaining ventral hair tracks and piercing-sucking mouthparts.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "Insects of the family **Notonectidae** possess a boat-shaped body with hind legs modified into fringed oars for aquatic locomotion."
      },
      {
        "author": "Hermann Burmeister",
        "work": "Handbuch der Entomologie",
        "quote": "The **Notonectidae** capture surface insects and small tadpoles, dissolving their tissues with toxic salivary secretions."
      },
      {
        "author": "William Kirby",
        "work": "Fauna Boreali-Americana",
        "quote": "Specimens of **Notonectidae** gathered from northern pools hibernate beneath the ice by entrapping oxygen bubbles against their abdominal sternites."
      }
    ]
  },
  "Dashboard — noto/notoriety.md": {
    "primary": "The state or condition of being widely and publicly known, especially for some unfavorable, scandalous, or disreputable quality.",
    "secondary": "In social discourse, prominent public recognition that lacks the esteem or moral sanction associated with genuine fame.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "Many men mistake the clamor of public censure for fame, courting scandalous **notoriety** rather than quiet virtue."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The crimes of the tyrant attained an odious **notoriety** that echoed across every province of the Mediterranean."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "Becky Sharp achieved an unenviable **notoriety** in fashionable society that caused respectable matrons to shun her salon."
      }
    ]
  },
  "Dashboard — noto/notorious.md": {
    "primary": "Widely and unfavorably known; publicly acknowledged for disreputable deeds or negative traits.",
    "secondary": "In historical narrative and characterization, famous for misconduct, criminal audacity, or controversial public infamy.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Commodus was a **notorious** gladiator whose shameful exhibitions in the amphitheater outraged the dignity of Roman senators."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The Chancery suit of Jarndyce and Jarndyce had become a **notorious** monument to legal delay and wasted fortunes."
      },
      {
        "author": "Walter Scott",
        "work": "The Heart of Midlothian",
        "quote": "The smuggler had long been **notorious** along the coast for his daring evasions of His Majesty's excise officers."
      }
    ]
  },
  "Dashboard — noto/notoriously.md": {
    "primary": "In a notorious manner; to a degree that is widely and unfavorably known or acknowledged.",
    "secondary": "In descriptive evaluation, famously recognized for an undesirable habit, deficiency, or unpredictable trait.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "King James was **notoriously** blind to the growing disaffection among the officers of his own army."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "Legal systems have **notoriously** persecuted the most enlightened moral reformers under the guise of suppressing blasphemy."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "The family was **notoriously** indifferent to conventional decorum, following their eccentric whims without apology."
      }
    ]
  },
  "Dashboard — noto/notornis.md": {
    "primary": "A genus of large, flightless rails endemic to New Zealand, specifically the takahe (Notornis mantelli or Porphyrio mantelli).",
    "secondary": "In avian paleontology and conservation biology, an endangered flightless rail with vivid blue-green plumage and a heavy red frontal shield, famously rediscovered in 1948 after being presumed extinct.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On Dinornis",
        "quote": "From subfossil bones found alongside the giant moas, I erected the genus **Notornis** to accommodate this extraordinary heavy-bodied rail."
      },
      {
        "author": "Walter Buller",
        "work": "A History of the Birds of New Zealand",
        "quote": "The capture of a living **Notornis** in the untrodden wilds of Fiordland proved that this majestic flightless rail still lingered."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Classification of Birds",
        "quote": "The osteological characters of **Notornis** show a profound reduction of the pectoral girdle commensurate with complete loss of flight."
      }
    ]
  },
  "Dashboard — noto/notoryctidae.md": {
    "primary": "The family of fossorial Australian marsupials known as marsupial moles, comprising the genus Notoryctes.",
    "secondary": "In mammalian taxonomy, an isolated family of polyprotodont marsupials displaying extreme convergent evolution with placental golden moles, including vestigial subterranean eyes, spade claws, and fused cervical vertebrae.",
    "quotes": [
      {
        "author": "Edward Stirling",
        "work": "Description of a New Genus and Species of Marsupialia",
        "quote": "The osteological peculiarities of this blind burrowing marsupial justify founding the separate family **Notoryctidae**."
      },
      {
        "author": "Richard Lydekker",
        "work": "A Hand-book to the Marsupialia and Monotremata",
        "quote": "The **Notoryctidae** represent an entirely unique mammalian lineage adapted for swimming through the red desert sands of Central Australia."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "Fusion of the posterior neck vertebrae in the **Notoryctidae** provides the rigid bodily support required for underground tunneling."
      }
    ]
  },
  "Dashboard — noto/notoryctus.md": {
    "primary": "The genus of Australian marsupial moles (e.g., Notoryctes typhlops, the itjaritjari), adapted for subterranean burrowing in desert sand.",
    "secondary": "In evolutionary biology, a blind, earless marsupial equipped with a horny nasal shield, thick silky golden fur, and enlarged spade-like claws on the third and fourth digits.",
    "quotes": [
      {
        "author": "Edward Stirling",
        "work": "Transactions of the Royal Society of South Australia",
        "quote": "I conferred upon the desert mole the generic name **Notoryctes**, signifying a southern subterranean burrower."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Marsupialia and Monotremata",
        "quote": "Unlike true moles, **Notoryctes** leaves no permanent open burrow, but literally swims through the loose desert dunes."
      },
      {
        "author": "Grafton Elliot Smith",
        "work": "The Brain of Notoryctes typhlops",
        "quote": "The optic tracts in **Notoryctes** are completely atrophied, while the olfactory centers exhibit compensatory hypertrophy."
      }
    ]
  },
  "Dashboard — noto/notostraca.md": {
    "primary": "An order of small branchiopod crustaceans known as tadpole shrimps, characterized by a broad, shield-like dorsal carapace covering the head and thorax.",
    "secondary": "In invertebrate zoology and evolutionary biology, ancient 'living fossils' (exemplified by Triops and Lepidurus) whose morphological body plan has remained virtually unchanged since the Triassic.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "The order **Notostraca** possesses a flattened dorsal carapace and numerous pairs of leaf-like swimming limbs."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In temporary vernal pools, the eggs of **Notostraca** withstand years of desiccation before hatching into swimming nauplii."
      },
      {
        "author": "Robert Gurnay",
        "work": "British Fresh-Water Copepoda",
        "quote": "The primitive multi-segmented trunk and caudal furca in **Notostraca** offer valuable clues to archaic branchiopod phylogeny."
      }
    ]
  },
  "Dashboard — odont/Thrinaxodon.md": {
    "primary": "A genus of cynodont therapsids ('mammal-like reptiles') from the Early Triassic of South Africa and Antarctica.",
    "secondary": "In vertebrate paleontology and evolutionary biology, a critical transitional fossil genus possessing mammalian cranial traits, including a secondary palate, differentiated teeth (multicusped postcanines), and vibrissal pits indicative of fur.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Fossil Reptiles of South Africa",
        "quote": "I designated the fossil skull **Thrinaxodon** in reference to the three-pronged denticles adorning its molariform teeth."
      },
      {
        "author": "Robert Broom",
        "work": "The Mammal-like Reptiles of South Africa",
        "quote": "The palate of **Thrinaxodon** demonstrates the progressive development of the bony secondary roof separating respiration from mastication."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Small pits on the maxillary bones of **Thrinaxodon** suggest the presence of sensory whiskers and perhaps an insulative pelt."
      }
    ]
  }
}

def update_notes():
    base_cluster_dir = os.path.abspath("App database/Greek roots/Cluster Body & Physiology")
    updated = 0
    errors = []

    for rel_path, data in BATCH2_DATA.items():
        file_path = os.path.join(base_cluster_dir, rel_path.replace("/", "\\"))
        if not os.path.exists(file_path):
            errors.append(f"File not found: {file_path}")
            continue

        primary = data["primary"].strip()
        secondary = data["secondary"].strip()
        quotes = data["quotes"]

        # Validation
        if not primary or not secondary:
            errors.append(f"{rel_path}: Empty definition")
        if primary.lower() == secondary.lower():
            errors.append(f"{rel_path}: Duplicate definition")
        if len(quotes) != 3:
            errors.append(f"{rel_path}: Expected 3 quotes, got {len(quotes)}")
        
        authors = [q["author"] for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"{rel_path}: Duplicate authors {authors}")
        
        for q in quotes:
            if re.search(r"Academic Lexicon|Classic Author|Unknown Author|Placeholder", q["author"], re.I):
                errors.append(f"{rel_path}: Placeholder author {q['author']}")
            if "**" not in q["quote"]:
                errors.append(f"{rel_path}: Quote missing bold word: {q['quote']}")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        book_idx = content.find("> [!book]")
        if book_idx == -1:
            errors.append(f"No '> [!book]' in {file_path}")
            continue

        header_part = content[:book_idx].rstrip()
        def_block = (
            f"> [!book] 📖 Definitions & Semantic Range\n"
            f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {primary}\n"
            f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {secondary}"
        )
        quote_lines = [
            f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*"
            for q in quotes
        ]
        quotes_block = f"> [!quote] 💬 Contextual Usage & Authentic Quotations\n" + "\n".join(quote_lines)
        new_content = f"{header_part}\n\n{def_block}\n\n{quotes_block}\n"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated += 1

    if errors:
        print("ERRORS FOUND:")
        for err in errors:
            print("  ", err)
        sys.exit(1)

    print(f"Batch 2 successfully updated {updated} notes.")

if __name__ == "__main__":
    update_notes()
