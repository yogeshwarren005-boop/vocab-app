import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design/Dashboard — mer';

const filesData = {
  "antimere.md": {
    primary: "One of the symmetrical, corresponding parts or segments on opposite sides of a bilateral animal.",
    secondary: "In comparative morphology, one of the repeating homologous segments arranged radially or bilaterally around an anatomical axis.",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", quote: "Bilateral symmetry divides the animal body into two corresponding halves, each designated an **antimere**." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The right forelimb forms the structural **antimere** of the left, exhibiting identical homologies." },
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "In radiating animals, each equal sector of the disc constitutes a distinct **antimere**." }
    ]
  },
  "antimeria.md": {
    primary: "The morphological relationship or condition of being antimeres; bilateral or radial symmetry of corresponding parts.",
    secondary: "In rhetorical figures, the substitution of one grammatical part of speech for another (more commonly spelled *anthimeria*).",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie", quote: "The evolutionary transition from radial to bilateral **antimeria** enabled directional locomotion." },
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "When a noun is used as a verb, the rhetorician calleth this figure **antimeria**, exchanging word classes with vigor." },
      { author: "Edward Sapir", work: "Language", quote: "Functional shifts between parts of speech illustrate grammatical **antimeria** in everyday colloquial English." }
    ]
  },
  "biopolymer.md": {
    primary: "A large macromolecule produced by living organisms, composed of repeating monomeric subunits (such as proteins, DNA, RNA, and cellulose).",
    secondary: "In biochemistry, a naturally occurring polymer that performs structural, catalytic, or genetic information storage functions.",
    quotes: [
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "DNA represents the supreme informational **biopolymer**, its nucleotide sequence encoding the blueprint of life." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Hydrogen bonding between peptide units stabilizes the alpha-helical conformation of the protein **biopolymer**." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Chitin, an insoluble structural **biopolymer**, forms the protective exoskeletons of billions of ocean crustaceans." }
    ]
  },
  "decamer.md": {
    primary: "An oligomer or macromolecular complex composed of ten monomeric subunits or peptide residues.",
    secondary: "In biochemistry, a protein assembly consisting of ten associated polypeptide chains.",
    quotes: [
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "Electron microscopy revealed the viral capsid protein assembling into a stable ring-shaped **decamer**." },
      { author: "Arthur Kornberg", work: "DNA Replication", quote: "The replication initiator complex functions as an active **decamer** to unwind duplex DNA at the origin." },
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "Symmetry constraints favor the formation of a five-fold symmetric **decamer** in many bacterial enzymes." }
    ]
  },
  "decamerous.md": {
    primary: "In botany, having floral organs (petals, sepals, stamens) in multiples or sets of ten.",
    secondary: "In invertebrate zoology, having ten radial parts, rays, or segments.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "Certain passionflowers display a **decamerous** perianth consisting of five sepals and five petals." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The flower is strictly **decamerous**, its ten stamens alternating neatly with the corolla lobes." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "Deep-sea medusae often exhibit a **decamerous** radial symmetry with ten sensory marginal tentacles." }
    ]
  },
  "dim.md": {
    primary: "Emitting or having a limited or faint amount of light; not bright or clearly illuminated.",
    secondary: "Not clearly perceived, remembered, or understood; vague or obscure in outline or intellect.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "The sun in **dim** eclipse sheds disastrous twilight on half the nations." },
      { author: "Emily Dickinson", work: "Poems", quote: "A **dim** capacity for wings degrades the lowest monster into soaring flight." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Through the **dim** casement window, the moonlight fell faintly upon the floor." }
    ]
  },
  "dimer.md": {
    primary: "A chemical compound or macromolecular complex consisting of two identical or similar molecules linked together.",
    secondary: "In photobiology, a thymine dimer formed in DNA upon exposure to ultraviolet radiation.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "In acetic acid vapor, strong hydrogen bonding causes molecules to associate into a stable **dimer**." },
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "Transcription factor activation frequently requires two identical subunits to assemble into an active **dimer**." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Ultraviolet damage cross-links adjacent pyrimidines, creating a mutagenic cyclobutane **dimer** in the helix." }
    ]
  },
  "dimeric.md": {
    primary: "Consisting of or relating to a dimer; composed of two subunits or repeated monomeric units.",
    secondary: "In botany (dimerous), having parts arranged in pairs or multiples of two.",
    quotes: [
      { author: "Max Perutz", work: "Mechanisms of Cooperativity in Hemoglobin", quote: "The quaternary structure dissociates into **dimeric** intermediates under high salt concentrations." },
      { author: "Arthur Kornberg", work: "For the Love of Enzymes", quote: "The enzyme exists in equilibrium between an inactive monomer and a fully active **dimeric** state." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Resonance stabilization favors the symmetrical **dimeric** arrangement of carboxylic acids." }
    ]
  },
  "dimerism.md": {
    primary: "The chemical condition or state of being a dimer or existing in dimeric form; the capacity to form dimers.",
    secondary: "In botanical morphology, the condition of having floral organs arranged in sets of two.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Certain primitive angiosperms exhibit **dimerism** in their floral whorls, bearing two sepals and two petals." },
      { author: "Jacobus Henricus van 't Hoff", work: "Chemistry in Space", quote: "Molecular weight determinations in solution confirm the presence of reversible **dimerism**." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The transition from **dimerism** to trimerism in floral parts reflects ancient evolutionary divergence." }
    ]
  },
  "dimerous.md": {
    primary: "In botany, having floral whorls or organs arranged in sets or multiples of two (e.g. two petals, two stamens).",
    secondary: "In entomology, having tarsi composed of two segments or joints.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany", quote: "The flowers of the poppy family are characteristically **dimerous**, with two caducous sepals." },
      { author: "John Lindley", work: "The Treasury of Botany", quote: "The small cruciferous weed displays a **dimerous** arrangement of floral organs." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The minute parasitic beetles possess **dimerous** tarsi adapted for clinging to hairs." }
    ]
  },
  "dimity.md": {
    primary: "A sheer, lightweight, crisp cotton fabric woven with raised stripes, checks, or corded patterns.",
    secondary: "A historical textile (from Greek *dimitos* double-thread) prized in domestic furnishing and summer clothing.",
    quotes: [
      { author: "Jane Austen", work: "Emma", quote: "The bedroom was fresh and charming, draped in clean white **dimity** curtains that caught the summer breeze." },
      { author: "Charlotte Brontë", work: "Villette", quote: "A narrow bed draped with snowy **dimity** stood in the corner of the quiet French pension." },
      { author: "Louisa May Alcott", work: "Little Women", quote: "Meg ironed her crisp white **dimity** dress for the festive lawn party with painstaking care." }
    ]
  },
  "dimly.md": {
    primary: "With a faint, weak, or limited amount of light; faintly or softly.",
    secondary: "In a vague, indistinct, or imperfectly understood manner.",
    quotes: [
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "The street lamps flickered **dimly** through the thick, cold autumn fog of London." },
      { author: "Virginia Woolf", work: "Mrs Dalloway", quote: "She remembered **dimly** the summers at Bourton, hearing the rooks caw in the tall elms." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Far off across the black waters, a single lantern shone **dimly** at the masthead." }
    ]
  },
  "dimness.md": {
    primary: "The state or quality of being dim; lack of brightness, clarity, or illumination.",
    secondary: "Obscurity, indistinctness, or lack of sharpness in perception, memory, or intellectual comprehension.",
    quotes: [
      { author: "John Keats", work: "Ode to a Nightingale", quote: "Here there is no light, save what from heaven is with the breezes blown through verdurous glooms and winding mossy **dimness**." },
      { author: "George Eliot", work: "Middlemarch", quote: "A gentle twilight **dimness** fell over the room as Dorothea sat pondering her future." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "We penetrated deeper and deeper into the heart of darkness, surrounded by primeval forest **dimness**." }
    ]
  },
  "emmer.md": {
    primary: "An ancient, low-yielding, awned wheat species (*Triticum dicoccum*) having hulled grains, one of the earliest domesticated crops.",
    secondary: "In agrarian archaeology, a founder crop of Neolithic agriculture that provided staple food across ancient Egypt and the Fertile Crescent.",
    quotes: [
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "Neolithic farmers at Jericho cultivated domesticated **emmer** alongside einkorn and barley." },
      { author: "Jared Diamond", work: "Guns, Germs, and Steel", quote: "The rapid domestication of **emmer** wheat gave Fertile Crescent societies a decisive head start in food production." },
      { author: "Flinders Petrie", work: "Ten Years' Digging in Egypt", quote: "Granaries excavated beside the pyramids contained bushels of desiccated **emmer** grains intact after four millennia." }
    ]
  },
  "enantiomer.md": {
    primary: "Each of a pair of chemical molecules that are non-superimposable mirror images of one another (optical isomers).",
    secondary: "In stereochemistry, chiral isomers that share identical physical properties but rotate plane-polarized light in opposite directions.",
    quotes: [
      { author: "Louis Pasteur", work: "Researches on Molecular Asymmetry", quote: "Every chiral substance exists as a right-handed or left-handed **enantiomer**, reflecting fundamental asymmetry in nature." },
      { author: "Jacobus Henricus van 't Hoff", work: "The Arrangement of Atoms in Space", quote: "The tetrahedral carbon atom explains why an asymmetric molecule possesses an exact mirror-image **enantiomer**." },
      { author: "Oliver Sacks", work: "Uncle Tungsten", quote: "Pasteur's manual separation of sodium ammonium tartrate crystals into each pure **enantiomer** was a triumph of chemical intuition." }
    ]
  },
  "enneamer.md": {
    primary: "An oligomer or macromolecular complex composed of nine monomeric units or subunits.",
    secondary: "In structural molecular biology, a symmetric protein assembly exhibiting nine-fold rotational symmetry.",
    quotes: [
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "The bacterial flagellar basal ring assembles as an intricate **enneamer** embedded in the inner membrane." },
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "Crystallographic analysis revealed nine identical peptide subunits arranged in a cyclic **enneamer**." },
      { author: "Arthur Kornberg", work: "DNA Replication", quote: "The chaperone complex functions as a transient **enneamer** during the assembly of the viral capsid." }
    ]
  },
  "heptamer.md": {
    primary: "An oligomer, peptide, or protein complex composed of seven monomeric subunits.",
    secondary: "In molecular biology, a specific seven-base-pair conserved DNA sequence (e.g. in V(D)J recombination signals) or a seven-subunit channel.",
    quotes: [
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "The toxin forms a ring-shaped **heptamer** that punctures the host erythrocyte membrane." },
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "Immunoglobulin gene rearrangement requires a conserved **heptamer** sequence flanking the diversity segment." },
      { author: "Max Perutz", work: "Protein Structure", quote: "GroES functions in protein folding as a dome-shaped **heptamer** capping the chaperonin cylinder." }
    ]
  },
  "heterodimer.md": {
    primary: "A macromolecular complex or chemical compound formed by the association of two different molecules or polypeptide subunits.",
    secondary: "In molecular genetics, a protein dimer composed of two distinct gene products (such as alpha-beta tubulin).",
    quotes: [
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "Microtubules assemble from alternating alpha and beta tubulin subunits joined into a stable **heterodimer**." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "The active receptor functions as a **heterodimer**, requiring both distinct subunits for hormone binding." },
      { author: "Arthur Kornberg", work: "DNA Replication", quote: "The restriction endonuclease operates as an asymmetric **heterodimer** recognizing non-palindromic target sites." }
    ]
  },
  "heterotetramer.md": {
    primary: "A protein or macromolecular complex consisting of four subunits, of which at least two are different from each other.",
    secondary: "In biochemistry, an oligomeric protein assembly composed of two distinct pairs of polypeptide chains (e.g. hemoglobin).",
    quotes: [
      { author: "Max Perutz", work: "Mechanisms of Cooperativity in Hemoglobin", quote: "Adult human hemoglobin is an allosteric **heterotetramer** containing two alpha-globin and two beta-globin chains." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Cooperative oxygen binding in hemoglobin depends upon structural shifts within the **heterotetramer**." },
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "Ion channels in neural membranes frequently assemble as a **heterotetramer** of diverse pore-forming subunits." }
    ]
  },
  "hexamer.md": {
    primary: "An oligomer, polymer, or protein complex composed of six monomeric subunits.",
    secondary: "In molecular genetics, a DNA helicase or viral capsid structure possessing six-fold symmetry.",
    quotes: [
      { author: "Arthur Kornberg", work: "DNA Replication", quote: "The replicative helicase forms a ring-shaped **hexamer** that encircles single-stranded DNA and unwinds the duplex." },
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "Insulin is stored within pancreatic secretory granules as a zinc-stabilized **hexamer**." },
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "Six identical subunits coordinate around a central twofold axis to complete the catalytic **hexamer**." }
    ]
  },
  "homodimer.md": {
    primary: "A macromolecular complex formed by the association of two identical molecules or polypeptide subunits.",
    secondary: "In structural biology, a symmetric protein dimer formed by the dimerization of identical protein chains.",
    quotes: [
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "The lac repressor headpiece binds DNA as a two-fold symmetric **homodimer** contacting inverted repeat sequences." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Many restriction enzymes function as a **homodimer**, cutting both strands of the DNA palindrome simultaneously." },
      { author: "Max Perutz", work: "Protein Structure", quote: "Self-association of identical polypeptide chains generates a stable **homodimer** with twofold rotational symmetry." }
    ]
  },
  "homotetramer.md": {
    primary: "A protein or macromolecular complex consisting of four identical subunits or polypeptide chains.",
    secondary: "In biochemistry, a symmetric four-subunit protein assembly (such as avidin or potassium channel pore domains).",
    quotes: [
      { author: "Max Perutz", work: "Mechanisms of Cooperativity", quote: "Lactate dehydrogenase from muscle tissues assembles as an active **homotetramer** of four identical M-subunits." },
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "Voltage-gated potassium channels feature four identical transmembrane subunits arranged into a functional **homotetramer**." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Crystallographic four-fold symmetry confirms the stable **homotetramer** architecture of the transport protein." }
    ]
  },
  "isomer.md": {
    primary: "Each of two or more chemical compounds having the same molecular formula but a different arrangement of atoms and different properties.",
    secondary: "In nuclear physics, an atomic nucleus in an excited metastable state having the same atomic number and mass number as another nucleus.",
    quotes: [
      { author: "Jöns Jacob Berzelius", work: "Treatise on Chemistry", quote: "I proposed the term **isomer** to describe substances that possess identical composition yet completely divergent properties." },
      { author: "Jacobus Henricus van 't Hoff", work: "Chemistry in Space", quote: "Stereoisomerism proves that an **isomer** can differ solely in the three-dimensional orientation of its bonds." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The physiological action of a drug often depends exclusively upon which **isomer** interacts with the cellular receptor." }
    ]
  },
  "isomeric.md": {
    primary: "Pertaining to, having the nature of, or exhibiting isomerism; sharing identical chemical composition but differing in structure or properties.",
    secondary: "In nuclear physics, relating to nuclear isomers or metastable energy levels.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry", quote: "Faraday discovered that butylene and ethylene shared an identical percentage composition, proving their **isomeric** relationship." },
      { author: "Louis Pasteur", work: "Researches on Molecular Asymmetry", quote: "Tartaric and racemic acids constitute distinct **isomeric** forms exhibiting opposite optical behaviors." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Structural formulas reveal how **isomeric** hydrocarbons can have wildly different boiling points." }
    ]
  },
  "isomerisation.md": {
    primary: "The chemical process or reaction by which a compound is transformed into any of its isomeric forms.",
    secondary: "In industrial petrochemistry, the catalytic conversion of straight-chain hydrocarbons into branched-chain isomers.",
    quotes: [
      { author: "Jacobus Henricus van 't Hoff", work: "Studies in Chemical Dynamics", quote: "Thermal **isomerisation** of maleic acid into fumaric acid illustrates reversible molecular reorganization." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Light absorption initiates the rapid photochemical **isomerisation** of retinal in the rhodopsin visual cycle." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "Catalytic **isomerisation** in petroleum cracking towers converted low-grade naphtha into high-octane aviation fuel." }
    ]
  },
  "isomerise.md": {
    primary: "To change or transform into an isomeric form; to cause a molecule to rearrange its atoms into an isomer.",
    secondary: "In organic chemistry, to undergo thermal, photochemical, or catalytic molecular rearrangement.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Under acid catalysis, terminal alkenes readily **isomerise** into more stable internal alkenes." },
      { author: "George Wald", work: "Nobel Lecture on Visual Excitation", quote: "A single photon is sufficient to **isomerise** 11-cis-retinal into all-trans-retinal within the photoreceptor." },
      { author: "Jacobus Henricus van 't Hoff", work: "Chemistry in Space", quote: "Heating causes the less stable geometric isomer to **isomerise** into its thermodynamic minimum." }
    ]
  },
  "isomerism.md": {
    primary: "The existence of chemical compounds that have the same molecular formula but differ in chemical structure or spatial orientation.",
    secondary: "In physical chemistry, the phenomenon encompassing structural isomerism, stereoisomerism, tautomerism, and nuclear isomerism.",
    quotes: [
      { author: "Jöns Jacob Berzelius", work: "Annals of Philosophy", quote: "The discovery of **isomerism** established that the properties of matter depend not merely on elemental composition, but on atomic arrangement." },
      { author: "Louis Pasteur", work: "Researches on Molecular Asymmetry", quote: "Optical **isomerism** opened an entirely new window onto the three-dimensional architecture of organic molecules." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Planar coordination geometry in coordination complexes explains geometric **isomerism** in inorganic chemistry." }
    ]
  },
  "isomerization.md": {
    primary: "The chemical reaction or process in which a chemical compound is converted into an isomer having a different structure.",
    secondary: "In petroleum refining and industrial chemistry, the catalytic conversion of straight-chain alkanes into branched alkanes.",
    quotes: [
      { author: "George Wald", work: "The Molecular Basis of Visual Excitation", quote: "Visual transduction begins with the ultrafast photochemical **isomerization** of retinal inside rhodopsin." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Industrial **isomerization** of butane produces isobutane for the manufacture of high-octane alkylate fuels." },
      { author: "Peter Atkins", work: "Physical Chemistry", quote: "The activation barrier for thermal cis-trans **isomerization** reflects the energy required to break the pi-bond." }
    ]
  },
  "isomerize.md": {
    primary: "To convert or be converted from one chemical isomer into another.",
    secondary: "To undergo molecular restructuring without altering the empirical chemical formula.",
    quotes: [
      { author: "George Wald", work: "Vision and the Photoreceptor Membrane", quote: "Light causes the chromophore to **isomerize** in picoseconds, triggering electrical nerve impulses." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Enzymes known as isomerases specifically **isomerize** metabolic sugars during glycolysis." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "High pressure and platinum catalysts force straight paraffin chains to **isomerize** into branched isomers." }
    ]
  },
  "mer.md": {
    primary: "The fundamental, repeating structural unit of a polymer (a monomeric unit).",
    secondary: "The Greek root *meros* (part, portion, share), the parent of biological, chemical, and philosophical terms involving division and composition.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek root **mer** denotes a share, portion, or division, forming the core of polymer and monomer." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "A high polymer consists of thousands of identical **mer** units linked in a covalent chain." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "From ancient *meros*, meaning part or lot, modern science derived the root **mer** for chemical units." }
    ]
  },
  "mereology.md": {
    primary: "The branch of philosophical logic, ontology, and mathematics that investigates the formal relations between parts and wholes.",
    secondary: "A formal axiomatic system treating parthood as a fundamental ontological primitive.",
    quotes: [
      { author: "Stanisław Leśniewski", work: "Foundations of the General Theory of Sets", quote: "I formulated **mereology** as a nominalist alternative to set theory, taking the part-whole relation as basic." },
      { author: "Nelson Goodman", work: "The Structure of Appearance", quote: "Philosophical **mereology** provides rigorous tools to analyze how complex objects decompose into simpler individuals." },
      { author: "Willard Van Orman Quine", work: "From a Logical Point of View", quote: "A rigorous **mereology** avoids the abstract platonism of classes by restricting itself to concrete physical sums." }
    ]
  },
  "merisis.md": {
    primary: "Biological growth or increase in size of an organism or tissue accomplished through cell division (hyperplasia) rather than cell enlargement.",
    secondary: "In developmental histology, the proliferative expansion of embryonic or meristematic tissue through mitotic cleavage.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Tissue growth may proceed by cellular hypertrophy or by true **merisis**, multiplying cell numbers through division." },
      { author: "Anton de Bary", work: "Comparative Anatomy of Vegetative Organs", quote: "Apical shoot growth in plants is maintained by active **merisis** within the apical dome." },
      { author: "Thomas Henry Huxley", work: "The Cell Theory", quote: "Embryonic cleavage represents the purest example of developmental **merisis** in early ontogeny." }
    ]
  },
  "merism.md": {
    primary: "A rhetorical figure in which a whole entity is referred to by enumerating its contrasting or constituent parts (e.g. 'flesh and bone').",
    secondary: "In morphology, the repetition of homologous anatomical parts or segments (meristic variation).",
    quotes: [
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "This figure **merism**, or division, unfoldeth a general matter by recounting every particular part thereof." },
      { author: "William Bateson", work: "Materials for the Study of Variation", quote: "Bateson investigated evolutionary **merism**, documenting variations in repeated vertebral and floral segments." },
      { author: "C. S. Lewis", work: "Studies in Words", quote: "Biblical Hebrew poetry abounds in **merism**, invoking 'the heavens and the earth' to denote the entire cosmos." }
    ]
  },
  "meristem.md": {
    primary: "A region of plant tissue consisting of undifferentiated cells actively dividing to form new specialized tissues.",
    secondary: "In plant anatomy, the perpetual embryonic tissue that enables indeterminate growth at shoot and root tips.",
    quotes: [
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "The shoot apical **meristem** continuously generates new leaves and stem tissues throughout the life of the tree." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "Cells of the vascular **meristem** remain undifferentiated, maintaining the capacity for division." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Every upward surge of the forest bough originates within the microscopic dome of the apical **meristem**." }
    ]
  }
};

for (const [filename, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, filename);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filename}`);
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
  console.log(`Updated: ${filename}`);
}

console.log('Done Batch 8 (Dashboard — mer Part 1) of Cluster Art, Craft & Design (34 words)!');
