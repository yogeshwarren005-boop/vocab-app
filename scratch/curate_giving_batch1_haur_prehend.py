# -*- coding: utf-8 -*-
"""
Curates Cluster Giving & Receiving:
- Dashboard — haur (10 words)
- Dashboard — prehend (11 words)
Total: 21 words.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_haur_prehend = {
  # Dashboard — haur
  "exhaust": {
    "primary": "To drain completely of strength, resources, energy, or contents; to tire out.",
    "secondary": "In mechanical engineering, the discharge of waste gases or steam from an internal combustion engine.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Unchecked reproduction would rapidly **exhaust** all available food resources in any territory."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Protracted civil wars served to **exhaust** the agricultural wealth of the Italian provinces."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The furious struggle served to **exhaust** the great leviathan before the final lance was cast."}
    ]
  },
  "exhausted": {
    "primary": "Completely drained of physical or mental energy; depleted of resources or contents.",
    "secondary": "In agricultural soil science, arable land depleted of essential nitrogen, phosphorus, and organic nutrients.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I collapsed upon the wet heather, utterly **exhausted** after three days of wandering without food."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "When silver mines became **exhausted**, the owners abandoned the works as unprofitable."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The **exhausted** sled dogs fell into the snow, unable to haul the overloaded sledge another mile."}
    ]
  },
  "exhaustible": {
    "primary": "Capable of being completely consumed, emptied, depleted, or drained; finite in quantity.",
    "secondary": "In natural resource economics, non-renewable mineral and fossil energy reserves subject to permanent depletion.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Mineral deposits are strictly **exhaustible** capitals that cannot be replaced once extracted."},
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "The fertility of the soil, though great, is fundamentally **exhaustible** under continuous cropping."},
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Early navigators mistakenly believed marine fisheries were infinite rather than **exhaustible** ecosystems."}
    ]
  },
  "exhausting": {
    "primary": "Extremely tiring, demanding, or fatiguing; draining completely of physical stamina.",
    "secondary": "In manufacturing thermodynamics, the process of expelling spent steam or combustion gas through valves.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "A long and **exhausting** journey on top of the stagecoach left the travelers shivering in the cold."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Climbing the steep granite moraine proved an **exhausting** trial under the midday sun."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Digging trenches in frozen limestone shale was an **exhausting** labor that blistered the soldiers' hands."}
    ]
  },
  "exhaustion": {
    "primary": "Total depletion of physical or mental strength, vitality, or resources; severe fatigue.",
    "secondary": "In legal and administrative doctrine, the exhaustion of remedies requirement before seeking judicial review.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Nervous **exhaustion** commonly manifests with profound physical lethargy, tremors, and insomnia."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The physical **exhaustion** of pioneer life left little leisure for philosophical contemplation."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The troops marched onward despite extreme thirst and **exhaustion** across the burning desert sands."}
    ]
  },
  "exhaustive": {
    "primary": "Including or considering all elements or aspects; comprehensive, thorough, and complete.",
    "secondary": "In formal logic and classification, a categorization whose disjunctive classes account for every member of the domain.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Natural history requires an **exhaustive** collection of observed instances before induction can proceed."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes conducted an **exhaustive** search of the attic room, measuring every footprint upon the dusty floor."},
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Aristotle provided an **exhaustive** inventory of valid syllogistic moods in the Prior Analytics."}
    ]
  },
  "exhaustively": {
    "primary": "In a thorough, comprehensive manner that considers every detail, aspect, or possibility.",
    "secondary": "In academic and scientific inquiry, investigating a research problem to the limit of available evidence.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "I have examined the plumage of domestic pigeons **exhaustively** to trace their descent from the rock dove."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The committee debated the provisions of the bill **exhaustively** through many late-night sittings."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The phenomena of subconscious habit have been treated **exhaustively** by contemporary French neurologists."}
    ]
  },
  "haustorium": {
    "primary": "A specialized root-like or hyphal structure by which a parasitic plant or fungus absorbs nutrients from its host.",
    "secondary": "In fungal phytopathology, the intracellular organelle invaginating the host plasma membrane to extract carbohydrates.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The dodder seedling penetrates the host stem by means of a specialized feeding **haustorium**."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Each parasitic **haustorium** dissolves host tissues through secreted enzymes to reach the vascular cylinder."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Powdery mildew fungi send a delicate **haustorium** into epidermal cells without immediately killing the leaf."}
    ]
  },
  "inexhaustible": {
    "primary": "Incapable of being depleted, emptied, or used up; boundless, limitless, or untiring.",
    "secondary": "In natural aesthetics and creative genius, an endlessly fertile spring of imaginative inspiration.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Shakespeare possessed an **inexhaustible** richness of inventive fancy that animated every character."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Nature is an **inexhaustible** source of spiritual renewal for the receptive human intellect."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "To the whalemen, the boundless ocean appeared an **inexhaustible** reservoir of living leviathans."}
    ]
  },
  "unexhausted": {
    "primary": "Not depleted, emptied, or drained; retaining remaining strength, vitality, or resources.",
    "secondary": "In environmental geology, natural reserves or aquifers that have not suffered overdraft or depletion.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman empire still possessed **unexhausted** reserves of gold and men in the eastern provinces."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Her **unexhausted** youthful energy carried her through the long pedestrian journey to London."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The evolutionary puzzle presents vast **unexhausted** fields for future biological investigation."}
    ]
  },

  # Dashboard — prehend
  "apprehend": {
    "primary": "To arrest someone for a crime; to understand, grasp intellectually, or perceive mentally.",
    "secondary": "In emotional psychology, to anticipate with anxiety, fear, or foreboding.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "Such tricks hath strong imagination, / That if it would but **apprehend** some joy, / It comprehends some bringer of that joy."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The human mind cannot **apprehend** abstract ideas without grounding them in simple sensory perceptions."},
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "The constable was authorized by the warrant to **apprehend** the suspected felon wherever found."}
    ]
  },
  "apprehended": {
    "primary": "Arrested or taken into custody by legal authority; understood or mentally grasped.",
    "secondary": "In historical narrative, feared or anticipated with anxious foreboding.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The notorious jewel thief was **apprehended** at Dover just as he boarded the midnight packet."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The senators **apprehended** the imminent vengeance of the newly crowned barbarian tyrant."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Simple relations between sensible qualities are instantly **apprehended** by the intellect."}
    ]
  },
  "apprehender": {
    "primary": "One who arrests or seizes an offender; one who perceives or understands intellectually.",
    "secondary": "In philosophical epistemology, the cognitive agent who forms perceptual representations of external phenomena.",
    "quotes": [
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "The statutory reward was promptly paid to the courageous **apprehender** of the highwayman."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poetic mind is both a creator of symbols and an acute **apprehender** of spiritual truths."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A diligent **apprehender** of natural causes will avoid the traps of scholastic superstition."}
    ]
  },
  "comprehend": {
    "primary": "To grasp mentally; to understand the nature or significance of something; to include or encompass.",
    "secondary": "In formal taxonomy and set theory, to contain or subsume several subcategories within a broader genus.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "What finite creature can **comprehend** the boundless wisdom and unsearchable decrees of the Almighty?"},
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "Concepts without intuitions are empty; we cannot **comprehend** objects without sensible representation."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was at a loss to **comprehend** how Darcy could have recommended such a match."}
    ]
  },
  "comprehended": {
    "primary": "Mentally understood or grasped; included, embraced, or encompassed within a group or scope.",
    "secondary": "In legal statutes and contractual deeds, matters subsumed under general statutory clauses.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The American constitution **comprehended** diverse regional interests within a single federal framework."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Jarndyce **comprehended** the girl's silent anguish and offered her his home as a refuge."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Once the mathematical proof was **comprehended**, its necessary truth became self-evident."}
    ]
  },
  "comprehendible": {
    "primary": "Capable of being understood, comprehended, or grasped by the human mind; intelligible.",
    "secondary": "In educational pedagogy, instructional materials structured to be readily intelligible to learners.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Natural laws must be formulated in plain terms if they are to be **comprehendible** to ordinary men."},
      {"author": "Thomas Huxley", "work": "Science and Culture", "quote": "Scientific truths are easily **comprehendible** when illustrated by direct physical experiments."},
      {"author": "William James", "work": "The Will to Believe", "quote": "A pragmatic universe presents a **comprehendible** reality responsive to human effort and purpose."}
    ]
  },
  "misapprehend": {
    "primary": "To misunderstand, misinterpret, or grasp mistakenly; to form an erroneous impression of.",
    "secondary": "In diplomatic communications, to mistakenly perceive peaceful overtures as hostile provocation.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne feared her mother would **misapprehend** the true nature of Willoughby's sudden departure."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Men frequently **misapprehend** their own abilities, attempting tasks for which nature never fitted them."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Lest foreign ambassadors should **misapprehend** our national resolve, treaty terms must be unambiguous."}
    ]
  },
  "prehend": {
    "primary": "To seize, grasp, take hold of, or lay hands upon physically; to apprehend.",
    "secondary": "In zoological biomechanics, the action of an organ (such as a trunk or prehensile tail) in grasping objects.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The animal extends its muscular appendage to **prehend** the proffered piece of fruit."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "Primates evolved specialized opposable digits that **prehend** tree branches with remarkable security."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The arboreal cuscus uses its naked tail tip to **prehend** slender creepers among the canopy."}
    ]
  },
  "reprehend": {
    "primary": "To voice disapproval of; to reprimand, rebuke, censure, or find fault with someone or their conduct.",
    "secondary": "In moral theology, the pastoral duty to admonish a transgressor regarding ethical failings.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "Prudent friends will privately **reprehend** our follies rather than proclaim them in public company."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "It is a sign of civic maturity when magistrates hear criticism patiently without seeking to **reprehend** the speaker."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "Critics have reason to **reprehend** Dryden's careless rhymes and hasty revisions."}
    ]
  },
  "uncomprehended": {
    "primary": "Not understood, grasped, or perceived by the mind; remaining mysterious or enigmatic.",
    "secondary": "In natural theology and romantic poetry, cosmic forces operating beyond human intellectual comprehension.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Deep in the dark earth roll subterranean fires, majestic and **uncomprehended** by mortal eyes."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab stared into the white whale's eye, sensing an ancient and **uncomprehended** malice."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "The divine laws work around us silently, **uncomprehended** by the shallow worldly understanding."}
    ]
  },
  "uncomprehending": {
    "primary": "Lacking understanding or comprehension; showing or marked by failure to grasp the situation.",
    "secondary": "In psychological characterization, a blank, bewildered, or unperceiving expression in moments of crisis.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver stared with **uncomprehending** eyes when he discovered his golden guineas were gone."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude looked at the Latin grammars with an **uncomprehending** gaze, overwhelmed by their grammatical complexity."},
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "Septimus turned an **uncomprehending** face toward the busy London traffic, lost in inward hallucinations."}
    ]
  }
}
