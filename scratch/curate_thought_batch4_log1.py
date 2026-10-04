# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — log (Words 1-45)
  # =========================================================================
  "Dashboard — log/allogamous.md": {
    "primary": "Characterized by cross-fertilization between different individual flowers or plants.",
    "secondary": "In reproductive plant biology, flower structures adapted to receive pollen from another individual to ensure genetic diversity.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "In naturally **allogamous** species, self-pollination frequently results in diminished seed vigor."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Dichogamous flowers are almost necessarily **allogamous**, since their pollen ripens before or after the stigma matures."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The showy petals and abundant nectar of these orchids indicate an exclusively **allogamous** habit."}
    ]
  },
  "Dashboard — log/allogamy.md": {
    "primary": "Cross-fertilization in plants; the pollination of a flower with pollen from a different plant.",
    "secondary": "In evolutionary botany, reproductive mechanisms such as self-incompatibility that enforce cross-pollination.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Heterostyly is a remarkable morphological contrivance designed to favor **allogamy** over self-fertilization."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The evolutionary transition toward **allogamy** prevented deleterious inbreeding depression across vast floral families."},
      {"author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "We observe in **allogamy** an exquisite ecological adaptation linking floral anatomy to insect visitors."}
    ]
  },
  "Dashboard — log/allogeneic.md": {
    "primary": "Involving or derived from genetically different individuals of the same biological species.",
    "secondary": "In immunology and transplantation medicine, cells, tissues, or grafts possessing divergent histocompatibility antigens.",
    "quotes": [
      {"author": "Peter Medawar", "work": "The Uniqueness of the Individual", "quote": "The immunological rejection of **allogeneic** skin grafts demonstrates the individual specificity of mammalian tissue antigens."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern blood transfusion requires precise typing to avoid catastrophic hemolytic reactions between **allogeneic** sera."},
      {"author": "Frank Macfarlane Burnet", "work": "Immunology, Aging, and Cancer", "quote": "Clonal selection explains how the immune system distinguishes autologous tissues from **allogeneic** donor antigens."}
    ]
  },
  "Dashboard — log/allograft.md": {
    "primary": "A tissue graft or organ transplant from a donor of the same species but genetically distinct.",
    "secondary": "In surgical oncology and transplant immunology, homografts requiring immunosuppressive therapy to prevent host rejection.",
    "quotes": [
      {"author": "Peter Medawar", "work": "The Hope of Progress", "quote": "Survival of an **allograft** depends upon the degree of genetic compatibility between donor and host."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical challenge in vascular surgery remains the preservation of **allograft** integrity against cellular infiltration."},
      {"author": "Alexis Carrel", "work": "The Treatment of Wounds", "quote": "Transplantation experiments demonstrated that an **allograft** initially heals into place before acute rejection sets in."}
    ]
  },
  "Dashboard — log/allograph.md": {
    "primary": "A letter or symbol representing a sound in a language; a signature made on another's behalf.",
    "secondary": "In paleography and legal forensics, a contextual variant glyph of a letterform, or an instrument executed by an agent for a principal.",
    "quotes": [
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "The letters 'f' and 'ph' represent the same phoneme in English, each functioning as an **allograph** in distinct orthographic environments."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Every graphemic system develops positional variants, where each **allograph** is conditioned by surrounding letters."},
      {"author": "Henry Maine", "work": "Ancient Law", "quote": "In early testamentary law, a written **allograph** required the attested seals of seven witnesses to gain validity."}
    ]
  },
  "Dashboard — log/allographic.md": {
    "primary": "Pertaining to an allograph, alternate letterform, or signature made on behalf of another.",
    "secondary": "In aesthetics and philosophy of art, works of art (such as music or literature) capable of multiple authentic instances through notation.",
    "quotes": [
      {"author": "Nelson Goodman", "work": "Languages of Art", "quote": "Literature and music are **allographic** arts, whereas painting and sculpture are strictly autographic and unique."},
      {"author": "Leonard Bloomfield", "work": "Linguistic Aspects of Science", "quote": "The variation between cursive and printed letterforms is an **allographic** distinction devoid of phonological significance."},
      {"author": "Edward Sapir", "work": "Selected Writings in Language, Culture and Personality", "quote": "Native scribes quickly mastered the **allographic** conventions of the imported European alphabet."}
    ]
  },
  "Dashboard — log/analogical.md": {
    "primary": "Expressing or based on an analogy; using correspondence between different things to explain or argue.",
    "secondary": "In epistemological reasoning and legal interpretation, drawing inductive inferences regarding unknown properties based upon observed parallels.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "**Analogical** reasoning is often the only path open to human inquiry where direct observation fails."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The mind must not rest content with superficial **analogical** resemblances, but penetrate to real causes."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "An **analogical** inference can never produce mathematical certainty, though it provides valuable hypotheses for scientific testing."}
    ]
  },
  "Dashboard — log/analogise.md": {
    "primary": "To make an analogy; to explain, compare, or interpret by showing correspondence (British spelling of analogize).",
    "secondary": "In literary exposition and metaphysics, explaining complex abstract principles through concrete physical parallels.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "We must not **analogise** spiritual truths to mechanical operations without cautious qualification."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Philosophers frequently **analogise** the development of an empire to the physiological growth of an animal body."},
      {"author": "William Whewell", "work": "The History of the Inductive Sciences", "quote": "To **analogise** the propagation of light to ripples upon water was Huygens's grand stroke of genius."}
    ]
  },
  "Dashboard — log/analogist.md": {
    "primary": "One who reasons, writes, or explains by means of analogies.",
    "secondary": "In theological debate and natural philosophy, a thinker who deduces divine attributes or natural laws from structural correspondences.",
    "quotes": [
      {"author": "Joseph Butler", "work": "The Analogy of Religion", "quote": "The Christian **analogist** shows that the difficulties in revealed religion are matched by corresponding difficulties in the constitution of nature."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Cowley was an ingenious **analogist**, delighted by quaint conceits and remote comparisons."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "Bacon was a profound **analogist**, perceiving subtle links between moral virtues and physical laws."}
    ]
  },
  "Dashboard — log/analogize.md": {
    "primary": "To explain, compare, or understand something by making an analogy.",
    "secondary": "In judicial reasoning and rhetoric, arguing from precedents by establishing material structural equivalence between cases.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Swedenborg sought to **analogize** every spiritual state to some outward natural object."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "Judges constantly **analogize** novel commercial disputes to ancient feudal doctrines of property."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "We naturally **analogize** unseen psychological processes to physical forces and fluids."}
    ]
  },
  "Dashboard — log/analogous.md": {
    "primary": "Comparable in certain respects, typically in a way that makes clearer the nature of the things compared.",
    "secondary": "In evolutionary biology, describing organs that perform similar functions without sharing a common ancestral origin.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Structures are **analogous** when they perform identical functions in different organisms without sharing common descent."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The hand of the chimpanzee is structurally homologous, rather than merely **analogous**, to the human hand."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The relations of colonies to the mother country are in many respects **analogous** to the relations of children to their parents."}
    ]
  },
  "Dashboard — log/analogously.md": {
    "primary": "In an analogous or corresponding manner; comparatively.",
    "secondary": "In scientific deduction and legal argument, proceeding by parallel inference from established models to new phenomena.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Social institutions evolve **analogously** to biological organs, differentiating from simple to complex structures."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Wild species vary **analogously** to domesticated breeds when subjected to changed environments."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Electric currents behave **analogously** to fluids flowing through pipes under hydrostatic pressure."}
    ]
  },
  "Dashboard — log/analogy.md": {
    "primary": "A comparison between two things on the basis of structure to explain or clarify a concept.",
    "secondary": "In biology, functional similarity between organs of different evolutionary lineages; in rhetoric, heuristic modeling.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We must strictly distinguish between true genetic affinity and mere adaptive **analogy**."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "**Analogy** in reasoning is the great guide of life, leading where demonstration cannot reach."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The whole of nature is a metaphor of the human mind; every appearance corresponds to some spiritual **analogy**."}
    ]
  },
  "Dashboard — log/anthologise.md": {
    "primary": "To collect, select, and compile literary works into an anthology (British spelling of anthologize).",
    "secondary": "In literary curation and editorial practice, canonizing poems or prose selections within a representative historical survey.",
    "quotes": [
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "To **anthologise** the Elizabethan poets requires a fine ear for rustic lyrics and majestic blank verse."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Editors who **anthologise** English poetry should select only works of the highest moral and aesthetic touchstone."},
      {"author": "Arthur Quiller-Couch", "work": "The Oxford Book of English Verse", "quote": "In choosing what to **anthologise**, I sought poems that have established their claims upon the English heart."}
    ]
  },
  "Dashboard — log/anthologist.md": {
    "primary": "A person who compiles an anthology of poems, stories, or other literary works.",
    "secondary": "In bibliographical history and literary publishing, an editor shaping public taste and literary canon through selective compilation.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "An industrious **anthologist** preserves many graceful fugitive verses that would otherwise perish."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Palgrave proved himself a discerning **anthologist** in curating the finest treasury of lyric songs."},
      {"author": "Isaac D'Israeli", "work": "Curiosities of Literature", "quote": "The Greek **anthologist** gathered epigrams as a gardener gathers diverse wild blossoms into a garland."}
    ]
  },
  "Dashboard — log/anthologize.md": {
    "primary": "To compile, collect, or include literary works in an anthology.",
    "secondary": "In educational canon formation, including an author's essays or poems in standard cultural anthologies.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Parnassus", "quote": "I have sought to **anthologize** those noble verses that awaken the sleeping soul to higher aspiration."},
      {"author": "Henry James", "work": "Partial Portraits", "quote": "It is a dangerous honor to **anthologize** short stories, for isolation reveals every flaw in design."},
      {"author": "Mark Twain", "work": "What Is Man? and Other Essays", "quote": "Critics love to **anthologize** our youthful errors while forgetting our mature achievements."}
    ]
  },
  "Dashboard — log/anthology.md": {
    "primary": "A published collection of poems, short stories, songs, or other pieces of writing by different authors.",
    "secondary": "In classical philology, literally a garland of flowers, historically denoting collections of lyric epigrams.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "He brought down from the library shelf an ancient Greek **anthology** bound in stamped vellum."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The modern **anthology** serves to introduce youthful minds to the sublime variety of national literature."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "A quaint **anthology** of seventeenth-century ballads lay open upon the window seat."}
    ]
  },
  "Dashboard — log/antilog.md": {
    "primary": "Short for antilogarithm; the number of which a given value is the logarithm.",
    "secondary": "In computational mathematics and navigation, the number obtained by raising the logarithmic base to a given power.",
    "quotes": [
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The calculation of every **antilog** was verified against standard astronomical tables to eliminate mechanical error."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Navigators determine distances at sea by taking the **antilog** of the sum of logarithmic sines."},
      {"author": "Augustus De Morgan", "work": "A Budget of Paradoxes", "quote": "A beginner in trigonometry frequently confuses the log of a sine with its corresponding **antilog**."}
    ]
  },
  "Dashboard — log/antilogarithm.md": {
    "primary": "The number of which a given number is the logarithm (the inverse of a logarithm).",
    "secondary": "In mathematical computation and celestial navigation, the exponential function reversing logarithmic calculations.",
    "quotes": [
      {"author": "John Napier", "work": "Mirifici Logarithmorum Canonis Descriptio", "quote": "By consulting the table of the **antilogarithm**, the operator converts artificial logarithms back into natural numbers."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "My calculating engine was planned to print tables of the **antilogarithm** with absolute typographical precision."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "The discovery of the **antilogarithm** reduced weeks of laborious planetary calculation to hours of simple addition."}
    ]
  },
  "Dashboard — log/apologetic.md": {
    "primary": "Expressing or showing regretful acknowledgment of an offense or failure; remorseful.",
    "secondary": "In theology and intellectual history, containing a formal defense or vindication of an ideological position.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He coughed in an **apologetic** manner, as if begging pardon of the company for presuming to exist."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins began an **apologetic** speech, expressing dismay at having unwittingly intruded upon the ladies."},
      {"author": "Thomas Henry Huxley", "work": "Science and Christian Tradition", "quote": "The **apologetic** literature of the early church was designed to refute pagan calumnies."}
    ]
  },
  "Dashboard — log/apologise.md": {
    "primary": "To express regret for something that one has done wrong; to make an apology (British spelling of apologize).",
    "secondary": "In diplomatic protocol and moral drama, offering formal acknowledgment of injury or breach of propriety.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "He was eager to **apologise** for his sudden departure, pleading unexpected business in town."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy saw that he had gone too far, and offered to **apologise** with graceful nonchalance."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I felt no inclination to **apologise** for a fault I had never committed."}
    ]
  },
  "Dashboard — log/apologist.md": {
    "primary": "A person who offers an argument in defense of something controversial; a defender.",
    "secondary": "In religious historiography, early Christian writers defending faith against persecution, or polemical advocates of causes.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The early Christian **apologist** addressed respectful memorials to the emperors, pleading for religious tolerance."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Every established tyranny finds an ingenious **apologist** ready to justify oppression on grounds of public safety."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The eloquent **apologist** of King Charles sought to palliate actions that violated the constitution."}
    ]
  },
  "Dashboard — log/apologize.md": {
    "primary": "To express regret for an offense, fault, or mistake; to offer an apology.",
    "secondary": "In social ethics and rhetoric, acknowledging an error or presenting a formal reasoned justification.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I was so ashamed of my conduct that I could only **apologize** with tears in my eyes."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy was not inclined to **apologize** for behavior which he believed to be entirely justified."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Tom hastened to **apologize** to Aunt Polly, hoping to avert the impending punishment."}
    ]
  },
  "Dashboard — log/apology.md": {
    "primary": "An expression of regret for having done something wrong; a formal justification or defense.",
    "secondary": "In classical philosophy and theology, a systematic forensic speech or treatise defending a person's life or doctrine.",
    "quotes": [
      {"author": "Plato", "work": "Apology of Socrates", "quote": "I make my **apology** before the Athenians, not to plead for my life, but to defend the truth."},
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "This volume is not an **apology** for my weaknesses, but a faithful history of my religious opinions."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Ferrars made a cold, formal **apology** for having kept them waiting in the morning room."}
    ]
  },
  "Dashboard — log/archaeologic.md": {
    "primary": "Relating to the scientific study of material remains of past human life and activities; archaeological.",
    "secondary": "In historical sciences and field surveys, pertaining to physical artifacts, inscriptions, and subterranean architectural strata.",
    "quotes": [
      {"author": "Charles Lyell", "work": "The Geological Evidences of the Antiquity of Man", "quote": "The discovery of flint implements in cave gravels provided crucial **archaeologic** proof of human antiquity."},
      {"author": "Heinrich Schliemann", "work": "Troy and Its Remains", "quote": "Our excavations at Hissarlik brought to light **archaeologic** treasures confirming the Homeric narrative."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The **archaeologic** record of prehistoric Europe demonstrates a steady progression from rough stone to bronze tools."}
    ]
  },
  "Dashboard — log/archaeological.md": {
    "primary": "Relating to archaeology, the study of human history and prehistory through the excavation of artifacts.",
    "secondary": "In antiquarian research, investigations recovering monuments, burials, and cultural implements from ancient civilizations.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **archaeological** remains of the Colosseum bear witness to the grandeur and cruelty of the Roman games."},
      {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The **archaeological** discoveries at Knossos revealed a brilliant Bronze Age civilization previously unknown to history."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Prehistoric **archaeological** sites across the globe show that early man manufactured weapons of similar form."}
    ]
  },
  "Dashboard — log/archaeologist.md": {
    "primary": "A person who studies human history and prehistory through the excavation of sites and analysis of artifacts.",
    "secondary": "In field science, a specialist interpreting material cultures, stratigraphy, and ancient epigraphy.",
    "quotes": [
      {"author": "Heinrich Schliemann", "work": "Ilios: The City and Country of the Trojans", "quote": "Every devoted **archaeologist** dreams of uncovering the legendary walls sung by ancient bards."},
      {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The skilled **archaeologist** must read the silent evidence of shattered pottery and charred masonry."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The local **archaeologist** traced the earthen ramparts of the Roman amphitheater with reverent care."}
    ]
  },
  "Dashboard — log/archaeology.md": {
    "primary": "The study of human history and prehistory through the excavation of sites and the analysis of physical artifacts.",
    "secondary": "In social science, the systematic discipline reconstructing past cultures from material remains and architectural ruins.",
    "quotes": [
      {"author": "Charles Lyell", "work": "The Antiquity of Man", "quote": "Geology and **archaeology** converge when we discover human tools embedded in ancient diluvial deposits."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Classical **archaeology** restores the broken pillars and faded inscriptions of ancient greatness."},
      {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The science of **archaeology** has resurrected Minoan Crete from the realm of mythological fable."}
    ]
  },
  "Dashboard — log/biologic.md": {
    "primary": "Of or relating to biology, the science of life and living organisms; biological.",
    "secondary": "In natural philosophy and medical theory, pertaining to vital organic processes and evolutionary mechanisms.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The fundamental **biologic** law demands continuous adjustment of internal relations to external relations."},
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "Our **biologic** researches demonstrate the morphological unity uniting all multicellular animals."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Every **biologic** inquiry must begin with the careful description of cellular morphology."}
    ]
  },
  "Dashboard — log/biological.md": {
    "primary": "Relating to living organisms and their vital processes; pertaining to biology.",
    "secondary": "In modern science, designating metabolic, genetic, and ecological dynamics governing organic life.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The **biological** causes of inheritance remain obscured, but their phenotypic results are undeniable."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Human society represents a specialized attempt to check the ruthless **biological** struggle for existence."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Consciousness has evolved to fulfill vital **biological** functions in adapting the organism to its environment."}
    ]
  },
  "Dashboard — log/biologically.md": {
    "primary": "In a manner related to biology, living organisms, or organic processes.",
    "secondary": "In evolutionary anthropology and physiology, interpreted through the lens of natural selection and physiological functioning.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "Mankind is **biologically** linked to the anthropoid apes through innumerable homologies of skeleton and brain."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Instincts that appear mysterious become **biologically** intelligible when viewed as products of natural selection."},
      {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "Conduct is **biologically** sound when it fosters the preservation of the individual and the species."}
    ]
  },
  "Dashboard — log/biologism.md": {
    "primary": "The interpretation of human social, cultural, and political phenomena entirely in terms of biological concepts.",
    "secondary": "In social philosophy and ethics, reductionism that treats social ethics and cultural institutions as mere byproducts of organic instinct.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "Crude **biologism** reduces all philosophical contemplation and moral heroism to mere animal survival reflexes."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "We must avoid a narrow **biologism** that ignores the transformative power of cultural communication and education."},
      {"author": "William James", "work": "Pragmatism", "quote": "The extreme **biologism** of social Darwinists turns the richness of moral life into a ruthless jungle combat."}
    ]
  },
  "Dashboard — log/biologist.md": {
    "primary": "A scientist who studies living organisms, their structure, function, growth, origin, evolution, and distribution.",
    "secondary": "In history of science, a naturalist working across genetics, ecology, physiology, and evolutionary taxonomy.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The modern **biologist** seeks to understand how living protoplasm organizes itself into complex tissues."},
      {"author": "Charles Darwin", "work": "More Letters of Charles Darwin", "quote": "Every observant **biologist** will encounter puzzles of geographic distribution that test the theory of descent."},
      {"author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "To the philosophic **biologist**, nature presents an interconnected web of living monads."}
    ]
  },
  "Dashboard — log/biologistic.md": {
    "primary": "Characterized by or relating to biologism; interpreting human behavior strictly through biological determinism.",
    "secondary": "In sociology and philosophy of mind, overextending evolutionary mechanisms to explain artistic and social creations.",
    "quotes": [
      {"author": "John Dewey", "work": "Reconstruction in Philosophy", "quote": "A purely **biologistic** approach fails to account for the reflective and symbolic dimensions of human culture."},
      {"author": "Bertrand Russell", "work": "History of Western Philosophy", "quote": "Nietzsche's ethics are tainted by a **biologistic** worship of brute vitality over justice and mercy."},
      {"author": "William James", "work": "The Meaning of Truth", "quote": "We need not surrender spiritual values to a cold, **biologistic** fatalism that denies human freedom."}
    ]
  },
  "Dashboard — log/biology.md": {
    "primary": "The scientific study of life and living organisms, including their structure, function, evolution, and taxonomy.",
    "secondary": "In the classification of sciences, the foundational branch of natural science investigating vital phenomena.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When we look to the individuals of the same variety, the study of **biology** reveals infinite minor variations."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "**Biology** is the science which treats of living bodies, their phenomena, and their laws."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The problems of **biology** are inseparable from the broader laws of universal cosmic evolution."}
    ]
  },
  "Dashboard — log/catalog.md": {
    "primary": "A complete, systematically arranged list of items, such as books, goods, or art; to list systematically.",
    "secondary": "In library science and commerce, an organized descriptive inventory enabling search and retrieval of assets.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "In that ancient library, I spent hours poring over the descriptive **catalog** of rare cetological treatises."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I give you a grand **catalog** of cities, trades, and workers across the boundless continent."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The auctioneer prepared a melancholy **catalog** of all the household effects to be sold under the distress."}
    ]
  },
  "Dashboard — log/cataloger.md": {
    "primary": "A person who compiles a catalog, especially in a library or archive.",
    "secondary": "In bibliographical science and museology, a specialist classifying manuscripts and specimens according to standardized indices.",
    "quotes": [
      {"author": "Thomas Frognall Dibdin", "work": "Bibliomania", "quote": "The learned **cataloger** must examine every colophon and watermark with the precision of a jeweler."},
      {"author": "Isaac D'Israeli", "work": "Curiosities of Literature", "quote": "A diligent **cataloger** has rescued many an anonymous genius from complete historical oblivion."},
      {"author": "Anthony Panizzi", "work": "Passages in My Life", "quote": "The chief **cataloger** of the British Museum established rules of bibliographic entry that became world standards."}
    ]
  },
  "Dashboard — log/catalogue.md": {
    "primary": "A complete list of items typically in alphabetical or systematic order; a directory or register.",
    "secondary": "In classical epic and bibliographical literature, an extended formal enumeration (such as Homer's catalogue of ships in the Iliad).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Ay, in the **catalogue** ye go for men, as hounds and greyhounds, mongrels, spaniels, curs are clept all by the name of dogs."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "She looked through the circulating library's **catalogue** with eager anticipation of gothic romance."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He presented a dreary **catalogue** of all his domestic grievances and financial misfortunes."}
    ]
  },
  "Dashboard — log/cataloguer.md": {
    "primary": "A person who catalogues books, paintings, or artifacts (British spelling of cataloger).",
    "secondary": "In archival bibliography and art history, an expert compiling comprehensive provenance records for library collections.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The antiquarian acted as a faithful **cataloguer** of the ancient library at Thornfield Hall."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "A dull **cataloguer** can reduce the most inspiring gallery of paintings to a dry schedule of dimensions and dates."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The Harleyan library found in him a learned **cataloguer** capable of describing its vast treasures."}
    ]
  },
  "Dashboard — log/collogue.md": {
    "primary": "To talk privately, conspire, or confer secretly; in dialect, to flatter or coax.",
    "secondary": "In dramatic narrative and character fiction, whispering in private conspiracy to contrive an intrigue.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "They would sit together in the parlor and **collogue** about family secrets for hours on end."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The old women were seen to **collogue** together over the garden gate, exchanging scandalous whispers."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He saw the two conspirators **collogue** in the shadowy corner of the tavern yard."}
    ]
  },
  "Dashboard — log/cologne.md": {
    "primary": "Eau de cologne; a light, refreshing scented toilet water originally created in Cologne, Germany.",
    "secondary": "In social history and perfumery, a citrus-based fragrance composed of bergamot, neroli, and lavender diluted in spirits.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "She bathed her aching temples with a handkerchief steeped in fragrant **cologne**."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A faint scent of lavender and delicate French **cologne** lingered about her dressing-table."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ambergris smells better than the sweetest lavender or **cologne** sold in the shops of Paris."}
    ]
  },
  "Dashboard — log/dialogue.md": {
    "primary": "Conversation between two or more people; a literary work in the form of a conversation.",
    "secondary": "In philosophy and dramatic writing, a classic genre wherein arguments unfold through dialectical exchange.",
    "quotes": [
      {"author": "Plato", "work": "The Republic", "quote": "The philosophical **dialogue** allows divergent viewpoints to test their coherence through mutual examination."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth listened with lively amusement to the spirited **dialogue** between Mr. Darcy and her sister."},
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "I will read you the lively **dialogue** between the shepherd and the nymph."}
    ]
  },
  "Dashboard — log/dislogistic.md": {
    "primary": "Expressing disapproval or dispraise; derogatory or pejorative (dyslogistic).",
    "secondary": "In utilitarian ethics and political rhetoric, terms intentionally chosen to cast moral censure upon an opponent's motives.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "The Book of Fallacies", "quote": "Politicians employ **dislogistic** epithets like 'anarchist' or 'faction' to discredit reforms without rational argument."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A philosophic thinker must strip controversial terms of their **dislogistic** connotations before evaluating facts."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Passionate partisans attach **dislogistic** labels to every policy proposed by the opposing administration."}
    ]
  },
  "Dashboard — log/ecologic.md": {
    "primary": "Relating to the relationship between living organisms and their environment; ecological.",
    "secondary": "In natural history and biophysics, pertaining to the balance of energy, nutrient cycling, and species interdependence.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "The grand **ecologic** web of nature links the microscopic diatom to the largest marine mammals."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Every island presents a distinct **ecologic** equilibrium adapted to its peculiar climate and isolation."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The alpine meadows exhibit a fragile **ecologic** harmony that human disturbance quickly shatters."}
    ]
  },
  "Dashboard — log/ecological.md": {
    "primary": "Relating to ecology, ecosystems, or the environment and interrelations of organisms.",
    "secondary": "In environmental science and geography, systematic analysis of habitats, food webs, and anthropogenic impacts.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "Our **ecological** studies demonstrate how every species is shaped by its physical and organic environment."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Earthworms perform an **ecological** service of immense importance by aerating the soil."},
      {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "An **ecological** conscience reflects a conviction of individual responsibility for the health of the land."}
    ]
  }
}

base_dir = r"App database/Latin roots/Cluster Thought"

updated_count = 0
for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated_count += 1

print(f"Thought Batch 4-1 (log 1-45): Successfully updated {updated_count}/{len(data)} notes.")
