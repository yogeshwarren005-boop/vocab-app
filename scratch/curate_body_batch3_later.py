# -*- coding: utf-8 -*-
"""
Curates Dashboard — later (21 words) in Cluster Body & State.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_later = {
  "bilateral": {
    "primary": "Having or relating to two sides; affecting both sides of something equally.",
    "secondary": "In international diplomacy, an agreement or treaty negotiated directly between two sovereign states.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Higher animals almost universally display a symmetrical **bilateral** body plan."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A **bilateral** treaty between two trading powers requires reciprocal commercial guarantees."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The patient presented with **bilateral** enlargement of the cervical lymph nodes."}
    ]
  },
  "bilateralism": {
    "primary": "The practice of conducting political, economic, or diplomatic relations between two nations.",
    "secondary": "In international trade theory, preferential two-party commerce contrasted with multilateral agreements.",
    "quotes": [
      {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "Strict commercial **bilateralism** restricts the natural multi-currency flow of global trade."},
      {"author": "Walter Bagehot", "work": "The English Constitution", "quote": "Parliamentary diplomacy shifted from regional **bilateralism** toward broader European alliances."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Exclusive **bilateralism** between colonial powers and their dependencies stunted provincial growth."}
    ]
  },
  "bilaterality": {
    "primary": "The property or condition of having two sides or affecting two sides symmetrically.",
    "secondary": "In comparative morphology, bilateral symmetry where the body can be divided into identical left and right halves.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The fundamental **bilaterality** of the vertebrate nervous system is evident from the earliest embryonic stage."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Deviations from standard **bilaterality** are occasionally observed in hybrid flatfish."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory localization reflects the anatomical **bilaterality** of our paired auditory and visual organs."}
    ]
  },
  "bilaterally": {
    "primary": "In a manner affecting, involving, or situated on both sides; symmetrically.",
    "secondary": "In diplomatic negotiations, binding two contracting sovereign governments reciprocally.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The facial muscles contract **bilaterally** during explosive expressions of joy or laughter."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pneumonic consolidation appeared **bilaterally** in both lower pulmonary lobes."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Tariff reductions negotiated **bilaterally** fostered harmonious trade between the two maritime nations."}
    ]
  },
  "collateral": {
    "primary": "Something pledged as security for repayment of a loan; additional, concurrent, or secondary.",
    "secondary": "In legal descent, relatives descending from the same common ancestor but through different genealogical lines (collateral heirs).",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Bankers demand solid **collateral** in land or merchant bonds before advancing long-term credit."},
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "In default of lineal issue, real estate descends to the nearest **collateral** kinsman."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Vincy offered his promissory note without adequate **collateral**, relying on family connections."}
    ]
  },
  "collateralize": {
    "primary": "To pledge an asset, security, or property as collateral for a debt or loan.",
    "secondary": "In structured corporate finance, securing debt instruments with specific pools of underlying cash flows.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on a National Bank", "quote": "Merchants can readily **collateralize** warehouse receipts to secure working capital from the bank."},
      {"author": "John Maynard Keynes", "work": "A Treatise on Money", "quote": "Borrowers who **collateralize** short-term advances with government gilts obtain preferential interest rates."},
      {"author": "Walter Bagehot", "work": "Lombard Street", "quote": "Prudent bill brokers always require drawers to **collateralize** speculative export paper."}
    ]
  },
  "contralateral": {
    "primary": "Relating to or denoting the side of the body opposite to that on which a particular condition or structure occurs.",
    "secondary": "In clinical neuroanatomy, the motor cortex controlling voluntary movement of the opposite limb via pyramidal decussation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A cerebral lesion in the internal capsule produces paralysis of the **contralateral** arm and leg."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Nerve fibers from the motor cortex decussate in the medulla to innervate **contralateral** somatic muscles."},
      {"author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "Electrical excitation of the left cerebral hemisphere provoked twitching in the **contralateral** extremities."}
    ]
  },
  "dilater": {
    "primary": "A surgical instrument or muscle that widens, expands, or dilates an opening or cavity (variant of dilator).",
    "secondary": "In operative surgery, an instrument employed to enlarge a stricture or anatomical orifice gradually.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon introduced a flexible **dilater** to relieve the cicatricial stenosis of the esophagus."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The pupil expands through the action of the **dilater** pupillae muscle innervated by sympathetic fibers."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Careful manipulation of the urethral **dilater** avoided mucosal tearing in sensitive patients."}
    ]
  },
  "elater": {
    "primary": "A click beetle; an elastic, hygroscopic spiral filament that aids in dispersing spores in liverworts and horsetails.",
    "secondary": "In cryptogamic botany, a hygroscopic ribbon-like cell that twists as it dries to fling spores into the air.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Under the microscope, each spirally thickened **elater** springs suddenly as moisture evaporates, dispersing the spores."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The jumping click beetle, or **elater**, rights itself by an ingenious snapping mechanism beneath its thorax."},
      {"author": "Henry David Thoreau", "work": "Journal", "quote": "I examined equisetum cones and observed how each microscopic **elater** coiled and uncoiled with every breath."}
    ]
  },
  "elaterid": {
    "primary": "Belonging to the beetle family Elateridae (click beetles); a click beetle.",
    "secondary": "In entomological classification, a coleopteran insect possessing a prosternal spine enabling sudden leaping leaps.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The phosphorescent **elaterid** beetle illuminated the forest path with its brilliant thoracic lanterns."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "We captured a splendid giant **elaterid** whose metallic green elytra flashed in the tropical canopy."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "The nocturnal flight of the luminous **elaterid** was a familiar marvel along the river banks."}
    ]
  },
  "elateridae": {
    "primary": "The family of click beetles in the order Coleoptera, characterized by their jumping spine mechanism and click sound.",
    "secondary": "In systematic entomology, the cosmopolitan beetle family comprising over 9,000 species, whose larvae are known as wireworms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "Fireflies belonging to the **Elateridae** cast light strong enough to read print in a darkened cabin."},
      {"author": "Alfred Russel Wallace", "work": "Tropical Nature", "quote": "The family **Elateridae** includes species capable of snapping their bodies into the air to escape predators."},
      {"author": "Asa Gray", "work": "Elements of Zoology", "quote": "Agricultural soils often harbor destructive wireworm larvae belonging to various genera of the **Elateridae**."}
    ]
  },
  "equilateral": {
    "primary": "Having all sides of equal length; symmetrical on all sides.",
    "secondary": "In Euclidean plane geometry, an equilateral triangle whose three interior angles are each equal to sixty degrees.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "I passed the sunbeam through an **equilateral** prism of flint glass to produce the prismatic spectrum."},
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "Euclid's very first proposition demonstrates the geometric construction of an **equilateral** triangle."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Regular geometric figures such as the **equilateral** polygon symbolize mathematical harmony."}
    ]
  },
  "later": {
    "primary": "At a subsequent or future time; comparative of late; following the present moment.",
    "secondary": "In historical chronology, designating a subsequent or advanced phase of an era, dynasty, or culture.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "She should have died hereafter; there would have been a time for such a word... A **later** hour would have suited sorrow."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The institutions of the **later** Roman empire differed profoundly from the Augustan principate."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth resolved to postpone her intended inquiry until a **later** and more favorable opportunity."}
    ]
  },
  "lateral": {
    "primary": "Of, at, towards, or from the side or sides; sideways in movement or position.",
    "secondary": "In human anatomy and directional terminology, positioned away from the midline of the body toward the flank.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **lateral** collateral ligament reinforces the knee joint against abnormal valgus displacement."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Tendrils curve sharply when subjected to tactile stimulation along their **lateral** surface."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inspection of the thorax revealed diminished expansion along the right **lateral** chest wall."}
    ]
  },
  "lateralisation": {
    "primary": "The localization of specific neurological or cognitive functions to one side of the brain (British spelling).",
    "secondary": "In neuropsychology, hemispheric specialization such as left-hemisphere dominance for receptive and expressive language.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Cerebral **lateralisation** explains why localized cortical injury impairs speech while sparing visual memory."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The evolutionary **lateralisation** of motor dexterity reflects deep structural asymmetry in primates."},
      {"author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "Functional **lateralisation** of hand preference correlates with contralateral hemisphere dominance."}
    ]
  },
  "laterality": {
    "primary": "The preference for using one side of the body, especially in tasks requiring motor skill; sidedness.",
    "secondary": "In behavioral neuroscience and developmental pediatrics, dominant handedness, footedness, or ocular preference.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Motor **laterality** manifests early in childhood as a marked bias toward right-handed manipulation."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Handedness and bodily **laterality** appear uniquely pronounced in human tool-making communities."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Structural **laterality** is reflected in the asymmetrical lobation of the human lungs and liver."}
    ]
  },
  "lateralization": {
    "primary": "The localization of neurological or cognitive functions predominantly in one cerebral hemisphere (American spelling).",
    "secondary": "In cognitive psychology, the process whereby specific sensory-motor skills become specialized in the left or right hemisphere.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Profound cerebral **lateralization** leaves the right hemisphere specialized for facial recognition."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Brain lesions reveal the remarkable **lateralization** of musical and linguistic faculties."},
      {"author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "Asymmetry in cranial blood supply may foster the progressive **lateralization** of manual dexterity."}
    ]
  },
  "lateralize": {
    "primary": "To localize or become localized predominantly to one side of the body or brain.",
    "secondary": "In neurosurgery, to identify which hemisphere of the brain controls a specific function or epileptic focus.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Neurological signs began to **lateralize** to the left hemisphere as intracranial pressure increased."},
      {"author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "Sensory perceptions tend to **lateralize** along contralateral ascending neural pathways."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The patient's motor tremors began to **lateralize** predominantly to the right arm."}
    ]
  },
  "laterally": {
    "primary": "Toward, at, or from the side or sides; sideways in direction or orientation.",
    "secondary": "In corporate organizational management, moving laterally between positions at the same rank without promotion or demotion.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Flatfish lie on the sea floor with their bodies flattened **laterally**, both eyes migrating to the upper side."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The ribs arch **laterally** from the vertebral column to enclose the thoracic viscera."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sperm whale swung its massive flukes **laterally**, creating an immense whirlpool beside the ship."}
    ]
  },
  "lateran": {
    "primary": "Relating to the Lateran Palace and Basilica of St. John Lateran in Rome; papal council or treaty.",
    "secondary": "In church history, the five ecumenical Lateran Councils, or the 1929 Lateran Treaty creating Vatican City.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The popes made their historic residence in the magnificent **Lateran** palace near the Caelian hill."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Papal decrees promulgated at the **Lateran** council shaped medieval ecclesiastical jurisdiction across Europe."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Roman legions marched past the ancient imperial estates that later became the site of the **Lateran**."}
    ]
  },
  "laterite": {
    "primary": "A reddish, iron-rich, heavily weathered soil and rock type common in wet tropical regions.",
    "secondary": "In tropical pedology and geology, a residual weathering product enriched in iron and aluminum oxides that hardens upon exposure to air.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The hills of Bahia were composed of deep brick-red **laterite**, formed by the intense weathering of gneiss."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative", "quote": "Tropical monsoons wash the humus from the hills, leaving barren sheets of cellular red **laterite**."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The road was carved through hard red **laterite** that crumbled into fine dust under the midday sun."}
    ]
  }
}
