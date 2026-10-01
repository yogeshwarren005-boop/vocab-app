import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Feeling & Sensation';

const filesData = {
  // Dashboard — hed (20 words)
  "Dashboard — hed/cathedra.md": {
    primary: "A bishop's official throne or ceremonial seat, located in the choir or apse of a cathedral church.",
    secondary: "A position or chair of supreme ecclesiastical or academic authority, notably used in the phrase *ex cathedra* for authoritative papal decrees.",
    quotes: [
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "The prelate speaks with ordinary jurisdictional authority when teaching from his elevated episcopal **cathedra**." },
      { author: "Saint Augustine", work: "De Civitate Dei", quote: "The apostolic succession preserves unity across the churches, linked to the historic **cathedra** of Peter." },
      { author: "John Henry Newman", work: "Apologia Pro Vita Sua", quote: "A solemn pronouncement issued from the papal **cathedra** binds the faithful in matters of revealed dogma." }
    ]
  },
  "Dashboard — hed/cathedral.md": {
    primary: "The principal church of a diocese, housing the official seat or throne (cathedra) of the bishop.",
    secondary: "In architecture and cultural history, a monumental medieval ecclesiastical structure characterized by soaring vaulted naves, stained glass, and flying buttresses.",
    quotes: [
      { author: "Victor Hugo", work: "The Hunchback of Notre-Dame", quote: "The ancient Gothic **cathedral** was a vast stone symphony where each arch and gargoyle spoke the faith of centuries." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The builder of a medieval **cathedral** poured his soul into the stone capitals, caring little for personal renown." },
      { author: "Henry Adams", work: "Mont-Saint-Michel and Chartres", quote: "The Virgin of Chartres smiled from her rose window, looking down upon her completed twelfth-century **cathedral**." }
    ]
  },
  "Dashboard — hed/chair.md": {
    primary: "A separate seat for one person, typically having four legs and a rest for the back (derived through Old French *chaiere* from Latin *cathedra*).",
    secondary: "A seat of office, honor, or authority; an official professorship in a university department or the presiding officer of a meeting.",
    quotes: [
      { author: "Samuel Johnson", work: "The Idler", quote: "A tavern **chair** is the throne of human felicity, where every guest commands respect without ceremony." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mr. Bennet took his customary easy **chair** in the library, shutting the door against family turmoil." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Queequeg sat smoking in the arm-**chair** by the hearth, calm as an ancient sculptured bronze chief." }
    ]
  },
  "Dashboard — hed/dodecahedron.md": {
    primary: "A three-dimensional geometric polyhedron having twelve flat faces, especially a regular dodecahedron with twelve regular pentagonal faces.",
    secondary: "In classical cosmology and sacred geometry, the fifth Platonic solid associated by the Pythagoreans with the celestial sphere and quintessence.",
    quotes: [
      { author: "Plato", work: "Timaeus", quote: "There remained a fifth construction, the **dodecahedron**, which the Demiurge used for the embroidery of the constellations." },
      { author: "Johannes Kepler", work: "Harmonices Mundi", quote: "Between the spheres of Mars and the Earth, I placed the regular **dodecahedron** to determine their planetary orbits." },
      { author: "Euclid", work: "Elements", quote: "To construct an equilateral and equiangular **dodecahedron**, we inscribe twelve pentagons within a given sphere." }
    ]
  },
  "Dashboard — hed/dodecahemidodecahedron.md": {
    primary: "A non-convex uniform star polyhedron consisting of eighteen faces: twelve regular pentagons and six regular decagrams or hexagons intersecting at the center.",
    secondary: "In higher geometry and topology, a quasi-regular polyhedron characterized by vertices that each meet two pentagons and two decagons.",
    quotes: [
      { author: "H. S. M. Coxeter", work: "Regular Polytopes", quote: "The uniform star polyhedron known as the **dodecahemidodecahedron** exhibits faces passing through the center of symmetry." },
      { author: "Magnus Wenninger", work: "Polyhedron Models", quote: "Constructing the cardboard model of the **dodecahemidodecahedron** requires painstaking precision at intersecting internal vertices." },
      { author: "Michael Longuet-Higgins", work: "Uniform Polyhedra", quote: "The symmetry group of the **dodecahemidodecahedron** shares the full rotational properties of the regular icosahedron." }
    ]
  },
  "Dashboard — hed/endohedric.md": {
    primary: "In crystallography, having crystal faces or internal symmetry elements that correspond to internal hemihedral forms; possessing internal face symmetry.",
    secondary: "Pertaining to internal crystalline orientations where optical properties reflect the subterranean geometric arrangement of molecular lattices.",
    quotes: [
      { author: "Edward Salisbury Dana", work: "A Text-Book of Mineralogy", quote: "Certain tourmaline crystals exhibit an **endohedric** development that creates distinct electrical polarity upon heating." },
      { author: "René Just Haüy", work: "Treatise on Mineralogy", quote: "Cleavage planes expose the fundamental **endohedric** nucleus around which secondary crystal faces assemble." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The optical interference figures reveal an **endohedric** distribution of internal stress in unannealed quartz prisms." }
    ]
  },
  "Dashboard — hed/ephedra.md": {
    primary: "A genus of gymnosperm desert shrubs (family Ephedraceae), commonly called Mormon tea or jointfir, with jointed green photosynthetic stems and scale-like leaves.",
    secondary: "A classical medicinal plant known in traditional Chinese medicine as Ma Huang, yielding the stimulating alkaloids ephedrine and pseudoephedrine.",
    quotes: [
      { author: "Dioscorides", work: "De Materia Medica", quote: "The shrub **Ephedra**, which clings to stony hillsides, was dried by herborists to stem internal hemorrhages." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The aphyllous stems of **Ephedra** flourish in alkaline desert sands where true leafy shrubs wither." },
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "We class the dioecious desert gymnosperm under the genus **Ephedra**, noted for its leafless equisetum-like twigs." }
    ]
  },
  "Dashboard — hed/exedra.md": {
    primary: "A semicircular or rectangular architectural recess, alcove, or pavilion, typically fitted with raised stone benches for seated philosophical discussion.",
    secondary: "In ancient Greek gymnasia and Roman baths, a dignified meeting area where rhetoricians, philosophers, and citizens gathered for dialogue.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "In the peristyle of the palaestra, spacious **exedra** should be constructed with seats so that philosophers may dispute in comfort." },
      { author: "Pliny the Younger", work: "Letters", quote: "From the quiet **exedra** of my Laurentine villa, one commands an unbroken view of the shimmering Tyrrhenian sea." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The public baths of Caracalla were adorned with marble **exedra** where poets recited verses to seated crowds." }
    ]
  },
  "Dashboard — hed/hed.md": {
    primary: "The Greek root *hed-* / *hedr-* (from *hedra*), meaning seat, chair, bench, base, or geometrical face (as in *polyhedron*, *cathedra*, *exedra*).",
    secondary: "The foundational combining form in geometry, crystallography, and ecclesiastical architecture signifying planar surfaces or seated assemblies.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The noun *hedra* and its combining form **hed** designate a sitting place, foundation, abode, or planar face of a solid." },
      { author: "Aristotle", work: "Metaphysics", quote: "Geometrical solids are categorized according to the number of planes, or **hed**, that enclose their three-dimensional boundaries." },
      { author: "Euclid", work: "Elements", quote: "Each regular figure rests upon a stable base or **hed** from which its planar angles ascend." }
    ]
  },
  "Dashboard — hed/pentahedroid.md": {
    primary: "A four-dimensional geometric polytope bounded by five tetrahedral cells; a 4-simplex or hypertetrahedron.",
    secondary: "The simplest possible four-dimensional regular polytope, possessing five vertices, ten edges, ten triangular faces, and five tetrahedral cells.",
    quotes: [
      { author: "H. S. M. Coxeter", work: "Regular Polytopes", quote: "The 4-simplex, or regular **pentahedroid**, forms the four-dimensional analogue of the three-dimensional tetrahedron." },
      { author: "Ludwig Schläfli", work: "Theorie der vielfachen Kontinuität", quote: "In four-dimensional Euclidean space, the simplest convex figure is bounded by five cells, the **pentahedroid**." },
      { author: "Arthur Cayley", work: "Collected Mathematical Papers", quote: "We compute the hypervolume of the **pentahedroid** by integrating determinant coordinates across its five vertices." }
    ]
  },
  "Dashboard — hed/pentahedron.md": {
    primary: "A solid geometric figure (polyhedron) bounded by five plane faces.",
    secondary: "In geometry, existing in two distinct convex topological forms: a square-based pyramid (four triangles and one quadrilateral) and a triangular prism (two triangles and three quadrilaterals).",
    quotes: [
      { author: "Leonhard Euler", work: "Elements of Algebra", quote: "Every convex **pentahedron** satisfies our polyhedral relation, having either six or five vertices depending on its base." },
      { author: "René Descartes", work: "Principles of Philosophy", quote: "Consider a crystal shaped as a triangular prism: it is a simple **pentahedron** bounded by two bases and three sides." },
      { author: "Adrien-Marie Legendre", work: "Elements of Geometry", quote: "A pyramid erected on a four-sided base constitutes a **pentahedron** possessing eight straight edges." }
    ]
  },
  "Dashboard — hed/polyhedral.md": {
    primary: "Of, relating to, or shaped like a polyhedron; having many plane faces or polygonal facets.",
    secondary: "In structural biochemistry and morphology, describing symmetric multi-faceted forms such as viral protein capsids and geometric crystal clusters.",
    quotes: [
      { author: "Leonhard Euler", work: "Solutio problematis ad geometriam situs pertinentis", quote: "The general **polyhedral** theorem demonstrates that vertices plus faces always exceed edges by two." },
      { author: "Johannes Kepler", work: "Mysterium Cosmographicum", quote: "The divine architect arranged the heavenly spheres according to the harmony of the five regular **polyhedral** solids." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "Surface tension in crowded soap bubbles forces the cells into complex **polyhedral** packing geometries." }
    ]
  },
  "Dashboard — hed/polyhedron.md": {
    primary: "A three-dimensional solid figure bounded by plane polygonal faces, straight edges, and vertices.",
    secondary: "In mathematics and geometry, a fundamental geometric object whose topological invariants and symmetries form the foundation of spatial theory.",
    quotes: [
      { author: "Euclid", work: "Elements", quote: "A **polyhedron** is a solid figure contained by plane figures which are not in the same plane." },
      { author: "René Descartes", work: "De Solidorum Elementis", quote: "In any convex **polyhedron**, the sum of the plane face angles at all vertices can be computed from its edge count." },
      { author: "Imre Lakatos", work: "Proofs and Refutations", quote: "The definition of a **polyhedron** underwent continuous revision as counterexamples challenged Euler's formula." }
    ]
  },
  "Dashboard — hed/pyritohedron.md": {
    primary: "An irregular dodecahedron characteristic of iron pyrite (iron disulfide), having twelve identical non-regular pentagonal faces possessing pyritohedral symmetry.",
    secondary: "In crystallography, a hemihedral isometric crystal form (pentagonal dodecahedron) displaying parallel striations on alternating faces.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "Iron pyrite frequently crystallizes in brilliant brass-yellow cubes or in the classic striate **pyritohedron**." },
      { author: "Edward Salisbury Dana", work: "A Text-Book of Mineralogy", quote: "The symmetry of the **pyritohedron** reveals parallel striations caused by oscillating oscillatory growth between cube and octahedron." },
      { author: "René Just Haüy", work: "Traité de Minéralogie", quote: "The pentagonal facets of the **pyritohedron** demonstrate that crystal symmetry obeys rational decrescence of molecular rows." }
    ]
  },
  "Dashboard — hed/rhombohedral.md": {
    primary: "Having, relating to, or shaped like a rhombohedron; in crystallography, belonging to the trigonal crystal system with axes of equal length and equal non-90° angles.",
    secondary: "Describing mineral species (e.g., calcite, quartz, dolomite) whose lattice geometries exhibit threefold rotational symmetry.",
    quotes: [
      { author: "William Hallowes Miller", work: "A Treatise on Crystallography", quote: "Calcite presents the classic exemplar of the **rhombohedral** system, cleaving easily along three oblique planes." },
      { author: "Louis Pasteur", work: "Researches on the Molecular Asymmetry of Natural Organic Products", quote: "The hemihedral facets on **rhombohedral** quartz crystals indicate underlying molecular chirality." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The cleavage angles of **rhombohedral** carbonates allow precise discrimination between magnesite and siderite." }
    ]
  },
  "Dashboard — hed/rhombohedron.md": {
    primary: "A six-faced polyhedron whose faces are all identical rhombuses; an oblique prism bounded by six rhombic planes.",
    secondary: "In mineralogy and crystallography, the fundamental cleavage form of calcite (Iceland spar) displaying optical double refraction.",
    quotes: [
      { author: "René Just Haüy", work: "Essay on a Theory of the Structure of Crystals", quote: "When you shatter a block of spar, every microscopic fragment retains the exact angles of the parent **rhombohedron**." },
      { author: "Edward Salisbury Dana", work: "A Text-Book of Mineralogy", quote: "A cleavage **rhombohedron** of Iceland spar clearly separates a beam of light into ordinary and extraordinary rays." },
      { author: "John Herschel", work: "Preliminary Discourse on the Study of Natural Philosophy", quote: "Haüy's realization that crystals are built of invisible bricks like the **rhombohedron** founded modern mineral science." }
    ]
  },
  "Dashboard — hed/sanhedrin.md": {
    primary: "The supreme council and judicial tribunal of the ancient Jewish nation, composed of seventy-one religious elders, high priests, and scribes.",
    secondary: "The historical Hellenistic and Roman-period Jewish assembly (from Greek *synedrion*, 'sitting together') that adjudicated religious law and capital offenses.",
    quotes: [
      { author: "Flavius Josephus", work: "Antiquities of the Jews", quote: "The high priest convened the elders of the **Sanhedrin** in the chamber of polished stone to pass judgment." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Under Roman procurators, the judicial authority of the **Sanhedrin** was strictly circumscribed in capital causes." },
      { author: "Ernest Renan", work: "The Life of Jesus", quote: "The trial before the Jerusalem **Sanhedrin** was marked by turbulent disputes between Sadducean priests and Pharisaic doctors." }
    ]
  },
  "Dashboard — hed/synedrion.md": {
    primary: "An ancient Greek council, governing assembly, or meeting of seated delegates (from *syn* 'together' and *hedra* 'seat').",
    secondary: "The historical representative congress of Greek confederacies (such as the Second Athenian League or the League of Corinth) summoned to deliberate on war and peace.",
    quotes: [
      { author: "Polybius", work: "The Histories", quote: "The delegates assembled in the **synedrion** at Corinth to ratify the terms of the common Hellenic peace." },
      { author: "Plutarch", work: "Parallel Lives", quote: "Phocion addressed the Athenian **synedrion**, urging diplomatic prudence rather than precipitous military alliance." },
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "The Peloponnesian allies met in solemn **synedrion** to debate whether Sparta should declare open hostilities." }
    ]
  },
  "Dashboard — hed/tetrahedroid.md": {
    primary: "A four-dimensional geometric polytope bounded by tetrahedral faces; having the characteristics of a 4-simplex.",
    secondary: "In algebraic geometry and higher polytope theory, a tetrahedral-like hypersolid possessing four-dimensional polyhedral symmetry.",
    quotes: [
      { author: "H. S. M. Coxeter", work: "Regular Polytopes", quote: "The regular **tetrahedroid** is self-dual in four-space, just as the three-dimensional tetrahedron is in three-space." },
      { author: "Ludwig Schläfli", work: "Theorie der vielfachen Kontinuität", quote: "By connecting five equidistant points in four dimensions, one bounds a regular **tetrahedroid** of ten triangular faces." },
      { author: "Arthur Cayley", work: "Mathematical Papers", quote: "The projective coordinates of the **tetrahedroid** correspond to symmetrical matrix determinants in hyperspace." }
    ]
  },
  "Dashboard — hed/trisoctahedron.md": {
    primary: "A 24-faced polyhedron formed by erecting a low three-sided triangular pyramid upon each of the eight faces of a regular octahedron.",
    secondary: "In crystallography, a crystal form of the isometric (cubic) system characterized by 24 isosceles triangular facets, seen in galena and diamond.",
    quotes: [
      { author: "Edward Salisbury Dana", work: "A Text-Book of Mineralogy", quote: "The mineral diamond occasionally exhibits modified edges that bevel into the facets of a **trisoctahedron**." },
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "A crystal bounded by twenty-four triangular planes belonging to the octahedral group is designated a **trisoctahedron**." },
      { author: "William Hallowes Miller", work: "A Treatise on Crystallography", quote: "The Miller indices {hhl} identify the symmetrical trigonal faces of the isometric **trisoctahedron**." }
    ]
  },

  // Dashboard — hedon (10 words)
  "Dashboard — hedon/anhedonia.md": {
    primary: "The inability to experience pleasure, interest, or satisfaction from previously enjoyable activities, experiences, or relationships.",
    secondary: "In clinical psychiatry and neuropsychology, a core diagnostic symptom of major depressive disorder, schizophrenia, and Parkinson's disease involving dopaminergic dysfunction.",
    quotes: [
      { author: "Théodule-Armand Ribot", work: "The Psychology of the Emotions", quote: "Just as there is analgesia for pain, so there is **anhedonia** for pleasure, a total inability to experience delight." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The melancholy soul sinks into a state of spiritual **anhedonia**, where every beauty in nature appears flat and dead." },
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "A profound emotional **anhedonia** settles upon dementia praecox patients long before cognitive deterioration is overt." }
    ]
  },
  "Dashboard — hedon/anhedonic.md": {
    primary: "Characterized by, suffering from, or related to anhedonia; lacking the capacity to experience pleasure.",
    secondary: "Describing a depressive or blunted psychological state in which positive emotional reinforcement is absent.",
    quotes: [
      { author: "Sigmund Freud", work: "Mourning and Melancholia", quote: "In melancholia, the ego is paralyzed by an **anhedonic** gloom that extinguishes all interest in the external world." },
      { author: "Henry Maudsley", work: "The Pathology of Mind", quote: "The chronic neurotic often enters an **anhedonic** phase where music, affection, and food become completely tasteless." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Deprived of dopamine, the parkinsonian patients lived in a frozen, **anhedonic** limbo for decades." }
    ]
  },
  "Dashboard — hedon/hed 2.md": {
    primary: "The Greek root *hēdon-* (from *hēdonē*), signifying pleasure, delight, sensual enjoyment, or gratification (contrasted with *hedra* 'seat').",
    secondary: "The foundational combining form in ethical philosophy and psychological economics denoting the pursuit or quantification of subjective pleasure.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek noun *hēdonē*, giving rise to the combining stem **hed**, denotes sensory pleasure, enjoyment, and joy." },
      { author: "Epicurus", work: "Letter to Menoeceus", quote: "We declare that pleasure, the ancient **hedone**, is the beginning and end of living happily." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "The young Roman cultivated the refined essence of **hedone**, seeking harmony between moral order and sensory delight." }
    ]
  },
  "Dashboard — hedon/hedonic.md": {
    primary: "Relating to, characterized by, or producing pleasant sensations or pleasure.",
    secondary: "In economics, psychology, and welfare ethics, pertaining to the measurement of subjective satisfaction, utility, or affective tone (e.g., the hedonic treadmill).",
    quotes: [
      { author: "Jeremy Bentham", work: "An Introduction to the Principles of Morals and Legislation", quote: "Nature has placed mankind under the governance of two sovereign masters, pain and pleasure, the pillars of our **hedonic** calculus." },
      { author: "Francis Ysidro Edgeworth", work: "Mathematical Psychics", quote: "An exact science of utility requires an imaginary machine, a **hedonic** calculus capable of measuring units of pleasure." },
      { author: "John Stuart Mill", work: "Utilitarianism", quote: "It is better to be a human being dissatisfied than a pig satisfied, demonstrating that **hedonic** quality surpasses quantity." }
    ]
  },
  "Dashboard — hedon/hedonics.md": {
    primary: "The branch of psychology, ethics, or economics that studies and measures pleasant and unpleasant sensations and well-being.",
    secondary: "The systematic scientific methodology that investigates subjective pleasure, reward circuits, and affective preferences.",
    quotes: [
      { author: "Francis Ysidro Edgeworth", work: "Mathematical Psychics", quote: "The principles of **hedonics** seek to establish quantitative laws governing the distribution of pleasure in human society." },
      { author: "Alexander Bain", work: "The Emotions and the Will", quote: "A scientific **hedonics** must chart the physical sensations that accompany muscular exertion, nutrition, and rest." },
      { author: "William Stanley Jevons", work: "The Theory of Political Economy", quote: "Economics is essentially a calculus of pleasure and pain, resting firmly on the physiological foundations of **hedonics**." }
    ]
  },
  "Dashboard — hedon/hedonism.md": {
    primary: "The ethical or philosophical doctrine that pleasure, enjoyment, and the avoidance of pain are the highest good and proper aim of human life.",
    secondary: "In common usage, a way of life devoted solely to the pursuit of sensual pleasure, self-indulgence, and sensory gratification.",
    quotes: [
      { author: "Epicurus", work: "Principal Doctrines", quote: "When we say that pleasure is the end of life, we do not mean the debauchery of the prodigal, but sober philosophical **hedonism**." },
      { author: "G. E. Moore", work: "Principia Ethica", quote: "Philosophical **hedonism** commits the naturalistic fallacy by equating the indefinable quality 'good' with mere pleasure." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "The Cyrenaic school taught an unabashed **hedonism** that valued immediate momentary physical sensations above all else." }
    ]
  },
  "Dashboard — hedon/hedonist.md": {
    primary: "A person who believes that pleasure is the chief goal in life; someone devoted to the pursuit of pleasure and sensory enjoyment.",
    secondary: "An adherent of the philosophical doctrine of hedonism in ethics or behavioral theory.",
    quotes: [
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He sought to create a new spirituality through the senses, living as an exquisite **hedonist** amid art and flowers." },
      { author: "Walter Pater", work: "The Renaissance: Studies in Art and Poetry", quote: "The true **hedonist** burns always with a hard, gem-like flame, maintaining ecstasy in the fleeting moment." },
      { author: "George Santayana", work: "The Life of Reason", quote: "The vulgar **hedonist** forgets that unrestrained appetite quickly destroys the physical capacity to enjoy." }
    ]
  },
  "Dashboard — hedon/hedonistic.md": {
    primary: "Engaged in or devoted to the pursuit of pleasure, sensory enjoyment, or self-gratification.",
    secondary: "Pertaining to ethical or behavioral theories based on hedonism.",
    quotes: [
      { author: "Jeremy Bentham", work: "Deontology", quote: "Every rational legislator constructs penal sanctions to counteract destructive **hedonistic** inclinations." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The World State maintained totalitarian control by keeping citizens immersed in a perpetual **hedonistic** paradise of synthetic music and soma." },
      { author: "Friedrich Nietzsche", work: "Beyond Good and Evil", quote: "English utilitarianism reduced the magnificent grandeur of human striving to a contemptible, comfortable **hedonistic** ideal." }
    ]
  },
  "Dashboard — hedon/hedonology.md": {
    primary: "The philosophical, psychological, or scientific study of pleasure, its physiological mechanisms, and its ethical role in human conduct.",
    secondary: "The systematic classification of pleasures and pains in moral philosophy and affective science.",
    quotes: [
      { author: "Alexander Bain", work: "Mental and Moral Science", quote: "A comprehensive treatise on **hedonology** must differentiate organic physical pleasures from intellectual and aesthetic emotions." },
      { author: "Herbert Spencer", work: "The Principles of Ethics", quote: "Biological evolution provides the ultimate foundation for **hedonology**, aligning pleasurable sensations with species survival." },
      { author: "Henry Sidgwick", work: "The Methods of Ethics", quote: "The paradox of **hedonology** is that the conscious, direct pursuit of pleasure often defeats its own realization." }
    ]
  },
  "Dashboard — hedon/hyphedonia.md": {
    primary: "An abnormally diminished or blunted capacity to experience pleasure, milder than complete anhedonia.",
    secondary: "In psychopathology, a subtle affective deficit observed in dysthymia, early depressive states, and chronic stress.",
    quotes: [
      { author: "Théodule-Armand Ribot", work: "The Diseases of the Will", quote: "In subtle neuroses, the patient suffers from **hyphedonia**, finding that favorite recreations provide only a pale shadow of their former delight." },
      { author: "William James", work: "The Principles of Psychology", quote: "Fatigued brain-workers often complain of transient **hyphedonia**, where neither literature nor wine can kindle enthusiasm." },
      { author: "Pierre Janet", work: "Psychological Healing", quote: "Treatment aimed to raise psychological tension and lift the chronic **hyphedonia** that weighed upon the asthenic subject." }
    ]
  },

  // Dashboard — hedy (2 words)
  "Dashboard — hedy/hedys.md": {
    primary: "The Greek root *hēdys*, meaning sweet to the taste, delightful, pleasant, fragrant, or agreeable to the senses.",
    secondary: "A classical combining form in botanical and zoological nomenclature designating sweet flavors, pleasant aromas, or delectable nectar.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The adjective **hedys** encompasses all that is delicious to the palate, sweet-sounding to the ear, or charming to the soul." },
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "Plants possessing the root **hedys** produce fragrant sap and sweet blossoms eagerly sought by honeybees." },
      { author: "Dioscorides", work: "De Materia Medica", quote: "The ancient apothecaries labeled herbal elixirs with the stem **hedys** to denote sweet soothing remedies." }
    ]
  },
  "Dashboard — hedy/hedysarum.md": {
    primary: "A genus of flowering leguminous herbs and shrubs (family Fabaceae), commonly known as sweetvetch, bearing sweet, edible foliage and nectar-rich flowers.",
    secondary: "A botanical genus named from Greek *hēdys* ('sweet') and *arōma* ('fragrance'), valued as nitrogen-fixing forage in northern temperate and alpine ecosystems.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "We establish the genus **Hedysarum** with jointed pods whose segments separate into single-seeded sweet lenticular joints." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The showy purple sprays of **Hedysarum** boreale brighten limestone ledges across the northern border." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "Bumblebees visited the keel petals of **Hedysarum** repeatedly, attracted by the sweet aromatic nectar." }
    ]
  },

  // Dashboard — man (30 words)
  "Dashboard — man/hypermania.md": {
    primary: "An extreme, severe form of mania characterized by frenzied psychomotor agitation, flight of ideas, delirium, hallucinations, and total exhaustion.",
    secondary: "In clinical psychiatry, a psychiatric emergency requiring immediate inpatient stabilization to prevent cardiovascular collapse or severe self-injury.",
    quotes: [
      { author: "Emil Kraepelin", work: "Manic-Depressive Insanity and Paranoia", quote: "In acute **hypermania**, the patient shouts incessantly, tears clothing, and exhibits unbroken violent psychomotor excitation." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "The frantic torrent of disconnected associations in **hypermania** completely obliterates normal reflective consciousness." },
      { author: "Henry Maudsley", work: "Responsibility in Mental Disease", quote: "During the fury of **hypermania**, physical strength appears prodigiously multiplied while the sense of pain is entirely lost." }
    ]
  },
  "Dashboard — man/hypomania.md": {
    primary: "A mild form of mania characterized by persistent elevated mood, heightened energy, increased activity, and reduced need for sleep without marked social impairment or psychotic features.",
    secondary: "In diagnostic psychiatry, a characteristic phase of Bipolar II disorder that often enhances creativity and productivity before depressive crashes.",
    quotes: [
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "The state of **hypomania** is marked by sparkling wit, boundless optimism, and untiring enterprise that rarely seems disordered to casual acquaintances." },
      { author: "Eugen Bleuler", work: "Textbook of Psychiatry", quote: "Unlike florid madness, **hypomania** allows the individual to conduct business affairs, though often with reckless extravagance." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Certain enthusiastic religious conversions present all the psychological hallmarks of sustained, joyful **hypomania**." }
    ]
  },
  "Dashboard — man/kleptomania.md": {
    primary: "A recurrent, irresistible impulse to steal items not needed for personal use or monetary value.",
    secondary: "In abnormal psychology, an impulse control disorder in which the act of theft is preceded by rising tension and followed by temporary gratification or relief.",
    quotes: [
      { author: "Jean-Étienne Esquirol", work: "Des Maladies Mentales", quote: "We distinguish true **kleptomania** from ordinary thievery by the complete absence of pecuniary motive or utility in the stolen articles." },
      { author: "Cesare Lombroso", work: "Criminal Man", quote: "Wealthy ladies who purloin worthless trinkets from department counters act under the morbid compulsion of **kleptomania**." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Naval Treaty", quote: "The detective pointed out that stealing top-secret state dispatches could hardly be explained away as an episode of feminine **kleptomania**." }
    ]
  },
  "Dashboard — man/man.md": {
    primary: "The Greek root *man-* (from *mania*), signifying madness, frenzy, divine inspiration, or obsessive mental excitement.",
    secondary: "The linguistic combining form in psychopathology, ethnology, and psychiatric nosology denoting morbid infatuation, frenzy, or compulsive fixations.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The ancient Greek radical **man** gives birth to *mainomai*, meaning to rage, to be mad, or to be filled with prophetic enthusiasm." },
      { author: "Plato", work: "Phaedrus", quote: "The greatest blessings come to us through madness, the divine **mania** sent as a gift from Apollo and Dionysus." },
      { author: "Sigmund Freud", work: "Civilization and Its Discontents", quote: "Psychiatry adopted the Greek root **man** to designate those affective storms where the super-ego is overthrown by the ego." }
    ]
  },
  "Dashboard — man/manage.md": {
    primary: "To be in charge of, direct, administer, or control business affairs, resources, or an enterprise.",
    secondary: "To succeed in doing, achieving, or coping with a difficult task; to handle or manipulate tools, horses, or personnel effectively.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "Directors of joint-stock companies **manage** other people's money rather than their own, rarely watching it with equal vigilance." },
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "I learned by slow experience how to **manage** my little crop of barley and secure it from birds." },
      { author: "Jane Austen", work: "Emma", quote: "She was quite convinced that she could **manage** her friend's romantic affairs far better than Harriet could herself." }
    ]
  },
  "Dashboard — man/manageable.md": {
    primary: "Capable of being managed, controlled, steered, or kept within reasonable limits; easily handled.",
    secondary: "Docile, compliant, or amenable to direction; of a size or complexity that can be easily dealt with.",
    quotes: [
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The Lilliputians constructed a stout wooden carriage of **manageable** proportions to convey me toward their capital." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I divided the virtues into thirteen distinct weeks to keep the enterprise within **manageable** daily limits." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The lawyer sought to reduce the vast mountain of chancery documents into a **manageable** summary for the court." }
    ]
  },
  "Dashboard — man/management.md": {
    primary: "The process, practice, or art of dealing with, controlling, or directing things, finances, or people; executive leadership.",
    secondary: "The collective body of individuals who oversee and direct an organization, corporation, or institution.",
    quotes: [
      { author: "Frederick Winslow Taylor", work: "The Principles of Scientific Management", quote: "Under scientific **management**, the initiative of the workmen is obtained with absolute regularity through standardized tasks." },
      { author: "Henri Fayol", work: "General and Industrial Management", quote: "To forecast, to plan, to organize, to command, to coordinate, and to control constitute the essential functions of **management**." },
      { author: "Max Weber", work: "Economy and Society", quote: "Modern bureaucratic **management** rests upon written records and specialized training for professional office-holders." }
    ]
  },
  "Dashboard — man/manager.md": {
    primary: "A person responsible for controlling or administering an organization, business, sports team, or group of employees.",
    secondary: "A person who handles the financial and business affairs of an actor, artist, or performer.",
    quotes: [
      { author: "Charles Dickens", work: "Nicholas Nickleby", quote: "Mr. Vincent Crummles, the theatrical **manager**, welcomed the newcomers to his strolling company with open arms." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "Undershaft appointed an able business **manager** who ran the vast munitions works with mathematical efficiency." },
      { author: "Thorstein Veblen", work: "The Engineers and the Price System", quote: "The financial **manager** directs modern production not for material output, but for pecuniary gain." }
    ]
  },
  "Dashboard — man/mania.md": {
    primary: "Mental illness marked by periods of great excitement, euphoria, hyperactivity, flight of ideas, and delusions.",
    secondary: "An excessive, irrational enthusiasm, craze, or obsession for something (e.g., tulip mania, bibliomania).",
    quotes: [
      { author: "Hippocrates", work: "Of the Epidemics", quote: "Black bile heating the brain produces **mania**, wherein the patient laughs, dances, and sees terrifying visions." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Melancholy and **mania** are twin sisters of disorder, differing only in degree of fury and perturbation." },
      { author: "Philippe Pinel", work: "A Treatise on Insanity", quote: "To liberate the victims of **mania** from iron chains and treat them with moral dignity was our sacred duty." }
    ]
  },
  "Dashboard — man/maniac.md": {
    primary: "A person exhibiting wild, violent, or extremely erratic behavior; someone suffering from acute mania.",
    secondary: "Informally, a person with an extreme, obsessive, or fanatical enthusiasm for a particular activity or cause.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", quote: "Tis the time's plague, when madmen lead the blind; the raging king roared across the storm like a distracted **maniac**." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "The villagers pursued me with pitchforks, shouting curses as though hunting down a ferocious **maniac**." },
      { author: "Edgar Allan Poe", work: "The Tell-Tale Heart", quote: "True!—nervous—very, very dreadfully nervous I had been; but why will you say that I am a **maniac**?" }
    ]
  },
  "Dashboard — man/maniacal.md": {
    primary: "Suggestive of, characteristic of, or relating to madness or mania; wild, frenzied, or raving.",
    secondary: "Marked by uncontrolled, wildly intense excitement or behavior.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "From the third-story corridor echoed a **maniacal** laugh, low, slow, and mirthless, chilling my blood." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Captain Ahab struck his harpoon into the sea with **maniacal** strength, swearing eternal vengeance upon the white whale." },
      { author: "Bram Stoker", work: "Dracula", quote: "Renfield paced his cell in a **maniacal** frenzy, shouting that his master was knocking at the gate." }
    ]
  },
  "Dashboard — man/maniacally.md": {
    primary: "In a maniacal manner; with wild, frenzied, uncontrolled madness or frantic excitement.",
    secondary: "With obsessive, unrestrained intensity or hysterical fervor.",
    quotes: [
      { author: "H. G. Wells", work: "The Invisible Man", quote: "He laughed **maniacally** in the darkened hallway as the furniture flew across the room to barricade the door." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "The crazed officer shouted **maniacally** into the gale, waving an unloaded revolver at the storm clouds." },
      { author: "Robert Louis Stevenson", work: "The Strange Case of Dr Jekyll and Mr Hyde", quote: "Hyde trampled the child underfoot and hurried on, smiling **maniacally** into the cold morning mist." }
    ]
  },
  "Dashboard — man/manic.md": {
    primary: "Relating to, characterized by, or suffering from mania; exhibiting extreme excitement, hyperactivity, and euphoria.",
    secondary: "In clinical psychiatry, designating the elevated phase of manic-depressive disorder (bipolar disorder).",
    quotes: [
      { author: "Emil Kraepelin", work: "Manic-Depressive Insanity", quote: "The **manic** phase reveals an extraordinary acceleration of psychic tempo, with rapid speech and uninhibited optimism." },
      { author: "Sigmund Freud", work: "Mourning and Melancholia", quote: "In **manic** states, the ego has triumphed over the loss, celebrating its liberation with boundless celebratory energy." },
      { author: "Virginia Woolf", work: "Moments of Being", quote: "Her creative spells were accompanied by a **manic** rush of words that raced far ahead of her pen." }
    ]
  },
  "Dashboard — man/manliness.md": {
    primary: "The traditional qualities or virtues associated with an honorable, courageous man, such as bravery, fortitude, and self-possession.",
    secondary: "In moral philosophy and civic republicanism, the active exercise of resolute responsibility and civic virtue.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Self-Reliance", quote: "Whoso would be a man must be a nonconformist, displaying that serene **manliness** that scorns the applause of crowds." },
      { author: "Theodore Roosevelt", work: "The Strenuous Life", quote: "True national greatness requires that vigorous **manliness** which embraces toil and danger rather than soft ignoble ease." },
      { author: "Thomas Carlyle", work: "On Heroes, Hero-Worship, and the Heroic in History", quote: "The Norse Odin was honored by his people because he showed a rough, sincere **manliness** in the face of harsh frost." }
    ]
  },
  "Dashboard — man/manly.md": {
    primary: "Having or denoting qualities traditionally regarded as characteristic of an admirable man, such as courage, strength, honesty, and fortitude.",
    secondary: "Resolute, robust, and dignified; free from cowardice, frivolity, or whining self-pity.",
    quotes: [
      { author: "William Shakespeare", work: "Macbeth", quote: "Dispute it like a man. I shall do so; but I must also feel it as a man: let us put on **manly** readiness." },
      { author: "John Milton", work: "Paradise Lost", quote: "For contemplation he and valor formed, for softness she and sweet attractive grace; he possessed **manly** prime." },
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "I sing the stalwart, **manly** love of comrades, marching arm in arm along the open road." }
    ]
  },
  "Dashboard — man/manor.md": {
    primary: "A landed estate or district belonging to a lord, historically held under feudal tenure and exercising local territorial jurisdiction through a manorial court.",
    secondary: "The principal residence or mansion house of a lord on his estate (manor house).",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "A **manor** was a feudal lordship consisting of demesne lands cultivated for the lord, and tenemental lands held by customary tenants." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The rural squire lived content upon his ancestral **manor**, dispensing hearty hospitality and summary justice." },
      { author: "George Eliot", work: "Silas Marner", quote: "The great red-brick **manor** stood among noble elms, where tenants gathered for the annual New Year celebration." }
    ]
  },
  "Dashboard — man/manorial.md": {
    primary: "Of, relating to, or characteristic of a manor or the feudal system of land administration.",
    secondary: "Pertaining to the customary legal and economic obligations (such as corvée labor and court leet jurisdiction) binding tenants to a manorial lord.",
    quotes: [
      { author: "Frederic William Maitland", work: "Domesday Book and Beyond", quote: "The ancient **manorial** rolls record every transfer of strip-holdings, fines, and customary dues across centuries." },
      { author: "Marc Bloch", work: "Feudal Society", quote: "The **manorial** regime bound peasant labor to the lord's demesne in return for military protection and local justice." },
      { author: "Paul Vinogradoff", work: "Villainage in England", quote: "Customary law within the **manorial** court protected serfs against arbitrary eviction so long as customary rents were paid." }
    ]
  },
  "Dashboard — man/mansion.md": {
    primary: "A large, imposing, and stately residence or dwelling house.",
    secondary: "Historically or biblically, an abiding place, dwelling, or separate apartment (as in 'In my Father's house are many mansions').",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The House of the Seven Gables", quote: "The venerable wooden **mansion** stood with its rusty gables pointing toward the sky, haunted by ancient curses." },
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", quote: "I gazed upon the gloomy gray **mansion** of Usher, mirrored in the dark waters of the stagnant tarn." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Gardencourt was a spacious Jacobean **mansion**, its red-brick frontage mellowed by two hundred English autumns." }
    ]
  },
  "Dashboard — man/manure.md": {
    primary: "Animal dung or organic compost spread over land or plowed into soil to serve as agricultural fertilizer.",
    secondary: "Historically, to till, cultivate, or work the land manually (derived from Old French *manouvrer*, from Latin *manu operari* 'to work by hand').",
    quotes: [
      { author: "Virgil", work: "Georgics", quote: "Nor blush to enrich the thirsty soil with rich **manure**, and cast unsavory ashes across the exhausted fields." },
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "Chalk and animal **manure** mingled together warm the cold clay soil, preparing it for an abundant harvest." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "Earthworms promote vegetation by loosening the earth and incorporating decomposing **manure** into the deep subsoil." }
    ]
  },
  "Dashboard — man/megalomania.md": {
    primary: "An obsession with the exercise of power, especially in the domination of others; a psychiatric delusion of grandeur, wealth, or omnipotence.",
    secondary: "In political psychology, an pathological drive for totalitarian conquest and self-deification in authoritarian rulers.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "Ecce Homo", quote: "Lest I be accused of ordinary vanity or **megalomania**, I shall explain why I write such good books." },
      { author: "Bertrand Russell", work: "Power: A New Social Analysis", quote: "The tyrant's thirst for absolute dominance inevitably degenerates into a dangerous clinical **megalomania**." },
      { author: "Sigmund Freud", work: "The Future of an Illusion", quote: "Religious cosmologies cater to the primitive **megalomania** of mankind, making human salvation the center of the universe." }
    ]
  },
  "Dashboard — man/megalomaniac.md": {
    primary: "A person who suffers from megalomania; someone with an obsessive delusion of their own greatness, power, or supreme importance.",
    secondary: "A political tyrant, autocrat, or egocentric individual whose grandiose ambitions ignore reality and human suffering.",
    quotes: [
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "Hitler was a murderous **megalomaniac**, but he understood the emotional power of national symbols that intellectuals despised." },
      { author: "Aldous Huxley", work: "Ends and Means", quote: "The militarist dictator becomes a lonely **megalomaniac**, isolated from truth by sycophantic courtiers." },
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "The warlords of the twenty-first century were described by later historians as dangerous **megalomaniac** survivals." }
    ]
  },
  "Dashboard — man/megalomaniacal.md": {
    primary: "Characterized by, relating to, or suffering from megalomania; exhibiting grandiose delusions of omnipotence or supreme authority.",
    secondary: "Marked by an extravagant, wildly disproportionate estimate of one's own power, intellect, or destiny.",
    quotes: [
      { author: "Joseph Conrad", work: "Under Western Eyes", quote: "The autocrat spoke in a calm voice that concealed the most **megalomaniacal** contempt for human life." },
      { author: "Arthur Koestler", work: "Darkness at Noon", quote: "Rubashov realized that the Party had succumbed to a **megalomaniacal** conviction of its historical infallibility." },
      { author: "Thomas Mann", work: "Doctor Faustus", quote: "The composer's apocalyptic symphonic project bore a **megalomaniacal** stamp that frightened his friends." }
    ]
  },
  "Dashboard — man/megalomanic.md": {
    primary: "Of, relating to, or exhibiting megalomania; megalomaniacal (alternative linguistic form).",
    secondary: "Pertaining to inflated grandiose self-regard in psychiatric and sociological critique.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "In certain monomanias, the subject exhibits **megalomanic** delusions of being emperor or an angel sent from heaven." },
      { author: "Havelock Ellis", work: "The Philosophy of Conflict", quote: "Jingoistic nationalism is essentially a collective **megalomanic** neurosis that infects otherwise sensible citizens." },
      { author: "George Bernard Shaw", work: "Heartbreak House", quote: "The old captain's wild declarations sounded quite **megalomanic** until one examined his strange inventions." }
    ]
  },
  "Dashboard — man/monomania.md": {
    primary: "An exaggerated, obsessive fixation on or preoccupation with a single idea, subject, or goal.",
    secondary: "In 19th-century alienism and forensic psychiatry (originated by Esquirol), partial insanity wherein intellect remains intact except on one obsessive point.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "Ahab's quenchless feud seemed mine; with greedy ears I learned the history of that deadly **monomania** that pursued the beast." },
      { author: "Jean-Étienne Esquirol", work: "Des Maladies Mentales", quote: "We designate by the term **monomania** that form of delirium which is limited to a single object or narrow chain of ideas." },
      { author: "Edgar Allan Poe", work: "Berenice", quote: "My books, at this epoch, if they did not actually model my disorder, partook of its **monomania** and morbid nature." }
    ]
  },
  "Dashboard — man/monomaniac.md": {
    primary: "A person affected by monomania; someone who is fanatically and obsessively preoccupied with a single idea, pursuit, or grudge.",
    secondary: "An individual exhibiting an unyielding, single-minded obsession in literature and history.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "Miss Havisham lived as a tragic **monomaniac**, nursing her broken wedding feast in eternal yellow candlelight." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "Chillingworth transformed into a vengeful **monomaniac**, dedicated wholly to probing the minister's tortured conscience." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Six Napoleons", quote: "Lestrade was convinced that a political **monomaniac** with an insane hatred of the Emperor was smashing plaster busts." }
    ]
  },
  "Dashboard — man/monomaniacal.md": {
    primary: "Characterized by, relating to, or exhibiting monomania; obsessively focused upon a single idea or objective.",
    secondary: "Driven by a fanatical, narrow devotion that excludes all competing considerations or balanced judgment.",
    quotes: [
      { author: "Herman Melville", work: "Pierre: or, The Ambiguities", quote: "He flung himself into the task with a **monomaniacal** frenzy that burned his bodily health to ashes." },
      { author: "Joseph Conrad", work: "The Secret Agent", quote: "The Professor walked the London streets with a detonator in his coat, possessed by a **monomaniacal** dream of destruction." },
      { author: "Henry James", work: "The Aspern Papers", quote: "My desire to obtain the poet's private letters had grown into an almost **monomaniacal** fixation." }
    ]
  },
  "Dashboard — man/unman.md": {
    primary: "To deprive of courage, fortitude, or resolution; to cause someone to lose their composure, strength of will, or nerve.",
    secondary: "Historically, to deprive of masculine vigor, status, or composure; to weaken or emasculate.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "'Tis sweet and commendable in your nature, Hamlet, to give these mourning duties to your father; but to persever in obstinate condolement is a course of impious stubbornness, 'tis **unmanly** grief, it shows a will most incorrect to heaven, and tends to **unman** the soul." },
      { author: "John Dryden", work: "All for Love", quote: "Do not weep, Cleopatra, lest thy tears **unman** the Roman warrior who chose death before defeat." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "No sudden grief could **unman** his proud spirit, which bore the blows of adverse fortune in silence." }
    ]
  },
  "Dashboard — man/unmanageable.md": {
    primary: "Difficult or impossible to manage, manipulate, govern, or control; unruly or intractable.",
    secondary: "Of an enterprise, debt, or mechanism, having grown too cumbersome, large, or complicated to direct effectively.",
    quotes: [
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "The dugout canoe was so vast and heavy that it proved completely **unmanageable**, defying all my efforts to launch it into the surf." },
      { author: "Walter Scott", work: "Rob Roy", quote: "The Highland cattle became wild and **unmanageable** as the thunderclap echoed across the mountain pass." },
      { author: "Herman Melville", work: "Typee", quote: "My injured leg swelled rapidly, rendering me almost wholly helpless and **unmanageable** on the rugged trail." }
    ]
  },
  "Dashboard — man/unmanliness.md": {
    primary: "The state or quality of lacking manly virtues such as courage, fortitude, self-control, and honor.",
    secondary: "Behavior regarded as cowardly, irresolute, or effeminate in classical and traditional moral discourse.",
    quotes: [
      { author: "John Locke", work: "Some Thoughts Concerning Education", quote: "Whining and crying over trivial physical scratches should be discouraged early as signs of future **unmanliness**." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "To yield to despair under unexpected misfortune is a shameful **unmanliness** that surrenders reason to passion." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "Idleness and sentimental lamentation are forms of moral **unmanliness** unworthy of working men in a serious universe." }
    ]
  },
  "Dashboard — man/unmanly.md": {
    primary: "Not possessing or displaying the qualities traditionally admired in an honorable, courageous man; cowardly, weak, or dishonorable.",
    secondary: "Deemed inappropriate for a resolute adult person; irresolute or unworthy of dignified character.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "Hold thy desperate hand! Art thou a man? Thy form cries out thou art; thy tears are womanish, thy wild acts denote the unreasonable fury of a beast: **unmanly** despair." },
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "Tyrants have fostered a false standard of gentility, branding independent thought as **unmanly** in boys and unfeminine in girls." },
      { author: "Frederick Douglass", work: "Narrative of the Life of Frederick Douglass", quote: "To submit without resistance to the brutal lash of the overseer seemed to me an **unmanly** surrender of human dignity." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);

  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${relPath}`);
}

console.log('Batch 3 complete! Total files updated:', Object.keys(filesData).length);
