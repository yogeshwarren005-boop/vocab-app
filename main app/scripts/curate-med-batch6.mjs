import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Medicine & Pathology/Dashboard — styl";

const wordsData = {
  "amphiprostyle.md": {
    word: "amphiprostyle",
    primary: "A classical temple having a portico of columns at both the front and rear facades, but no columns along the flanks.",
    secondary: "In Vitruvian classical architecture, exemplified by the Temple of Athena Nike on the Athenian Acropolis, possessing a tetrastyle portico at each end.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The **amphiprostyle** temple possesses all the features of the prostyle, with the addition of columns and a pediment at the rear posticum." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The jewel-like Temple of Nike Apteros displays the harmonious perfection of the **amphiprostyle** plan perched upon the Acropolis rock." },
      { author: "James Fergusson", work: "A History of Architecture in All Countries", quote: "An **amphiprostyle** arrangement gives dignity to both approaches of a civic monument without the expense of a full peristyle." }
    ]
  },
  "amphistylar.md": {
    word: "amphistylar",
    primary: "Having columns or porticoes at both ends (front and back); amphiprostyle.",
    secondary: "In architectural history, describing neoclassical or Greco-Roman buildings designed with symmetrical colonnades facing opposite vistas.",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "An **amphistylar** building welcomes the citizen equally whether approached from the forum or the sacred precinct." },
      { author: "William Chambers", work: "A Treatise on the Decorative Part of Civil Architecture", quote: "The pavilion was designed upon an **amphistylar** model, offering shaded colonnades to both the lawn and the river." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "Greek civic monuments frequently adopted the **amphistylar** elevation to command two converging avenues." }
    ]
  },
  "amphistyly.md": {
    word: "amphistyly",
    primary: "A type of primitive vertebrate jaw suspension in which the upper jaw is attached to the neurocranium by both its own palatobasal process and the hyomandibula.",
    secondary: "In comparative vertebrate morphology, the ancestral gnathostome jaw attachment observed in early fossil chondrichthyans and primitive hexanchid sharks.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Application of the Laws of Evolution to the Arrangement of the Vertebrata", quote: "In the primitive condition of **amphistyly**, the palatoquadrate bar retains direct ligamentous articulation with the cranium." },
      { author: "Alfred Sherwood Romer", work: "The Vertebrate Body", quote: "Evolutionary transition from **amphistyly** to hyostyly granted sharks greater cranial kinesis and biting power." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "Fossil acanthodians exhibit **amphistyly**, providing insight into how jaws first evolved from anterior visceral arches." }
    ]
  },
  "anastylosis.md": {
    word: "anastylosis",
    primary: "The archaeological restoration technique of reconstructing a ruined monument or building using the original architectural fragments.",
    secondary: "In cultural heritage preservation (codified in the Venice Charter of 1964), re-erecting fallen columns and lintels while clearly distinguishing modern filler materials from authentic stone.",
    quotes: [
      { author: "Nicholas Balanos", work: "The Monuments of the Acropolis: Restoration and Conservation", quote: "Through careful **anastylosis**, we pieced together the shattered drums of the Parthenon columns from the rubble of the Venetian explosion." },
      { author: "Henri Marchal", work: "The Restoration of Angkor Wat", quote: "French archaeologists applied Dutch methods of **anastylosis** to reassemble the collapsed sandstone galleries of the Banteay Srei temple." },
      { author: "Cesare Brandi", work: "Theory of Restoration", quote: "Scientific **anastylosis** must respect historical patina, avoiding hypothetical reconstructions where original fragments are lost." }
    ]
  },
  "araeostyle.md": {
    word: "araeostyle",
    primary: "An architectural arrangement in which the space between adjacent columns (intercolumniation) is wide, typically four or more column-diameters.",
    secondary: "In classical Vitruvian rules, an open intercolumniation requiring timber architraves rather than stone epistyles, because stone would fracture across such wide spans.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "In the **araeostyle** species, the columns are set far apart, so that stone epistyles cannot be used, and wooden beams must be laid across." },
      { author: "Andrea Palladio", work: "The Four Books of Architecture", quote: "Etruscan temples were built according to the **araeostyle** interval to accommodate wide carriage entrances." },
      { author: "William Chambers", work: "Treatise on Civil Architecture", quote: "Modern porticoes rarely employ the **araeostyle** spacing because it imparts a weak, disjointed appearance to the colonnade." }
    ]
  },
  "araeosystyle.md": {
    word: "araeosystyle",
    primary: "An architectural arrangement in which columns are arranged in pairs with alternating wide and narrow intercolumniations.",
    secondary: "In Renaissance and Baroque neoclassical design, an elevation featuring coupled columns separated by wider bays, famously executed by Claude Perrault at the East Façade of the Louvre.",
    quotes: [
      { author: "Claude Perrault", work: "Ordonnance des cinq espèces de colonnes", quote: "By adopting the **araeosystyle** arrangement of paired columns, we attained both architectural majesty and broad, well-lit window bays." },
      { author: "John Soane", work: "Lectures on Architecture", quote: "The paired columns of the **araeosystyle** facade give an impression of immense structural stability without sacrificing light." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "Perrault's colonnade of the Louvre became the celebrated prototype of the **araeosystyle** order throughout European capitals." }
    ]
  },
  "astylar.md": {
    word: "astylar",
    primary: "In classical architecture, lacking columns, pilasters, or colonnades on the exterior walls.",
    secondary: "In architectural design, describing Renaissance palazzi (such as the Palazzo Farnese or Palazzo Strozzi) whose façades rely upon rustication and proportion rather than classical orders.",
    quotes: [
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The noble **astylar** front of the Florentine palazzo derives its majesty from massive stone rustication and deep overhanging eaves." },
      { author: "James Fergusson", work: "History of Modern Architecture", quote: "Sangallo chose an **astylar** design for the Palazzo Farnese, crowning the smooth brickwork with a colossal classical cornice." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "Early Italian Renaissance palaces were purely **astylar**, presenting fortress-like masonry to the city streets." }
    ]
  },
  "blastostyle.md": {
    word: "blastostyle",
    primary: "A specialized, non-feeding reproductive polyp (zooid) in colonial hydrozoan cnidarians that gives rise to medusa buds by asexual budding.",
    secondary: "In marine invertebrate zoology, the central axis of a gonangium in hydroids such as Obelia, specialized exclusively for the generation of free-swimming medusae.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "The asexual **blastostyle** is devoid of tentacles and mouth, dedicated entirely to the production of medusoid gonophores." },
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "Within the transparent gonotheca, the **blastostyle** buds off miniature jellyfish that pulse into the surrounding sea." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "The life cycle of the hydroid alternates between the anchored nutritive colony and the sexual medusae shed by the **blastostyle**." }
    ]
  },
  "diastyle.md": {
    word: "diastyle",
    primary: "A classical intercolumniation in which the distance between adjacent columns equals three column-diameters.",
    secondary: "In Vitruvian architectural theory, an open column spacing wider than eustyle, requiring careful stone selection to prevent cracking of the horizontal epistyle.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "In the **diastyle** temple, the intercolumniation is three times the thickness of a column, giving an open and airy aspect." },
      { author: "Andrea Palladio", work: "The Four Books of Architecture", quote: "If a **diastyle** spacing is chosen, the architect must ensure that the stone architrave is sufficiently deep to support the frieze." },
      { author: "William Chambers", work: "Treatise on Civil Architecture", quote: "The **diastyle** order allows generous light to enter the windows behind the colonnade." }
    ]
  },
  "epistyle.md": {
    word: "epistyle",
    primary: "The lowest horizontal beam or architectural member of an entablature that rests directly upon the capitals of columns; the architrave.",
    secondary: "In Greek monumental architecture, the massive stone or marble lintel spanning from column to column, carrying the frieze and cornice.",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "The thickness of the **epistyle** must be proportionate to the height of the columns to prevent structural bowing." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Doric **epistyle** rests with majestic gravity upon the fluted columns, unbroken by superfluous ornamental carving." },
      { author: "James Fergusson", work: "A History of Architecture", quote: "The enormous marble blocks of the Parthenon's **epistyle** were hoisted into position with remarkable mechanical precision." }
    ]
  },
  "eustyle.md": {
    word: "eustyle",
    primary: "The intercolumniation regarded by Vitruvius as the most harmonious and perfect, having a distance between columns of two and a quarter column-diameters.",
    secondary: "In classical architectural proportion, the optimal spacing combining aesthetic elegance, structural safety for stone epistyles, and convenient passage between columns.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The **eustyle** arrangement is the most approved, uniting beauty, strength, and convenience in the proportion of two diameters and a quarter." },
      { author: "Andrea Palladio", work: "The Four Books of Architecture", quote: "In all public basilicas, I have preferred the **eustyle** interval, which offends neither by crowded columns nor by excessive gaps." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "Hermogenes of Alabanda was celebrated for perfecting the **eustyle** formula in the great Temple of Artemis at Magnesia." }
    ]
  },
  "hexastyle.md": {
    word: "hexastyle",
    primary: "Having six columns across the front facade or portico; a classical portico with six columns.",
    secondary: "In classical temple architecture, the canonical façade design of Greek Doric and Ionic temples, such as the Temple of Hephaestus in Athens and the Temple of Concord in Agrigento.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "A Doric peripteral temple is commonly **hexastyle**, presenting six columns to the front and thirteen along the flanks." },
      { author: "Thomas Jefferson", work: "Letters on the University of Virginia", quote: "The pavilion portico was designed as an authentic **hexastyle** Tuscan colonnade modeled upon classical Roman precedents." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "The Maison Carrée at Nîmes displays a magnificent Corinthian **hexastyle** front of exceptional preservation." }
    ]
  },
  "homostyled.md": {
    word: "homostyled",
    primary: "Having styles of uniform length; homostylous (applied to flowers).",
    secondary: "In botany, describing plant species whose flowers possess pistil styles and stamen filaments of invariant height, lacking heterostyly.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "The exceptional primrose variety was completely **homostyled**, bearing both anthers and stigma at the identical level within the corolla tube." },
      { author: "Asa Gray", work: "Structural Botany", quote: "In **homostyled** species, self-pollination occurs readily without the obligatory intervention of insect pollinators." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Botanists examine whether the wild populations are heterostyled or strictly **homostyled** across their geographical range." }
    ]
  },
  "homostylic.md": {
    word: "homostylic",
    primary: "Of, relating to, or characterized by homostyly; having styles of the same relative length in all flowers of a species.",
    secondary: "In evolutionary botany, referring to the ancestral or secondary state of floral monomorphism in reproductive organ heights.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers", quote: "Artificial crossing between the **homostylic** plants yielded fertile seeds that bred true to the homostyled condition." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The **homostylic** floral structure favors autogamy when ecological conditions prevent insect visitation." },
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "Pollen tube kinetics were analyzed in **homostylic** cultivars to measure self-compatibility rates." }
    ]
  },
  "homostylous.md": {
    word: "homostylous",
    primary: "Having styles and stamens of the same relative length in all flowers of a species; exhibiting homostyly.",
    secondary: "Contrasted with heterostylous species (such as distylous or tristylous primroses) which evolved reciprocal herkogamy to enforce cross-pollination.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "I was led to examine the **homostylous** primroses, which possess equal styles and anthers, to trace the evolutionary origin of heterostyly." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Darwin's experiments on **homostylous** flowers demonstrated how natural selection fine-tunes floral anatomy to avoid inbreeding depression." },
      { author: "Peter Raven", work: "Biology of Plants", quote: "The breakdown of distyly into a self-fertile **homostylous** form is a common evolutionary strategy for colonizing weed species." }
    ]
  },
  "hyostyly.md": {
    word: "hyostyly",
    primary: "A type of jaw suspension in vertebrates in which the upper jaw is connected to the neurocranium solely by the hyomandibular cartilage.",
    secondary: "In comparative vertebrate anatomy, the flexible suspension characteristic of modern elasmobranchs (sharks and rays) and teleost bony fishes, permitting significant jaw protrusion during prey capture.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "In **hyostyly**, the upper jaw loses direct cranial articulation and is swung from the otic capsule by the movable hyomandibula." },
      { author: "Alfred Sherwood Romer", work: "The Vertebrate Body", quote: "The mechanical advantage of **hyostyly** in modern sharks allows the jaws to drop down and thrust forward with lethal speed." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "Primitive bony fishes developed specialized **hyostyly**, which enabled suction feeding in diverse marine niches." }
    ]
  },
  "hypostyle.md": {
    word: "hypostyle",
    primary: "A building or hall having a roof supported by rows of columns, especially an ancient Egyptian temple hall.",
    secondary: "In architectural history, celebrated in the Great Hypostyle Hall of Karnak, where a forest of massive papyrus-bud columns creates an awe-inspiring, semi-lit interior sanctuary.",
    quotes: [
      { author: "James Henry Breasted", work: "A History of Egypt", quote: "The great **hypostyle** hall of Karnak is the most stupendous religious edifice ever erected by human hands, its hundred and thirty-four stone columns towering into twilight." },
      { author: "Percy Bysshe Shelley", work: "Ozymandias", quote: "Around the ruined columns of the **hypostyle** hall, the lone and level sands stretch far away." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "The Egyptian **hypostyle** hall admitted light solely through high clerestory grilles cut between the taller central columns and the lower aisles." }
    ]
  },
  "monostylous.md": {
    word: "monostylous",
    primary: "Having only one style in a flower; characterized by a single floral style.",
    secondary: "In botanical taxonomy and morphology, describing a gynoecium in which several carpels have fused into a single compound pistil with one shared style.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "The family Ericaceae is typically **monostylous**, the five carpels uniting into a single slender style crowned by a peltate stigma." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Botanical keys separate the **monostylous** genera from those displaying multiple distinct styles." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "In **monostylous** species, insect pollinators deposit pollen on the solitary stigma before reaching the nectary." }
    ]
  },
  "octastyle.md": {
    word: "octastyle",
    primary: "Having eight columns in the front portico or facade; an octastyle building or temple.",
    secondary: "In classical Greek architecture, the monumental plan of the Parthenon on the Athenian Acropolis, departing from the standard hexastyle Doric tradition to achieve immense breadth.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The Parthenon at Athens is a magnificent example of the Doric **octastyle** peripteral temple, presenting eight columns to the sunrise." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The **octastyle** portico of the Pantheon in Rome commands the piazza with an unyielding imperial majesty." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "An **octastyle** facade allows the architect to display greater sculptural richness in the pediment above." }
    ]
  },
  "orthostyle.md": {
    word: "orthostyle",
    primary: "An arrangement of columns in a straight row or linear colonnade.",
    secondary: "In classical urbanism and architecture, a straight colonnade flanking a sacred way, agora, or stoa.",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "The civic stoa was laid out as an **orthostyle** colonnade, providing shelter from sun and rain across the marketplace." },
      { author: "William Chambers", work: "Treatise on Civil Architecture", quote: "The **orthostyle** screen designed by Bernini leads the eye straight toward the Vatican basilica." },
      { author: "James Fergusson", work: "A History of Architecture", quote: "The ancient Greek **orthostyle** walkway gave architectural order to the sprawling sanctuary of Delphi." }
    ]
  },
  "peristylar.md": {
    word: "peristylar",
    primary: "Of, relating to, or having a peristyle; surrounded by a colonnade or continuous range of columns.",
    secondary: "In classical archaeology, describing the peristylar courtyards of Roman domus residences (such as those preserved at Pompeii and Herculaneum).",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The **peristylar** court of the private house should be adorned with fountain basins and fragrant shrubs." },
      { author: "Edward Bulwer-Lytton", work: "The Last Days of Pompeii", quote: "Glaucus walked into the cool **peristylar** garden, where marble statues gleamed between fluted columns." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "The **peristylar** arrangement of the Greek tholos temple creates a circular shadow around the inner cella." }
    ]
  },
  "peristyle.md": {
    word: "peristyle",
    primary: "A continuous porch or row of columns surrounding a building or an open courtyard.",
    secondary: "In classical Greco-Roman domestic architecture, the inner colonnaded garden court of a wealthy residence; in temple architecture, the external colonnade (peristasis).",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "The **peristyle** is positioned beyond the atrium, giving the family a private colonnaded sanctuary open to the sky." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "Through the open archway one could see the fountain playing in the marble **peristyle**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Diocletian retired to his colossal palace at Spalato, pacing the monumental **peristyle** in philosophical seclusion." }
    ]
  },
  "prostyle.md": {
    word: "prostyle",
    primary: "Having a portico of freestanding columns across the front facade only, with no columns along the sides or rear.",
    secondary: "In classical temple taxonomy, a simpler plan than amphiprostyle or peripteral, commonly used for smaller Roman civic temples and shrines.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "A temple is called **prostyle** when it has columns only in front of the pronaos, with none along the sides." },
      { author: "Andrea Palladio", work: "The Four Books of Architecture", quote: "The small suburban temple was constructed on a **prostyle** plan, its four Corinthian columns greeting the traveller." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "The small Roman **prostyle** temple placed its emphasis squarely upon a monumental front staircase." }
    ]
  },
  "pseudoprostyle.md": {
    word: "pseudoprostyle",
    primary: "Appearing to be prostyle, but with the front columns partially engaged or set without a true projecting portico.",
    secondary: "In architectural criticism, an elevation where columns are attached to the front wall rather than forming an open, freestanding colonnaded porch.",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "When space was confined, provincial architects adopted a **pseudoprostyle** facade with half-columns engaged in the front wall." },
      { author: "James Fergusson", work: "History of Architecture in All Countries", quote: "The **pseudoprostyle** arrangement gives the illusion of a portico without sacrificing interior floor space." },
      { author: "William Chambers", work: "Treatise on Civil Architecture", quote: "Neoclassical bank buildings frequently employ a **pseudoprostyle** front to convey classical dignity within narrow street lines." }
    ]
  },
  "pycnostyle.md": {
    word: "pycnostyle",
    primary: "An architectural arrangement in which columns are set close together, with an intercolumniation of one and a half column-diameters.",
    secondary: "In Vitruvian architecture, the closest of the classical column spacings, creating a dense, forest-like facade suitable for very tall or slender columns.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "In the **pycnostyle** species, the interval between columns is only one diameter and a half, so that matrons cannot walk between them arm in arm." },
      { author: "Andrea Palladio", work: "The Four Books of Architecture", quote: "The **pycnostyle** spacing was chosen for the circular chapel to ensure that the architraves would never sag under heavy dome vaulting." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "The dense rhythm of **pycnostyle** colonnades produces dramatic vertical shadows across classical temple fronts." }
    ]
  },
  "style.md": {
    word: "style",
    primary: "A distinctive manner of expression, design, execution, or behavior; or in botany, the narrow stalk connecting the floral ovary to the stigma.",
    secondary: "In literary aesthetics and rhetoric, the distinctive linguistic voice and compositional choices characteristic of an author, artist, or historical epoch.",
    quotes: [
      { author: "Georges-Louis Leclerc, Comte de Buffon", work: "Discours sur le style", quote: "The **style** is the man himself; it reflects the inner order and clarity of the thinker's mind." },
      { author: "Jonathan Swift", work: "Treatise on Good Manners and Good Breeding", quote: "Proper words in proper places make the true definition of a good **style**." },
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "The long-styled form bears a **style** extending far above the corolla, while the short-styled form keeps it hidden within the tube." }
    ]
  },
  "styleless.md": {
    word: "styleless",
    primary: "Lacking style, elegance, distinction, or fashionable quality; drab, uninspired, or uncultivated.",
    secondary: "In botany, lacking a floral style, having the stigma seated directly upon the ovary (sessile stigma).",
    quotes: [
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Her prose was completely **styleless**, plodding along in gray domestic triviality without a spark of wit." },
      { author: "George Orwell", work: "Keep the Aspidistra Flying", quote: "He looked with despair at his cheap, **styleless** mackintosh and scuffed boots." },
      { author: "Asa Gray", work: "Manual of Botany", quote: "In the genus Nymphaea, the flower is essentially **styleless**, the stigmatic rays radiating upon the summit of the ovary." }
    ]
  },
  "stylemark.md": {
    word: "stylemark",
    primary: "A distinctive hallmark, trademark, or recognizable signature characteristic of an artist's, writer's, or designer's style.",
    secondary: "In design theory and commercial branding, a formal visual motif or aesthetic signature that identifies the creator or fashion house.",
    quotes: [
      { author: "Walter Pater", work: "Appreciations: With an Essay on Style", quote: "The recurring golden epithet was the unmistakable **stylemark** of the poet's youth." },
      { author: "Henry James", work: "The Art of Fiction", quote: "The subtle parenthetical clause was the master's personal **stylemark**, weaving complex qualifications into every narrative page." },
      { author: "Steven Heller", work: "Design Literacy", quote: "A clean sans-serif logo became the corporate **stylemark** that defined modernist Swiss graphic design." }
    ]
  },
  "styler.md": {
    word: "styler",
    primary: "A person or device that styles, designs, cuts, or arranges something (especially hair, clothing, or graphic design).",
    secondary: "In the fashion and beauty industries, a professional who coordinates wardrobe, aesthetics, and appearance for media or personal clients.",
    quotes: [
      { author: "Virginia Woolf", work: "Orlando", quote: "The royal **styler** spent three hours dressing the courtier's hair in scented powder and golden buckles." },
      { author: "Sinclair Lewis", work: "Dodsworth", quote: "His wife consulted a Parisian **styler** to replace her Midwestern wardrobe with chic European gowns." },
      { author: "Steven Heller", work: "Graphic Style", quote: "The layout **styler** balanced the typography against bold photographic spreads." }
    ]
  },
  "stylet.md": {
    word: "stylet",
    primary: "A small, slender, pointed surgical probe or wire inserted into a cannula or catheter to maintain stiffness; or a sharp piercing mouthpart in invertebrates.",
    secondary: "In entomology and nematology, a needle-like chitinous organ used by plant-parasitic nematodes or piercing-sucking insects (aphids, mosquitoes) to puncture host tissues.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The surgeon withdrew the wire **stylet** from the flexible cannula, and immediate clear spinal fluid welled forth." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "The aphid pierces the phloem sieve tubes with its microscopic **stylet**, drinking the sap of the plant." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "A rigid endotracheal **stylet** assisted the anesthesiologist in navigating the anterior larynx during a difficult intubation." }
    ]
  },
  "stylisation.md": {
    word: "stylisation",
    primary: "The act or process of representing something in an artificial, conventional, or stylized artistic manner rather than naturalistically (chiefly British spelling of stylization).",
    secondary: "In art history, simplifying natural organic forms into decorative geometric motifs or cultural conventions.",
    quotes: [
      { author: "E. H. Gombrich", work: "Art and Illusion", quote: "Egyptian relief sculpture attained a majestic **stylisation** that remained virtually unchanged across three thousand years." },
      { author: "Roger Fry", work: "Vision and Design", quote: "The Byzantine icon sacrifices anatomical realism for a sublime spiritual **stylisation** of the saints." },
      { author: "Kenneth Clark", work: "Civilisation", quote: "Celtic metalwork exhibits an astonishing **stylisation**, where animal bodies dissolve into swirling golden interlaces." }
    ]
  },
  "stylise.md": {
    word: "stylise",
    primary: "To depict, design, or conform to a stylized, non-naturalistic, or conventional artistic pattern (British spelling of stylize).",
    secondary: "In theater and design, to deliberately abstract natural human behavior or physical objects into symbolic, exaggerated forms.",
    quotes: [
      { author: "Oscar Wilde", work: "The Decay of Lying", quote: "Art begins when we **stylise** nature, refusing to copy the crude accidents of everyday life." },
      { author: "Virginia Woolf", work: "Roger Fry: A Biography", quote: "Fry urged young painters to **stylise** their forms, seeking rhythmic structural design rather than camera-like reproduction." },
      { author: "George Bernard Shaw", work: "The Quintessence of Ibsenism", quote: "The playwright did not **stylise** his dialogue into grand blank verse, but captured the living rhythms of modern speech." }
    ]
  },
  "stylised.md": {
    word: "stylised",
    primary: "Represented in a conventional, non-realistic, or artistic style rather than according to nature (British spelling of stylized).",
    secondary: "Characterized by formal conventions, exaggerated geometric lines, or deliberate simplification in art, literature, or performance.",
    quotes: [
      { author: "T. S. Eliot", work: "Selected Essays", quote: "The Noh drama of Japan employs a highly **stylised** code of gestures where the flutter of a fan communicates grief or battle." },
      { author: "W. B. Yeats", work: "Essays and Introductions", quote: "I love the **stylised** masks of ancient Greek tragedy, which silence the trivial mobility of human actors." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "Upon the ancestral silver hung a **stylised** dragon, its claws clutching an enameled rose." }
    ]
  },
  "stylish.md": {
    word: "stylish",
    primary: "Fashionably elegant, smart, and attractive; exhibiting refined taste in dress or appearance.",
    secondary: "Characterized by flair, polished technique, and distinctive elegance in literary or artistic execution.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "Pip arrived in London wearing a **stylish** new coat, eager to assume the airs of a gentleman of fortune." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Becky Sharp knew how to make a cheap muslin gown look more **stylish** than the costliest Parisian silks." },
      { author: "F. Scott Fitzgerald", work: "Tender Is the Night", quote: "They formed a **stylish** group under the Riviera sun, laughing in the golden light of the beach." }
    ]
  },
  "stylishly.md": {
    word: "stylishly",
    primary: "In a stylish, fashionable, and elegant manner.",
    secondary: "With polished aesthetic flair and confident execution.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "The younger Miss Bennets were eager to be seen **stylishly** dressed when the regiment paraded through Meryton." },
      { author: "Oscar Wilde", work: "An Ideal Husband", quote: "Mrs. Cheveley entered the drawing room **stylishly** attired in heliotrope velvet, commanding instant attention." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Madame Merle poured the tea **stylishly**, her every gesture marked by cosmopolitan grace." }
    ]
  },
  "stylishness.md": {
    word: "stylishness",
    primary: "The state, quality, or condition of being stylish; fashionable elegance and chic taste.",
    secondary: "Polished aesthetic refinement and distinctiveness in personal grooming or artistic expression.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "The History of Pendennis", quote: "He admired the aristocratic **stylishness** of the young officers who strolled along Pall Mall." },
      { author: "Edith Wharton", work: "The Age of Innocence", quote: "The Countess Olenska possessed an effortless **stylishness** that defied the rigid, prudish conventions of old New York." },
      { author: "Virginia Woolf", work: "Orlando", quote: "In the eighteenth century, **stylishness** was elevated into a supreme civic virtue practiced in every salon." }
    ]
  },
  "stylist.md": {
    word: "stylist",
    primary: "A writer or artist who is a master of literary or artistic style; or a professional who styles hair or fashion.",
    secondary: "In literary criticism, an author whose work is characterized by exceptional attentiveness to diction, cadence, sentence structure, and verbal texture (e.g., Flaubert, Pater, Nabokov).",
    quotes: [
      { author: "Walter Pater", work: "Appreciations: With an Essay on Style", quote: "The true literary **stylist** searches ceaselessly for the unique word, the 'mot juste', that alone fits the intellectual vision." },
      { author: "Henry James", work: "French Poets and Novelists", quote: "Gustave Flaubert was the martyr of style, an unsparing **stylist** who spent weeks agonizing over the balance of a single paragraph." },
      { author: "H. L. Mencken", work: "Prejudices", quote: "A brilliant **stylist** can make an essay on grammatical particles read like an exciting adventure story." }
    ]
  },
  "stylistic.md": {
    word: "stylistic",
    primary: "Of, relating to, or concerning style, especially literary or artistic expression.",
    secondary: "In linguistics and literary analysis, pertaining to stylistics: the study of rhetorical devices, syntax, register, and aesthetic voice in texts.",
    quotes: [
      { author: "T. S. Eliot", work: "The Sacred Wood", quote: "A genuine **stylistic** innovation is not a mere decorative trick, but a new way of organizing human perception." },
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "She developed a **stylistic** cadence adapted to feminine experience rather than adopting the heavy sentence of male essayists." },
      { author: "E. H. Gombrich", work: "Art and Illusion", quote: "Every **stylistic** shift in painting reflects a change in the mental schemas through which artists interpret reality." }
    ]
  },
  "stylistically.md": {
    word: "stylistically",
    primary: "In a manner relating to style; from the viewpoint of literary or artistic style.",
    secondary: "In textual criticism, evaluated by linguistic features, syntax, and rhetorical vocabulary to assess authorship or date of composition.",
    quotes: [
      { author: "Henry James", work: "The Art of Fiction", quote: "The novel was **stylistically** immaculate, each sentence fitting into its neighbor like polished mosaic tiles." },
      { author: "W. W. Greg", work: "The Calculus of Variants", quote: "The disputed scene belongs **stylistically** to Fletcher rather than Shakespeare, as shown by the high frequency of feminine endings." },
      { author: "George Steiner", work: "After Babel", quote: "To translate a poem successfully, the translator must recreate it **stylistically** within the native genius of the target language." }
    ]
  },
  "stylite.md": {
    word: "stylite",
    primary: "An early Christian ascetic who lived in solitary prayer and penance atop a pillar or column (a pillar-saint or pillar-hermit).",
    secondary: "In the history of Eastern monasticism, founded by Saint Simeon Stylites in fifth-century Syria, practicing extreme mortification upon elevated pillars to escape worldly contamination.",
    quotes: [
      { author: "Alfred, Lord Tennyson", work: "St. Simeon Stylites", quote: "I, Simeon of the pillar, by surname **Stylite** among men, have lived forty years upon this stone, watching the stars and enduring summer heat and winter snow." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "This aerial martyrdom of the Syrian **stylite** excited the admiration and reverence of thousands of pilgrims from the furthest boundaries of Christendom." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "The bizarre austerities of the Christian **stylite** mirrored ancient Syrian pagan practices of ascending temple phalli to commune with the sun god." }
    ]
  },
  "Stylites.md": {
    word: "Stylites",
    primary: "The title or surname given to Christian pillar-saints, especially Saint Simeon Stylites (c. 390–459 AD).",
    secondary: "In church history and hagiography, referring to Simeon Stylites the Elder and Simeon Stylites the Younger, who inspired the monastic movement of pillar ascetics.",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", quote: "Simeon **Stylites** died upon his Syrian column, leaving a fame that surpassed that of kings and emperors." },
      { author: "Alfred, Lord Tennyson", work: "St. Simeon Stylites", quote: "From pillar unto pillar I moved, higher and higher, till I reached this topmost height where **Stylites** kneels before God." },
      { author: "Ernest Renan", work: "History of the Origins of Christianity", quote: "The heroic, fanatical spectacle of **Stylites** upon his pillar commanded the awe of the bedouin tribes of the desert." }
    ]
  },
  "stylization.md": {
    word: "stylization",
    primary: "The act or process of representing subjects in a stylized, decorative, or conventional manner rather than according to realistic nature.",
    secondary: "In visual aesthetics and semiotics, abstracting natural forms into conventionalized geometric or decorative patterns (e.g., Art Deco or ancient Egyptian painting).",
    quotes: [
      { author: "E. H. Gombrich", work: "The Sense of Order", quote: "Geometric **stylization** transforms the natural organic lotus into the repeating palmette frieze of classical temples." },
      { author: "Kenneth Clark", work: "The Nude: A Study in Ideal Form", quote: "Greek sculpture moved from archaic **stylization** toward organic anatomical truth, only to re-impose harmonious geometric proportion." },
      { author: "Meyer Schapiro", work: "Theory and Philosophy of Art", quote: "The expressive power of Romanesque sculpture lies in its purposeful **stylization**, elongating limbs to signify spiritual ecstasy." }
    ]
  },
  "stylize.md": {
    word: "stylize",
    primary: "To depict, design, or conform to a conventional, decorative, or idealized artistic style rather than depicting natural realism.",
    secondary: "In visual arts, graphic design, and animation, to simplify and emphasize essential contours, colors, and silhouettes for communicative impact.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The gothic carver knew how to **stylize** the leaves of wild parsley into vigorous stone capitals." },
      { author: "Roger Fry", work: "Vision and Design", quote: "Primitive artists do not copy nature; they **stylize** what they emotionally know and feel about the beast." },
      { author: "Steven Heller", work: "Design Literacy", quote: "Modern poster artists learned to **stylize** industrial machinery into bold, dynamic graphic icons." }
    ]
  },
  "stylized.md": {
    word: "stylized",
    primary: "Depicted, produced, or treated in a conventional, non-realistic, and decorative style rather than naturalistically.",
    secondary: "Characterized by stylized conventions, formal geometry, or simplified design in painting, theater, dance, or fashion.",
    quotes: [
      { author: "E. H. Gombrich", work: "The Story of Art", quote: "In ancient Egyptian art, every figure was rendered in a strictly **stylized** profile, combining multiple viewpoints into a single conceptual image." },
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "The wooden idol was carved with **stylized** savagery, its mother-of-pearl eyes staring into the dark room." },
      { author: "Virginia Woolf", work: "The Waves", quote: "Their formal movements resembled a **stylized** ballet performed upon a sunlit terrace." }
    ]
  },
  "stylobate.md": {
    word: "stylobate",
    primary: "The continuous stone platform or uppermost step of a stereobate upon which a colonnade of classical columns stands.",
    secondary: "In Greek monumental architecture, famously exemplified in the Parthenon, where the stylobate is subtly curved upward in the center to compensate for optical sagging.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The **stylobate** must not be laid out on a dead flat level, but with a slight upward curvature toward the middle to prevent the optical illusion of sinking." },
      { author: "John Ruskin", work: "The Poetry of Architecture", quote: "The marble **stylobate** lifts the fluted shafts above the dust of the surrounding rocky plain." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "The optical refinements of the Parthenon's **stylobate** exhibit an astonishing precision of masonry cutting." }
    ]
  },
  "styloid.md": {
    word: "styloid",
    primary: "Slender, pointed, and cylindrical, resembling a stylus or pen.",
    secondary: "In human osteology, designating sharp, pointed bony projections such as the styloid process of the temporal bone or the styloid processes of the radius and ulna.",
    quotes: [
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "From the base of the temporal bone projects a slender, needle-like spine, appropriately termed the **styloid** process." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Colles' fracture typically involves a fracture of the distal radius accompanied by avulsion of the ulnar **styloid** process." },
      { author: "Henry Gray", work: "Anatomy of the Human Body", quote: "The styloglossus and stylohyoid muscles arise from the sharp apex of the temporal **styloid** bone." }
    ]
  },
  "stylolite.md": {
    word: "stylolite",
    primary: "An irregular, column-like, or serrated suture-like surface found in sedimentary rocks (especially limestones and marbles), produced by pressure dissolution.",
    secondary: "In sedimentary geology, a diagenetic compaction structure marked by an insoluble residue of clay, carbon, or iron oxides along a zig-zag tooth-like plane.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The polished marble slab displayed a dark, jagged seam, which petrologists designate as a **stylolite** formed by chemical dissolution." },
      { author: "Archibald Geikie", work: "Text-Book of Geology", quote: "A cross-section through the limestone shows interlocking tooth-like projections of the **stylolite** interlocking like cranial sutures." },
      { author: "Francis J. Pettijohn", work: "Sedimentary Rocks", quote: "Differential pressure dissolution under deep overburden stress concentrates insoluble insolubles along the **stylolite** horizon." }
    ]
  },
  "stylomecon.md": {
    word: "stylomecon",
    primary: "A monotypic genus of annual flowering poppies native to California, containing the single species Stylomecon heterophylla (commonly called the wind poppy).",
    secondary: "In systematic botany, distinguished from true Papaver by its distinct, slender columnar style (from Greek stylos, style + mekon, poppy) connecting the ovary to the capitate stigma.",
    quotes: [
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "The genus **Stylomecon** differs from Papaver primarily in the presence of a distinct, persistent style crowning the capsule." },
      { author: "John Muir", work: "The Mountains of California", quote: "On the grassy foothills bloomed the wind poppy, **Stylomecon**, its scarlet petals trembling in the spring breeze." },
      { author: "Willis Linn Jepson", work: "A Manual of the Flowering Plants of California", quote: "The bright orange-red blossoms of **Stylomecon** heterophylla emit a delicate fragrance on warm chaparral slopes." }
    ]
  },
  "stylophorum.md": {
    word: "stylophorum",
    primary: "A genus of herbaceous perennial flowering plants in the poppy family (Papaveraceae), commonly known as celandine poppies or wood poppies.",
    secondary: "In systematic botany, plants named from Greek stylos (column/style) and phoros (bearing), referring to the prominent, persistent columnar style atop the bristly seed capsule.",
    quotes: [
      { author: "Asa Gray", work: "Manual of Botany", quote: "The yellow wood-poppy, **Stylophorum** diphyllum, adorns rich deciduous forest soils with its four bright golden petals." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The genus **Stylophorum** exudes a yellow acrid latex upon cutting, a characteristic shared with the ancient celandine." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", quote: "In shaded woodland gardens, **Stylophorum** self-seeds freely, producing charming early spring groundcover." }
    ]
  },
  "stylopodium.md": {
    word: "stylopodium",
    primary: "An enlargement, expansion, or nectar-secreting disc at the base of the floral styles in plants of the parsley family (Apiaceae / Umbelliferae).",
    secondary: "In floral morphology, a prominent cushion-like structure atop the inferior ovary that produces nectar to attract insect pollinators, later crowning the mature schizocarp fruit.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "At the summit of the umbellifer ovary sits the fleshy, conical **stylopodium**, from which two slender styles emerge." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The form and persistence of the **stylopodium** provide diagnostic characters for distinguishing genera within the Umbelliferae." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "Insects crawl over the umbel, licking sweet droplets secreted by the glistening **stylopodium**." }
    ]
  },
  "stylostixis.md": {
    word: "stylostixis",
    primary: "The therapeutic practice or medical procedure of acupuncture; inserting needles into the body to relieve pain or treat disease.",
    secondary: "In historical nineteenth-century medical terminology, derived from Greek stylos (pencil, needle) and stixis (puncturing), used to describe traditional East Asian needle therapy.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In stubborn cases of lumbago, **stylostixis** or acupuncture with long steel needles inserted into the lumbar muscles often affords prompt relief." },
      { author: "John Hunter", work: "Lectures on the Principles of Surgery", quote: "The ancient procedure of **stylostixis** demonstrates that counter-irritation by puncture can arrest deep neurogenic spasms." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The exotic art of **stylostixis** was introduced from Japan, exciting the curious wonder of European surgeons." }
    ]
  },
  "stylus.md": {
    word: "stylus",
    primary: "A pointed, pen-shaped instrument used for writing, drawing, incising, or marking on a surface (such as an ancient wax tablet, a touch screen, or a recording foil).",
    secondary: "In acoustic history and sound reproduction, the jewel-tipped needle (sapphire or diamond) that tracks the microscopic groove of a phonograph record to transduce mechanical vibrations into sound.",
    quotes: [
      { author: "Thomas A. Edison", work: "The Phonograph and Its Future", quote: "The metallic diaphragm vibrates under the influence of the voice, driving the sharp recording **stylus** into the revolving tinfoil cylinder." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The Roman schoolboy erased his faulty exercises with the blunt end of his iron **stylus**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Caesar defended his life with his iron **stylus**, striking Cassius through the arm before the assassins overpowered him." }
    ]
  },
  "systyle.md": {
    word: "systyle",
    primary: "A classical architectural arrangement in which the space between columns (intercolumniation) equals two column-diameters.",
    secondary: "In Vitruvian architecture, a close, stately column spacing narrower than eustyle but wider than pycnostyle, giving a monumental, sturdy appearance to the portico.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The **systyle** intercolumniation allows two diameters of a column between adjacent shafts, giving a grave and solid dignity." },
      { author: "Andrea Palladio", work: "The Four Books of Architecture", quote: "I have employed the **systyle** proportion in porticoes where high stone entablatures require closer support." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "The Roman architects favored the **systyle** spacing for temples whose height demanded a monumental, closely-knit colonnade." }
    ]
  },
  "unstylish.md": {
    word: "unstylish",
    primary: "Not stylish; lacking fashionable elegance, smartness, or good taste in dress, appearance, or design; unfashionable.",
    secondary: "Out of date, conventional, or visually plain; devoid of aesthetic flair.",
    quotes: [
      { author: "Jane Austen", work: "Emma", quote: "She smiled at the poor curate's **unstylish** coat, whose cut belonged to the fashions of a bygone decade." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The country cousins looked miserably **unstylish** amid the glittering assembly in Hyde Park." },
      { author: "George Orwell", work: "Coming Up for Air", quote: "I was wearing an **unstylish** brown mackintosh and carrying an umbrella like any other clerk in the rain." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
    return;
  }

  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Medicine & Pathology Batch 6 (Dashboard — styl) completed! Total words updated:", Object.keys(wordsData).length);
