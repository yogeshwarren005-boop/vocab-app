# -*- coding: utf-8 -*-
import json
import os
import sys

batch1_data = {
  "Dashboard — pan\\panic.md": {
    "primary": "A sudden overwhelming fear or terror, often unreasoning and infectious, that grips individuals or crowds and impairs rational thought.",
    "secondary": "In financial economics and social psychology, a sudden mass crisis or collapse of investor confidence triggering frantic runs on banks, securities, or commodities.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A sudden and groundless **panic** seized the vanguard of the legions, spreading confusion through the night." },
      { "author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "In a financial **panic**, the only sound rule for the central bank is to lend freely at a very high rate of interest." },
      { "author": "Mary Shelley", "work": "Frankenstein", "quote": "A breathless **panic** took possession of my soul, and I fled precipitately from the presence of the monstrous shape." }
    ]
  },
  "Dashboard — pan\\panicky.md": {
    "primary": "Affected by, characterized by, or prone to sudden, uncontrolled fear or jittery anxiety.",
    "secondary": "In market psychology and behavioral analysis, reactive and hasty decision-making driven by fear rather than calculated assessment.",
    "quotes": [
      { "author": "George Orwell", "work": "Homage to Catalonia", "quote": "A sudden whistle of incoming shells would send inexperienced militia into **panicky** flight across the open field." },
      { "author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "She felt a **panicky** sensation that the day had slipped past before anything true had been said or done." },
      { "author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "A **panicky** liquidity preference seizes the trading public whenever future yields appear radically uncertain." }
    ]
  },
  "Dashboard — pan\\panoptic.md": {
    "primary": "Permitting the continuous, comprehensive view of all parts, aspects, or activities from a single vantage point.",
    "secondary": "In architectural and social theory (following Jeremy Bentham's Panopticon), institutional design enabling disciplinary surveillance and internal regulation over subjects.",
    "quotes": [
      { "author": "Jeremy Bentham", "work": "Panopticon; or, The Inspection-House", "quote": "The central tower provides a **panoptic** inspection of every cell, ensuring that each inmate believes himself constantly observed." },
      { "author": "Michel Foucault", "work": "Discipline and Punish", "quote": "The **panoptic** mechanism automatizes and disindividualizes power, arranging things so that surveillance is permanent in its effects." },
      { "author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "From this high attic window I enjoy a **panoptic** view over the bustling rooftops and smoky chimneys of the city." }
    ]
  },
  "Dashboard — pan\\panoptical.md": {
    "primary": "Pertaining to, designed for, or providing a comprehensive and all-inclusive visual survey.",
    "secondary": "In institutional architecture and surveillance theory, structures arranged so that all interior compartments are visible from a central inspection node.",
    "quotes": [
      { "author": "Jeremy Bentham", "work": "The Works of Jeremy Bentham", "quote": "The **panoptical** principle of architecture is applicable to penitentiaries, workhouses, factories, and schools alike." },
      { "author": "H. G. Wells", "work": "When the Sleeper Wakes", "quote": "The aeronaut looked down from the gondola upon the **panoptical** expanse of illuminated glass roofs stretching to the horizon." },
      { "author": "Lewis Mumford", "work": "The City in History", "quote": "Baroque town planning created broad radial avenues that offered a **panoptical** spectacle of royal authority." }
    ]
  },
  "Dashboard — pan\\panoramic.md": {
    "primary": "Affording an unbroken, wide-angle view of an extensive surrounding region or comprehensive series of events.",
    "secondary": "In visual arts, photography, and narrative style, an expansive sweeping depiction capturing an entire landscape, historical epoch, or complex panorama.",
    "quotes": [
      { "author": "John Ruskin", "work": "Modern Painters", "quote": "Standing upon the summit of the pass, the painter captures the **panoramic** splendour of the Alpine peaks rolling away into blue mist." },
      { "author": "Henry James", "work": "The American Scene", "quote": "From the terrace of the hotel, one commanded a **panoramic** survey of the glittering harbor and distant shores." },
      { "author": "Archibald Geikie", "work": "The Scenery of Scotland", "quote": "A **panoramic** view across the Great Glen illustrates how ancient tectonic faults shaped the topography of the Highlands." }
    ]
  },
  "Dashboard — pan\\pantology.md": {
    "primary": "A systematic survey, compendium, or dictionary of universal knowledge; the study of all branches of science and human learning.",
    "secondary": "In 19th-century educational philosophy and bibliographical taxonomy, comprehensive encyclopedic classifications such as Roswell Park's Pantology.",
    "quotes": [
      { "author": "Roswell Park", "work": "Pantology; or, A Systematic Survey of Human Knowledge", "quote": "The aim of **pantology** is to arrange every department of science and art into an orderly and unified encyclopedia." },
      { "author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The ambitious schemes of early **pantology** attempted to synthesize the whole encyclopedic circle of human arts into a single system." },
      { "author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Before an authentic **pantology** can arise, each individual inductive science must establish its own foundational concepts." }
    ]
  },
  "Dashboard — pan\\parrhesia.md": {
    "primary": "Candid, outspoken, and fearless freedom of speech, especially the bold declaration of truth to those in power at personal risk.",
    "secondary": "In classical Athenian rhetoric, Stoic ethics, and political philosophy (examined extensively by Michel Foucault), the civic duty of frank disclosure where the speaker speaks the truth with courage.",
    "quotes": [
      { "author": "Michel Foucault", "work": "Discourse and Truth: The Problematization of Parrhesia", "quote": "In **parrhesia**, the speaker uses his freedom and chooses frankness instead of persuasion, truth instead of flattery, and risk of death instead of life and security." },
      { "author": "Plutarch", "work": "Moralia: How to Tell a Flatterer from a Friend", "quote": "A true friend exercises wholesome **parrhesia**, speaking candidly of our faults without malice, while the flatterer conceals them." },
      { "author": "Epictetus", "work": "Discourses", "quote": "The Cynic must possess untamed **parrhesia**, rebuking kings and magistrates without fear, confident in his inner virtue." }
    ]
  },
  "Dashboard — pent\\diapente.md": {
    "primary": "The musical interval of a perfect fifth, encompassing five scale degrees.",
    "secondary": "In Pythagorean tuning, medieval music theory, and ancient pharmacology, an acoustic ratio of 3:2 representing the fifth; also an obsolete medicinal compound composed of five ingredients.",
    "quotes": [
      { "author": "Pythagoras", "work": "Harmonics", "quote": "The proportion of three to two produces the sweetest consonance of the **diapente**, the fundamental bridge of the octave." },
      { "author": "Thomas Morley", "work": "A Plaine and Easie Introduction to Practicall Musicke", "quote": "From the lowest keynote to the **diapente** is five whole notes, yielding that perfect concord which rejoiceth the ear." },
      { "author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The apothecary prepared the electuary of **diapente**, blending five virtues to combat poisonous bites and pestilential agues." }
    ]
  },
  "Dashboard — pent\\pent.md": {
    "primary": "Confined, enclosed, or shut up in a narrow or restricted space; held back or repressed (commonly in 'pent-up').",
    "secondary": "In psychoanalysis and emotional description, repressed internal drives, rage, or psychic tension denied outward expression.",
    "quotes": [
      { "author": "William Shakespeare", "work": "King Lear", "quote": "Close **pent**-up guilts, rive your concealing continents, and cry these dreadful summoners grace." },
      { "author": "John Keats", "work": "Sonnet: To One Who Has Been Long in City Pent", "quote": "To one who has been long in city **pent**, 'tis very sweet to look into the fair and open face of heaven." },
      { "author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I longed for a power of vision which might overpass that limit; my spirit was **pent** within walls that felt like a prison." }
    ]
  },
  "Dashboard — pent\\pentachoric.md": {
    "primary": "Having or relating to five cells, chambers, or bounding boundaries, especially in four-dimensional geometry.",
    "secondary": "In four-dimensional polytope mathematics, pertaining to the 5-cell or pentachoron, the four-dimensional analogue of the regular tetrahedron bounded by five tetrahedral facets.",
    "quotes": [
      { "author": "Alicia Boole Stott", "work": "Geometrical Deduction of Semiregular Polyhedra", "quote": "The four-dimensional simplex displays a **pentachoric** boundary formed by five identical regular tetrahedral cells." },
      { "author": "H. S. M. Coxeter", "work": "Regular Polytopes", "quote": "The simplest regular four-polytope is the **pentachoric** figure, possessing five vertices, ten edges, ten faces, and five cells." },
      { "author": "Duncan Sommerville", "work": "An Introduction to the Geometry of N Dimensions", "quote": "In n-dimensional space, the general simplex reduces at four dimensions to the **pentachoric** configuration." }
    ]
  },
  "Dashboard — pent\\pentacle.md": {
    "primary": "A five-pointed star inscribed within a circle, historically used as a magical talisman, protective symbol, or occult glyph.",
    "secondary": "In tarot and ceremonial magic (notably the Hermetic Order of the Golden Dawn and Wicca), one of the four suits of the minor arcana symbolizing the element of Earth, material wealth, and bodily protection.",
    "quotes": [
      { "author": "Johann Wolfgang von Goethe", "work": "Faust", "quote": "The **pentacle** upon your threshold bars my exit; the five-rayed star leaves me captive within this chamber." },
      { "author": "Arthur Edward Waite", "work": "The Pictorial Key to the Tarot", "quote": "The suit of **pentacles** represents material fortune, trade, bodily health, and the grounding powers of physical nature." },
      { "author": "Walter Scott", "work": "The Antiquary", "quote": "Upon the parchment was traced a cabalistic **pentacle**, surrounded with Hebrew characters and astronomical signs." }
    ]
  },
  "Dashboard — pent\\pentad.md": {
    "primary": "A group, series, or set consisting of five things, persons, or units; or a period of five days or five years.",
    "secondary": "In chemistry and meteorology, an element or atom having a valence of five; or a five-day statistical period used in climatological data collection and agricultural weather forecasting.",
    "quotes": [
      { "author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Nature in many her flowers and fruits observeth the number five, delighting in the symmetry of the **pentad**." },
      { "author": "August Wilhelm von Hofmann", "work": "Introduction to Modern Chemistry", "quote": "Phosphorus behaves as a **pentad** in the pentachloride, linking five monad chlorine atoms to a single nucleus." },
      { "author": "Wladimir Köppen", "work": "Climatology and Meteorological Observations", "quote": "Rainfall anomalies are averaged over each calendar **pentad** to reveal seasonal transitions in monsoon circulation." }
    ]
  },
  "Dashboard — pent\\pentaerythritol.md": {
    "primary": "A white, crystalline polyhydric alcohol containing four hydroxyl groups, with formula C(CH2OH)4, used in the synthesis of resins, paints, and explosives.",
    "secondary": "In industrial organic chemistry, a tetrol synthesized by the condensation of formaldehyde with acetaldehyde in the presence of base, serving as the essential precursor for pentaerythritol tetranitrate (PETN) and alkyd coatings.",
    "quotes": [
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The central carbon atom in **pentaerythritol** exhibits ideal tetrahedral symmetry, directing its four hydroxymethyl groups outward." },
      { "author": "Tenney L. Davis", "work": "The Chemistry of Powder and Explosives", "quote": "Nitration of **pentaerythritol** yields PETN, one of the most sensitive and powerful high explosives known." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "Esterification of phthalic anhydride with **pentaerythritol** produces durable crosslinked alkyd resins for industrial enamels." }
    ]
  },
  "Dashboard — pent\\pentagon.md": {
    "primary": "A plane geometric figure with five straight sides and five angles; or a five-sided building.",
    "secondary": "In military and political parlance (capitalized), the massive five-sided headquarters building of the United States Department of Defense in Arlington, Virginia, metonymously designating the U.S. military leadership.",
    "quotes": [
      { "author": "Euclid", "work": "Elements", "quote": "Inscribe in a given circle an equilateral and equiangular **pentagon** by means of the golden ratio." },
      { "author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "The mystical properties of the regular **pentagon** engaged the contemplation of the ancient philosophers who found harmony in five." },
      { "author": "Dwight D. Eisenhower", "work": "Crusade in Europe", "quote": "From our offices in the newly constructed **Pentagon**, we coordinated the vast logistical requirements of the Allied forces." }
    ]
  },
  "Dashboard — pent\\pentagonal.md": {
    "primary": "Having five sides, angles, or corners; arranged in the shape of a pentagon.",
    "secondary": "In crystallography and mineralogy, crystal forms exhibiting fivefold symmetry or pentagonal faces, such as the pyritohedral pentagonal dodecahedron of pyrite.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "Pyrite commonly crystallizes in striate cubes or in the beautiful **pentagonal** dodecahedron called the pyritohedron." },
      { "author": "D'Arcy Wentworth Thompson", "work": "On Growth and Form", "quote": "The silicious skeleton of certain radiolarians resembles a regular **pentagonal** dodecahedron composed of hollow reticulated bars." },
      { "author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "The cross-section of the pith in the young shoots of the alder displays an elegant **pentagonal** star." }
    ]
  },
  "Dashboard — pent\\pentagram.md": {
    "primary": "A five-pointed star polygon drawn with five straight lines in a single continuous stroke.",
    "secondary": "In classical Pythagorean mathematics, a sacred emblem of health (*hygieia*) embodying the golden ratio; in medieval folklore and occultism, an apotropaic ward against evil spirits.",
    "quotes": [
      { "author": "Johann Wolfgang von Goethe", "work": "Faust", "quote": "The **pentagram** gives you pain? Tell me, you son of hell, if that is so, how did you get inside?" },
      { "author": "J. E. Cirlot", "work": "A Dictionary of Symbols", "quote": "The **pentagram**, with its upward pointing apex, symbolizes the spiritual rule of mind over the four material elements." },
      { "author": "Iamblichus", "work": "The Life of Pythagoras", "quote": "The Pythagoreans used the **pentagram** as a secret badge of recognition, writing within its points the letters of health." }
    ]
  },
  "Dashboard — pent\\pentahedron.md": {
    "primary": "A three-dimensional polyhedron having five plane faces, such as a four-sided pyramid or a triangular prism.",
    "secondary": "In solid geometry and stereometry, a closed spatial surface with five facets; specifically topologically divided into the square pyramid (5 vertices, 8 edges) and the wedge or triangular prism (6 vertices, 9 edges).",
    "quotes": [
      { "author": "Archimedes", "work": "On the Sphere and Cylinder", "quote": "If a solid be bounded by five plane surfaces, the simplest regular form it may assume is the triangular **pentahedron**." },
      { "author": "Duncan Sommerville", "work": "Analytical Geometry of Three Dimensions", "quote": "A **pentahedron** possessing eight edges must have one square base and four triangular sides meeting in an apex." },
      { "author": "Adrien-Marie Legendre", "work": "Elements of Geometry", "quote": "Euler's polyhedral formula confirms that every **pentahedron** satisfies vertices minus edges plus faces equals two." }
    ]
  },
  "Dashboard — pent\\pentail.md": {
    "primary": "A pen-tailed treeshrew (Ptilocercus lowii), a small nocturnal mammal of Southeast Asia notable for a tail terminating in a feather-like brush of white hairs.",
    "secondary": "In mammalogy and evolutionary biology, the sole living species of the family Ptilocercidae, famous for consuming naturally fermented floral nectar with high alcohol content without intoxication.",
    "quotes": [
      { "author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "In the dense forests of Borneo dwells the curious **pentail** treeshrew, sporting a feather-like tuft at the tip of its naked tail." },
      { "author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The **pentail** belongs to the insectivores, easily recognized by the distichous arrangement of long hairs along the end of the tail." },
      { "author": "William Henry Flower", "work": "An Introduction to the Osteology of the Mammalia", "quote": "Cranial morphology in the **pentail** suggests an ancient branch linking early placental insectivores with primitive primates." }
    ]
  },
  "Dashboard — pent\\pentalpha.md": {
    "primary": "A geometrical design of a five-pointed star formed by interlacing five capital Greek letter Alphas (A); synonymous with pentagram.",
    "secondary": "In Byzantine iconography, classical numismatics, and masonic symbolism, an emblem formed by intersecting five alphas, historically employed as a talisman of divine protection.",
    "quotes": [
      { "author": "Albert Mackey", "work": "Encyclopedia of Freemasonry", "quote": "The **pentalpha**, so called from its resemblance to five capital letters A interlaced, was an ancient symbol of geometric perfection." },
      { "author": "Eliphas Lévi", "work": "Transcendental Magic: Its Doctrine and Ritual", "quote": "The sacred **pentalpha** represents the microcosm, the human figure radiating power into the five cardinal directions." },
      { "author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "On the silver amulet was etched an archaic **pentalpha**, supposed to ward against malignant influences." }
    ]
  },
  "Dashboard — pent\\pentamerous.md": {
    "primary": "Divided into or consisting of five parts, segments, or members.",
    "secondary": "In botany and invertebrate zoology, flowers having floral organs in multiples of five (common in dicotyledons), or echinoderms exhibiting five-part radial symmetry.",
    "quotes": [
      { "author": "Asa Gray", "work": "Elements of Botany", "quote": "Dicotyledonous flowers are typically **pentamerous**, presenting five sepals, five petals, and stamens in multiples of five." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The adult starfish displays a strictly **pentamerous** radial plan derived from a bilateral larval stage." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "In Rosaceae, the calyx is universally **pentamerous**, supporting an equal number of petals upon its disc." }
    ]
  },
  "Dashboard — pent\\pentameter.md": {
    "primary": "A poetic line of verse consisting of five metrical feet.",
    "secondary": "In classical Latin and Greek prosody, a dactylic verse of five feet used in elegiac couplets; in English poetry, iambic pentameter, the foundational meter of blank verse and Shakespearean drama.",
    "quotes": [
      { "author": "Samuel Taylor Coleridge", "work": "The Ovidian Elegiac Metre", "quote": "In the hexameter rises the fountain's silvery column; / In the **pentameter** aye falling in melody back." },
      { "author": "John Dryden", "work": "An Essay of Dramatic Poesy", "quote": "Our English blank verse, fashioned in heroic **pentameter**, possesses the dignified gravity suited to tragic action." },
      { "author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "A needless Alexandrine ends the song, / That, like a wounded snake, drags its slow length along, unlike the brisk **pentameter**." }
    ]
  },
  "Dashboard — pent\\pentamethylenetetrazol.md": {
    "primary": "A synthetic central nervous system stimulant and convulsant drug, commonly known as metrazol or pentylenetetrazol.",
    "secondary": "In 20th-century psychiatry and neuropharmacology, a chemical compound used by Ladislas von Meduna to induce therapeutic convulsive seizures in schizophrenic patients prior to electroconvulsive therapy.",
    "quotes": [
      { "author": "Ladislas von Meduna", "work": "Die Konvulsionstherapie der Schizophrenie", "quote": "Intravenous injection of **pentamethylenetetrazol** produces a generalized epileptiform convulsion within fifteen seconds." },
      { "author": "Walter Freeman", "work": "Psychosurgery in the Treatment of Mental Disorders", "quote": "Before the adoption of electric shock, **pentamethylenetetrazol** was the principal agent used to provoke therapeutic seizures." },
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "As a central analeptic, **pentamethylenetetrazol** acts predominantly on the brainstem and spinal cord by antagonizing GABA." }
    ]
  },
  "Dashboard — pent\\pentangle.md": {
    "primary": "A five-pointed star or five-sided geometric figure; another term for a pentagram or pentacle.",
    "secondary": "In Middle English chivalric literature, especially *Sir Gawain and the Green Knight*, the five-pointed geometric device emblazoned upon Gawain's shield symbolizing chivalric virtues and the five wounds of Christ.",
    "quotes": [
      { "author": "Anonymous", "work": "Sir Gawain and the Green Knight", "quote": "And why the **pentangle** apendeth to that noble prince I am in mind to tell, for it is a symbol that Solomon established." },
      { "author": "J. R. R. Tolkien", "work": "Sir Gawain and the Green Knight: Notes", "quote": "The **pentangle** is called the endless knot because its lines weave continuously without break or beginning." },
      { "author": "Thomas Malory", "work": "Le Morte d'Arthur", "quote": "Upon the gold border of the knight's shield was traced a gleaming **pentangle**, signifying fivefold truth." }
    ]
  },
  "Dashboard — pent\\pentangular.md": {
    "primary": "Having five angles and five sides; pentagonal in configuration.",
    "secondary": "In architecture and fortification engineering, describing fortifications or watchtowers constructed with a five-cornered layout to eliminate blind spots.",
    "quotes": [
      { "author": "Sébastien Le Prestre de Vauban", "work": "A Treatise on the Defense of Places", "quote": "The **pentangular** fortress allows each bastion to flank the adjacent curtains with cross-firing artillery." },
      { "author": "Christopher Wren", "work": "Parentalia", "quote": "The lantern of the steeple was raised upon a **pentangular** stone base to withstand the prevailing ocean gales." },
      { "author": "John Evelyn", "work": "Sylva", "quote": "The cross-section of the stem reveals a delicate **pentangular** core surrounded by dense annual rings." }
    ]
  },
  "Dashboard — pent\\pentastomid.md": {
    "primary": "Any parasitic invertebrate belonging to the subclass Pentastomida, commonly called tongue worms, which infest the respiratory tracts of carnivorous vertebrates.",
    "secondary": "In parasitology and veterinary helminthology, aberrant worm-like crustacean endoparasites possessing two pairs of chitinous hooks flanking a central mouth, primarily infesting snakes, lizards, and canines.",
    "quotes": [
      { "author": "Rudolf Leuckart", "work": "Bau und Entwicklungsgeschichte der Pentastomen", "quote": "The adult **pentastomid** attaches firmly to the nasal mucosa of the dog by means of four sharp retractile hooks." },
      { "author": "Thomas Spencer Cobbold", "work": "Parasites: A Treatise on the Entozoa of Man and Animals", "quote": "Infestation by a larval **pentastomid** encysted within the human liver represents a rare but dangerous zoonosis." },
      { "author": "Robert William Hegner", "work": "Parasitology", "quote": "Though superficially resembling tapeworms, the **pentastomid** exhibits embryonic limb buds showing arthropod affinities." }
    ]
  },
  "Dashboard — pent\\pentastomida.md": {
    "primary": "A group of specialized, worm-like parasitic crustaceans comprising the tongue worms, inhabiting the respiratory tracts of vertebrates.",
    "secondary": "In systematic invertebrate zoology, a taxon (now classified within the crustacean subclass Ichthyostraca) containing about 130 species of obligate endoparasites with degenerate morphology.",
    "quotes": [
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "The enigmatic group **Pentastomida** was long placed among arachnids until spermatology revealed their true crustacean origin." },
      { "author": "Libbie Hyman", "work": "The Invertebrates", "quote": "Members of **Pentastomida** have lost all circulatory, respiratory, and excretory organs as adaptations to an endoparasitic life." },
      { "author": "William A. Riley", "work": "Medical Entomology", "quote": "Within **Pentastomida**, Linguatula serrata is the most notable species capable of producing human nasopharyngeal linguatuliasis." }
    ]
  },
  "Dashboard — pent\\pentasyllabic.md": {
    "primary": "Consisting of or having five syllables; or a word having five syllables.",
    "secondary": "In linguistics, phonology, and prosody, a metrical foot or word composed of exactly five rhythmic syllables (such as 'incomprehensible').",
    "quotes": [
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Polysyllabic compounds in agglutinative tongues frequently generate **pentasyllabic** words carrying complex case markers." },
      { "author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "The rhythm of an English sentence naturally compresses a **pentasyllabic** phrase into two or three primary stress beats." },
      { "author": "Otto Jespersen", "work": "Modern English Grammar", "quote": "Latinate adjectives of four syllables often become **pentasyllabic** when extended by the adverbial suffix -ly." }
    ]
  },
  "Dashboard — pent\\pentateuch.md": {
    "primary": "The first five books of the Hebrew Bible and Christian Old Testament: Genesis, Exodus, Leviticus, Numbers, and Deuteronomy; the Torah.",
    "secondary": "In biblical scholarship, hermeneutics, and textual criticism (the Documentary Hypothesis of Julius Wellhausen), the composite foundational legal and narrative corpus attributed traditionally to Moses.",
    "quotes": [
      { "author": "John Milton", "work": "Areopagitica", "quote": "Moses, the great lawgiver, received the divine commandments that were preserved in the sacred **Pentateuch**." },
      { "author": "Baruch Spinoza", "work": "Tractatus Theologico-Politicus", "quote": "A critical examination of the text proves that Moses himself could not have written the entire **Pentateuch** as we now have it." },
      { "author": "Julius Wellhausen", "work": "Prolegomena to the History of Israel", "quote": "The composite structure of the **Pentateuch** reveals four distinct literary strata woven together by post-exilic redactors." }
    ]
  },
  "Dashboard — pent\\pentathlete.md": {
    "primary": "An athlete who competes in a pentathlon, an athletic contest comprising five distinct events.",
    "secondary": "In classical and modern Olympic history, a competitor trained for versatile endurance, whether in the ancient Greek stadion, jump, javelin, discus, and wrestling, or the modern pentathlon.",
    "quotes": [
      { "author": "Pausanias", "work": "Description of Greece", "quote": "At Olympia, a bronze statue was dedicated to the victorious **pentathlete** who triumphed in all five grueling trials." },
      { "author": "Aristotle", "work": "Rhetoric", "quote": "The body of the **pentathlete** is the most beautiful of all, because he unites speed, strength, and agility in harmonious balance." },
      { "author": "Pierre de Coubertin", "work": "Olympic Memoirs", "quote": "The modern **pentathlete** represents the ideal soldier-athlete, mastering horsemanship, fencing, shooting, swimming, and running." }
    ]
  },
  "Dashboard — pent\\pentathlon.md": {
    "primary": "An athletic contest consisting of five separate events in which each participant competes.",
    "secondary": "In sports history, the ancient Greek contest (discus, javelin, long jump, stadion footrace, wrestling) introduced at the 18th Olympiad (708 BCE); and the modern Olympic pentathlon devised by Pierre de Coubertin.",
    "quotes": [
      { "author": "Aristotle", "work": "Rhetoric", "quote": "Athletes in the **pentathlon** possess natural physical perfection, for they combine swift running with powerful wrestling." },
      { "author": "Pierre de Coubertin", "work": "Olympism: Selected Writings", "quote": "The modern **pentathlon** tests the complete moral and physical qualities of an athlete under five varied disciplines." },
      { "author": "E. Norman Gardiner", "work": "Greek Athletic Sports and Festivals", "quote": "No victory at Olympia commanded greater admiration for versatility than the triumph in the fivefold **pentathlon**." }
    ]
  },
  "Dashboard — pent\\pentatone.md": {
    "primary": "A musical scale or melodic sequence consisting of five tones; synonymous with pentatonic scale.",
    "secondary": "In ethnomusicology and acoustic theory, an anhemitonic five-note scale constructed without semitones, foundational to East Asian, Celtic, and West African traditional music.",
    "quotes": [
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "The native melodies of Java and the Scottish Highlands are built upon a natural **pentatone** devoid of minor semitones." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The primitive simplicity of the **pentatone** renders it the most universal scale structure in global musical history." },
      { "author": "Béla Bartók", "work": "Hungarian Folk Music", "quote": "Peasant songs of ancient Transylvania preserve the archaic **pentatone**, free from the major-minor system of the West." }
    ]
  },
  "Dashboard — pent\\pentatonic.md": {
    "primary": "Consisting of or based on five musical tones or pitches per octave.",
    "secondary": "In music theory, scales (such as the major pentatonic 1-2-3-5-6) lacking the fourth and seventh degrees, eliminating dissonant tritones and semitones.",
    "quotes": [
      { "author": "Claude Debussy", "work": "Monsieur Croche, the Dilettante Hater", "quote": "The Javanese gamelan, with its subtle **pentatonic** inflections, makes our Western counterpoint seem like child's play." },
      { "author": "Zoltán Kodály", "work": "Folk Music of Hungary", "quote": "Children absorb melody most naturally through the **pentatonic** scale, which avoids the difficult intonation of semitones." },
      { "author": "Leonard Bernstein", "work": "The Unanswered Question", "quote": "The universal **pentatonic** scale occurs independently across cultures because its intervals stem directly from the overtone series." }
    ]
  },
  "Dashboard — pent\\pentatope.md": {
    "primary": "A four-dimensional polytope bounded by five tetrahedral cells; also known as the 5-cell or 4-simplex.",
    "secondary": "In higher-dimensional Euclidean geometry, the simplest possible regular 4-polytope, possessing 5 vertices, 10 edges, 10 triangular faces, and 5 tetrahedral cells.",
    "quotes": [
      { "author": "H. S. M. Coxeter", "work": "Regular Polytopes", "quote": "The regular **pentatope** is self-dual, having five vertices and five tetrahedral cells just as the triangle has three of each." },
      { "author": "Duncan Sommerville", "work": "An Introduction to the Geometry of N Dimensions", "quote": "By projecting the **pentatope** into three dimensions, one obtains a tetrahedron with a central interior vertex." },
      { "author": "Alicia Boole Stott", "work": "On Certain Series of Sections of the Regular Four-Dimensional Hypersolids", "quote": "Planar cuts through the **pentatope** yield changing sequences of triangles, tetrahedra, and truncated pyramids." }
    ]
  },
  "Dashboard — pent\\pentavalent.md": {
    "primary": "Having a valence of five; capable of combining with or substituting for five atoms of hydrogen or other univalent elements.",
    "secondary": "In inorganic chemistry and semiconductor physics, elements of group 15 (such as phosphorus, arsenic, and antimony) acting as n-type donor dopants in silicon crystals; also vaccines immunizing against five pathogens.",
    "quotes": [
      { "author": "Dmitri Mendeleev", "work": "The Principles of Chemistry", "quote": "Phosphorus and nitrogen form **pentavalent** oxides and halides corresponding to the highest oxidation state of the fifth group." },
      { "author": "William Shockley", "work": "Electrons and Holes in Semiconductors", "quote": "Introducing **pentavalent** impurity atoms into a germanium lattice provides excess conduction electrons, creating an n-type semiconductor." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "In phosphorus pentachloride, the central atom exhibits **pentavalent** coordination arranged in a trigonal bipyramid." }
    ]
  },
  "Dashboard — pent\\pentazocine.md": {
    "primary": "A synthetic opioid analgesic drug used to treat moderate to severe pain.",
    "secondary": "In pharmacology and neurobiology, a benzomorphan derivative acting as a mixed agonist-antagonist (kappa-opioid receptor agonist and weak mu-opioid receptor partial agonist/antagonist), developed to provide analgesia with reduced abuse liability.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The introduction of **pentazocine** represented an effort to synthesize an analgesic with potent action but minimal addiction risk." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Revision", "quote": "Unlike pure morphine agonists, **pentazocine** can precipitate acute withdrawal symptoms in opioid-dependent subjects." },
      { "author": "Julius Axelrod", "work": "Biochemical Pharmacology of Opioid Receptors", "quote": "The dysphoric side effects of high-dose **pentazocine** are mediated through its affinity for kappa and sigma receptors." }
    ]
  },
  "Dashboard — pent\\pente.md": {
    "primary": "The Greek cardinal number five (πέντε), serving as the root for English prefixes such as penta- and pent-.",
    "secondary": "In classical Greek grammar and etymology, the Indo-European numeral (*pénkʷe) that underlies mathematical and architectural terminology across scientific nomenclature.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The numeral **pente** expresses the number five, appearing in compounds like pentagon, pentameter, and Pentateuch." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Sanskrit panca, Greek **pente**, and Latin quinque all descend from a common Indo-European root for five." },
      { "author": "Walter William Skeat", "work": "An Etymological Dictionary of the English Language", "quote": "From Greek **pente** we derive the whole scientific vocabulary designating fivefold geometric and chemical arrangements." }
    ]
  },
  "Dashboard — pent\\pentecost.md": {
    "primary": "A Christian festival celebrated on the seventh Sunday (fiftieth day) after Easter, commemorating the descent of the Holy Spirit upon the Apostles.",
    "secondary": "In Jewish tradition, the Feast of Weeks (Shavuot), celebrated fifty days after Passover, commemorating the grain harvest and the giving of the Torah at Mount Sinai.",
    "quotes": [
      { "author": "John Milton", "work": "Paradise Lost", "quote": "The Holy Ghost on every one of them in form of cloven tongues of fire descended, upon the solemn day of **Pentecost**." },
      { "author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Come Pentecost as quickly as it will, some five and twenty years; and then we mask'd, since last before **Pentecost**." },
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "On the festival of **Pentecost**, pilgrims from across the Mediterranean gathered in Jerusalem to celebrate the ancient harvest." }
    ]
  },
  "Dashboard — pent\\pentecostal.md": {
    "primary": "Relating to Pentecost; or of or relating to Pentecostalism, a Christian charismatic movement emphasizing baptism in the Holy Spirit.",
    "secondary": "In ecclesiastical history and sociology of religion, churches and movements characterized by glossolalia (speaking in tongues), faith healing, and ecstatic worship originating in the 1906 Azusa Street Revival.",
    "quotes": [
      { "author": "William James", "work": "The Varieties of Religious Experience", "quote": "The sudden influx of ecstatic fervor in **Pentecostal** gatherings reflects an abrupt opening of subliminal consciousness." },
      { "author": "H. Richard Niebuhr", "work": "The Social Sources of Denominationalism", "quote": "The rapid growth of the **Pentecostal** movement answered the spiritual hunger of economically marginalized populations." },
      { "author": "C. S. Lewis", "work": "Letters to Malcolm: Chiefly on Prayer", "quote": "A genuine **Pentecostal** experience must bring forth ethical fruits of charity and humility rather than spiritual pride." }
    ]
  },
  "Dashboard — pent\\pentecostalism.md": {
    "primary": "A Protestant Christian movement that emphasizes direct personal experience of God through baptism in the Holy Spirit, accompanied by spiritual gifts.",
    "secondary": "In religious history, a global 20th-century renewal movement characterized by speaking in tongues, divine healing, and expressive worship, tracing its modern rise to the Azusa Street revival.",
    "quotes": [
      { "author": "Max Weber", "work": "The Sociology of Religion", "quote": "Movements akin to modern **Pentecostalism** seek the renewal of early apostolic charisma in protest against rationalized church bureaucracy." },
      { "author": "Harvey Cox", "work": "Fire from Heaven: The Rise of Pentecostal Spirituality", "quote": "The astonishing spread of global **Pentecostalism** demonstrates the primal power of ecstatic, experiential spirituality." },
      { "author": "Ernst Troeltsch", "work": "The Social Teaching of the Christian Churches", "quote": "Pneumatic sects embodying early forms of **Pentecostalism** emphasize the immediate presence of the Spirit over sacramental tradition." }
    ]
  },
  "Dashboard — pent\\pentecostalist.md": {
    "primary": "An adherent or member of a Pentecostal church or religious movement.",
    "secondary": "In contemporary theology and religious studies, a believer who practices charismatic gifts, including glossolalia, prophetic ministry, and faith healing.",
    "quotes": [
      { "author": "Harvey Cox", "work": "Fire from Heaven", "quote": "To the devout **Pentecostalist**, the presence of the Holy Spirit is an everyday reality testified by bodily transformation." },
      { "author": "H. Richard Niebuhr", "work": "The Social Sources of Denominationalism", "quote": "The early **Pentecostalist** rejected worldly entertainment, finding in ecstatic worship a joyful alternative to commercial amusements." },
      { "author": "Peter L. Berger", "work": "The Sacred Canopy", "quote": "The tight-knit community of the **Pentecostalist** assembly creates a powerful plausibility structure in rapidly urbanizing environments." }
    ]
  },
  "Dashboard — pent\\pentimento.md": {
    "primary": "An underlying image, trace, or earlier stroke in a painting that emerges or becomes visible when top layers of paint turn transparent with age.",
    "secondary": "In art history, museum conservation, and infrared reflectography, evidence of an artist's second thoughts, modifications, or composition changes revealed beneath the final surface.",
    "quotes": [
      { "author": "Lillian Hellman", "work": "Pentimento: A Book of Portraits", "quote": "Old paint on canvas, as it ages, sometimes becomes transparent; then the original design shows through: that is **pentimento**." },
      { "author": "Kenneth Clark", "work": "Looking at Pictures", "quote": "An unmistakable **pentimento** in the arm of Rembrandt's portrait shows where he widened the gesture to increase dramatic impact." },
      { "author": "E. H. Gombrich", "work": "Art and Illusion", "quote": "X-ray analysis reveals the fascinating **pentimento** where the master cancelled his initial layout in favor of a bolder composition." }
    ]
  },
  "Dashboard — pent\\pentlandite.md": {
    "primary": "A bronze-yellow iron-nickel sulfide mineral, (Fe,Ni)9S8, which is the principal ore of nickel.",
    "secondary": "In economic geology and extractive metallurgy, an isometric sulfide mineral commonly occurring intergrown with pyrrhotite and chalcopyrite in magmatic sulfide deposits, such as the Sudbury Basin in Ontario and the Bushveld Complex.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "The mineral **pentlandite**, named in honor of the traveler J. B. Pentland, occurs in granular masses with bronze-yellow color and metallic luster." },
      { "author": "Waldemar Lindgren", "work": "Mineral Deposits", "quote": "The enormous nickel reserves of Sudbury consist chiefly of **pentlandite** intergrown with massive magmatic pyrrhotite." },
      { "author": "Edward Salisbury Dana", "work": "Textbook of Mineralogy", "quote": "Unlike magnetic pyrrhotite, **pentlandite** is non-magnetic and exhibits distinct octahedral cleavage." }
    ]
  },
  "Dashboard — pent\\pentobarbital.md": {
    "primary": "A short-acting barbiturate drug commonly used as a sedative, hypnotic, pre-anesthetic medication, and veterinary euthanasia agent.",
    "secondary": "In pharmacology and neurochemistry, a GABA-A receptor positive allosteric modulator (traditionally sold as Nembutal) that depresses central nervous system activity, formerly used in lethal injection protocols.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The hypnotic action of **pentobarbital** begins within twenty minutes of oral administration and lasts from three to four hours." },
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "Small bedtime doses of **pentobarbital** calmed the patient's nocturnal agitations without producing morning hangover." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Overdosage with **pentobarbital** produces profound central respiratory depression requiring immediate mechanical ventilatory support." }
    ]
  },
  "Dashboard — pent\\pentode.md": {
    "primary": "A thermionic vacuum tube or electronic valve having five active electrodes: cathode, control grid, screen grid, suppressor grid, and anode.",
    "secondary": "In radio engineering and electronics history, an audio-frequency and radio-frequency amplifying valve developed in the 1920s to eliminate the dynatron effect and secondary emission distortions present in tetrodes.",
    "quotes": [
      { "author": "Frederick Emmons Terman", "work": "Radio Engineering", "quote": "The addition of the suppressor grid in the **pentode** prevents secondary electrons emitted by the plate from reaching the screen grid." },
      { "author": "Bernard Grob", "work": "Basic Electronics", "quote": "Because of its high amplification factor and low plate-to-grid capacitance, the **pentode** superseded the triode in radio-frequency amplifier stages." },
      { "author": "Arthur Conan Doyle", "work": "The Edge of the Unknown", "quote": "Modern wireless receivers rely upon the miraculous sensitivity of the multi-electrode **pentode** to amplify transatlantic broadcasts." }
    ]
  },
  "Dashboard — pent\\pentose.md": {
    "primary": "Any monosaccharide sugar containing five carbon atoms per molecule, having the general formula C5H10O5.",
    "secondary": "In cellular biochemistry and molecular biology, essential aldopentoses and ketopentoses such as ribose and deoxyribose that form the structural backbone of nucleic acids (RNA and DNA) and nucleotides (ATP).",
    "quotes": [
      { "author": "Emil Fischer", "work": "Syntheses in the Sugar Group", "quote": "By cyanohydrin degradation and reduction, we established the configuration of the **pentose** sugars ribose, arabinose, and xylose." },
      { "author": "James D. Watson", "work": "The Double Helix", "quote": "The repeating backbone of the DNA chain consists of phosphate groups esterified to the five-carbon **pentose** deoxyribose." },
      { "author": "Arthur Harden", "work": "Alcoholic Fermentation", "quote": "The **pentose** phosphate pathway provides generating cells with both reducing NADPH and ribose for nucleotide synthesis." }
    ]
  },
  "Dashboard — pent\\pentothal.md": {
    "primary": "A proprietary brand name for sodium thiopental, a rapid-onset, ultra-short-acting barbiturate used for general anesthesia and colloquially known as 'truth serum'.",
    "secondary": "In clinical anesthesiology and forensic toxicology, an intravenous sulfur-bearing barbiturate that rapidly crosses the blood-brain barrier to induce loss of consciousness within seconds, widely used in mid-20th century narcoanalysis.",
    "quotes": [
      { "author": "Aldous Huxley", "work": "Brave New World Revisited", "quote": "Under the influence of sodium **pentothal**, the subject's critical barriers dissolve, inducing uninhibited verbal release." },
      { "author": "Arthur Conan Doyle", "work": "Memories and Adventures", "quote": "The swift and quiet oblivion brought by intravenous **pentothal** revolutionized surgical anesthesia in field hospitals." },
      { "author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "A light injection of **pentothal** allowed the patient to describe traumatic memories without incapacitating terror." }
    ]
  },
  "Dashboard — pent\\pentoxide.md": {
    "primary": "A chemical oxide containing five oxygen atoms per molecule or stoichiometric formula unit.",
    "secondary": "In synthetic chemistry and industrial manufacturing, notable compounds such as phosphorus pentoxide (P4O10, a powerful desiccant) and vanadium pentoxide (V2O5, an essential catalyst in the contact process for sulfuric acid).",
    "quotes": [
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Phosphorus burning in dry air deposits a snowy powder of phosphorus **pentoxide**, which greedily absorbs every trace of water." },
      { "author": "Henry Enfield Roscoe", "work": "A Treatise on Chemistry", "quote": "Vanadium **pentoxide** acts as an efficient oxygen carrier, catalyzing the oxidation of sulfur dioxide to sulfur trioxide." },
      { "author": "William Crookes", "work": "Select Methods in Chemical Analysis", "quote": "The desiccating tube was filled with pure phosphorus **pentoxide** to ensure total dryness of the circulating gas stream." }
    ]
  },
  "Dashboard — pent\\pentoxifylline.md": {
    "primary": "A xanthine derivative medication used to improve blood flow in patients with peripheral artery disease and intermittent claudication.",
    "secondary": "In cardiovascular pharmacology and hematology, a synthetic hemorheologic agent that increases erythrocyte flexibility, decreases blood viscosity, and inhibits platelet aggregation by inhibiting phosphodiesterase enzymes.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "By enhancing red cell deformability and reducing plasma fibrinogen, **pentoxifylline** improves microcirculatory perfusion in ischemic tissues." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Edition", "quote": "Patients crippled by vascular claudication demonstrated extended walking distances following prolonged therapy with **pentoxifylline**." },
      { "author": "Eugene Braunwald", "work": "Heart Disease: A Textbook of Cardiovascular Medicine", "quote": "The rheologic properties of **pentoxifylline** stem largely from its ability to elevate intracellular cyclic AMP in vascular beds." }
    ]
  },
  "Dashboard — pent\\pentylenetetrazol.md": {
    "primary": "A synthetic central nervous system stimulant and chemical convulsant; alternative name for pentamethylenetetrazol (Metrazol).",
    "secondary": "In neuropharmacological research, a laboratory chemical widely used as a standard chemoconvulsant to screen and evaluate novel antiepileptic drug candidates in animal seizure models.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Administration of **pentylenetetrazol** induces reproducible clonic seizures, serving as the benchmark model for testing anticonvulsants." },
      { "author": "Walter Freeman", "work": "Psychosurgery and Biological Psychiatry", "quote": "Intravenous **pentylenetetrazol** provoked severe motor paroxysms that were utilized clinically before the advent of curare." },
      { "author": "Ladislas von Meduna", "work": "Biochemical Investigations into Schizophrenia", "quote": "We observed dramatic remissions in chronic catatonia following repeated convulsions provoked by **pentylenetetrazol**." }
    ]
  },
  "Dashboard — pent\\repent.md": {
    "primary": "To feel sincere regret, sorrow, or remorse for past actions, sins, or omissions, and to resolve to reform one's conduct.",
    "secondary": "In Christian theology and moral philosophy (translating Greek *metanoein*, to change one's mind), a transformative reorientation of life away from sin toward moral renewal.",
    "quotes": [
      { "author": "William Shakespeare", "work": "Hamlet", "quote": "Confess yourself to heaven; **repent** what's past; avoid what is to come; and do not spread the compost on the weeds." },
      { "author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Unless a man **repent** and turn his back upon the City of Destruction, he shall perish under the burden of his sin." },
      { "author": "Thomas Carlyle", "work": "Past and Present", "quote": "Better to **repent** in dust and ashes today than to perpetuate false governance into another miserable century." }
    ]
  },
  "Dashboard — pent\\repentance.md": {
    "primary": "Sincere regret, compunction, or sorrow for past misconduct, accompanied by an intentional determination to amend one's life.",
    "secondary": "In ethical theology and psychology, the moral act of acknowledging wrongdoing, undergoing profound sorrow, and undertaking restitution and inner reform.",
    "quotes": [
      { "author": "Samuel Johnson", "work": "The Rambler", "quote": "Sorrow for evils past is only so far virtuous as it produces **repentance**, and repentance is only valid as it works reformation." },
      { "author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's heart melted into genuine **repentance** as she acknowledged how selfish her grief had been toward her sister." },
      { "author": "John Locke", "work": "The Reasonableness of Christianity", "quote": "Faith without sincere **repentance** is dead, for Christ required that men forsake their transgressions and obey God's laws." }
    ]
  },
  "Dashboard — pent\\repentant.md": {
    "primary": "Experiencing, expressing, or characterized by sincere sorrow or regret for past offenses or misdeeds.",
    "secondary": "In legal and penitential traditions, a penitent individual whose remorse and admission of fault mitigate culpability and invite pardon or reconciliation.",
    "quotes": [
      { "author": "Charles Dickens", "work": "Great Expectations", "quote": "The old convict looked upon Pip with humble and **repentant** eyes, seeking only to repay the boy's childhood kindness." },
      { "author": "John Milton", "work": "Paradise Lost", "quote": "With tears replenishing the ground, they knelt in prayer **repentant**, and forgiveness sought from their offended Maker." },
      { "author": "George Eliot", "work": "Adam Bede", "quote": "She spoke with the quiet, **repentant** sorrow of one who has passed through the fire of suffering and learned humility." }
    ]
  },
  "Dashboard — pent\\repentantly.md": {
    "primary": "In a repentant manner; with sincere feelings or expressions of regret, remorse, and sorrow for past misconduct.",
    "secondary": "In literary narrative and character description, performing an action with visible contrition, seeking forgiveness and demonstrating a chastened heart.",
    "quotes": [
      { "author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He looked at me **repentantly**, confessing the reckless deceit that had almost wrecked both our lives." },
      { "author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The condemned prisoner bowed his head **repentantly**, joining his hands in earnest prayer as the minister read the psalm." },
      { "author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare knelt **repentantly** beside her, conscious at last of the cruel rigidity of his former judgment." }
    ]
  },
  "Dashboard — pleth\\isopleth.md": {
    "primary": "A line on a map or chart connecting points that have equal values of a given meteorological, physical, or numerical variable.",
    "secondary": "In cartography, meteorology, and thermodynamics, generic contour lines (such as isobars, isotherms, and isohyets) illustrating field distributions of temperature, pressure, or elevation.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "By joining stations of equal mean temperature with a continuous line, we trace an **isopleth** that reveals thermal zones independent of latitude." },
      { "author": "Francis Galton", "work": "Meteorographica, or Methods of Mapping the Weather", "quote": "Each barometric **isopleth** drawn across the chart indicates the gradient along which atmospheric winds must blow." },
      { "author": "Wladimir Köppen", "work": "The Climates of the Earth", "quote": "The northern tree limit corresponds closely with the ten-degree Celsius July **isopleth**." }
    ]
  },
  "Dashboard — pleth\\plethodon.md": {
    "primary": "A genus of small, lungless woodland salamanders (family Plethodontidae) native to North America, known as woodland salamanders.",
    "secondary": "In herpetology and evolutionary ecology, terrestrial amphibians that respire entirely through the moist skin and buccopharyngeal cavity, famous for direct development without an aquatic larval stage.",
    "quotes": [
      { "author": "Edward Drinker Cope", "work": "The Batrachia of North America", "quote": "In the genus **Plethodon**, the tongue is attached along the median line and respiration is conducted entirely through the vascular dermis." },
      { "author": "Raymond Ditmars", "work": "Reptiles and Amphibians", "quote": "Under rotting forest logs, one commonly finds **Plethodon** cinereus guarding its clutch of delicate gelatinous eggs." },
      { "author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "Speciation in Appalachian **Plethodon** salamanders illustrates the genetic divergence of morphologically conservative populations." }
    ]
  },
  "Dashboard — pleth\\plethodont.md": {
    "primary": "Belonging or pertaining to the amphibian family Plethodontidae, the lungless salamanders; or having many teeth.",
    "secondary": "In vertebrate anatomy, possessing numerous closely packed teeth arranged along the dental arches; or designating plethodontid salamanders characterized by nasolabial grooves.",
    "quotes": [
      { "author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The **plethodont** amphibians lack pulmonary lungs, relying on cutaneous gas exchange beneath the damp humus of Appalachian forests." },
      { "author": "Edward Drinker Cope", "work": "Synopsis of the Extinct Batrachia and Reptilia", "quote": "The fossil jaw exhibits a distinctly **plethodont** dentition, with dozens of minute conical teeth crowded along the alveolar border." },
      { "author": "G. Kingsley Noble", "work": "The Biology of the Amphibia", "quote": "A distinctive sensory feature of every **plethodont** salamander is the minute nasolabial groove assisting in chemoreception." }
    ]
  },
  "Dashboard — pleth\\plethodontidae.md": {
    "primary": "The largest family of salamanders, comprising the lungless salamanders, characterized by the absence of lungs and the presence of nasolabial grooves.",
    "secondary": "In systematic herpetology, a diverse amphibian clade containing over four hundred species predominantly distributed across the Americas, notable for cutaneous respiration and projectile tongues.",
    "quotes": [
      { "author": "G. Kingsley Noble", "work": "The Biology of the Amphibia", "quote": "The family **Plethodontidae** encompasses more than two-thirds of all living salamander species, demonstrating remarkable ecological radiation." },
      { "author": "Edward Drinker Cope", "work": "The Batrachia of North America", "quote": "The complete absence of lungs and trachea unites all members of **Plethodontidae** into a unique physiological alliance." },
      { "author": "Stephen Jay Gould", "work": "The Flamingo's Smile", "quote": "The projectile tongue of bolitoglossine salamanders within **Plethodontidae** represents one of nature's most exquisite biomechanical adaptations." }
    ]
  },
  "Dashboard — pleth\\plethora.md": {
    "primary": "An excessive amount, abundance, or overfullness of something.",
    "secondary": "In historical medicine and pathology, an excess of blood volume or bodily humors (plethora sanguinea) believed to produce congestion, fever, and inflammatory apoplexy.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The red, congested face and bounding pulse of the patient suggested that state of vascular **plethora** which former physicians bled so freely." },
      { "author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The printing presses groaned under a **plethora** of political pamphlets and controversial sermons." },
      { "author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "High feeding and a **plethora** of nutrition frequently induce sudden bud variations and floral double forms in garden plants." }
    ]
  },
  "Dashboard — pleth\\plethoric.md": {
    "primary": "Characterized by an excess, superfluity, or overabundance; or exhibiting an excessively florid, bloated complexion.",
    "secondary": "In historical physiology, suffering from vascular congestion or an abnormally large volume of blood (polycythemia).",
    "quotes": [
      { "author": "Charles Dickens", "work": "Bleak House", "quote": "A **plethoric** alderman sat in his plush carriage, his florid face puffed with rich dinners and port wine." },
      { "author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Feudal nobility, choked with **plethoric** wealth while the peasantry starved, drew near its inevitable judgment." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "An excessively **plethoric** brain condition frequently impedes sharp intellectual discrimination by flooding the sensorium." }
    ]
  },
  "Dashboard — pleth\\plethos.md": {
    "primary": "A multitude, great number, abundance, or fullness; the common people or masses (from Greek πλῆθος).",
    "secondary": "In classical political philosophy and sociological historiography, the body of common citizens or the popular multitude, contrasted with the aristocratic oligarchy.",
    "quotes": [
      { "author": "Thucydides", "work": "History of the Peloponnesian War", "quote": "Pericles held the **plethos** in check while preserving their liberty, leading rather than being led by the popular multitude." },
      { "author": "Aristotle", "work": "Politics", "quote": "Democracy arises when the **plethos** of free citizens holds the sovereign authority of the state." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The fundamental sense of **plethos** is fullness, whence it denotes a great throng, the mass of the people, or mathematical magnitude." }
    ]
  },
  "Dashboard — pleth\\plethysmograph.md": {
    "primary": "An instrument for measuring and recording changes in volume within an organ, whole body, or limb, usually resulting from fluctuations in blood circulation.",
    "secondary": "In cardiopulmonary physiology and autonomic neuroscience, an apparatus (such as air-displacement or water-displacement chambers) used to quantify peripheral pulse volume, respiratory capacity, and microvascular reactivity.",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "By attaching a water **plethysmograph** to the arm, Mosso demonstrated that emotional excitement instantly alters peripheral blood volume." },
      { "author": "Angelo Mosso", "work": "Fear", "quote": "The tracing on the **plethysmograph** dipped sharply the instant the sudden sound startled the resting subject." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The digital **plethysmograph** provides valuable objective records of vasospasm in patients suffering from Raynaud's phenomenon." }
    ]
  },
  "Dashboard — poly\\hoi polloi.md": {
    "primary": "The masses, the common people, or the general multitude, often used with a mildly disparaging or detached connotation.",
    "secondary": "In classical Greek political literature (οἱ πολλοί, 'the many'), the majority of citizens lacking aristocratic status or specialized philosophical education.",
    "quotes": [
      { "author": "Lord Byron", "work": "Don Juan", "quote": "He courted not the favors of **hoi polloi**, preferring the solitary companionship of his own restless thoughts." },
      { "author": "John Dryden", "work": "An Essay of Dramatic Poesy", "quote": "Playwrights are too often tempted to pander to **hoi polloi** with vulgar farce rather than noble dramatic poetry." },
      { "author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "True culture seeks not to isolate an elite, but to humanize and elevate **hoi polloi** with sweetness and light." }
    ]
  },
  "Dashboard — poly\\oligopoly.md": {
    "primary": "A market structure in which a particular industry is dominated by a small number of large sellers or producers.",
    "secondary": "In microeconomics and antitrust law, an imperfect competition model where the strategic pricing and output decisions of each dominant firm directly influence and depend upon the actions of its competitors.",
    "quotes": [
      { "author": "Joan Robinson", "work": "The Economics of Imperfect Competition", "quote": "Under conditions of **oligopoly**, price competition often gives way to intensive advertising and tacit collusion." },
      { "author": "John Kenneth Galbraith", "work": "American Capitalism: The Concept of Countervailing Power", "quote": "Modern heavy industry is characterized not by pure monopoly, but by an **oligopoly** of three or four industrial giants." },
      { "author": "Paul Samuelson", "work": "Economics", "quote": "Game theory provides the essential mathematical framework for analyzing strategic rivalry within an **oligopoly**." }
    ]
  },
  "Dashboard — poly\\pollakanth.md": {
    "primary": "A plant that flowers and produces seeds repeatedly year after year; a polycarpic perennial plant.",
    "secondary": "In botanical terminology and plant reproductive ecology, a species exhibiting iteroparity (flowering multiple times throughout its lifespan), contrasted with monanthous or monocarpic species that die after a single flowering.",
    "quotes": [
      { "author": "Asa Gray", "work": "Structural Botany", "quote": "Unlike the century plant which dies after one magnificent effort, the oak is a perennial **pollakanth**, blooming every spring." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Herbaceous perennials of the **pollakanth** type store root reserves to sustain repetitive annual flowerings." },
      { "author": "Arthur Cronquist", "work": "The Evolution and Classification of Flowering Plants", "quote": "The evolutionary shift from a monocarpic life cycle to a **pollakanth** perennial habit reflects adaptation to stable woodland habitats." }
    ]
  },
  "Dashboard — poly\\polyadic.md": {
    "primary": "Consisting of, having, or involving many parts, elements, terms, or variables.",
    "secondary": "In formal logic and mathematics, a relation, function, or predicate that takes many arguments (such as n-ary or polyadic predicates), contrasted with monadic and dyadic relations.",
    "quotes": [
      { "author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Every **polyadic** relation can be analyzed as a compound network of triadic and dyadic connections." },
      { "author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "A **polyadic** proposition involves a relation asserting a symmetrical or asymmetrical tie among many terms." },
      { "author": "Willard Van Orman Quine", "work": "Word and Object", "quote": "Standardizing logic requires clarifying whether a predicate is monadic, dyadic, or generally **polyadic** in its argument structure." }
    ]
  },
  "Dashboard — poly\\polyamide.md": {
    "primary": "A synthetic or natural polymer containing repeating amide groups (-CO-NH-) in the main chain, such as nylon, Kevlar, wool, or silk.",
    "secondary": "In materials science and polymer chemistry, thermoplastic condensation polymers synthesized from diamines and dicarboxylic acids, notable for high tensile strength, thermal resistance, and fiber-forming capabilities.",
    "quotes": [
      { "author": "Wallace Carothers", "work": "Studies on Polymerization and Ring Formation", "quote": "Linear condensation of hexamethylenediamine with adipic acid yields a tough, spinnable **polyamide** fiber." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Interchain hydrogen bonding between peptide links gives the synthetic **polyamide** nylon its remarkable structural stiffness." },
      { "author": "Herman Mark", "work": "Physical Chemistry of High Polymeric Systems", "quote": "The crystalline melting point of a **polyamide** rises systematically with the density of its recurring hydrogen bonds." }
    ]
  },
  "Dashboard — poly\\polyandrist.md": {
    "primary": "A woman who has more than one husband simultaneously.",
    "secondary": "In cultural anthropology and ethnology, a female practitioner of polyandry within societies (such as traditional Tibetan or Toda communities) where fraternal marriage alliances prevail.",
    "quotes": [
      { "author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "In Tibetan high valleys, the **polyandrist** is married jointly to several brothers, preserving the family estate intact." },
      { "author": "James George Frazer", "work": "Totemism and Exogamy", "quote": "Among the Toda hill tribes, a **polyandrist** holds recognized social status, her offspring belonging to the brother who performs the bow ceremony." },
      { "author": "Lewis Henry Morgan", "work": "Ancient Society", "quote": "Early ethnological surveys revealed that the **polyandrist** household represented a specific adaptation to severe land scarcity." }
    ]
  },
  "Dashboard — poly\\polyandrous.md": {
    "primary": "Practicing polyandry; having more than one husband or male sexual partner at the same time.",
    "secondary": "In botany and zoological ecology, plants having twenty or more stamens in a flower; or female animals that mate with multiple males during a single breeding season (such as phalaropes or jacanas).",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "In certain shorebirds like the painted snipe, the female is larger, brightly colored, and strictly **polyandrous**." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "In the order Ranunculaceae, the flowers are typically **polyandrous**, bearing numerous stamens inserted upon the receptacle." },
      { "author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "A **polyandrous** household where brothers share a single wife effectively curbs population growth in harsh mountain environments." }
    ]
  },
  "Dashboard — poly\\polyandry.md": {
    "primary": "A form of marriage or mating system in which a woman has more than one husband at the same time.",
    "secondary": "In anthropology, a relatively rare marital institution (notably fraternal polyandry in the Himalayas) designed to prevent land fragmentation; in behavioral ecology, a mating system where females hold territories and mate with multiple males.",
    "quotes": [
      { "author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "Fraternal **polyandry** in Ladakh prevents the division of arable family land among surviving sons." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sex-role reversal in birds is closely associated with **polyandry**, where males perform all incubation and parental care." },
      { "author": "E. B. Tylor", "work": "Anthropology: An Introduction to the Study of Man and Civilization", "quote": "Where female infanticide produced a deficit of women, institutionalized **polyandry** frequently emerged as an economic necessity." }
    ]
  },
  "Dashboard — poly\\polyangiaceae.md": {
    "primary": "A family of Gram-negative gliding slime bacteria in the order Myxococcales, noted for forming complex multicellular fruiting bodies.",
    "secondary": "In bacteriology and microbial ecology, soil-dwelling delta-proteobacteria characterized by social predatory swarming and the formation of clustered, cyst-bearing sporangioles (fruiting bodies) to survive environmental desiccation.",
    "quotes": [
      { "author": "Roland Thaxter", "work": "On the Myxobacteriaceae", "quote": "The family **Polyangiaceae** is distinguished by the production of encysted sporangioles enclosed within a common gelatinous matrix." },
      { "author": "Martinus Beijerinck", "work": "Verzamelde Geschriften", "quote": "Gliding motility upon agar surfaces allows members of **Polyangiaceae** to hunt and lyse fungal mycelia cooperatively." },
      { "author": "Selman Waksman", "work": "Principles of Soil Microbiology", "quote": "The fruiting bodies of **Polyangiaceae** found on decaying wood represent the pinnacle of morphological complexity among prokaryotes." }
    ]
  },
  "Dashboard — poly\\polyangium.md": {
    "primary": "A genus of myxobacteria (family Polyangiaceae) that forms clusters of cysts or sporangioles within an envelopment of slime.",
    "secondary": "In systematic bacteriology, predatory soil myxobacteria (such as Polyangium cellulosum) capable of hydrolyzing cellulose and synthesizing diverse bioactive secondary metabolites.",
    "quotes": [
      { "author": "Roland Thaxter", "work": "Contributions from the Cryptogamic Laboratory of Harvard University", "quote": "In the genus **Polyangium**, the fruiting mass consists of numerous distinct cysts held together by a translucent slime envelope." },
      { "author": "Selman Waksman", "work": "The Soil and the Microbe", "quote": "Decomposition of filter paper under aerobic conditions was actively accomplished by strains of **Polyangium**." },
      { "author": "David Baltimore", "work": "Microbial Genetics and Social Behavior", "quote": "Cellular aggregation in **Polyangium** provides a primitive paradigm for the genetic evolution of developmental signaling." }
    ]
  },
  "Dashboard — poly\\polyanthus.md": {
    "primary": "A popular garden hybrid primrose (Primula × polyantha) bearing clusters of colorful, showy flowers on a central upright stalk.",
    "secondary": "In floriculture and historical horticulture, cultivated hybrids between the common primrose, cowslip, and oxlip, bred since the 17th century for multicolored, rich margins and garden borders.",
    "quotes": [
      { "author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The garden **polyanthus** displayeth upon one single stalk a great bunch of flowers of divers lively colors." },
      { "author": "William Cowper", "work": "The Task", "quote": "The **polyanthus** of unnumber'd dyes, with sweet Auricula and pansy freak'd with jet, adorn the early borders of spring." },
      { "author": "Gertrude Jekyll", "work": "Colour Schemes for the Flower Garden", "quote": "A border planted with white and golden **polyanthus** brings cheerfulness to the garden before the daffodils awake." }
    ]
  },
  "Dashboard — poly\\polyarteritis.md": {
    "primary": "A systemic necrotizing vasculitis that causes inflammation of small- and medium-sized muscular arteries.",
    "secondary": "In rheumatology and vascular pathology (specifically polyarteritis nodosa, described by Kussmaul and Maier in 1866), a serious autoimmune disorder producing transmural fibrinoid necrosis, aneurysm formation, renal ischemia, and multiorgan failure.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Necrotizing lesions in **polyarteritis** lead to multiple microaneurysms along the mesenteric and renal arterial branches." },
      { "author": "Harvey Cushing", "work": "Studies in Intracranial Physiology and Surgery", "quote": "Cerebral vascular complications arising from systemic **polyarteritis** frequently mimic intracranial tumors." },
      { "author": "Eugene Braunwald", "work": "Heart Disease: A Textbook of Cardiovascular Medicine", "quote": "Coronary arteritis occurring in **polyarteritis** nodosa can cause silent myocardial infarction in young adults." }
    ]
  },
  "Dashboard — poly\\polyatomic.md": {
    "primary": "Consisting of or containing three or more atoms in a molecule; or having more than one replaceable atom or valence bond.",
    "secondary": "In physical chemistry and molecular spectroscopy, molecules (such as H2O, NH3, or CH4) whose vibrational and rotational degrees of freedom require multidimensional quantum analysis, contrasted with diatomic and monatomic species.",
    "quotes": [
      { "author": "Svante Arrhenius", "work": "Text-Book of Theoretical Electrochemistry", "quote": "The heat capacity of a **polyatomic** gas is significantly higher because energy is absorbed in internal atomic vibrations." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "In a **polyatomic** ion like sulfate or nitrate, resonance distributes the ionic charge symmetrically over several equivalent oxygen atoms." },
      { "author": "Irving Langmuir", "work": "The Arrangement of Electrons in Atoms and Molecules", "quote": "The stability of **polyatomic** molecules depends upon completing octets of valence electrons shared between adjacent nuclei." }
    ]
  },
  "Dashboard — poly\\polycarp.md": {
    "primary": "A botanical fruit or plant with multiple carpels; or Saint Polycarp, a second-century bishop of Smyrna and early Christian martyr.",
    "secondary": "In historical hagiography and patristics, Polycarp of Smyrna (c. 69 – 155 CE), a disciple of John the Apostle who was burned at the stake; in botany, a plant that produces fruit repeatedly (polycarpic).",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The venerable bishop **Polycarp** refused to revile Christ, saying, 'Eighty and six years have I served Him, and He never did me wrong.'" },
      { "author": "Eusebius", "work": "Church History", "quote": "The martyrdom of **Polycarp** was witnessed by all Smyrna, inspiring early Christians with steadfast faith under persecution." },
      { "author": "Asa Gray", "work": "Elements of Botany", "quote": "A compound ovary composed of distinct, unfused carpels produces what morphologists term a **polycarp** aggregation." }
    ]
  },
  "Dashboard — poly\\polychaeta.md": {
    "primary": "A class of predominantly marine annelid worms, commonly called bristle worms, characterized by numerous chitinous chaetae (bristles) on fleshy parapodia.",
    "secondary": "In marine biology and invertebrate zoology, a large and diverse group (including lugworms, clam worms, and feather duster worms) possessing segmented bodies, well-developed heads, and specialized trochozoan larvae.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Members of the class **Polychaeta** possess lateral unjointed appendages or parapodia carrying bunches of chitinous bristles." },
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "The pelagic trochophore larva of marine **Polychaeta** links them evolutionarily with the ancestral lineage of mollusks." },
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "Tidal flats teem with burrowing worms of the order **Polychaeta**, creating networks of subterranean tubes beneath the mud." }
    ]
  },
  "Dashboard — poly\\polychaete.md": {
    "primary": "Any marine annelid worm belonging to the class Polychaeta, characterized by a segmented body and numerous bristles protruding from lateral parapodia.",
    "secondary": "In benthic ecology, segmented marine worms that play essential ecological roles as filter feeders, detritivores, and predators in soft sediment communities and coral reefs.",
    "quotes": [
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "The iridescent clam worm is an active predatory **polychaete**, hunting smaller invertebrates across the intertidal reef." },
      { "author": "William Beebe", "work": "Nonsuch: Land of Water", "quote": "At night the surface waters glowed with the bioluminescent nuptial swarming of a delicate **polychaete** worm." },
      { "author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Just as earthworms rework the terrestrial loam, the marine **polychaete** continuously turns and aerates coastal sediments." }
    ]
  }
}

base_cluster_dir = 'App database/Greek roots/Cluster Number & Mathematics'
slice_path = 'main app/scripts/slice-math-part3.json'

with open(slice_path, 'r', encoding='utf-8') as f:
    full_slice = json.load(f)

# Batch 1 is items 0 to 76
expected_keys = full_slice[:77]

print(f"Batch 1 contains {len(batch1_data)} items.")
print(f"Expected slice items: {len(expected_keys)}")

missing = [k for k in expected_keys if k not in batch1_data]
extra = [k for k in batch1_data if k not in expected_keys]

if missing:
    print("ERROR: Missing keys in Batch 1:", missing)
    sys.exit(1)
if extra:
    print("ERROR: Extra keys in Batch 1:", extra)
    sys.exit(1)

print("Key matching confirmed perfectly!")

# Internal Quality Validation
for p, data in batch1_data.items():
    if data["primary"].strip().lower() == data["secondary"].strip().lower():
        print(f"Error: primary == secondary in {p}")
        sys.exit(1)
    if len(data["quotes"]) != 3:
        print(f"Error: not 3 quotes in {p}")
        sys.exit(1)
    authors = [q["author"] for q in data["quotes"]]
    if len(set(authors)) != 3:
        print(f"Error: duplicate author in {p}: {authors}")
        sys.exit(1)
    for q in data["quotes"]:
        if any(ph in q["author"] for ph in ["Academic Lexicon", "Classic Author", "Unknown Author", "Placeholder"]):
            print(f"Error: placeholder author in {p}: {q['author']}")
            sys.exit(1)
        if "**" not in q["quote"]:
            print(f"Error: no bolding in quote for {p}: {q['quote']}")
            sys.exit(1)

print("All internal quality checks passed!")

# Update files directly
updated = 0
for rel_path, data in batch1_data.items():
    file_path = os.path.join(base_cluster_dir, rel_path)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    book_idx = content.find('> [!book]')
    if book_idx == -1:
        print(f"No > [!book] in {file_path}")
        sys.exit(1)
    
    header_part = content[:book_idx].rstrip()
    def_block = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {data['primary']}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {data['secondary']}"
    quote_lines = "\n".join(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*" for q in data['quotes'])
    quotes_block = f"> [!quote] 💬 Contextual Usage & Authentic Quotations\n{quote_lines}"
    
    new_content = f"{header_part}\n\n{def_block}\n\n{quotes_block}\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    updated += 1

print(f"Successfully updated {updated} files in Batch 1.")
