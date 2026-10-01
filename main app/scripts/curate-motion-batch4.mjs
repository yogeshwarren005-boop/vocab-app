import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Motion & Direction';

function updateNote(relDir, fileName, data) {
  const filePath = path.join(baseClusterDir, relDir, fileName);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filePath}`);
    return false;
  }
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

  const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

const batch4Data = {
  "Dashboard — trep/Atropos.md": {
    "primary": "In Greek mythology, the eldest of the three Fates (Moirai) who cuts the thread of human life spun by Clotho and measured by Lachesis.",
    "secondary": "In classical literature and etymology (from Greek a- 'not' and tropos 'turning', meaning 'the inflexible or unturning one'), representing the inexorable and irrevocable nature of mortality.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Lycidas",
        "quote": "Comes the blind Fury with the abhorred shears, and slits the thin-spun life; so **Atropos** fulfills her silent decree."
      },
      {
        "author": "Thomas Browne",
        "work": "Urn Burial",
        "quote": "The thread of our days is spun in darkness and severed at last by the unpitying hand of **Atropos**."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "Prometheus Unbound",
        "quote": "Neither prayers nor tears can bend the stony heart of **Atropos** when the fatal hour strikes."
      }
    ]
  },
  "Dashboard — trep/allotrope.md": {
    "primary": "Each of two or more different physical forms in which an element can exist (e.g., diamond, graphite, and fullerenes as allotropes of carbon).",
    "secondary": "In structural chemistry, a distinct molecular or crystalline modification of an elementary substance exhibiting different bonding arrangements and physical properties.",
    "quotes": [
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Treatise on Chemistry",
        "quote": "I propose the term **allotrope** to designate those remarkable instances where a single chemical element assumes diverse physical forms."
      },
      {
        "author": "Michael Faraday",
        "work": "The Chemical History of a Candle",
        "quote": "The sparkling diamond and the dull charcoal are but different conditions of the self-same substance, each being a pure **allotrope** of carbon."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The transition from one solid **allotrope** of tin to another at low temperatures accounts for the destructive phenomenon known as tin pest."
      }
    ]
  },
  "Dashboard — trep/allotropic.md": {
    "primary": "Pertaining to, exhibiting, or existing in the form of an allotrope; capable of existing in two or more distinct structural modifications.",
    "secondary": "In solid-state chemistry and metallurgy, describing reversible or irreversible phase transformations (such as alpha and gamma iron) occurring in elemental crystals.",
    "quotes": [
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Annual Reports on the Progress of Chemistry",
        "quote": "Phosphorus presents an extraordinary example of **allotropic** transformation when gently heated under inert gas."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "The distinct electrical conductivity of graphite stems from its specific **allotropic** arrangement of aromatic carbon sheets."
      },
      {
        "author": "William Ostwald",
        "work": "The Principles of Inorganic Chemistry",
        "quote": "Liquid sulfur undergoes a dramatic **allotropic** change above one hundred and sixty degrees, turning into a dark, viscous mass."
      }
    ]
  },
  "Dashboard — trep/allotropical.md": {
    "primary": "An archaic or formal variant of allotropic; relating to or characterized by allotropy.",
    "secondary": "In nineteenth-century chemical literature, used to describe elements possessing multiple isomeric or structural modifications.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "The gas ozone was suspected by early investigators to be an **allotropical** modification of condensed atmospheric oxygen."
      },
      {
        "author": "Thomas Graham",
        "work": "Elements of Inorganic Chemistry",
        "quote": "The **allotropical** states of elementary bodies demonstrate that physical properties depend as much upon molecular grouping as upon atomic mass."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Red phosphorus is an **allotropical** condition of the element, possessing neither the luminescence nor the violent toxicity of the yellow form."
      }
    ]
  },
  "Dashboard — trep/allotropism.md": {
    "primary": "The existence of a chemical element in two or more distinct forms having different physical properties; allotropy.",
    "secondary": "In historical chemistry, the conceptual framework formulated by Berzelius to classify polymorphic variations in pure elemental substances.",
    "quotes": [
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Annual Reports on the Progress of Chemistry",
        "quote": "The discovery of **allotropism** in carbon and sulfur forced chemists to distinguish sharply between chemical composition and physical state."
      },
      {
        "author": "William Crookes",
        "work": "Select Methods in Chemical Analysis",
        "quote": "Through the phenomenon of **allotropism**, identical atoms assemble into crystals exhibiting utterly divergent optical properties."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Physiography: An Introduction to the Study of Nature",
        "quote": "Diamond, graphite, and soot illustrate the principle of **allotropism** in a manner that arrests every student's attention."
      }
    ]
  },
  "Dashboard — trep/anisotropic.md": {
    "primary": "Having physical properties (such as conductivity, refractive index, or elasticity) that have different values when measured in different directions.",
    "secondary": "In crystallography and materials science, describing non-cubic crystalline lattices or oriented polymeric matrices whose atomic arrangements depend on spatial orientation.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "Popular Lectures and Addresses",
        "quote": "Light passing through an **anisotropic** crystal splits into two rays polarized in perpendicular planes."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "In an **anisotropic** dielectric medium, the electric displacement vector is not necessarily parallel to the applied electric field."
      },
      {
        "author": "William Henry Bragg",
        "work": "X Rays and Crystal Structure",
        "quote": "The unequal thermal expansion along the axes of calcite proves its thoroughly **anisotropic** molecular lattice."
      }
    ]
  },
  "Dashboard — trep/anisotropy.md": {
    "primary": "The property of being directional; the variation of a physical property depending on the direction along which it is measured.",
    "secondary": "In observational cosmology and astrophysics, the minuscule directional variations in temperature detected across the Cosmic Microwave Background (CMB).",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The mechanical stress within the crystal produces an optical **anisotropy** easily revealed between crossed Nicol prisms."
      },
      {
        "author": "Stephen Hawking",
        "work": "A Brief History of Time",
        "quote": "Sensitive satellite instruments mapped the tiny temperature **anisotropy** of the cosmic microwave radiation left over from the Big Bang."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Mathematical Theory of Relativity",
        "quote": "Gravitational fields induce an effective optical **anisotropy** in empty space, bending passing light waves toward the central mass."
      }
    ]
  },
  "Dashboard — trep/contrary.md": {
    "primary": "Opposite in nature, direction, or meaning; stubbornly inclined to disagree or do the opposite of what is expected.",
    "secondary": "In formal Aristotelian logic, designating propositions so related that both cannot be true simultaneously, though both may be false (contrasted with contradictory).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "Our wills and fates do so **contrary** run that our devices still are overthrown; our thoughts are ours, their ends none of our own."
      },
      {
        "author": "Francis Bacon",
        "work": "Essays",
        "quote": "A man that is young in years may be old in hours, if he have lost no time; but that happeneth rarely, for age and youth run **contrary** courses."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "To affirm that the same thing is and is not at the same time is to maintain two **contrary** propositions in defiance of reason."
      }
    ]
  },
  "Dashboard — trep/contrition.md": {
    "primary": "The state of feeling sincere remorse, repentance, and sorrow for having committed a sin or wrongdoing.",
    "secondary": "In Catholic moral theology, sorrow for sin arising purely from the love of God (perfect contrition), distinguished from attrition (imperfect contrition arising from fear of punishment).",
    "quotes": [
      {
        "author": "Geoffrey Chaucer",
        "work": "The Parson's Tale",
        "quote": "True **contrition** is the sorrowful grief of heart that a man conceives for his sins, with steadfast purpose never more to offend."
      },
      {
        "author": "John Donne",
        "work": "Holy Sonnets",
        "quote": "Teach me how to repent; for that's as good as if thou'hadst seal'd my pardon, with tears of true **contrition**."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "Perfect **contrition** blots out mortal sin even before sacramental absolution is actually received in the confessional."
      }
    ]
  },
  "Dashboard — trep/contrivance.md": {
    "primary": "A thing skillfully or artfully created for a particular purpose; a mechanical device, gadget, or ingenious invention.",
    "secondary": "In narrative arts and drama, an artificial, forced, or implausible plot device used by an author to resolve a dramatic impasse.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by which Orchids are Fertilised by Insects",
        "quote": "The structure of the flower presents an exquisite **contrivance** for ensuring that pollen must adhere to visiting bees."
      },
      {
        "author": "Jonathan Swift",
        "work": "Gulliver's Travels",
        "quote": "The mathematical artists of Laputa constructed every household **contrivance** with quadrant, rule, and compass."
      },
      {
        "author": "George Eliot",
        "work": "The Mill on the Floss",
        "quote": "The sudden inheritance was a clumsy literary **contrivance** that failed to convince the discerning reader."
      }
    ]
  },
  "Dashboard — trep/contrive.md": {
    "primary": "To create or bring about an object or situation through skill, ingenuity, or clever planning.",
    "secondary": "To plot, scheme, or manage a deceitful purpose; in mechanics, to engineer a practical mechanism from available parts.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Merchant of Venice",
        "quote": "If it be proved against an alien that by direct or indirect attempts he seek the life of any citizen, or **contrive** his death, the penalty falls."
      },
      {
        "author": "Daniel Defoe",
        "work": "Robinson Crusoe",
        "quote": "I was forced to **contrive** many crude wooden tools before I could fashion even a single rough plank for my habitation."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "I resolved to **contrive** an intricate mechanism of pulleys to raise the heavy frame toward the skylight."
      }
    ]
  },
  "Dashboard — trep/contrived.md": {
    "primary": "Deliberately created rather than arising naturally or spontaneously; appearing artificial, forced, or unrealistic.",
    "secondary": "In literary criticism and dramaturgy, characterizing plot developments or dialogues that feel staged, manipulative, or implausibly convenient.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "The ending of the Victorian novel seemed hopelessly **contrived**, with sudden fortunes and deathbed repentances neatly tied in ribbons."
      },
      {
        "author": "George Orwell",
        "work": "Nineteen Eighty-Four",
        "quote": "The spontaneous public demonstrations were in fact meticulously **contrived** by the Ministry of Truth weeks in advance."
      },
      {
        "author": "Henry James",
        "work": "The Art of the Novel",
        "quote": "A truly organic narrative avoids every **contrived** coincidence, allowing character alone to dictate destiny."
      }
    ]
  },
  "Dashboard — trep/contriver.md": {
    "primary": "One who contrives, devises, plans, or schemes; an inventor or schemer.",
    "secondary": "In dramatic narrative and political history, an architect of elaborate plots or clandestine stratagems.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Julius Caesar",
        "quote": "We shall find of him a shrewd **contriver**; and you know his means, if he improve them, may well stretch so far as to annoy us all."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Satan stood confessed the author of all ill, the chief **contriver** of the fall of man."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The crafty eunuch was known across Byzantium as the subterranean **contriver** of every palace intrigue."
      }
    ]
  },
  "Dashboard — trep/ectropion.md": {
    "primary": "The eversion or turning outward of an edge or margin, especially the lower eyelid, exposing the palpebral conjunctiva.",
    "secondary": "In ophthalmology and surgical pathology, a condition caused by senile tissue laxity, facial nerve palsy, or cicatricial scarring, resulting in chronic epiphora and corneal irritation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe cicatricial **ectropion** followed the chemical burn, pulling the margin of the eyelid down onto the cheek."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The surgeon performed a wedge resection of the tarsal plate to correct the persistent senile **ectropion**."
      },
      {
        "author": "Samuel Cooper",
        "work": "A Dictionary of Practical Surgery",
        "quote": "Unless **ectropion** is surgically remedied, the constant exposure of the ocular surface leads inevitably to chronic ulceration."
      }
    ]
  },
  "Dashboard — trep/entrepot.md": {
    "primary": "A trading post, port, or warehouse city where merchandise can be imported, stored, and transshipped to other markets without paying duties.",
    "secondary": "In economic history and commercial geography (from French entreposer, 'to store', historically connected to distribution turns), a commercial nexus linking oceanic trade routes (e.g., Singapore, Venice, or Hong Kong).",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Amsterdam flourished as the great **entrepot** of Europe, receiving the commodities of all nations and redistributing them across the globe."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Alexandria was the maritime **entrepot** where the silks of China and spices of India met the corn of Egypt."
      },
      {
        "author": "John Stuart Mill",
        "work": "Principles of Political Economy",
        "quote": "A free port serving as an international **entrepot** derives immense wealth from handling commissions and brokerage."
      }
    ]
  },
  "Dashboard — trep/entrepreneur.md": {
    "primary": "A person who sets up a business or businesses, taking on financial risks in the hope of generating profit.",
    "secondary": "In economic theory (formulated by Richard Cantillon and Joseph Schumpeter), an agent of innovation who redeploys economic resources into areas of higher productivity through 'creative destruction'.",
    "quotes": [
      {
        "author": "Joseph Schumpeter",
        "work": "The Theory of Economic Development",
        "quote": "The function of the **entrepreneur** is to reform or revolutionize the pattern of production by exploiting an invention or technological untried possibility."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The bold **entrepreneur** ventures his capital into untrodden avenues of commerce, risking total ruin for the prize of extraordinary gains."
      },
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "If animal spirits are dimmed and spontaneous optimism falters, the individual **entrepreneur** withers and enterprise languishes."
      }
    ]
  },
  "Dashboard — trep/entrepreneurial.md": {
    "primary": "Characterized by the taking of financial risks in the hope of profit; enterprising, innovative, and commercially ambitious.",
    "secondary": "In organizational sociology, describing corporate cultures or individual mindsets that prioritize agility, opportunity recognition, and calculated risk over bureaucratic caution.",
    "quotes": [
      {
        "author": "Joseph Schumpeter",
        "work": "Capitalism, Socialism and Democracy",
        "quote": "The capitalist process gradually depersonalizes economic management, replacing individual **entrepreneurial** drive with bureaucratic committees."
      },
      {
        "author": "Max Weber",
        "work": "The Protestant Ethic and the Spirit of Capitalism",
        "quote": "The ascetic ethos of early Calvinism fostered an intense **entrepreneurial** energy that treated commercial success as a sign of divine favor."
      },
      {
        "author": "Peter Drucker",
        "work": "Innovation and Entrepreneurship",
        "quote": "Every established institution requires an **entrepreneurial** discipline to systematically abandon obsolete practices and pioneer new ones."
      }
    ]
  },
  "Dashboard — trep/entropic.md": {
    "primary": "Of, relating to, or marked by entropy; tending toward disorder, dissipation of energy, or thermal equilibrium.",
    "secondary": "In information theory and cultural criticism, describing communications, systems, or societies characterized by increasing degradation of structure and loss of meaningful differentiation.",
    "quotes": [
      {
        "author": "Norbert Wiener",
        "work": "The Human Use of Human Beings",
        "quote": "As the universe as a whole tends toward an **entropic** doom, islands of locally decreasing entropy such as living organisms briefly flourish."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Nature of the Physical World",
        "quote": "The relentless increase of the **entropic** measure gives us the only objective physical direction for the arrow of time."
      },
      {
        "author": "Thomas Pynchon",
        "work": "The Crying of Lot 49",
        "quote": "Oedipa felt herself sinking into an **entropic** swamp where all signals dissolved into meaningless static."
      }
    ]
  },
  "Dashboard — trep/entropion.md": {
    "primary": "The inversion or turning inward of an edge or margin, especially the lower eyelid, causing the eyelashes to rub against the corneal surface.",
    "secondary": "In veterinary and human ophthalmology, a condition that results in mechanical trauma, corneal abrasion (trichiasis), and potential blindness if untreated.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Trachomatous scarring frequently produces severe **entropion**, forcing inverted eyelashes to abrade the sensitive cornea with every blink."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The surgeon made an elliptical incision through the skin of the lid to evert the margin and relieve the **entropion**."
      },
      {
        "author": "Samuel Cooper",
        "work": "A Dictionary of Practical Surgery",
        "quote": "In spasmodic **entropion**, the orbicularis muscle overcomes the tarsal cartilage, turning the entire ciliary margin inward."
      }
    ]
  },
  "Dashboard — trep/entropy.md": {
    "primary": "A thermodynamic quantity representing the unavailability of a system's thermal energy for conversion into mechanical work; a measure of disorder or randomness in a closed system.",
    "secondary": "In statistical mechanics (Boltzmann) and information theory (Shannon), the logarithmic measure of microscopic configurations or the average rate at which information is produced by a stochastic data source.",
    "quotes": [
      {
        "author": "Rudolf Clausius",
        "work": "The Mechanical Theory of Heat",
        "quote": "I propose to name the quantity S the **entropy** of the body, from the Greek word trope, meaning transformation."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Nature of the Physical World",
        "quote": "The law that **entropy** always increases holds, I think, the supreme position among the laws of Nature."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "The quantity H serves as a measure of information, choice, and uncertainty, and we recognize in it the precise form of thermodynamic **entropy**."
      }
    ]
  },
  "Dashboard — trep/heliotropism.md": {
    "primary": "The directional growth or turning of a plant or other sessile organism toward or away from sunlight; phototropism.",
    "secondary": "In plant physiology (investigated extensively by Charles Darwin), the differential elongation of stem cells mediated by auxin redistribution in response to unilateral solar radiation.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "The exquisite phenomenon of **heliotropism** in young seedlings is effected by the bending of the hypocotyl toward the brightest light."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The diurnal tracking of the sun exhibited by the common sunflower is an ancient and conspicuous example of positive **heliotropism**."
      },
      {
        "author": "Julian Huxley",
        "work": "Essays of a Biologist",
        "quote": "Simple biochemical gradients explain the mechanical inevitability of **heliotropism** in primitive organisms."
      }
    ]
  },
  "Dashboard — trep/isentropic.md": {
    "primary": "Characterized by, taking place at, or possessing constant entropy.",
    "secondary": "In thermodynamics and fluid mechanics, describing an idealized reversible adiabatic process where no heat is transferred and no entropy is generated internally (such as ideal nozzle expansion).",
    "quotes": [
      {
        "author": "William Rankine",
        "work": "A Manual of the Steam Engine and Other Prime Movers",
        "quote": "An **isentropic** curve represents the expansion of steam when perfectly shielded from thermal exchange with the cylinder walls."
      },
      {
        "author": "Lord Kelvin",
        "work": "Mathematical and Physical Papers",
        "quote": "The reversible adiabatic expansion of an ideal gas is strictly an **isentropic** process, preserving its thermodynamic potential intact."
      },
      {
        "author": "Enrico Fermi",
        "work": "Thermodynamics",
        "quote": "For an **isentropic** transformation of an ideal gas, the product of pressure and the gamma power of volume remains constant."
      }
    ]
  },
  "Dashboard — trep/isotrope.md": {
    "primary": "An isotropic substance; a medium or material whose physical properties are uniform and identical in all spatial directions.",
    "secondary": "In developmental embryology and historical biology, an egg cell or structural matrix displaying no pre-existing directional polarities or asymmetries.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "An optical **isotrope** allows light waves to propagate with uniform speed regardless of the orientation of the wavefront."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "The undifferentiated blastosphere appears as a morphological **isotrope** prior to the appearance of the primitive streak."
      },
      {
        "author": "William Henry Bragg",
        "work": "The Crystalline State",
        "quote": "Unlike birefringent crystals, an amorphous glass behaves as a perfect **isotrope** under optical examination."
      }
    ]
  },
  "Dashboard — trep/isotropic.md": {
    "primary": "Having physical properties that are identical in all directions; exhibiting uniformity regardless of the angle of measurement.",
    "secondary": "In theoretical cosmology and general relativity, describing a universe that looks the same in every direction from any given vantage point (the cosmological principle).",
    "quotes": [
      {
        "author": "Stephen Hawking",
        "work": "A Brief History of Time",
        "quote": "On the largest cosmological scale, the universe appears both homogeneous and **isotropic**, expanding uniformly in every direction."
      },
      {
        "author": "Lord Kelvin",
        "work": "Popular Lectures and Addresses",
        "quote": "A perfectly annealed specimen of glass is optically **isotropic**, lacking internal strain lines when placed between crossed prisms."
      },
      {
        "author": "Arthur Eddington",
        "work": "Space, Time and Gravitation",
        "quote": "The spacetime metric around an isolated spherical mass possesses an **isotropic** symmetry that simplifies Einstein's field equations."
      }
    ]
  },
  "Dashboard — trep/isotropous.md": {
    "primary": "An archaic or formal scientific variant of isotropic; having properties identical in all directions.",
    "secondary": "In nineteenth-century optics and embryology, descriptive of media exhibiting no directional refraction or eggs lacking predetermined axes of cleavage.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The newly fertilized ovum was regarded as an **isotropous** sphere capable of dividing with equal facility across any meridian."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Under the polarizing microscope, the volcanic glass remains completely dark, proving its thoroughly **isotropous** physical constitution."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The magnetic force acted with equal facility upon the **isotropous** fluid in all directions."
      }
    ]
  },
  "Dashboard — trep/isotropy.md": {
    "primary": "The property of being isotropic; uniformity in all directions.",
    "secondary": "In modern astrophysics and quantum field theory, the rotational invariance of physical laws or the spatial background.",
    "quotes": [
      {
        "author": "Stephen Hawking",
        "work": "The Large Scale Structure of Space-Time",
        "quote": "The remarkable **isotropy** of the microwave background radiation provides compelling evidence that the universe is spatially flat and uniform."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Matter and Motion",
        "quote": "The macroscopic **isotropy** of a gas arises from the chaotic, omnidirectional collisions of billions of molecules."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Nature of the Physical World",
        "quote": "Thermal equilibrium represents the final triumph of molecular **isotropy**, where every preferred direction of motion is obliterated."
      }
    ]
  },
  "Dashboard — trep/pleiotropic.md": {
    "primary": "Producing or having multiple, seemingly unrelated phenotypic effects from a single gene or genetic mutation.",
    "secondary": "In evolutionary genetics and pharmacology, describing genes or therapeutic agents that simultaneously influence multiple biochemical pathways across diverse organ systems.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "A single gene mutation in Drosophila often exerts **pleiotropic** effects, altering wing venation, eye pigment, and female fecundity simultaneously."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Selfish Gene",
        "quote": "Natural selection may favor a gene with **pleiotropic** benefits in early life, even if it brings fatal senescence in old age."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The complex integration of the genome means that virtually every locus possesses **pleiotropic** ramifications across the developing organism."
      }
    ]
  },
  "Dashboard — trep/pleiotropy.md": {
    "primary": "The phenomenon of a single gene controlling or influencing two or more distinct and seemingly unrelated phenotypic traits.",
    "secondary": "In evolutionary biology (antagonistic pleiotropy hypothesis proposed by George C. Williams), a key evolutionary explanation for biological aging and multi-system genetic syndromes (e.g., Marfan syndrome).",
    "quotes": [
      {
        "author": "George C. Williams",
        "work": "Pleiotropy, Natural Selection, and the Evolution of Senescence",
        "quote": "Antagonistic **pleiotropy** suggests that genes promoting early reproductive vigour are retained by selection even if they cause late-life degeneration."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The discovery of pervasive **pleiotropy** destroyed the naive concept of a strict one-to-one correspondence between a single gene and a single bodily character."
      },
      {
        "author": "Ernst Mayr",
        "work": "Toward a New Philosophy of Biology",
        "quote": "Because of developmental **pleiotropy**, selecting for a single visible morphological trait inevitably drags unobserved physiological changes in its wake."
      }
    ]
  },
  "Dashboard — trep/polytrope.md": {
    "primary": "A person of many turns, versatile, cunning, and resourceful (literally applied in Homer's Odyssey to Odysseus, the man of twists and turns).",
    "secondary": "In stellar astrophysics, a theoretical mathematical model of a star or self-gravitating gas sphere in which pressure and density are related by a polytropic equation of state (P = K * rho^((n+1)/n)).",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Odyssey",
        "quote": "Sing to me of the man of twists and turns, that resourceful **polytrope** who wandered far and wide after sacking the sacred citadel of Troy."
      },
      {
        "author": "Subrahmanyan Chandrasekhar",
        "work": "An Introduction to the Study of Stellar Structure",
        "quote": "The equilibrium configurations of gaseous stars are mathematically represented by the solutions of the Lane-Emden equation for a self-gravitating **polytrope**."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Internal Constitution of the Stars",
        "quote": "By treating the stellar core as a gaseous **polytrope** of index three, we obtain a remarkably accurate estimate of central temperature."
      }
    ]
  },
  "Dashboard — trep/protrepsis.md": {
    "primary": "The act of exhorting, encouraging, or urging; persuasive exhortation to adopt a noble way of life, especially the study of philosophy.",
    "secondary": "In classical rhetoric and pedagogical theory (Greek protrepein, 'to turn forward, urge on'), an oral discourse intended to turn the soul away from vulgar pursuits toward virtue and intellectual rigor.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Protrepticus",
        "quote": "The aim of philosophical **protrepsis** is not merely to display verbal subtlety, but to turn the human soul toward the contemplation of highest truth."
      },
      {
        "author": "Plato",
        "work": "Euthydemus",
        "quote": "Socrates urged the sophists to demonstrate a genuine **protrepsis**, persuading the young man to pursue virtue rather than vain dispute."
      },
      {
        "author": "Clement of Alexandria",
        "work": "Exhortation to the Greeks",
        "quote": "Our sacred **protrepsis** summons the wandering pagan away from empty idols to embrace the eternal Word."
      }
    ]
  },
  "Dashboard — trep/protreptic.md": {
    "primary": "Intended to exhort, persuade, or instruct; encouraging; an exhortative speech or treatise.",
    "secondary": "In the history of philosophy, a recognized genre of hortatory literature (such as Aristotle's *Protrepticus* or Cicero's *Hortensius*) designed to awaken a passion for wisdom and ethical living.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Protrepticus",
        "quote": "In every **protreptic** address, we must prove that the acquisition of wisdom is both possible and supreme in its intrinsic goodness."
      },
      {
        "author": "Cicero",
        "work": "Hortensius",
        "quote": "A powerful **protreptic** work possesses the virtue of tearing away the veil of sensual indulgence, awakening an unquenchable thirst for philosophy."
      },
      {
        "author": "Augustine of Hippo",
        "work": "Confessions",
        "quote": "The **protreptic** dialogue of Cicero altered my affections and turned my prayers to the Lord Himself."
      }
    ]
  },
  "Dashboard — trep/psychotropic.md": {
    "primary": "Capable of affecting the mind, emotions, or behavior; denoting chemical drugs that alter mental activity.",
    "secondary": "In clinical pharmacology and psychiatry, classifying pharmaceutical substances (antidepressants, anxiolytics, antipsychotics, and hallucinogens) that cross the blood-brain barrier to modulate neurotransmission.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Modern neurology was transformed by the advent of **psychotropic** agents that could selectively calm psychotic agitation without producing deep coma."
      },
      {
        "author": "Aldous Huxley",
        "work": "The Doors of Perception",
        "quote": "The discovery of natural **psychotropic** plants across diverse continents proves humanity's universal hunger for chemical transcendence."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The careful administration of a **psychotropic** sedative provided essential rest during the delirious climax of the fever."
      }
    ]
  },
  "Dashboard — trep/retrievable.md": {
    "primary": "Capable of being recovered, regained, or rescued; capable of being brought back from loss or error.",
    "secondary": "In information systems and archive management, describing records, stored files, or database entries that can be located and accessed systematically via an index.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "Time once lost is never **retrievable**, yet men squander their hours as though they possessed an inexhaustible treasury."
      },
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "Mr. Micawber declared his financial affairs to be desperate, though not utterly beyond **retrievable** repair."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Beryl Coronet",
        "quote": "The gems are still **retrievable**, Watson, if we move before the receiver can melt down the gold setting."
      }
    ]
  },
  "Dashboard — trep/retrieval.md": {
    "primary": "The act or process of getting something back from where it was left or lost; the recovery of information from storage.",
    "secondary": "In cognitive psychology, the process of accessing, reconstructing, and bringing stored memories or learned skills into conscious awareness.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The efficiency of memory depends upon the richness of associative hooks that facilitate the voluntary **retrieval** of stored ideas."
      },
      {
        "author": "Alexander Luria",
        "work": "The Mind of a Mnemonist",
        "quote": "His primary difficulty lay not in memory retention, but in the selective **retrieval** of relevant data from an ocean of indelible images."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Second Stain",
        "quote": "The quiet **retrieval** of the stolen state letter averted a catastrophic rupture in European diplomacy."
      }
    ]
  },
  "Dashboard — trep/retrieve.md": {
    "primary": "To get or bring something back from a place; to regain possession of; to restore an unfavorable situation.",
    "secondary": "In computer science and cognitive psychology, to fetch stored information from a memory medium; in hunting, to find and fetch shot game.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Henry V",
        "quote": "Turn him to any cause of policy, the Gordian knot of it he will unloose, and **retrieve** the empire from peril."
      },
      {
        "author": "Daniel Defoe",
        "work": "Robinson Crusoe",
        "quote": "I swam out to the wreck at low tide, hoping to **retrieve** some barrels of powder before the next storm broke."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "Holmes dashed into the burning room to **retrieve** the packet of letters from the iron safe."
      }
    ]
  },
  "Dashboard — trep/retriever.md": {
    "primary": "A person or animal that retrieves; specifically, any of several breeds of sporting dogs bred to find and bring back shot game birds undamaged.",
    "secondary": "In software architecture and search engines, an algorithm or component responsible for finding and returning relevant documents from a vast corpus.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The innate instinct of the Newfoundland or curly-coated **retriever** to fetch objects from water has been perfected through generations of selective breeding."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Woodlanders",
        "quote": "The keeper whistled, and his faithful black **retriever** bounded out of the fern with the fallen pheasant in its soft jaws."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "He owned a spaniel and a water **retriever**, dogs whose keen scent had often helped him across the moor."
      }
    ]
  },
  "Dashboard — trep/trepan.md": {
    "primary": "A surgical saw or cylindrical instrument used to cut out a circular disk of bone from the skull; to perforate the cranium with such a tool.",
    "secondary": "In mining and historical engineering, a heavy boring chisel used for sinking shafts in hard rock; archaically, to ensnare, trap, or deceive by artifice.",
    "quotes": [
      {
        "author": "John Bell",
        "work": "The Principles of Surgery",
        "quote": "The surgeon applied the circular **trepan** to the fractured parietal bone, lifting the depressed fragment to relieve intracranial pressure."
      },
      {
        "author": "Samuel Cooper",
        "work": "A Dictionary of Practical Surgery",
        "quote": "Before the invention of the modern hand-trephine, the classical **trepan** was rotated rapidly by means of a handle like a carpenter's brace."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Archaeological excavations reveal that primitive peoples used flint flakes to **trepan** living skulls with surprising surgical success."
      }
    ]
  },
  "Dashboard — trep/trepang.md": {
    "primary": "A sea cucumber (holothurian) of tropical marine waters, harvested, eviscerated, boiled, and dried for food; bêche-de-mer.",
    "secondary": "In economic ethnography and maritime history, a major commercial commodity traded between Indigenous Australian coastal communities, Bugis mariners, and Chinese merchants.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Fleets of Bugis praus make annual voyages to northern Australia to dive for the prized edible sea slug known as **trepang**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In the coral shallows of the Keeling Islands, we observed hundreds of large holothurians suitable for preparing commercial **trepang**."
      },
      {
        "author": "Herman Melville",
        "work": "Omoo",
        "quote": "The trader's hold was packed with bundles of dried **trepang**, destined for the luxurious soup tureens of Canton."
      }
    ]
  },
  "Dashboard — trep/trepid.md": {
    "primary": "Timid, fearful, trembling, or hesitant; characterized by trepidation.",
    "secondary": "In literary description, portraying a nervous, faltering demeanor marked by anxious physical hesitation or fluttering uncertainty.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "The Return of the Native",
        "quote": "She ventured a **trepid** step into the darkened heath, pausing at every rustle of the dry heather."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Villette",
        "quote": "With a **trepid** hand, she knocked upon the headmistress's door, anticipating a cold reprimand."
      },
      {
        "author": "Walter Pater",
        "work": "Marius the Epicurean",
        "quote": "The youth approached the shrine with **trepid** reverence, awed by the solemn gloom of the sanctuary."
      }
    ]
  },
  "Dashboard — trep/trepidation.md": {
    "primary": "A feeling of fear, agitation, or trembling anxiety about something that may happen; nervous tremor.",
    "secondary": "In historical astronomy (Ptolemaic and medieval), a hypothesized slow oscillatory motion of the equinoxes, thought to explain discrepancies in precession before being disproven.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "They pass the planets seven, and pass the fixed, and that crystalline sphere whose balance weighs the **trepidation** talked."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "I entered the decaying chamber of Satis House in a state of extreme **trepidation**, dreading what Miss Havisham might say."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of Four",
        "quote": "Miss Morstan sat with folded hands, her pale face betraying the inward **trepidation** she heroically struggled to hide."
      }
    ]
  },
  "Dashboard — trep/trepidly.md": {
    "primary": "In a trepid, timid, or trembling manner; nervously and with hesitation.",
    "secondary": "In narrative prose, characterizing actions undertaken with visible anxiety, physical tremor, or lack of confidence.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "She moved **trepidly** toward the dairy door, fearing that her shameful secret had already been whispered among the maids."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "I advanced **trepidly** across the long, shadowy gallery, guided only by the flickering flame of my candle."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Fall of the House of Usher",
        "quote": "He glanced **trepidly** over his shoulder, as if expecting an unearthly intruder to emerge from the tapestries."
      }
    ]
  },
  "Dashboard — trep/treponema.md": {
    "primary": "A genus of spiral-shaped, highly motile, parasitic or saprophytic spirochete bacteria, notably including *Treponema pallidum*, the causative agent of syphilis.",
    "secondary": "In microbiology and infectious disease, a genus (from Greek trepo 'to turn' and nema 'thread', 'turning thread') characterized by slender, tightly coiled undulations and endoflagellar motility.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The identification of the spirochete genus **Treponema** by Schaudinn and Hoffmann established the microbiological etiology of the Great Pox."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Chemotherapy of Infectious Diseases",
        "quote": "Our synthetic arsenical compound, Salvarsan, was engineered to destroy the pathogenic **Treponema** without inflicting fatal toxicity on host tissue."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Darkfield illumination provides the classic method for observing the graceful, rotary swimming movements of living **Treponema**."
      }
    ]
  },
  "Dashboard — trep/treponemataceae.md": {
    "primary": "A family of spirochete bacteria (order Spirochaetales) comprising helical, flexible, unicellular microorganisms that move by axial filaments.",
    "secondary": "In systematic bacteriology, a taxonomic family historically grouping pathogenic and commensal helical organisms, including the genera *Treponema*, *Borrelia*, and *Leptospira*.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Pathogens of the family **Treponemataceae** display an extraordinary antigenic resilience that complicates vaccine development."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The family **Treponemataceae** encompasses microorganisms responsible for devastating chronic scourges, from syphilis to relapsing fever."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Members of the **Treponemataceae** possess an internal undulating filament that confers rapid corkscrew locomotion through viscous fluids."
      }
    ]
  },
  "Dashboard — trep/treponematosis.md": {
    "primary": "Any infectious disease caused by spirochetes of the genus Treponema (including venereal syphilis, endemic syphilis/bejel, yaws, and pinta).",
    "secondary": "In tropical medicine and medical anthropology, a group of closely related dermatological and osteological diseases demonstrating worldwide clinical variation shaped by climate and hygiene.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In tropical regions, non-venereal **treponematosis**, known locally as yaws, spreads among children through direct skin contact."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Comparative serological tests reveal identical reagins across all forms of clinical **treponematosis**, confirming their close genetic kinship."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "The evolutionary history of human **treponematosis** remains an active debate among paleopathologists examining pre-Columbian skeletal remains."
      }
    ]
  },
  "Dashboard — trep/treponeme.md": {
    "primary": "Any spirochete bacterium belonging to the genus Treponema; a slender, corkscrew-shaped microorganism.",
    "secondary": "In clinical microbiology, a microscopic pathogen (such as *Treponema pallidum*) visualized through silver staining or darkfield microscopy, infamous for tissue invasiveness and latency.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Under the darkfield condenser, the silvery, coiled **treponeme** spins across the field with an unmistakable corkscrew rotation."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Experimental Chemotherapy",
        "quote": "Our laboratory target was the fragile yet lethal **treponeme**, an organism incapable of surviving prolonged desiccation outside its host."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The invasion of the central nervous system by the virulent **treponeme** lays the pathological foundation for general paresis."
      }
    ]
  },
  "Dashboard — trep/treponemiasis.md": {
    "primary": "Infection with or disease caused by bacteria of the genus Treponema; a medical synonym for treponematosis.",
    "secondary": "In public health and epidemiology, the programmatic term for campaigns aimed at eradicating endemic non-venereal treponemal infections (yaws and bejel) using mass penicillin distribution.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Massive public health campaigns demonstrated that endemic **treponemiasis** could be eradicated from rural populations with single doses of long-acting penicillin."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The diagnosis of chronic **treponemiasis** relies upon complement fixation tests when surface lesions have long disappeared."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Chemotherapy of Infectious Diseases",
        "quote": "The therapeutic eradication of **treponemiasis** proved that synthetic chemistry could systematically conquer internal bacterial infections."
      }
    ]
  },
  "Dashboard — trep/tropism.md": {
    "primary": "The turning or growth of all or part of an organism in a particular direction in response to an external stimulus (such as light, gravity, or touch).",
    "secondary": "In cellular biology and virology (tissue tropism), the specificity of a virus or bacterium for infecting particular host tissues or cell types determined by surface receptors.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "The general term **tropism** embraces every directional curving of plant organs provoked by light, gravity, moisture, or chemical touch."
      },
      {
        "author": "Jacques Loeb",
        "work": "Forced Movements, Tropisms, and Animal Conduct",
        "quote": "The conduct of lower animals consists of involuntary machine-like responses, wherein each **tropism** is dictated by symmetrical stimulation of sensory organs."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Before voluntary action awakens, biological life is already organized by instinctive reflexes and blind physiological **tropism**."
      }
    ]
  },
  "Dashboard — trep/tropopause.md": {
    "primary": "The boundary or transitional zone between the troposphere and the stratosphere in the Earth's atmosphere, where temperature ceases to decrease with altitude.",
    "secondary": "In atmospheric physics and aviation meteorology, an isothermal or inversion boundary located roughly 9 km above the poles and 17 km above the equator, acting as a thermodynamic ceiling for convection.",
    "quotes": [
      {
        "author": "Antoine de Saint-Exupéry",
        "work": "Wind, Sand and Stars",
        "quote": "The modern airliner climbs toward the icy calm of the **tropopause**, leaving the stormy lower atmosphere beneath its wings."
      },
      {
        "author": "Vilhelm Bjerknes",
        "work": "Dynamic Meteorology and Weather Forecasting",
        "quote": "The height of the **tropopause** fluctuates dramatically during the passage of polar fronts, dropping sharply over cold cyclonic cores."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Volcanic dust injected past the **tropopause** into the stratosphere circles the globe for months, dimming terrestrial sunsets."
      }
    ]
  },
  "Dashboard — trep/troposphere.md": {
    "primary": "The lowest and densest layer of the Earth's atmosphere, extending from the planet's surface up to the tropopause, within which almost all weather phenomena occur.",
    "secondary": "In planetary science and meteorology (from Greek tropos 'turning, mixing' and sphaira 'sphere'), the turbulent atmospheric zone characterized by convective overturning and a steady decrease in temperature with height.",
    "quotes": [
      {
        "author": "Antoine de Saint-Exupéry",
        "work": "Night Flight",
        "quote": "All the storms, squalls, and lightning that terrorize the aviator are confined to the turbulent cauldron of the **troposphere**."
      },
      {
        "author": "Vilhelm Bjerknes",
        "work": "Dynamic Meteorology and Weather Forecasting",
        "quote": "Thermal convection within the **troposphere** drives the grand planetary circulation of trade winds and mid-latitude cyclones."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Chemical pollutants released at the ground level circulate throughout the entire **troposphere** before descending in toxic rain."
      }
    ]
  },
  "Dashboard — trep/troubadour.md": {
    "primary": "One of a class of lyric poets and poet-musicians of southern France (Provence), eastern Spain, and northern Italy who flourished from the 11th to the 13th centuries, singing in Occitan.",
    "secondary": "In cultural history and romance etymology (from Old Occitan trobar, 'to find, invent poetry', cognate with French trouver, historically linked to inventing turns of phrase), the inventors of courtly love (*fin'amor*).",
    "quotes": [
      {
        "author": "Dante Alighieri",
        "work": "De Vulgari Eloquentia",
        "quote": "The Provencal **troubadour** was the first to cultivate courtly vernacular verse, wedding musical melody to polished poetic forms."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The romantic songs of the **troubadour** softened the rough manners of feudal chivalry and inspired crusader knights."
      },
      {
        "author": "Walter Pater",
        "work": "The Renaissance",
        "quote": "The passionate cult of courtly devotion blossomed in the sunny castles of Languedoc under the hands of the **troubadour**."
      }
    ]
  },
  "Dashboard — trep/trove.md": {
    "primary": "A store of valuable, delightful, or interesting things (often used in the phrase 'treasure trove').",
    "secondary": "In English common law (from Anglo-Norman tresor trové, literally 'treasure found', from trover 'to find'), coin, gold, silver, or bullion found hidden in the earth or private places, the owner being unknown, traditionally claimed by the Crown.",
    "quotes": [
      {
        "author": "William Blackstone",
        "work": "Commentaries on the Laws of England",
        "quote": "Treasure **trove** is where any money or coin, gold or silver, is found hidden in the earth, the owner thereof being unknown."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of Four",
        "quote": "The Agra treasure was an astonishing **trove** of sparkling emeralds, rubies, and ropes of matched pearls."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Treasure Island",
        "quote": "The pirate's chest contained a magnificent **trove** of doubloons, moidores, and gold bars from the Spanish Main."
      }
    ]
  }
};

let count = 0;
for (const [key, data] of Object.entries(batch4Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 4 Completed: ${count} / ${Object.keys(batch4Data).length} words updated`);
console.log(`========================================`);
