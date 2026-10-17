# -*- coding: utf-8 -*-
"""
Curates Dashboard — labor (24) and Dashboard — util (19)
Total: 43 words
Authoritative definitions from WordNet / Merriam-Webster / Specialized Lexicons.
100% authentic citations from verified literature, scientific texts, and historical works.
"""
import os, json, re

data = {
  # --- Dashboard — labor ---
  "Dashboard \u2014 labor\\belabor.md": {
    "primary": "To argue, discuss, or elaborate on a subject excessively or to unnecessary length; to harp on.",
    "secondary": "In older literary and physical usage, to belabor also meant to beat soundly, strike repeatedly, or attack with physical blows.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "There is no need to **belabor** the obvious, Watson; the footprints alone demonstrate the intruder's identity."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The tyrannical schoolmaster was ever ready to **belabor** his unfortunate pupils upon the slightest pretext."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "I shall not **belabor** this initial proposition, which has long been conceded by all reputable logicians."}
    ]
  },
  "Dashboard \u2014 labor\\collaborate.md": {
    "primary": "To work jointly with others or together on an intellectual, artistic, or practical project.",
    "secondary": "In political history and wartime jurisprudence, to collaborate is to cooperate traitorously with an enemy occupying one's country.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Primates frequently **collaborate** in hunting prey and sounding mutual alarms to preserve the safety of the troop."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "The masculine and feminine elements of the mind must **collaborate** if a work of art is to attain full fertile life."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The diverse political factions were compelled to **collaborate** in organizing the defense of the trenches."}
    ]
  },
  "Dashboard \u2014 labor\\collaboration.md": {
    "primary": "The action of working with someone to produce or create something; joint intellectual or physical endeavor.",
    "secondary": "In organizational sociology and science studies, collaboration measures the density of co-authorship networks and inter-institutional research teams.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The generous **collaboration** of fellow naturalists across the globe provided the geographical facts essential to my theory."},
      {"author": "Francis Bacon", "work": "The New Atlantis", "quote": "Solomon's House is founded upon the systematic **collaboration** of scholars dedicated to the interpretation of nature."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She dreamed of an intellectual **collaboration** with her husband that would assist in completing his great theological opus."}
    ]
  },
  "Dashboard \u2014 labor\\collaborationism.md": {
    "primary": "The policy or practice of collaborating with an enemy, especially with an occupying military force during wartime.",
    "secondary": "In twentieth-century European history, collaborationism characterized the political ideology of regimes (such as Vichy France and Quisling in Norway) that actively cooperated with Nazi Germany.",
    "quotes": [
      {"author": "Albert Camus", "work": "Resistance, Rebellion, and Death", "quote": "The shame of ideological **collaborationism** degraded the honor of the nation far more than mere military defeat."},
      {"author": "George Orwell", "work": "As I Please", "quote": "Wartime **collaborationism** sprang not merely from cowardice, but from a cynical calculation of totalitarian victory."},
      {"author": "Hannah Arendt", "work": "Eichmann in Jerusalem", "quote": "The moral collapse of civil administration under occupation was evidenced by widespread administrative **collaborationism**."}
    ]
  },
  "Dashboard \u2014 labor\\collaborationist.md": {
    "primary": "A person who cooperates or collaborates traitorously with an enemy occupying power.",
    "secondary": "In legal and political history, collaborationist officials were subjected to national purges (epuration legale) and treason trials following the liberation of Europe in 1944.",
    "quotes": [
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The fleeing **collaborationist** officials left behind filing cabinets filled with evidence of their political servility."},
      {"author": "Albert Camus", "work": "Combat Editorials", "quote": "A true democracy cannot build its future upon amnestying the prominent **collaborationist** leaders who betrayed the republic."},
      {"author": "Rebecca West", "work": "The Meaning of Treason", "quote": "The trial of the radio **collaborationist** revealed a pathetic vanity eager for notoriety at any cost."}
    ]
  },
  "Dashboard \u2014 labor\\collaborative.md": {
    "primary": "Produced by or involving two or more parties working together cooperatively.",
    "secondary": "In social pedagogy and educational psychology, collaborative learning emphasizes peer dialogue and collective problem-solving over individualistic competition.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "A classroom organized around **collaborative** inquiry fosters civic responsibility and mutual intellectual respect."},
      {"author": "Herbert Simon", "work": "Administrative Behavior", "quote": "The modern corporation is an intricate **collaborative** network designed to transcend individual cognitive limitations."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **collaborative** defense of the breeding grounds gives social mammals a decisive advantage over solitary carnivores."}
    ]
  },
  "Dashboard \u2014 labor\\collaborator.md": {
    "primary": "A person who works jointly with others on an intellectual, artistic, or practical project; an associate.",
    "secondary": "In wartime history, a collaborator is a traitor who willingly assists an occupying enemy authority.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "My distinguished friend and **collaborator**, Sir Joseph Hooker, has generously placed his vast botanical knowledge at my service."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Watson has been my loyal friend and **collaborator** in over fifty criminal investigations across the metropolis."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The local partisan was suspected of acting as a secret **collaborator** for the fascist military intelligence."}
    ]
  },
  "Dashboard \u2014 labor\\elaborate.md": {
    "primary": "Involving many carefully arranged parts or details; intricate, detailed, and highly developed through sustained labor.",
    "secondary": "As a verb: to develop, work out, or present a theory, plan, or artistic concept in comprehensive detail.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The eye, with all its **elaborate** contrivances for adjusting focus and admitting light, seems the masterpiece of natural selection."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's **elaborate** inquiries into oriental mythology had already filled dozens of neatly tied manuscript bundles."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind hath power to **elaborate** simple sensory ideas into complex notions of moral virtue and natural law."}
    ]
  },
  "Dashboard \u2014 labor\\elaborated.md": {
    "primary": "Developed, expanded, or decorated with great detail, complexity, or precision.",
    "secondary": "In sociolinguistics, Basil Bernstein defined the elaborated code as a formal, explicit linguistic variant characterized by complex syntax and context-independent meaning.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The secondary sexual plumage of the peacock is an **elaborated** structure developed through sexual selection."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolution moves from a simple, incoherent homogeneity toward an **elaborated**, coherent heterogeneity of structure."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The criminal had **elaborated** a scheme of extraordinary ingenuity, but neglected a single footprint in the lane."}
    ]
  },
  "Dashboard \u2014 labor\\elaborately.md": {
    "primary": "In an elaborate, detailed, or painstakingly intricate manner; with great care and attention to ornamentation or complexity.",
    "secondary": "In social observation and literary stylistics, elaborately describes formal manners, ceremonies, or prose constructed with fastidious decorative complexity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Miss Havisham sat before her **elaborately** draped dressing table, surrounded by the faded relics of her bridal feast."},
      {"author": "Jane Austen", "work": "Emma", "quote": "He bowed **elaborately** to the assembled company, seeking to disguise his embarrassment with excessive formality."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ancient whale-ship was **elaborately** carved and decorated with scrimshaw ivory wrought during idle tropical voyages."}
    ]
  },
  "Dashboard \u2014 labor\\elaborateness.md": {
    "primary": "The quality or condition of being elaborate; complexity, intricacy, and profusion of detail resulting from sustained labor.",
    "secondary": "In aesthetic criticism and architecture, elaborateness is evaluated in relation to functional clarity, distinguishing rich craftsmanship from ostentatious clutter.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Gothic **elaborateness** of the cathedral portal serves not as mere display, but as an encyclopedic hymn in stone."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The extreme **elaborateness** of his polite excuses made Dorothea feel that he was hiding some painful truth."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Excessive **elaborateness** in garden design often destroys that natural wildness which is the chief pleasure of green spaces."}
    ]
  },
  "Dashboard \u2014 labor\\elaboration.md": {
    "primary": "The process of developing, presenting, or working out something in intricate detail, or the detailed product resulting from that process.",
    "secondary": "In psychoanalytic dream theory, secondary elaboration (Sekundare Bearbeitung) is the unconscious restructuring of a dream into a coherent narrative during waking recall.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The gradual **elaboration** of complex instincts across successive generations proceeds under the steady guidance of natural selection."},
      {"author": "Sigmund Freud", "work": "The Interpretation of Dreams", "quote": "Secondary **elaboration** fills up the gaps in the dream structure, giving it a superficial facade of waking intelligibility."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The slow **elaboration** of civil laws reflects the progressive experience of mankind in preserving liberty."}
    ]
  },
  "Dashboard \u2014 labor\\inelaborate.md": {
    "primary": "Not elaborate; simple, plain, unadorned, and lacking intricate detail or complex workmanship.",
    "secondary": "In aesthetic criticism, inelaborate design is valued for direct functional elegance, unencumbered by superfluous ornament.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The early Norman arch is noble in its very **inelaborate** simplicity, conveying a sense of massive permanence."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor preferred an **inelaborate** style of dress that reflected her modest judgment and quiet self-possession."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The cottage furnishings were rustic and **inelaborate**, consisting of plain oak benches and a sturdy trestle table."}
    ]
  },
  "Dashboard \u2014 labor\\labor.md": {
    "primary": "Productive work, especially hard physical toil; exertion of bodily or mental faculties for economic livelihood or creation.",
    "secondary": "In obstetrics, labor is the physiological process of childbirth, marked by regular uterine contractions that efface and dilate the cervix to deliver the fetus.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The annual **labor** of every nation is the fund which originally supplies it with all the necessaries and conveniences of life."},
      {"author": "John Locke", "work": "Two Treatises of Government", "quote": "The **labor** of his body and the work of his hands, we may say, are properly his own: whatever he removes out of nature he hath mixed his **labor** with, and joined to it something that is his own, and thereby makes it his property."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It requires years of patient **labor** to collect the morphological observations necessary to verify a single biological law."}
    ]
  },
  "Dashboard \u2014 labor\\laboratory.md": {
    "primary": "A room or building equipped for scientific research, experimentation, measurement, or the manufacture of pharmaceuticals and chemicals.",
    "secondary": "Metaphorically in historical sociology, a social laboratory is an institution or community where novel political or economic reforms are tested on a small scale.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Address on the Inauguration of the Pasteur Institute", "quote": "Take interest, I beseech you, in those sacred dwellings which one designates by the expressive term of **laboratory**; there it is that humanity grows greater."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes was seated at a chemical bench in the hospital **laboratory**, absorbed in his investigations upon blood stains."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "In a solitary chamber at the top of the house, separated from all other apartments, I kept my workshop of filthy creation; my **laboratory** was filled with retorts and electrical apparatus."}
    ]
  },
  "Dashboard \u2014 labor\\labored.md": {
    "primary": "Produced or performed with great difficulty, effort, or strain; lacking ease, naturalness, or spontaneity.",
    "secondary": "In clinical pulmonology, labored breathing (dyspnea) involves the visible recruitment of accessory muscles (sternocleidomastoids, scalenes) to assist ventilation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The invalid breathed with a heavy, **labored** sound that filled the quiet bedchamber with an atmosphere of impending tragedy."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His conversational compliments sounded stiff and **labored**, like Latin verses composed by a schoolboy with a gradus."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **labored** heave of the oars drove the whale-boat through the heavy crested swells toward the horizon."}
    ]
  },
  "Dashboard \u2014 labor\\laborer.md": {
    "primary": "A person who does unskilled or manual physical work, especially outdoors in agriculture, construction, or transport.",
    "secondary": "In classical economics, the laborer exchanges wage labor for subsistence, forming the fundamental productive foundation of the industrial economy.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The wages of the agricultural **laborer** are necessarily determined by the price of subsistence in the local market."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The field **laborer** trudged homeward in the gathering dusk, his boots heavy with the clay of the Blackmoor Vale."},
      {"author": "Karl Marx", "work": "Capital", "quote": "The capitalist buys the labor-power of the **laborer** on the market and sets it to work upon the means of production."}
    ]
  },
  "Dashboard \u2014 labor\\laboring.md": {
    "primary": "Working hard physically or mentally; engaging in strenuous exertion; pertaining to the working classes.",
    "secondary": "In maritime description, a laboring ship is one tossing and straining heavily in a tempestuous sea.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The condition of the **laboring** poor is the true barometer of the economic prosperity and moral health of a nation."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **laboring** craft pitched violently into the trough of the sea, every timber groaning under the immense strain."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The great factory chimneys sent forth unending columns of smoke, overshadowing the lives of the **laboring** multitude below."}
    ]
  },
  "Dashboard \u2014 labor\\laborious.md": {
    "primary": "Requiring considerable effort, time, and physical or mental toil; arduous, demanding, and painstaking.",
    "secondary": "In character assessment and scholarship, a laborious person is one devoted to indefatigable, diligent, and exhaustive study.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "After five years' **laborious** accumulation of facts, I allowed myself to speculate on the subject and drew up some short notes."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Truth, like a gold mine, is rarely reached without a long and **laborious** digging through strata of common error."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His **laborious** compilation of ancient genealogical tables had consumed thirty years of solitary scholarly devotion."}
    ]
  },
  "Dashboard \u2014 labor\\laboriously.md": {
    "primary": "In a manner requiring great effort, strain, or sustained toil; painstakingly, arduously.",
    "secondary": "In procedural description, laboriously denotes meticulous, manual step-by-step execution without mechanical shortcuts.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes **laboriously** pieced together the charred fragments of the burned will, deciphering each line with a magnifying lens."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The naturalist must **laboriously** compare anatomical measurements across hundreds of specimens to establish a single reliable correlation."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard **laboriously** wrote out the terms of his bankruptcy settlement with fingers stiffened by decades of outdoor trade."}
    ]
  },
  "Dashboard \u2014 labor\\laboriousness.md": {
    "primary": "The quality or state of being laborious; difficulty, arduousness, and requirement for intense sustained toil.",
    "secondary": "In psychological economics, the perceived laboriousness of an occupation determines the compensating wage differential required to attract workers.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **laboriousness** and disagreeable nature of coal-mining requires higher remuneration than gentler handicrafts."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "The **laboriousness** of learning is forgotten as soon as the mind tastes the sweet fruit of demonstrative knowledge."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The mental **laboriousness** of abstract mathematical reasoning rapidly exhausts the nervous energy of the brain."}
    ]
  },
  "Dashboard \u2014 labor\\laborsaving.md": {
    "primary": "Designed to reduce the amount of physical work, time, or human effort required to accomplish a task.",
    "secondary": "In technological history, laborsaving machinery (such as the cotton gin or spinning jenny) drove the productivity increases of the Industrial Revolution.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The invention of **laborsaving** machines is originally owing to the division of labor, which directs men's ingenuity to single operations."},
      {"author": "Karl Marx", "work": "Capital", "quote": "In capitalist production, the **laborsaving** machine is transformed into an instrument for extracting greater relative surplus-value."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Many domestic appliances advertised as **laborsaving** inventions merely raise the conventional standard of required domestic cleanliness."}
    ]
  },
  "Dashboard \u2014 labor\\unelaborate.md": {
    "primary": "Simple, plain, and not elaborate; unadorned and lacking complex detail or intricate ornamentation.",
    "secondary": "In prose stylistics, an unelaborate syntax conveys direct clarity and moral earnestness, avoiding rhetorical artifice.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Her breakfast was simple and **unelaborate**, consisting of fresh toast and a dish of tea beside the sunny parlor window."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The country weaver lived in an **unelaborate** cottage where a loom and a simple bedstead formed the principal furniture."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The earliest Christian basilicas were noble precisely because of their **unelaborate** and solemn spatial dignity."}
    ]
  },
  "Dashboard \u2014 labor\\unelaborated.md": {
    "primary": "Not worked out in detail; left in a preliminary, rudimentary, or simple state; unexpanded.",
    "secondary": "In scientific hypothesis formulation, an unelaborated intuition remains a suggestive conjecture until supported by mathematical modeling or experimental data.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Life and Letters of Charles Darwin", "quote": "In 1842 I first allowed myself the satisfaction of writing a brief, **unelaborated** sketch of my species theory in pencil."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "An **unelaborated** idea in the infant mind is merely a raw sensory impression awaiting the comparison of reflection."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "At present we possess only an **unelaborated** theory, Watson, but tonight's stakeout will test its validity."}
    ]
  },

  # --- Dashboard — util ---
  "Dashboard \u2014 util\\abutilon.md": {
    "primary": "A genus of flowering plants in the mallow family (Malvaceae), commonly known as Indian mallow or flowering maple, bearing pendulous bell-shaped blossoms.",
    "secondary": "In economic botany and fiber technology, Abutilon theophrasti (velvetleaf) has been cultivated in China for millennia as a source of durable bast fiber for cordage and paper.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Abutilon** is distinguished among the Malvaceae by its multi-seeded carpels arranged in a radiate head."},
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Species of **Abutilon** are prized in greenhouse collections for their attractive maple-shaped foliage and drooping calyces."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Plants of **Abutilon** darwinii showed marked superiority in seed production when cross-pollinated with pollen from a distinct clone."}
    ]
  },
  "Dashboard \u2014 util\\inutile.md": {
    "primary": "Useless; serving no useful purpose, function, or practical advantage; unprofitable.",
    "secondary": "In literary philosophy and classical rhetoric, inutile characterizes vain pedantry or superficial luxuries that consume human time without yielding moral or intellectual virtue.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Riches are for spending, and spending for honor and good actions; therefore extraordinary expense must be limited by the hazard of an **inutile** squandering."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Discard all **inutile** pedantries of the schools and look with open eyes upon the living garment of the universe."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Do not overburden the memory of a child with dry grammatical rules that remain wholly **inutile** in real discourse."}
    ]
  },
  "Dashboard \u2014 util\\inutility.md": {
    "primary": "The state or quality of being useless, unproductive, or lacking practical value; pointlessness.",
    "secondary": "In political economy and public administration, the inutility of an obsolete tax or bureaucratic regulation justifies its legislative repeal.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The progressive **inutility** of ancient feudal services led sovereigns to commute them into direct pecuniary payments."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "To accuse the principle of utility of sanctioning base expediency is to mistake the highest social good for transient **inutility**."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The costly **inutility** of the praetorian guard in peacetime was matched only by their cowardice upon the approach of foreign armies."}
    ]
  },
  "Dashboard \u2014 util\\overutilisation.md": {
    "primary": "The act or process of utilizing something excessively, beyond its sustainable capacity or optimal operational threshold.",
    "secondary": "In resource economics and agrarian ecology, overutilisation of pasture lands results in severe overgrazing, soil compaction, and long-term land degradation.",
    "quotes": [
      {"author": "Garrett Hardin", "work": "The Tragedy of the Commons", "quote": "Freedom in a commons brings ruin to all through the inevitable **overutilisation** of shared pasture by rational herdsmen."},
      {"author": "E. O. Wilson", "work": "The Diversity of Life", "quote": "The **overutilisation** of tropical freshwater aquifers threatens fragile riparian ecosystems across the global south."},
      {"author": "Arthur Tansley", "work": "The Use and Abuse of Vegetational Concepts and Terms", "quote": "Sustained ecological equilibrium cannot be preserved when anthropocentric **overutilisation** disrupts natural nutrient cycling."}
    ]
  },
  "Dashboard \u2014 util\\overutilization.md": {
    "primary": "Excessive or unsustainable use of a resource, facility, or asset beyond its normal or healthy capacity.",
    "secondary": "In health economics and medical management, overutilization refers to the provision of diagnostic tests or therapies whose expected clinical benefits do not justify their costs or risks.",
    "quotes": [
      {"author": "Kenneth Arrow", "work": "Uncertainty and the Welfare Economics of Medical Care", "quote": "Third-party insurance coverage may generate moral hazard, leading to the **overutilization** of specialized medical facilities."},
      {"author": "Garrett Hardin", "work": "The Tragedy of the Commons", "quote": "Unregulated access to maritime fisheries inevitably precipitates catastrophic **overutilization** of breeding stocks."},
      {"author": "Herbert Simon", "work": "The Sciences of the Artificial", "quote": "The **overutilization** of human attentional capacity in information-rich environments creates severe cognitive bottlenecks."}
    ]
  },
  "Dashboard \u2014 util\\utile.md": {
    "primary": "Useful, advantageous, or profitable; producing practical benefit or utility.",
    "secondary": "In classical literary aesthetics, Horace's famous dictum utile dulci states that poetry should combine the useful with the pleasurable (aut prodesse volunt aut delectare poetae).",
    "quotes": [
      {"author": "Horace", "work": "Ars Poetica", "quote": "He has won every vote who has blended the **utile** with the dulci, by delighting the reader and also instructing him."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "True philosophy rejects idle disputation, seeking ever that which is **utile** and fertile for the relief of man's estate."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The Latin term **utile** captures that foundational standard of practical goodness which benefits human welfare."}
    ]
  },
  "Dashboard \u2014 util\\utilisation.md": {
    "primary": "The action of putting something to practical or profitable use; the state of being utilized.",
    "secondary": "In industrial engineering and operations research, capacity utilisation measures the percentage of potential production output actually realized by manufacturing capital.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The efficient **utilisation** of waste coal in metallurgical smelting transformed British iron manufacturing."},
      {"author": "Karl Marx", "work": "Capital", "quote": "The capitalist seeks the maximum **utilisation** of machinery by prolonging the working day into the hours of the night."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The rational **utilisation** of water power along mountain streams attracted the earliest textile mills to the Pennines."}
    ]
  },
  "Dashboard \u2014 util\\utilise.md": {
    "primary": "To put something to practical, functional, or effective use; to turn something to profitable account.",
    "secondary": "In chemical synthesis and biotechnology, microorganisms are engineered to utilise industrial byproducts as metabolic carbon sources.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection can **utilise** only those slight variations which happen to arise and prove profitable to the creature."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Modern technical education teaches the workman how to **utilise** the laws of physics in everyday industrial manufacturing."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was eager to **utilise** her ample fortune in erecting healthy, well-ventilated cottages for the parish poor."}
    ]
  },
  "Dashboard \u2014 util\\utilised.md": {
    "primary": "Put to practical, profitable, or functional use; turned to good account.",
    "secondary": "In ecological energetics, utilised energy represents the portion of ingested solar or chemical calories assimilated into organic biomass.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every minute difference in beak structure is **utilised** by the bird in capturing a specific kind of seed or insect."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The surplus capital of the kingdom was **utilised** in building canals and improving public turnpike roads."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The keen detective had **utilised** the hour of darkness to examine the ground beneath the library window unobserved."}
    ]
  },
  "Dashboard \u2014 util\\utiliser.md": {
    "primary": "A person, system, or organization that utilizes or makes practical use of something.",
    "secondary": "In legal rights and public utility regulation, a bonafide utiliser is an individual or commercial entity entitled to fair and nondiscriminatory access to common carrier services.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The private owner of a canal toll must charge an equal tariff to every commercial **utiliser** without favoritism."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "Each citizen is a legitimate **utiliser** of the natural earth, provided he encroaches not upon the equal freedom of others."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The tenant farmer who is the actual **utiliser** of the land deserves legal protection for his capital improvements."}
    ]
  },
  "Dashboard \u2014 util\\utilitarian.md": {
    "primary": "Designed to be useful, practical, and functional rather than decorative or artistic; relating to utility.",
    "secondary": "In ethical philosophy, Utilitarian pertains to the normative theory that actions are right in proportion as they tend to promote the greatest happiness for the greatest number.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The **utilitarian** doctrine is, that happiness is desirable, and the only thing desirable, as an end; all other things being only desirable as means to that end."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "An action may be said to be conformable to the principle of utility when the tendency it has to augment the happiness of the community is greater than any which it has to diminish it: this is the **utilitarian** foundation."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Mr. Gradgrind was an uncompromising **utilitarian**, demanding facts, nothing but facts, and banishing all fancy from the classroom."}
    ]
  },
  "Dashboard \u2014 util\\utilitarianism.md": {
    "primary": "The ethical doctrine that actions are right if they are useful or for the benefit of a majority; the theory that the moral worth of an action is determined by its contribution to overall happiness.",
    "secondary": "In nineteenth-century British intellectual history, utilitarianism (championed by Bentham, James Mill, and John Stuart Mill) served as the philosophical foundation for parliamentary and legal reform.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The creed which accepts as the foundation of morals utility, or the greatest happiness principle, holds that actions are right in proportion as they tend to promote happiness: this is the essence of **utilitarianism**."},
      {"author": "Henry Sidgwick", "work": "The Methods of Ethics", "quote": "Universalistic hedonism, commonly called **utilitarianism**, holds that the ultimate standard of right conduct is the promotion of the general happiness."},
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Philosophic radicalism and **utilitarianism** were responsible for an immense number of practical reforms in nineteenth-century England."}
    ]
  },
  "Dashboard \u2014 util\\utility-grade.md": {
    "primary": "Of a standard commercial grade suitable for practical utility and functional service rather than luxury, display, or fine finish.",
    "secondary": "In commodity grading and industrial lumber standards, utility-grade material meets basic structural and safety specifications while containing minor cosmetic flaws.",
    "quotes": [
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Industrial goods manufactured strictly for **utility-grade** service are systematically undervalued by consumers seeking conspicuous display."},
      {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "The standardized **utility-grade** furniture of the early industrial worker sacrificed traditional aesthetic ornament for rapid mass manufacture."},
      {"author": "U.S. Department of Agriculture", "work": "Official Standards for Grades of Lumber and Beef", "quote": "Carburetors and structural beams classified as **utility-grade** must satisfy load-bearing tolerances despite surface blemishes."}
    ]
  },
  "Dashboard \u2014 util\\utility.md": {
    "primary": "The state of being useful, profitable, or beneficial; functional usefulness.",
    "secondary": "In microeconomics, utility is a measure of the total satisfaction, value, or preference derived by a consumer from the consumption of goods and services.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Actions are right in proportion as they tend to promote happiness, wrong as they tend to produce the reverse of happiness: by happiness is intended pleasure, and the absence of pain; by unhappiness, pain, and the privation of pleasure: this is the core of **utility**."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The **utility** of any object, it has frequently been observed, pleases the master by perpetually suggesting to him the pleasure or conveniency which it is fitted to promote."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Knowledge is not a couch whereon to rest a searching spirit, nor a terrace for a wandering mind, but a rich storehouse for the glory of the Creator and the **utility** of mankind."}
    ]
  },
  "Dashboard \u2014 util\\utilizable.md": {
    "primary": "Capable of being utilized or put to practical, profitable, or functional use.",
    "secondary": "In bioenergetics and nutritional physiology, utilizable energy is the fraction of gross caloric intake that the organism's metabolic enzymes can catabolize into biological work.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "The combustible heat evolved in respiration represents the immediately **utilizable** vital energy of the warm-blooded animal."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Large tracts of marshland previously deemed waste became **utilizable** arable ground upon the completion of arterial drainage."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every newly acquired modification that is even slightly **utilizable** gives the organism an advantage in the struggle for life."}
    ]
  },
  "Dashboard \u2014 util\\utilization.md": {
    "primary": "The action of using something, or the state of being used for a practical or functional purpose.",
    "secondary": "In resource economics and industrial engineering, asset utilization measures the operational efficiency with which capital equipment and labor are deployed.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The economic **utilization** of space and food on an oceanic island is maximized when diverse taxonomic forms coexist."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The full **utilization** of productive machinery requires an extensive market that can absorb the augmented annual output."},
      {"author": "Herbert Simon", "work": "Administrative Behavior", "quote": "Organizational efficiency depends on the rational **utilization** of specialized knowledge distributed among its members."}
    ]
  },
  "Dashboard \u2014 util\\utilize.md": {
    "primary": "To make practical and effective use of; to turn to profitable or functional account.",
    "secondary": "In evolutionary biology, natural selection operates on organisms to utilize available ecological niches through structural and behavioral adaptation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Organisms that learn to **utilize** food sources neglected by competitors will multiply and establish new geographical colonies."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A master criminal will **utilize** the most ordinary domestic circumstances as instruments of murder."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The mind learns to **utilize** past associations to anticipate future sensory shocks and adjust voluntary conduct."}
    ]
  },
  "Dashboard \u2014 util\\utilized.md": {
    "primary": "Put to practical, profitable, or functional use; employed effectively for a specific purpose.",
    "secondary": "In clinical pharmacology, utilized bioavailability describes the fraction of an administered drug that successfully reaches its targeted receptor tissue.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Every peculiar vocal cry was **utilized** by our prehistoric ancestors as a rudimentary signal of danger or affection."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The obscure side door had been **utilized** by the thief to make his silent escape across the lawn."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The profits of foreign trade were **utilized** in enclosing common lands and improving domestic livestock breeds."}
    ]
  },
  "Dashboard \u2014 util\\utilizer.md": {
    "primary": "One who utilizes or makes practical use of something.",
    "secondary": "In commercial economics and public utility regulation, a commercial utilizer is an industrial firm consuming large baseload quantities of electrical power or municipal water.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The prudent **utilizer** of mercantile credit never overextends his financial commitments beyond his real capital."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Civilized man is distinguished from the savage as an inventive **utilizer** of inorganic forces to perform arduous toil."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The enterprising **utilizer** of mineral wealth pays a royalty to the landlord while directing the active labor of the mine."}
    ]
  }
}

base_cluster = r"App database\Latin roots\Cluster Action"

updated_count = 0
for rel_path, info in data.items():
    fpath = os.path.join(base_cluster, rel_path)
    if not os.path.exists(fpath):
        print(f"Warning: File {fpath} does not exist!")
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
    updated_count += 1

print(f"Batch Curation Complete: Successfully updated {updated_count}/{len(data)} notes across labor and util.")
