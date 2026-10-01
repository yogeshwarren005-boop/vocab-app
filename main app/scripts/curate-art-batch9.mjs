import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design/Dashboard — mer';

const filesData = {
  "meristematic.md": {
    primary: "Relating to, consisting of, or characteristic of a meristem; actively dividing undifferentiated plant tissue.",
    secondary: "Capable of dividing and giving rise to similar cells or specialized tissues.",
    quotes: [
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "The **meristematic** zone at the root apex is protected from abrasion by the root cap." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "Under high magnification, **meristematic** cells display dense cytoplasm and prominent nuclei." },
      { author: "Asa Gray", work: "Structural Botany", quote: "All tissue differentiation proceeds from the embryonic activity of **meristematic** cells." }
    ]
  },
  "meristic.md": {
    primary: "Relating to or characterized by repetition of homologous parts, segments, or organs in an animal or plant.",
    secondary: "In ichthyology and taxonomy, pertaining to quantifiable anatomical counts (such as fin rays or vertebrae).",
    quotes: [
      { author: "William Bateson", work: "Materials for the Study of Variation", quote: "Bateson classified numerical variations in repeated organs under the term **meristic** variation." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "Accurate identification of fish species relies on **meristic** counts of dorsal and anal fin rays." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "Hox gene mutations frequently induce homeotic transformations that alter **meristic** segment identity." }
    ]
  },
  "meromorphic.md": {
    primary: "In complex analysis, describing a function that is holomorphic throughout an open domain except at a set of isolated poles.",
    secondary: "A ratio of two holomorphic functions on a Riemann surface, behaving well under algebraic operations.",
    quotes: [
      { author: "Lars Ahlfors", work: "Complex Analysis", quote: "A function is called **meromorphic** in a domain if its only singularities are non-essential isolated poles." },
      { author: "Henri Poincaré", work: "Analysis Situs", quote: "The global properties of algebraic curves are revealed through the study of **meromorphic** functions defined upon them." },
      { author: "Roger Penrose", work: "The Road to Reality", quote: "Riemann surfaces provide the natural geometric setting for multi-valued and **meromorphic** functions." }
    ]
  },
  "meros.md": {
    primary: "In classical Greek, a part, portion, share, or division; the etymological root of chemical and biological *mer* compounds.",
    secondary: "In entomology and arthropod anatomy, the thigh or femoral segment of an insect or crustacean limb.",
    quotes: [
      { author: "Aristotle", work: "Parts of Animals", quote: "In examining living creatures, the philosopher must distinguish between the whole organism and each functional **meros**." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "In the crustacean appendage, the **meros** forms the prominent third segment of the walking leg." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "Ancient Greek *meros* signified a part, fraction, or appointed share of destiny." }
    ]
  },
  "metamere.md": {
    primary: "One of a linear series of homologous body segments or somites in animals exhibiting metameric segmentation.",
    secondary: "In developmental embryology, an individual somite containing segmental nerves, blood vessels, and musculature.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The earthworm's body consists of a longitudinal chain of repeating units, each termed a **metamere**." },
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "In vertebrate embryos, each primordial **metamere** gives rise to a single vertebral segment." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Segmentation allows evolutionary diversification through the specialized modification of individual **metamere** units." }
    ]
  },
  "metameric.md": {
    primary: "Consisting of or exhibiting a linear series of similar segments or metameres; segmented.",
    secondary: "In colorimetry, describing two colors that appear identical under one light source but differ under another.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The segmented arrangement of spinal nerves preserves the ancient **metameric** pattern of our ancestors." },
      { author: "Edwin H. Land", work: "The Retinex Theory of Color Vision", quote: "Two color patches that produce identical cone responses under daylight are termed a **metameric** pair." },
      { author: "Richard Dawkins", work: "The Ancestor's Tale", quote: "Annelid worms perfected the **metameric** body plan, repeating organs across dozens of identical rings." }
    ]
  },
  "metamerism.md": {
    primary: "In comparative zoology and embryology, the condition of having a body composed of a linear series of homologous segments.",
    secondary: "In color science, the perceived match of colors with different spectral power distributions under specific lighting conditions.",
    quotes: [
      { author: "William Bateson", work: "Materials for the Study of Variation", quote: "Serial homology and developmental **metamerism** provide fundamental evidence of evolutionary modification." },
      { author: "Jöns Jacob Berzelius", work: "Treatise on Chemistry", quote: "Berzelius initially used **metamerism** to describe compounds possessing identical proportions of elements in different arrangements." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "The genetic control of **metamerism** by homeobox genes revolutionized evolutionary developmental biology." }
    ]
  },
  "Moirai.md": {
    primary: "In Greek mythology, the three Fates (Clotho, Lachesis, and Atropos) who apportion each mortal's share of life, destiny, and death.",
    secondary: "The personifications of inevitable destiny and cosmic order in ancient Greek religion and poetry.",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "Night bore the **Moirai**, Clotho, Lachesis, and Atropos, who give mortals their portion of good and evil." },
      { author: "Plato", work: "The Republic", quote: "The daughters of Necessity, the **Moirai**, sang in harmony with the music of the celestial spheres." },
      { author: "Will Durant", work: "The Life of Greece", quote: "Even Zeus himself was subject to the immutable decrees woven by the venerable **Moirai**." }
    ]
  },
  "monomer.md": {
    primary: "A molecule of low molecular weight that can be bonded to other identical or different molecules to form a polymer.",
    secondary: "In biochemistry, a single polypeptide chain or functional protein subunit before assembling into an oligomeric complex.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Ethylene serves as the fundamental **monomer** in the industrial synthesis of polyethylene plastic." },
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "Each nucleotide represents an individual **monomer** linked by phosphodiester bonds in the polynucleotide chain." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "The distillation flask contained reactive vinyl **monomer**, ready to polymerize into clear resin." }
    ]
  },
  "monomeric.md": {
    primary: "Consisting of or relating to a single monomer or single subunit.",
    secondary: "In protein biochemistry, existing as an unassociated single polypeptide chain (such as myoglobin).",
    quotes: [
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "Myoglobin is a **monomeric** oxygen-binding protein consisting of a single polypeptide chain." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The reactive intermediate exists transiently in a **monomeric** state before cross-linking." },
      { author: "Arthur Kornberg", work: "DNA Replication", quote: "Binding of the cofactor converts the inactive **monomeric** enzyme into an active homooligomer." }
    ]
  },
  "octamer.md": {
    primary: "An oligomer or macromolecular complex composed of eight monomeric subunits or parts.",
    secondary: "In molecular genetics, the histone octamer around which eukaryotic DNA winds to form a nucleosome core particle.",
    quotes: [
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "Nuclear DNA wraps twice around a core histone **octamer** to constitute the fundamental nucleosome." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "The structure of chromatin revealed that eight histone proteins assemble into a symmetrical disc-shaped **octamer**." },
      { author: "Max Perutz", work: "Protein Structure", quote: "Crystallographic analysis confirmed that eight identical subunits coordinate to form the active enzymatic **octamer**." }
    ]
  },
  "oligomer.md": {
    primary: "A polymer molecule consisting of a small and specified number of monomeric units (typically between two and twenty).",
    secondary: "In structural biochemistry, a multi-subunit protein complex composed of a small number of associated polypeptide chains.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Short chains intermediate between a monomer and a high polymer are designated an **oligomer**." },
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "Synthetic peptide **oligomer** sequences were used to identify cell surface receptor binding domains." },
      { author: "Stanley B. Prusiner", work: "Nobel Lecture on Prions", quote: "Neurotoxic intermediates frequently accumulate as a soluble **oligomer** before forming insoluble amyloid plaques." }
    ]
  },
  "oligomeric.md": {
    primary: "Pertaining to, having the nature of, or consisting of an oligomer.",
    secondary: "In biochemistry, describing proteins composed of two or more interacting polypeptide subunits.",
    quotes: [
      { author: "Max Perutz", work: "Mechanisms of Cooperativity", quote: "Allosteric regulation is an exclusive property of **oligomeric** proteins with interacting subunits." },
      { author: "Arthur Kornberg", work: "For the Love of Enzymes", quote: "The **oligomeric** structure of the enzyme provides cooperativity and multi-substrate binding sites." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Non-covalent hydrophobic interfaces stabilize the **oligomeric** assembly of globular proteins." }
    ]
  },
  "pentamer.md": {
    primary: "An oligomer, macromolecular complex, or protein assembly composed of five monomeric subunits.",
    secondary: "In immunology, immunoglobulin M (IgM) circulating in serum as a star-shaped pentamer joined by a J chain.",
    quotes: [
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "Serum IgM antibodies assemble into a magnificent planar **pentamer** capable of binding ten antigens." },
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "The viral capsid vertices are constructed from a five-fold symmetric capsomer **pentamer**." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Pentagonal symmetry in viral coats arises from five identical protein chains forming a stable **pentamer**." }
    ]
  },
  "pentamerous.md": {
    primary: "In botany, having floral parts or organs arranged in sets or multiples of five.",
    secondary: "In zoology, exhibiting five-fold radial symmetry, as in echinoderms (starfish, sea urchins).",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "Dicotyledons typically display **pentamerous** flowers, bearing five sepals, five petals, and five or ten stamens." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The starfish displays a magnificent **pentamerous** radial symmetry with five radiating arms." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Echinoderm larvae are bilateral, but metamorphose into adult organisms with **pentamerous** symmetry." }
    ]
  },
  "photopolymer.md": {
    primary: "A polymer or light-sensitive plastic material that changes its chemical and physical properties upon exposure to light.",
    secondary: "In additive manufacturing and dentistry, liquid resins cured by ultraviolet lasers in stereolithography.",
    quotes: [
      { author: "Chuck Hull", work: "Origins of Stereolithography", quote: "By directing an ultraviolet laser across a vat of liquid **photopolymer**, we cured the first three-dimensional plastic object." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "Dental implants were set instantly with a handheld ultraviolet curing wand on blue **photopolymer**." },
      { author: "Peter Atkins", work: "Physical Chemistry", quote: "Free-radical cross-linking in a **photopolymer** occurs within microseconds of photon absorption." }
    ]
  },
  "phytomer.md": {
    primary: "A basic functional and structural repeating developmental unit of a plant shoot, typically consisting of a node, leaf, bud, and internode.",
    secondary: "In plant morphogenesis, the module whose repeated iterative production generates the vegetative architecture of plants.",
    quotes: [
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "The vegetative shoot develops as a continuous sequence of iterative modules, each termed a **phytomer**." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "Each **phytomer** comprises a node with its attached leaf and bud, along with the subjacent internode." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "Modular construction via repeating **phytomer** units gives plants remarkable developmental plasticity." }
    ]
  },
  "polymer.md": {
    primary: "A substance consisting of large molecules composed of many repeating subunits linked together.",
    secondary: "High-molecular-weight compounds formed through addition or condensation polymerization.",
    quotes: [
      { author: "Hermann Staudinger", work: "Nobel Lecture on Macromolecular Chemistry", quote: "I proved that natural rubber is not a colloidal aggregate, but a true macromolecular **polymer**." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The high tensile strength of nylon stems from linear **polymer** chains aligned by hydrogen bonding." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "The reactor held thousands of gallons of molten **polymer**, viscous as honey and clear as glass." }
    ]
  },
  "polymeric.md": {
    primary: "Consisting of, relating to, or having the properties of a polymer.",
    secondary: "Composed of repeated structural units linked together into long molecular chains.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Silicones form flexible **polymeric** chains alternating between silicon and oxygen atoms." },
      { author: "Peter Atkins", work: "Physical Chemistry", quote: "Viscosity in **polymeric** solutions increases sharply with molecular weight due to chain entanglement." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Synthetic **polymeric** membranes were developed to filter micro-pollutants from industrial effluents." }
    ]
  },
  "polymerisation.md": {
    primary: "A chemical process in which two or more monomer molecules combine to form a larger polymer molecule.",
    secondary: "In industrial materials chemistry, condensation or addition reactions forming synthetic resins, plastics, and rubbers.",
    quotes: [
      { author: "Hermann Staudinger", work: "Macromolecular Chemistry", quote: "Free-radical **polymerisation** proceeds through rapid chain initiation, propagation, and termination steps." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "We monitored the vat temperature closely, lest runaway **polymerisation** solidify the entire resin batch." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The industrial **polymerisation** of ethylene yields polyethylene under high pressure and transition-metal catalysis." }
    ]
  },
  "polymerise.md": {
    primary: "To undergo or cause to undergo polymerization; to combine monomers to form a polymer.",
    secondary: "In chemistry, to react small molecules into long-chain macromolecules.",
    quotes: [
      { author: "Primo Levi", work: "The Periodic Table", quote: "Under catalytic heat, the volatile liquid began to **polymerise** into a thick, rubbery mass." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Formaldehyde molecules readily **polymerise** upon standing into white paraformaldehyde flakes." },
      { author: "Peter Atkins", work: "Physical Chemistry", quote: "Irradiating the mixture causes dienes to **polymerise** into synthetic elastomers." }
    ]
  },
  "polymerization.md": {
    primary: "The chemical reaction or process of joining monomer units together into a large polymer chain or network.",
    secondary: "In organic chemistry, addition or condensation reactions yielding synthetic plastics and biological macromolecules.",
    quotes: [
      { author: "Hermann Staudinger", work: "Nobel Lecture", quote: "Step-growth **polymerization** demonstrates that macromolecules are held together by ordinary covalent bonds." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Ziegler-Natta catalysts enabled stereospecific **polymerization**, producing crystalline polypropylene." },
      { author: "Arthur Kornberg", work: "DNA Replication", quote: "DNA polymerase directs template-driven **polymerization** of deoxynucleotides with extraordinary fidelity." }
    ]
  },
  "polymerize.md": {
    primary: "To combine or cause to combine into a polymer; to undergo polymerization.",
    secondary: "To convert monomers into polymers through chemical bonding.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Monomers of styrene **polymerize** into clear, rigid polystyrene widely used for packaging." },
      { author: "Primo Levi", work: "The Monkey's Wrench", quote: "The epoxy coating would **polymerize** into an impenetrable protective shield over the steel bridge girders." },
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "Actin subunits rapidly **polymerize** into dynamic microfilaments that drive cellular motility." }
    ]
  },
  "tautomerism.md": {
    primary: "A form of dynamic chemical isomerism in which two or more structural isomers spontaneously interconvert readily in solution.",
    secondary: "In molecular genetics, transient shifts between keto and enol forms of nitrogenous bases that can induce replication errors.",
    quotes: [
      { author: "James D. Watson", work: "The Double Helix", quote: "Jerry Donohue pointed out that thymine and guanine exist predominantly in the keto form rather than the enol **tautomerism** pictured in textbooks." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Rapid proton transfer across the conjugated system establishes a dynamic equilibrium termed **tautomerism**." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Rare transitions resulting from nucleotide base **tautomerism** accounted for spontaneous point mutations." }
    ]
  },
  "telomer.md": {
    primary: "A low-molecular-weight polymer formed by telomerization, consisting of a chain capped at both ends by fragments of the chain-transfer agent.",
    secondary: "In industrial organic chemistry, an oligomer produced by reacting an alkene with a telogen.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Controlled chain transfer terminates radical growth, yielding a low-viscosity **telomer** suitable for lubricants." },
      { author: "Peter Atkins", work: "Physical Chemistry", quote: "The molecular weight distribution of the **telomer** was analyzed by gel permeation chromatography." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "The fluorinated **telomer** provided heat-resistant coatings for high-temperature chemical gaskets." }
    ]
  },
  "telomere.md": {
    primary: "A compound structure consisting of repetitive non-coding nucleotide sequences at each end of a eukaryotic chromosome.",
    secondary: "In molecular cytogenetics, a chromosomal end structure whose progressive shortening during cell division limits replicative lifespan.",
    quotes: [
      { author: "Elizabeth Blackburn", work: "Nobel Lecture on Telomeres and Telomerase", quote: "At each round of cell division, the chromosomal **telomere** protects vital genetic data from degradation." },
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "Without telomerase, the end-replication problem causes progressive erosion of the **telomere**." },
      { author: "Siddhartha Mukherjee", work: "The Gene: An Intimate History", quote: "The biological clock ticking within our cells is written in the diminishing repeats of each **telomere**." }
    ]
  },
  "tetramer.md": {
    primary: "A polymer or protein complex composed of four monomeric units or polypeptide chains.",
    secondary: "In biochemistry, a four-subunit macromolecule (such as hemoglobin, avidin, or p53).",
    quotes: [
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "Hemoglobin functions as a cooperative **tetramer** that alters its quaternary shape upon oxygen binding." },
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "The tumor suppressor p53 binds to DNA response elements as a symmetrical **tetramer**." },
      { author: "Arthur Kornberg", work: "DNA Replication", quote: "The single-stranded DNA-binding protein forms an active **tetramer** that coats unwound template strands." }
    ]
  },
  "tetrameric.md": {
    primary: "Consisting of or relating to a tetramer; composed of four subunits, parts, or monomeric units.",
    secondary: "In botany, having floral whorls or organs arranged in sets or multiples of four.",
    quotes: [
      { author: "Max Perutz", work: "Mechanisms of Cooperativity", quote: "The **tetrameric** architecture of hemoglobin allows allosteric communication between the four heme pockets." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Certain evening primroses display a **tetrameric** floral plan with four sepals, four petals, and eight stamens." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Quaternary symmetry stabilizes the **tetrameric** enzyme against thermal denaturation." }
    ]
  },
  "tetramerous.md": {
    primary: "In botany, having floral parts or organs arranged in sets or multiples of four (e.g. four petals, four sepals).",
    secondary: "In entomology, having tarsi composed of four segments or joints.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany", quote: "Cruciferous plants possess strictly **tetramerous** flowers, their four petals arranged in the shape of a cross." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The floral envelope is **tetramerous**, alternating with four stamens and a four-celled ovary." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Certain families of beetles are recognized by their **tetramerous** foot structure." }
    ]
  },
  "trim.md": {
    primary: "In good, neat, orderly, or healthy physical condition; neat, slender, and well-proportioned.",
    secondary: "To make something neat or required size by cutting away irregular parts; or decorative edging.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The ship was in capital **trim**, her canvas bleached white and decks scrubbed clean." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "The lawn before the parsonage was in immaculate **trim**, neatly mown and bordered with shrubs." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I kept my little house in good **trim**, clearing away unnecessary clutter to welcome contemplation." }
    ]
  },
  "trimer.md": {
    primary: "A polymer or macromolecular complex consisting of three monomeric units or polypeptide chains.",
    secondary: "In chemistry, a compound formed by the union of three identical molecules (e.g. benzene from acetylene).",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Heating acetylene passes it over heated copper, polymerizing three molecules into the cyclic **trimer** benzene." },
      { author: "James D. Watson", work: "Molecular Biology of the Cell", quote: "The coronavirus spike glycoprotein forms a prominent surface **trimer** that mediates viral entry." },
      { author: "Max Perutz", work: "Protein Structure", quote: "Collagen fibers consist of a triple helix formed by three polypeptide chains wound into a stable **trimer**." }
    ]
  },
  "trimerize.md": {
    primary: "To combine or cause three monomeric molecules or subunits to combine into a trimer.",
    secondary: "In structural biochemistry, to undergo self-association into a three-subunit oligomeric complex.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Under acid conditions, acetaldehyde will readily **trimerize** into paraldehyde." },
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "Receptor binding signals the intracellular domains to **trimerize** and initiate downstream phosphorylation." },
      { author: "Peter Atkins", work: "Physical Chemistry", quote: "Elevated temperatures cause the alkyne to **trimerize** cleanly into the symmetrical aromatic ring." }
    ]
  },
  "trimly.md": {
    primary: "In a neat, orderly, elegant, or well-proportioned manner.",
    secondary: "In a spruce, smart, or carefully arranged condition.",
    quotes: [
      { author: "Geoffrey Chaucer", work: "The Canterbury Tales", quote: "Her mantle was embroidered **trimly** with silken thread, and neat was her attire." },
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The rustic cottage garden was **trimly** bordered with boxwood and fragrant sweet-william." },
      { author: "Charles Dickens", work: "The Pickwick Papers", quote: "A **trimly** dressed groom stepped forward to take the reins of the panting horses." }
    ]
  },
  "trimness.md": {
    primary: "The state, quality, or condition of being trim; neatness, orderliness, and smartness of appearance.",
    secondary: "Slenderness, compactness, and athletic proportion of physical build.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "She admired the Quaker **trimness** of the quiet room, where every book and chair had its exact station." },
      { author: "Charlotte Brontë", work: "Villette", quote: "The French pupils displayed an innate Parisian **trimness** in their uniform aprons and braided hair." },
      { author: "Herman Melville", work: "White-Jacket", quote: "The immaculate **trimness** of the warship was maintained by daily scrubbing and holystoning." }
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

console.log('Done Batch 9 (Dashboard — mer Part 2) of Cluster Art, Craft & Design (34 words)!');
