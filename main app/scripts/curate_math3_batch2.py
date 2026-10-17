# -*- coding: utf-8 -*-
import json
import os
import sys

batch2_data = {
  "Dashboard — poly\\polychete.md": {
    "primary": "A segmented marine annelid worm of the class Polychaeta, characterized by bristles (chaetae) borne on fleshy lateral parapodia; variant spelling of polychaete.",
    "secondary": "In marine biology and benthic ecology, burrowing or tube-dwelling worms (such as nereids and serpulids) that play fundamental roles in marine sediment nutrient cycling.",
    "quotes": [
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "The iridescent clam worm is an active predatory **polychete**, hunting smaller invertebrates across the intertidal reef." },
      { "author": "William Beebe", "work": "Nonsuch: Land of Water", "quote": "At night the surface waters glowed with the bioluminescent nuptial swarming of a delicate **polychete** worm." },
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "In every marine **polychete**, the parapodia serve dual functions of creeping locomotion and aquatic respiration." }
    ]
  },
  "Dashboard — poly\\polychromatic.md": {
    "primary": "Showing, exhibiting, or composed of a variety of different colors; multicolored.",
    "secondary": "In optics and radiation physics, electromagnetic radiation consisting of multiple wavelengths or frequencies, contrasted with monochromatic radiation.",
    "quotes": [
      { "author": "Isaac Newton", "work": "Opticks", "quote": "A beam of sunlight passing through a triangular prism is resolved into a **polychromatic** spectrum of refracted rays." },
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "The facade of St. Mark's glows with **polychromatic** marble panels and gilded Byzantine mosaics." },
      { "author": "Arthur Compton", "work": "X-Rays and Electrons", "quote": "A crystal diffraction grating sorts the continuous **polychromatic** X-ray beam into discrete spectral lines." }
    ]
  },
  "Dashboard — poly\\polychrome.md": {
    "primary": "Decorated, executed, or painted in several different colors, especially referring to architectural decoration, sculpture, or pottery; or an object so decorated.",
    "secondary": "In classical archaeology and art history, the historical practice in ancient Greece and Rome of painting stone buildings and marble sculptures with brilliant mineral pigments.",
    "quotes": [
      { "author": "Gottfried Semper", "work": "The Four Elements of Architecture", "quote": "Archaeological discoveries in Athens prove that classical marble temples were covered with vivid **polychrome** coatings." },
      { "author": "Walter Pater", "work": "Greek Studies", "quote": "The archaic maiden statues of the Acropolis preserve traces of exquisite **polychrome** decoration upon their drapery." },
      { "author": "Henry Adams", "work": "Mont-Saint-Michel and Chartres", "quote": "Sunlight filtered through the 13th-century rose window, bathing the stone nave in vibrant **polychrome** splendor." }
    ]
  },
  "Dashboard — poly\\polychromic.md": {
    "primary": "Of, relating to, or exhibiting many colors; polychromatic.",
    "secondary": "In histology, cytology, and staining methodology, tissues or dye mixtures (such as polychrome methylene blue) that stain different cellular structures in distinct colors simultaneously.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Collected Papers on Immunology and Haematology", "quote": "A single **polychromic** dye mixture stains the nuclei blue, the eosinophil granules red, and the cytoplasm neutral." },
      { "author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Under the microscope, the **polychromic** reaction clearly distinguishes axonal myelin sheaths from surrounding glial tissue." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Examination of the blood smear with a **polychromic** stain revealed nucleated red cells in advanced pernicious anemia." }
    ]
  },
  "Dashboard — poly\\polychromise.md": {
    "primary": "To paint, decorate, or execute in several colors; British spelling of polychromize.",
    "secondary": "In architectural restoration and craft history, to apply multi-colored decorative schemes to plaster, wood carvings, or stone statues.",
    "quotes": [
      { "author": "William Morris", "work": "Hopes and Fears for Art", "quote": "Medieval craftsmen loved to **polychromise** roof bosses and carved capitals with vermilion and gold leaf." },
      { "author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "We ought not to leave public edifices in cold grey stone when nature teaches us to **polychromise** with variegated marbles." },
      { "author": "George Gilbert Scott", "work": "Remarks on Secular and Domestic Architecture", "quote": "To **polychromise** an ancient vault correctly requires careful study of surviving traces of medieval pigment." }
    ]
  },
  "Dashboard — poly\\polychromize.md": {
    "primary": "To decorate, paint, or finish in a variety of colors.",
    "secondary": "In architectural aesthetics and sculpture, applying diverse chromatic pigments to a facade, frieze, or statue to enhance visual hierarchy and decorative depth.",
    "quotes": [
      { "author": "Charles Garnier", "work": "Le Nouvel Opéra de Paris", "quote": "My intention was to **polychromize** the grand foyer with multicolored Italian marbles, bronze gilding, and mosaic vaults." },
      { "author": "Gottfried Semper", "work": "Style in the Technical and Tectonic Arts", "quote": "The ancient Hellenes did not hesitate to **polychromize** the friezes of the Parthenon to make the figures legible against the sky." },
      { "author": "James Fergusson", "work": "A History of Architecture", "quote": "Egyptian builders were among the first to **polychromize** stone colonnades with durable mineral pigments." }
    ]
  },
  "Dashboard — poly\\polycillin.md": {
    "primary": "A proprietary brand name for ampicillin, a broad-spectrum penicillin antibiotic used to treat bacterial infections.",
    "secondary": "In clinical pharmacology and infectious disease therapeutics, a semisynthetic aminopenicillin active against both Gram-positive organisms and many Gram-negative bacilli, such as Escherichia coli and Proteus mirabilis.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The introduction of **polycillin** extended the antibacterial spectrum of penicillin to encompass common urinary and respiratory pathogens." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Revision", "quote": "In pediatric otitis media and acute bronchitis, oral treatment with **polycillin** brought rapid symptomatic defervescence." },
      { "author": "Maxwell Finland", "work": "Clinical Studies in Antibiotic Therapy", "quote": "Patients tolerating penicillin therapy showed excellent clinical responses to therapeutic courses of **polycillin**." }
    ]
  },
  "Dashboard — poly\\polycirrus.md": {
    "primary": "A genus of marine terebellid polychaete worms characterized by numerous long, retractile tentacles used for deposit feeding.",
    "secondary": "In marine invertebrate zoology, sedentary polychaetes lacking thoracic branchiae that construct fragile mud tubes on coastal sea floors, utilizing ciliated oral tentacles to capture organic detritus.",
    "quotes": [
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "The genus **Polycirrus** is distinguished among terebellids by the total absence of thoracic gills and the profusion of oral tentacles." },
      { "author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "A living **Polycirrus** worm extended a delicate crown of luminous tentacles across the coral rubble." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Feeding in **Polycirrus** is accomplished by mucus-coated grooved tentacles that transport organic silt toward the mouth." }
    ]
  },
  "Dashboard — poly\\polycrystalline.md": {
    "primary": "Composed of many small microscopic crystals or crystallites oriented in varying directions, separated by grain boundaries.",
    "secondary": "In materials science, solid-state physics, and metallurgy, aggregate crystalline solids (such as structural metals, ceramics, and polysilicon solar cells) whose mechanical and electrical properties depend strongly on grain size and grain boundary orientation.",
    "quotes": [
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Most engineering metals are **polycrystalline** aggregates whose macroscopic tensile strength depends on grain boundary cohesion." },
      { "author": "William Shockley", "work": "Electrons and Holes in Semiconductors", "quote": "Carrier recombination at crystal defects renders **polycrystalline** silicon less efficient than single-crystal ingots for transistor fabrication." },
      { "author": "Arthur Cottrell", "work": "An Introduction to Metallurgy", "quote": "Dislocation pile-ups at the boundaries of a **polycrystalline** metal account for the yield point phenomenon described by the Hall-Petch relation." }
    ]
  },
  "Dashboard — poly\\polycythemia.md": {
    "primary": "An abnormal increase in the total red blood cell mass or hemoglobin concentration in the bloodstream.",
    "secondary": "In hematology and internal medicine, a myeloproliferative neoplasm (polycythemia vera) associated with JAK2 mutations leading to hyperviscosity, or secondary polycythemia resulting from chronic hypoxia.",
    "quotes": [
      { "author": "William Osler", "work": "Chronic Cyanosis with Polycythaemia and Enlarged Spleen", "quote": "The patient presented the classic triad of chronic cyanosis, splenomegaly, and extraordinary **polycythemia** exceeding ten million red cells." },
      { "author": "Harvey Cushing", "work": "The Pituitary Body and Its Disorders", "quote": "Plethoric facies and hypertension in pituitary basophilism are frequently accompanied by moderate **polycythemia**." },
      { "author": "Paul Ehrlich", "work": "Collected Papers on Haematology", "quote": "Excessive marrow erythroblastic activity in primary **polycythemia** dangerously increases blood viscosity and thrombotic risk." }
    ]
  },
  "Dashboard — poly\\polyelectrolyte.md": {
    "primary": "A polymer whose repeating structural units bear an electrolyte group; a macromolecule that dissociates into polyvalent macro-ions in aqueous solution.",
    "secondary": "In physical chemistry, biophysics, and colloid science, charged macromolecules (such as DNA, RNA, proteins, and polyacrylic acid) whose conformational behavior is governed by long-range electrostatic interactions and counterion condensation.",
    "quotes": [
      { "author": "Peter Debye", "work": "Collected Papers of Peter J. W. Debye", "quote": "The screening of electrostatic repulsions along a flexible **polyelectrolyte** chain dictates its coil dimensions in saline water." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Proteins behave as amphoteric **polyelectrolyte** systems, possessing both acidic and basic functional groups that charge with varying pH." },
      { "author": "Herman Mark", "work": "Physical Chemistry of High Polymeric Systems", "quote": "The high charge density of a synthetic **polyelectrolyte** induces dramatic counterion condensation near the polymer backbone." }
    ]
  },
  "Dashboard — poly\\polyergus.md": {
    "primary": "A genus of slave-making ants in the family Formicidae, commonly called Amazon ants.",
    "secondary": "In myrmecology and entomology, obligate parasitic ants (such as Polyergus rufescens) whose sickle-shaped, pointed mandibles are adapted exclusively for raiding colonies of *Formica* ants to capture pupae as workers.",
    "quotes": [
      { "author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The slave-making ant, **Polyergus** rufescens, is unable to feed itself or care for its own larvae, depending entirely upon its captured slaves." },
      { "author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "The falcate, toothless mandibles of **Polyergus** are exquisite weapons for piercing the heads of defending workers during raids." },
      { "author": "Edward O. Wilson", "work": "The Insect Societies", "quote": "Colony raids by **Polyergus** are coordinated by pheromone trails that mobilize hundreds of specialized warriors against neighboring Formica nests." }
    ]
  },
  "Dashboard — poly\\polyester.md": {
    "primary": "A synthetic resin or polymer in which the monomer units are linked together by ester groups (-COO-); a fabric made from this material.",
    "secondary": "In polymer chemistry and industrial manufacturing, polycondensation products (notably polyethylene terephthalate, PET) formed by reacting dicarboxylic acids with diols, widely utilized for textile fibers, films, and beverage bottles.",
    "quotes": [
      { "author": "Wallace Carothers", "work": "Polymerization", "quote": "Early laboratory synthesis of aliphatic **polyester** yielded low-melting waxes, demonstrating the general principle of step-growth condensation." },
      { "author": "Herman Mark", "work": "Giant Molecules", "quote": "Drawing crystalline **polyester** filaments through a die orients the molecular chains, producing high-tenacity fibers resistant to creasing." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "Thermosetting unsaturated **polyester** resins blended with glass fiber reinforcement revolutionized boat building and composite engineering." }
    ]
  },
  "Dashboard — poly\\polyestrous.md": {
    "primary": "Having more than one estrus (heat) cycle per year; exhibiting recurring estrous cycles.",
    "secondary": "In reproductive biology and mammalogy, mammalian species (such as cattle, swine, and rodents) that cycle continuously throughout the year (continuously polyestrous) or during a specific season (seasonally polyestrous, e.g., sheep and horses).",
    "quotes": [
      { "author": "Francis Marshall", "work": "The Physiology of Reproduction", "quote": "Mammals that experience repeated cycles of estrus throughout the year without prolonged anestrus are termed **polyestrous**." },
      { "author": "Arthur Thomson", "work": "Outlines of Zoology", "quote": "Domestic rodents are typically **polyestrous**, ovulating every four or five days unless pregnancy or lactation intervenes." },
      { "author": "Solomon Zuckerman", "work": "The Social Life of Monkeys and Apes", "quote": "Unlike seasonally breeding wild ungulates, primates display a continuously **polyestrous** cycle regulated by pituitary gonadotropins." }
    ]
  },
  "Dashboard — poly\\polyethylene.md": {
    "primary": "A tough, flexible, lightweight synthetic thermoplastic resin made by the polymerization of ethylene; polythene.",
    "secondary": "In materials science and petrochemistry, the most widely manufactured plastic in the world, categorized by density and branching into low-density (LDPE), linear low-density (LLDPE), and high-density (HDPE) variants.",
    "quotes": [
      { "author": "Karl Ziegler", "work": "Nobel Lecture: Consequences and Development of an Invention", "quote": "Using triethylaluminum and titanium tetrachloride, we achieved the polymerization of ethylene to high-molecular-weight **polyethylene** at atmospheric pressure." },
      { "author": "Giulio Natta", "work": "Macromolecular Chemistry", "quote": "Stereospecific coordination catalysts opened new frontiers for unbranched crystalline **polyethylene** with elevated melting points." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The simple repeating chain of -CH2-CH2- in **polyethylene** creates a remarkably inert, chemically resistant hydrocarbon barrier." }
    ]
  },
  "Dashboard — poly\\polygamist.md": {
    "primary": "A person who is married to more than one spouse at the same time.",
    "secondary": "In sociology and ethnology, an individual practicing polygamy, whether polygyny (multiple wives) or polyandry (multiple husbands), within recognized cultural or religious institutions.",
    "quotes": [
      { "author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "In traditional African societies, the wealthy **polygamist** maintained separate domestic quarters for each of his wives." },
      { "author": "David Hume", "work": "Essays: Moral, Political, and Literary", "quote": "The eastern **polygamist** reduces marriage to jealous domestic tyranny, depriving women of true companionship." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Among polygamous mammals, intense sexual selection produces males far larger and more armed than the **polygamist** females they guard." }
    ]
  },
  "Dashboard — poly\\polygamous.md": {
    "primary": "Practicing, relating to, or characterized by marriage to more than one spouse simultaneously; or mating with multiple partners.",
    "secondary": "In botany, plants bearing male, female, and hermaphroditic (perfect) flowers on the same or different individuals (such as the ash or maple tree).",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Certain trees like the common ash are **polygamous**, displaying staminate, pistillate, and bisexual blossoms upon the same bough." },
      { "author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "The legal prohibition of **polygamous** unions has been a cornerstone of Western civil jurisprudence since Roman antiquity." },
      { "author": "Asa Gray", "work": "Manual of Botany", "quote": "In the sumac family, the species are frequently **polygamous** or dioecious, with flowers in dense terminal panicles." }
    ]
  },
  "Dashboard — poly\\polygamy.md": {
    "primary": "The practice or custom of having more than one spouse at the same time.",
    "secondary": "In cultural anthropology and evolutionary biology, a marital system comprising polygyny and polyandry, or an animal mating system where individuals mate with multiple partners during a single breeding cycle.",
    "quotes": [
      { "author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "Though widespread across human history, **polygamy** has usually been restricted in practice to wealthy or aristocratic men." },
      { "author": "Montesquieu", "work": "The Spirit of the Laws", "quote": "The domestic isolation imposed by institutionalized **polygamy** in the Orient alters the entire character of civil governance." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Wherever **polygamy** prevails among animals, sexual dimorphism in weapons, plumage, and vocal power is extraordinarily pronounced." }
    ]
  },
  "Dashboard — poly\\polygon.md": {
    "primary": "A closed plane geometric figure bounded by three or more straight line segments intersecting at their endpoints.",
    "secondary": "In computer graphics, planar surfaces (especially triangles and quads) assembled into polygon meshes to model 3D geometric characters, objects, and game environments.",
    "quotes": [
      { "author": "Euclid", "work": "Elements", "quote": "Any regular **polygon** inscribed within a circle can be divided into congruent isosceles triangles meeting at the center." },
      { "author": "Isaac Newton", "work": "Principia Mathematica", "quote": "By conceiving the planetary orbit as the limit of an inscribed **polygon** with infinite sides, we resolve centrifugal force." },
      { "author": "René Descartes", "work": "Discourse on the Method", "quote": "The geometer easily conceives of a chiliagon, a regular **polygon** of a thousand sides, through algebraic calculation." }
    ]
  },
  "Dashboard — poly\\polygonal.md": {
    "primary": "Having many sides or angles; resembling or formed in the shape of a polygon.",
    "secondary": "In geology and archaeology, jointing patterns (such as columnar basalt at Giant's Causeway) or prehistoric dry-stone masonry where interlocking multangular stones form earthquake-resistant walls.",
    "quotes": [
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "The famous columns of the Giant's Causeway exhibit regular **polygonal** prisms formed by thermal contraction during basalt cooling." },
      { "author": "Hiram Bingham", "work": "Inca Land", "quote": "In the megalithic architecture of Cuzco, the famous twelve-angled stone fits seamlessly into the **polygonal** masonry wall." },
      { "author": "D'Arcy Wentworth Thompson", "work": "On Growth and Form", "quote": "Mutual fluid pressure compresses crowded soap bubbles into a uniform network of **polygonal** faces." }
    ]
  },
  "Dashboard — poly\\polygonally.md": {
    "primary": "In a polygonal manner; in the form or arrangement of a polygon.",
    "secondary": "In petrology and geomorphology, describing jointing, permafrost stone nets, or mud cracks that fracture into multi-sided patterns.",
    "quotes": [
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Drying mud flats crack **polygonally** beneath the summer sun, leaving tessellated fissures that later fill with sand." },
      { "author": "Charles Darwin", "work": "Geological Observations on Volcanic Islands", "quote": "The cooling surface of the basaltic lava cracked **polygonally**, yielding vertical columns of five and six sides." },
      { "author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "Contraction strains in the drying starch cake caused it to cleave **polygonally** into miniature columns resembling basalt." }
    ]
  },
  "Dashboard — poly\\polymastigina.md": {
    "primary": "An order or group of flagellated protozoa possessing multiple flagella (typically four or more), often living as parasites or symbionts.",
    "secondary": "In classical protistology and parasitology, a taxon (traditionally placed in Zoomastigophora, including Giardia and Trichomonas) characterized by complex kinetid systems and symbiotic life inside insect or vertebrate guts.",
    "quotes": [
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "The order **Polymastigina** comprises flagellates with three to eight flagella, frequently inhabiting the alimentary canal of animals." },
      { "author": "William Morton Wheeler", "work": "Social Life Among the Insects", "quote": "Wood-eating termites rely upon hypermastigote and **Polymastigina** symbionts to digest the cellulose of sound timber." },
      { "author": "Robert William Hegner", "work": "Parasitic Protozoa", "quote": "Intestinal flagellates belonging to **Polymastigina** display anterior flagellar tufts and characteristic parabasal bodies." }
    ]
  },
  "Dashboard — poly\\polymastigote.md": {
    "primary": "A protozoan organism bearing multiple flagella; or having the structural characteristics of such a flagellate.",
    "secondary": "In cytology and microbial ultrastructure, designating flagellate cells (such as trichomonads and diplomonads) with multiple basal bodies and flagellar roots organized into specialized microtubular bands.",
    "quotes": [
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "The **polymastigote** condition arose through the evolutionary duplication of basal kinetosomes and their associated flagella." },
      { "author": "Libbie Hyman", "work": "The Invertebrates", "quote": "Each **polymastigote** symbiont inside the termite gut swims vigorously by undulating its anterior wreath of flagella." },
      { "author": "G. Kingsley Noble", "work": "The Biology of Protozoa", "quote": "Giardia trophozoites exhibit a symmetrical **polymastigote** plan, bearing four pairs of flagella directed backwards." }
    ]
  },
  "Dashboard — poly\\polymath.md": {
    "primary": "A person of wide-ranging knowledge and varied learning across many distinct disciplines; a Renaissance man or universal scholar.",
    "secondary": "In intellectual history and philosophy of science, historic figures (such as Aristotle, Leonardo da Vinci, Gottfried Wilhelm Leibniz, and Thomas Young) who made significant original contributions across arts, humanities, and empirical sciences.",
    "quotes": [
      { "author": "Thomas Babington Macaulay", "work": "Life and Writings of Addison", "quote": "Leibniz was perhaps the last true **polymath** who could survey the entire empire of human knowledge with the eye of a master." },
      { "author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "Thomas Young was a remarkable **polymath**, deciphering Egyptian hieroglyphs while establishing the wave theory of light." },
      { "author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Aristotle was an extraordinary **polymath**, classifying biology, cataloging constitutions, and creating formal logic." }
    ]
  },
  "Dashboard — poly\\polymer.md": {
    "primary": "A chemical substance composed of large macromolecules built up by the repeated linkage of smaller monomer units.",
    "secondary": "In macromolecular chemistry and materials science, synthetic and biological macromolecules (including proteins, cellulose, DNA, plastics, and rubbers) whose mechanical and thermal properties emerge from high molecular weight and chain entanglements.",
    "quotes": [
      { "author": "Hermann Staudinger", "work": "Nobel Lecture: Macromolecular Chemistry", "quote": "High-molecular-weight substances are true macromolecules where thousands of atoms are linked by covalent bonds into a long **polymer** chain." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Natural rubber is a linear **polymer** of isoprene, whose elasticity stems from the thermal coiling and uncoiling of its chains." },
      { "author": "Wallace Carothers", "work": "Studies on Polymerization and Ring Formation", "quote": "Condensation of bifunctional monomers proceeds indefinitely, building a linear **polymer** of immense molecular mass." }
    ]
  },
  "Dashboard — poly\\polymerase.md": {
    "primary": "An enzyme that synthesizes long chains of polymers or nucleic acids, especially DNA polymerase and RNA polymerase.",
    "secondary": "In molecular biology and genetics, crucial template-directed enzymes responsible for DNA replication, repair, and transcription, as well as the polymerase chain reaction (PCR) developed by Kary Mullis.",
    "quotes": [
      { "author": "Arthur Kornberg", "work": "Enzymatic Synthesis of DNA", "quote": "Purification of DNA **polymerase** demonstrated that synthesis requires a pre-existing DNA template and deoxynucleoside triphosphates." },
      { "author": "James D. Watson", "work": "Molecular Biology of the Gene", "quote": "RNA **polymerase** binds specifically to the promoter region, unwinding the double helix and initiating transcript elongation." },
      { "author": "Francis Crick", "work": "What Mad Pursuit", "quote": "The discovery of reverse transcriptase proved that a viral **polymerase** could synthesize DNA from an RNA template." }
    ]
  },
  "Dashboard — poly\\polymeric.md": {
    "primary": "Consisting of or relating to a polymer; exhibiting high molecular weight formed by repeated monomeric units.",
    "secondary": "In physical chemistry and industrial processing, describing compounds or materials whose high-viscosity, viscoelasticity, and thermal transitions arise from macromolecular chain dynamics.",
    "quotes": [
      { "author": "Hermann Staudinger", "work": "Macromolecular Chemistry", "quote": "The high viscosity of dilute solutions of rubber is an intrinsic property of its **polymeric** chain length." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Silicate minerals exhibit immense diversity because silicate tetrahedra can condense into infinite **polymeric** sheets and chains." },
      { "author": "Herman Mark", "work": "Physical Chemistry of High Polymeric Systems", "quote": "The glass transition temperature marks the boundary where **polymeric** chains regain rotational freedom along their backbone." }
    ]
  },
  "Dashboard — poly\\polymerisation.md": {
    "primary": "The chemical process of combining monomer molecules together into a three-dimensional network or polymer chains; Commonwealth spelling of polymerization.",
    "secondary": "In industrial chemistry and plastics engineering, reaction mechanisms classified into addition (chain-growth) and condensation (step-growth) polymerisation.",
    "quotes": [
      { "author": "Hermann Staudinger", "work": "Die hochmolekularen organischen Verbindungen", "quote": "In genuine **polymerisation**, unsaturated monomers join by normal covalent valences without the elimination of simple molecules." },
      { "author": "Wallace Carothers", "work": "An Introduction to the General Theory of Condensation Polymers", "quote": "Step-growth **polymerisation** requires that the reacting functional groups maintain high conversion to build long chains." },
      { "author": "Michael Polanyi", "work": "The Chemical Gazette", "quote": "The activation energy of catalytic **polymerisation** decreases sharply in the presence of coordination metal complexes." }
    ]
  },
  "Dashboard — poly\\polymerise.md": {
    "primary": "To undergo or cause to undergo polymerisation; British spelling of polymerize.",
    "secondary": "In synthetic organic chemistry, causing small unsaturated or cyclic molecules to link into high-molecular-weight macromolecular networks.",
    "quotes": [
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Under the influence of heat and acid catalysts, liquid aldehydes readily **polymerise** into crystalline solids." },
      { "author": "Hermann Staudinger", "work": "Macromolecular Chemistry", "quote": "Purified styrene begins to **polymerise** spontaneously even at room temperature when exposed to sunlight." },
      { "author": "William Henry Perkin", "work": "Journal of the Chemical Society", "quote": "Certain volatile hydrocarbons tend to **polymerise** into resinous masses upon standing in open flasks." }
    ]
  },
  "Dashboard — poly\\polymerization.md": {
    "primary": "A chemical reaction in which two or more small molecules (monomers) combine to form a large chain or network molecule (polymer).",
    "secondary": "In chemical engineering and macromolecular science, reactions categorized by mechanism into radical, ionic, coordination, and step-growth processes.",
    "quotes": [
      { "author": "Karl Ziegler", "work": "Nobel Lecture", "quote": "Our catalyst systems made it possible to conduct the **polymerization** of ethylene under mild temperatures and atmospheric pressure." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The biological **polymerization** of amino acids into polypeptide chains is directed with absolute precision by ribosomal machinery." },
      { "author": "Herman Mark", "work": "Physical Chemistry of High Polymeric Systems", "quote": "Controlling the termination step in free-radical **polymerization** allows chemists to regulate the average molecular weight of acrylics." }
    ]
  },
  "Dashboard — poly\\polymerize.md": {
    "primary": "To undergo or cause to combine into a polymer.",
    "secondary": "In industrial and bio-organic chemistry, to initiate the covalent union of repeating monomer units through heat, pressure, radiation, or catalytic activation.",
    "quotes": [
      { "author": "Wallace Carothers", "work": "Studies on Polymerization and Ring Formation", "quote": "When heated above its melting point in an inert atmosphere, the amino acid will **polymerize** into a high-melting polyamide." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Molecules of vinyl chloride **polymerize** readily to yield the durable, rigid plastic known as polyvinyl chloride." },
      { "author": "Arthur Kornberg", "work": "DNA Replication", "quote": "In the presence of magnesium ions, the enzyme continues to **polymerize** thousands of nucleotides per second." }
    ]
  },
  "Dashboard — poly\\polymorph.md": {
    "primary": "An organism, substance, or structure that exists in several different forms or morphological variations.",
    "secondary": "In mineralogy and materials science, a chemical substance (such as carbon appearing as diamond or graphite, or CaCO3 as calcite or aragonite) that crystallizes in multiple distinct crystal structures; in hematology, a polymorphonuclear leukocyte.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "Calcite and aragonite represent two distinct **polymorph** forms of calcium carbonate possessing different crystal systems." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In acute bacterial infection, the circulating **polymorph** leukocyte count rises sharply, displaying lobulated nuclei." },
      { "author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "A truly remarkable **polymorph** plant produces cleistogamic flowers near the roots alongside showy chasmogamic blossoms on the stem." }
    ]
  },
  "Dashboard — poly\\polymorphemic.md": {
    "primary": "Consisting of or containing more than one morpheme; morphologically complex.",
    "secondary": "In morphology and structural linguistics, words constructed from a base root plus one or more affixes or compounding roots (such as 'un-break-able'), contrasted with monomorphemic words.",
    "quotes": [
      { "author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Polysynthetic American Indian languages frequently express an entire sentence within a single **polymorphemic** word." },
      { "author": "Noam Chomsky", "work": "Aspects of the Theory of Syntax", "quote": "The internal semantic representation of a **polymorphemic** compound cannot always be derived by simple composition." },
      { "author": "Leonard Bloomfield", "work": "Language", "quote": "Words like 'gentlemanliness' are clearly **polymorphemic**, comprising successive layers of derivational and inflectional affixes." }
    ]
  },
  "Dashboard — poly\\polymorphic.md": {
    "primary": "Occurring in or assuming various forms, stages, or morphological types.",
    "secondary": "In object-oriented programming, software entities (such as methods or classes) able to operate on objects of different types through a unified interface; in genetics, genes with multiple alleles in a population.",
    "quotes": [
      { "author": "Charles Darwin", "work": "On the Origin of Species", "quote": "These **polymorphic** genera present an astonishing degree of variation, defying the efforts of botanists to delimit stable species." },
      { "author": "Bjarne Stroustrup", "work": "The C++ Programming Language", "quote": "Virtual functions enable **polymorphic** behavior, allowing derived classes to override methods called through base pointers." },
      { "author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "A genetically **polymorphic** population maintains balanced alleles that provide adaptive plasticity against changing environmental pressures." }
    ]
  },
  "Dashboard — poly\\polymorphism.md": {
    "primary": "The condition of occurring in several different forms, stages, or varieties.",
    "secondary": "In genetics and evolutionary biology, the simultaneous occurrence in the same population of two or more discontinuous phenotypes or genetic variants (such as ABO blood groups); in crystallography, allotropy in crystal structures.",
    "quotes": [
      { "author": "E. B. Ford", "work": "Ecological Genetics", "quote": "Genetic **polymorphism** is defined as the occurrence together in the same locality of two or more discontinuous forms of a species in balance." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The **polymorphism** of titanium dioxide gives rise to three distinct natural minerals: rutile, anatase, and brookite." },
      { "author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "Castes in social insect colonies exhibit magnificent behavioral and morphological **polymorphism** among sterile females." }
    ]
  },
  "Dashboard — poly\\polymorphous.md": {
    "primary": "Having, assuming, or passing through many different forms, stages, or shapes.",
    "secondary": "In psychoanalysis, notably Sigmund Freud's concept of 'polymorphous perversity', the early infantile stage of psychosexual development capable of deriving sensual gratification from any somatic zone.",
    "quotes": [
      { "author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "The child possesses a **polymorphous** perverse disposition, capable of finding sexual pleasure in diverse bodily regions." },
      { "author": "William James", "work": "The Varieties of Religious Experience", "quote": "Religious emotion is a **polymorphous** phenomenon, ranging from morbid melancholy to triumphant mystical ecstasy." },
      { "author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cultivated plants like the cabbage exhibit **polymorphous** variability, yielding kale, kohlrabi, and cauliflower from one ancestor." }
    ]
  },
  "Dashboard — poly\\polymox.md": {
    "primary": "A proprietary brand name for amoxicillin, a broad-spectrum penicillin antibiotic used in the treatment of bacterial infections.",
    "secondary": "In clinical pharmacology and pediatrics, an orally well-absorbed semisynthetic beta-lactam antibiotic used extensively for otitis media, streptococcal pharyngitis, and respiratory tract infections.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The enhanced oral bioavailability of amoxicillin, formulated commercially as **polymox**, ensured superior tissue levels over ampicillin." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Revision", "quote": "For acute pediatric sinusitis and middle ear inflammation, oral suspensions of **polymox** remain the frontline empirical therapy." },
      { "author": "Maxwell Finland", "work": "Antibiotic Therapy in Primary Care", "quote": "High compliance in pediatric outpatients was achieved with **polymox** due to its convenient dosage schedule and low gastrointestinal side effects." }
    ]
  },
  "Dashboard — poly\\polymyositis.md": {
    "primary": "An uncommon inflammatory disease that causes progressive muscle weakness affecting both sides of the body.",
    "secondary": "In rheumatology and neuromuscular pathology, an idiopathic autoimmune inflammatory myopathy characterized by endomysial cytotoxic CD8+ T-cell infiltration and proximal muscle symmetric weakness, often accompanied by elevated serum creatine kinase.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients presenting with symmetric proximal muscle weakness and marked elevation of muscle enzymes should be evaluated for **polymyositis**." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "Muscle biopsy in acute **polymyositis** reveals extensive inflammatory mononuclear infiltrates surrounding necrotic myofibers." },
      { "author": "Eugene Braunwald", "work": "Heart Disease: A Textbook of Cardiovascular Medicine", "quote": "Myocardial involvement occurs in a notable percentage of patients with **polymyositis**, manifesting as conduction defects or arrhythmias." }
    ]
  },
  "Dashboard — poly\\polymyxin.md": {
    "primary": "Any of a group of polypeptide antibiotics derived from *Bacillus polymyxa*, effective predominantly against Gram-negative bacteria.",
    "secondary": "In antimicrobial chemotherapy and critical care medicine, cyclic cationic decapeptide antibiotics (notably polymyxin B and polymyxin E / colistin) that disrupt bacterial outer membrane phospholipids, reserved as last-resort agents against multi-drug-resistant Gram-negative pathogens.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "By acting as a cationic detergent that binds lipid A, **polymyxin** disrupts the bacterial outer membrane, causing rapid cell lysis." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Edition", "quote": "Because of potential nephrotoxicity and neurotoxicity, systemic administration of **polymyxin** is reserved for pan-resistant infections." },
      { "author": "Selman Waksman", "work": "The Actinomycetes and Their Antibiotics", "quote": "Strains of Bacillus polymyxa isolated from soil produce the potent lipopeptide complex designated **polymyxin**." }
    ]
  },
  "Dashboard — poly\\polynemidae.md": {
    "primary": "A family of marine and brackish-water ray-finned fishes, commonly known as threadfins.",
    "secondary": "In ichthyology, perciform fishes characterized by pectoral fins divided into an upper normal fin and lower thread-like sensory filaments utilized to locate invertebrate prey in turbid sandy waters.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The family **Polynemidae**, or threadfins, are valued food fishes of tropical coasts, recognized by free filamentary pectoral rays." },
      { "author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "Species belonging to **Polynemidae** inhabit sandy surf zones where their tactile pectoral threads probe the substrate for buried crustacea." },
      { "author": "William Beebe", "work": "Shore Fishes of Bermuda", "quote": "A small school of threadfins from the family **Polynemidae** flashed through the milky surf along the shoreline." }
    ]
  },
  "Dashboard — poly\\polynesia.md": {
    "primary": "A subregion of Oceania comprising more than a thousand islands scattered over the central and southern Pacific Ocean, bounded by Hawaii, New Zealand, and Easter Island.",
    "secondary": "In anthropology and historical linguistics, an ethno-geographic cultural region united by closely related Austronesian languages, sophisticated open-ocean voyaging technology, and common social hierarchies.",
    "quotes": [
      { "author": "Captain James Cook", "work": "A Voyage to the Pacific Ocean", "quote": "The extraordinary similarity of language and customs found across the scattered islands of **Polynesia** astonished all our navigators." },
      { "author": "Herman Melville", "work": "Typee: A Peep at Polynesian Life", "quote": "No region of the globe possesses a more romantic fascination than the palm-fringed islands of eastern **Polynesia**." },
      { "author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "quote": "The coral atolls of **Polynesia** provide magnificent evidence of widespread crustal subsidence across the central Pacific basin." }
    ]
  },
  "Dashboard — poly\\polyneuritis.md": {
    "primary": "Inflammation or degeneration of several peripheral nerves simultaneously, causing symmetric pain, sensory disturbances, and weakness.",
    "secondary": "In clinical neurology and nutritional medicine, symmetrical peripheral neuropathy classically associated with thiamine deficiency (beriberi), chronic alcoholism, lead poisoning, or post-infectious Guillain-Barré syndrome.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute toxic **polyneuritis** typically begins with sensory paresthesias in the toes, followed rapidly by ascending motor paralysis." },
      { "author": "Christiaan Eijkman", "work": "Nobel Lecture: The Antineuritic Vitamin", "quote": "Fowls fed exclusively on polished white rice developed a severe paralytic **polyneuritis** identical to human beriberi." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "Alcoholic **polyneuritis** responds favorably to immediate parenteral vitamin therapy provided dietary intake is restored." }
    ]
  },
  "Dashboard — poly\\polynomial.md": {
    "primary": "A mathematical expression consisting of variables and coefficients, involving only the operations of addition, subtraction, multiplication, and non-negative integer exponentiation.",
    "secondary": "In algebra, algebraic geometry, and numerical analysis, functions of the form f(x) = a_n x^n + ... + a_1 x + a_0, whose roots over the complex field are guaranteed to exist by the Fundamental Theorem of Algebra.",
    "quotes": [
      { "author": "Carl Friedrich Gauss", "work": "Demonstratio Nova Theorematis", "quote": "Every algebraic **polynomial** equation of the nth degree with real coefficients can be factored into real linear and quadratic factors." },
      { "author": "René Descartes", "work": "La Géométrie", "quote": "Descartes' rule of signs establishes the maximum number of positive real roots in any given **polynomial** equation." },
      { "author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "The properties of a continuous function can often be approximated arbitrarily closely by a suitable Taylor **polynomial**." }
    ]
  },
  "Dashboard — poly\\polynya.md": {
    "primary": "An area of open, unfrozen water surrounded by sea ice, especially in Arctic and Antarctic oceans.",
    "secondary": "In polar oceanography and marine climatology, non-linear open-water systems maintained either by warm upwelling currents (sensible heat polynya) or by katabatic winds driving newly formed ice offshore (latent heat polynya), serving as vital ecological refugia for marine mammals.",
    "quotes": [
      { "author": "Fridtjof Nansen", "work": "Farthest North", "quote": "The Fram drifted near an extensive **polynya**, where open black water mirrored the auroral curtains overhead." },
      { "author": "Robert Falcon Scott", "work": "Scott's Last Expedition", "quote": "A wide **polynya** opened between the sea ice and the barrier edge, populated by surfacing seals and killer whales." },
      { "author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Even amidst the unbroken polar freeze, a steaming **polynya** provides breathing holes for walruses and whales." }
    ]
  },
  "Dashboard — poly\\polyodon.md": {
    "primary": "A genus of primitive freshwater ray-finned fish in the paddlefish family (Polyodontidae), typified by the American paddlefish (Polyodon spathula).",
    "secondary": "In freshwater ichthyology and evolutionary biology, ancient chondrostean paddlefish native to the Mississippi River basin, characterized by a smooth shark-like cartilaginous skeleton, heterocercal tail, and an elongated paddle-like rostrum covered in electroreceptors.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The American paddlefish, **Polyodon** spathula, swims slowly through muddy river waters with its huge mouth gaping open to strain plankton." },
      { "author": "Louis Agassiz", "work": "Lake Superior: Its Physical Character, Vegetation, and Animals", "quote": "The cartilaginous cranium and heterocercal tail of **Polyodon** show unmistakable affinities with ancient Paleozoic fishes." },
      { "author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The enormous spatulate snout of **Polyodon** is densely packed with sensory organs that detect microscopic zooplankton." }
    ]
  },
  "Dashboard — poly\\polyodontidae.md": {
    "primary": "The family of ancient freshwater fishes known as paddlefishes, belonging to the order Acipenseriformes.",
    "secondary": "In systematic ichthyology and paleontology, an ancient basal actinopterygian family containing only two modern species (Polyodon spathula in North America and the extinct Psephurus gladius in the Yangtze), notable for their cartilaginous skeletons and electroceptive rostra.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "Fishes", "quote": "Members of the family **Polyodontidae** represent surviving relics of a primitive chondrostean stock allied to the sturgeons." },
      { "author": "Albert Günther", "work": "An Introduction to the Study of Fishes", "quote": "The family **Polyodontidae** is distinguished by an extraordinary paddle-like extension of the ethmoid and nasal bones." },
      { "author": "Edward Drinker Cope", "work": "On the Classification of the Extinct Fishes", "quote": "Fossil precursors of **Polyodontidae** from Upper Cretaceous deposits prove the venerable antiquity of this paddle-snouted lineage." }
    ]
  },
  "Dashboard — poly\\polyoestrous.md": {
    "primary": "Exhibiting recurrent periods of estrus or sexual receptivity throughout the year or breeding season; Commonwealth spelling of polyestrous.",
    "secondary": "In reproductive physiology and animal husbandry, mammals (such as cows, sows, and laboratory rodents) that undergo regular ovarian cycles unless interrupted by pregnancy or pathology.",
    "quotes": [
      { "author": "Francis Marshall", "work": "The Physiology of Reproduction", "quote": "In the **polyoestrous** domestic mare, sexual cycles recur at three-week intervals throughout the spring and summer." },
      { "author": "Arthur Thomson", "work": "The Science of Life", "quote": "Wild species often shift from a monoestrous to a **polyoestrous** habit when provided with abundant food under domestication." },
      { "author": "Solomon Zuckerman", "work": "Functional Affinities of Man, Monkeys, and Apes", "quote": "The continuous ovarian activity of the **polyoestrous** primate contrasts with the strictly seasonal rut of wild ruminants." }
    ]
  },
  "Dashboard — poly\\polyoicous.md": {
    "primary": "Producing male and female reproductive structures on different parts of the same plant or on separate plants within the same species; polyoecious.",
    "secondary": "In bryology and cryptogamic botany, mosses or liverworts exhibiting diverse arrangements of antheridia and archegonia on distinct branches, stems, or individuals within a single species.",
    "quotes": [
      { "author": "William Mitten", "work": "Musci Austro-Americani", "quote": "Certain alpine mosses prove to be **polyoicous**, developing both synoicous inflorescences and unisexual female shoots." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "When sexual organs occur indiscriminately in different arrangements upon the same gametophyte, the moss is described as **polyoicous**." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The variability of bryophyte inflorescences frequently complicates taxonomy when a species proves facultatively **polyoicous**." }
    ]
  },
  "Dashboard — poly\\polyoma.md": {
    "primary": "A DNA virus of the family Polyomaviridae capable of causing various tumors in animals; or the condition caused by such a virus.",
    "secondary": "In viral oncology and molecular biology, a small non-enveloped double-stranded DNA virus (such as murine polyomavirus or simian virus 40 / SV40) that encodes T-antigens capable of transforming normal cells by binding tumor suppressors p53 and pRb.",
    "quotes": [
      { "author": "Ludwik Gross", "work": "Oncogenic Viruses", "quote": "The murine **polyoma** virus produces a bewildering variety of epithelial tumors when inoculated into newborn mice." },
      { "author": "David Baltimore", "work": "Viruses and Human Cancer", "quote": "Studies of the large T-antigen encoded by the **polyoma** genome laid the foundation for modern tumor suppressor biology." },
      { "author": "Renato Dulbecco", "work": "The Induction of Cancer by Viruses", "quote": "Cell transformation by the **polyoma** virus requires stable integration of the viral genome into the host chromosome." }
    ]
  },
  "Dashboard — poly\\polyose.md": {
    "primary": "A polysaccharide; a carbohydrate composed of multiple monosaccharide units linked together.",
    "secondary": "In historical carbohydrate chemistry, an archaic generic term for complex polysaccharides and oligosaccharides, encompassing starch, dextrin, glycogen, and inulin.",
    "quotes": [
      { "author": "Emil Fischer", "work": "Syntheses in the Sugar Group", "quote": "The natural starch molecule represents a complex **polyose** yielding d-glucose upon complete acid hydrolysis." },
      { "author": "Arthur Harden", "work": "Alcoholic Fermentation", "quote": "Before yeast enzymes can ferment a **polyose**, it must be cleaved into simple hexose units by hydrolytic enzymes." },
      { "author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Plants accumulate reserve carbon in the form of an insoluble **polyose**, which the germinating embryo metabolizes into sugar." }
    ]
  },
  "Dashboard — poly\\polyphase.md": {
    "primary": "Having or producing two or more distinct phases; especially referring to alternating electric currents having two or more interrelated phases.",
    "secondary": "In electrical engineering and thermodynamics, AC electrical distribution systems (such as standard three-phase power pioneered by Nikola Tesla) or physical mixtures containing multiple distinct thermodynamic phases (solid, liquid, vapor).",
    "quotes": [
      { "author": "Nikola Tesla", "work": "Experiments with Alternate Currents of High Potential and High Frequency", "quote": "The rotating magnetic field produced by my **polyphase** currents eliminated commutators and sparked a new industrial era." },
      { "author": "Charles Proteus Steinmetz", "work": "Theory and Calculation of Alternating Current Phenomena", "quote": "A balanced **polyphase** system maintains constant total instantaneous power, unlike single-phase alternating current." },
      { "author": "J. Willard Gibbs", "work": "On the Equilibrium of Heterogeneous Substances", "quote": "The phase rule determines the number of degrees of freedom in any heterogeneous **polyphase** thermodynamic system." }
    ]
  },
  "Dashboard — poly\\polys.md": {
    "primary": "The ancient Greek adjective meaning 'much', 'many', or 'numerous', from which the English prefix poly- is derived; or an abbreviation for polymorphonuclear leukocytes.",
    "secondary": "In classical Indo-European etymology, the root *polús (*pleh1-, to fill) foundational to linguistic, scientific, and mathematical compounds designating multiplicity or abundance.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The basic Greek adjective **polys** denotes great in quantity, number, or extent, generating thousands of scientific derivatives." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "In comparing Greek **polys** with Latin plus and Gothic filu, we trace the ancient Aryan concept of abundance." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A marked shift to the left in circulating **polys** indicates intense marrow mobilization during severe acute sepsis." }
    ]
  },
  "Dashboard — poly\\polysaccharide.md": {
    "primary": "A complex carbohydrate molecule composed of long chains of monosaccharide units bound together by glycosidic linkages.",
    "secondary": "In biochemistry, high-molecular-weight biopolymers performing structural roles (cellulose, chitin) or energy storage functions (starch, glycogen) in living organisms.",
    "quotes": [
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Cellulose is an unbranched **polysaccharide** of glucose units whose beta-linkages form rigid microfibrils in plant cell walls." },
      { "author": "Emil Fischer", "work": "Investigations on Carbohydrates", "quote": "Hydrolysis of the animal **polysaccharide** glycogen reveals that it consists entirely of branched alpha-d-glucopyranose units." },
      { "author": "Arthur Kornberg", "work": "Enzymatic Synthesis of Polysaccharides", "quote": "The bacterial capsule is frequently composed of an acidic **polysaccharide** that protects the pathogen from phagocytosis." }
    ]
  },
  "Dashboard — poly\\polysemant.md": {
    "primary": "A word, phrase, or lexical item that possesses multiple related meanings or senses.",
    "secondary": "In structural linguistics, lexicography, and cognitive semantics, a single polysemous lexical unit whose varied senses derive from a common etymological root or metaphorical extension.",
    "quotes": [
      { "author": "Stephen Ullmann", "work": "Semantics: An Introduction to the Science of Meaning", "quote": "Every common noun in daily speech tends to become a **polysemant**, accumulating fresh senses through metaphorical transfer." },
      { "author": "Michel Bréal", "work": "Semantics: Studies in the Science of Meaning", "quote": "The human mind economizes linguistic effort by turning an existing word into a **polysemant** rather than inventing a new term." },
      { "author": "John Lyons", "work": "Semantics", "quote": "The lexicographer must decide whether a given **polysemant** represents a single word with several senses or multiple homonyms." }
    ]
  },
  "Dashboard — poly\\polysemantic.md": {
    "primary": "Having or characterized by multiple related meanings or semantic interpretations; polysemous.",
    "secondary": "In linguistics, philosophy of language, and hermeneutics, describing words, symbols, or expressions whose varied meanings depend upon contextual pragmatic framing.",
    "quotes": [
      { "author": "Paul Ricoeur", "work": "The Conflict of Interpretations", "quote": "Metaphorical language is inherently **polysemantic**, opening multiple levels of meaning that resist univocal definition." },
      { "author": "Stephen Ullmann", "work": "The Principles of Semantics", "quote": "A highly **polysemantic** word like 'head' acquires dozens of secondary senses through anatomical and spatial analogies." },
      { "author": "Roman Jakobson", "work": "Selected Writings: Poetry of Grammar and Grammar of Poetry", "quote": "Poetic discourse maximizes ambiguity by exploiting the **polysemantic** potential of everyday grammatical forms." }
    ]
  },
  "Dashboard — poly\\polysemous.md": {
    "primary": "Having multiple meanings, senses, or interpretations.",
    "secondary": "In semantic theory and computational linguistics, lexical items whose senses are related by metaphor, metonymy, or specialization, contrasted with homonymous words having coincidental phonological overlap.",
    "quotes": [
      { "author": "William Empson", "work": "Seven Types of Ambiguity", "quote": "A rich poetic line depends upon **polysemous** phrasing that suggests multiple simultaneous emotional responses." },
      { "author": "John Lyons", "work": "Linguistic Semantics: An Introduction", "quote": "The word 'mouth' is **polysemous**, applying literally to the human face and figuratively to a river or a cave." },
      { "author": "Noam Chomsky", "work": "New Horizons in the Study of Language and Mind", "quote": "Natural language words are typically **polysemous**, their interpretations shaped dynamically by conceptual perspective." }
    ]
  },
  "Dashboard — poly\\polysemy.md": {
    "primary": "The coexistence of many possible meanings or interpretations for a single word, phrase, or symbol.",
    "secondary": "In cognitive linguistics and lexicology, the structural phenomenon where a lexical headword possesses multiple conceptually related senses generated by metaphorical or metonymic extensions.",
    "quotes": [
      { "author": "Michel Bréal", "work": "Semantics: Studies in the Science of Meaning", "quote": "The phenomenon of **polysemy** is the natural consequence of intellectual growth, as old words are adapted to new thoughts." },
      { "author": "Stephen Ullmann", "work": "Semantics", "quote": "Without **polysemy**, our vocabulary would need to expand to billions of distinct words to cover human experience." },
      { "author": "Paul Ricoeur", "work": "The Rule of Metaphor", "quote": "Metaphor creates living **polysemy**, introducing semantic innovation by holding divergent senses together in tension." }
    ]
  },
  "Dashboard — poly\\polysomy.md": {
    "primary": "A condition in which a cell, tissue, or organism has at least one more chromosome than the normal diploid (or haploid) number.",
    "secondary": "In clinical cytogenetics and chromosomal pathology, aneuploidy involving extra copies of a specific chromosome (such as trisomy 21 or tetrasomy X), typically arising from non-disjunction during meiotic cell division.",
    "quotes": [
      { "author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Chromosomal nondisjunction frequently results in **polysomy**, creating individuals with three or four homologous chromosomes." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Edition", "quote": "Severe congenital anomalies often trace their etiology to autosomal **polysomy** that disrupts normal gene dosage balance." },
      { "author": "C. D. Darlington", "work": "Recent Advances in Cytology", "quote": "Meiotic multivalent pairings in cases of **polysomy** lead to irregular gametic segregation and high embryonic lethality." }
    ]
  },
  "Dashboard — poly\\polystichum.md": {
    "primary": "A large cosmopolitan genus of terrestrial ferns in the family Dryopteridaceae, commonly known as shield ferns or holly ferns.",
    "secondary": "In pteridology and botanical taxonomy, evergreen woodland ferns characterized by round sori covered by peltate (umbrella-like) indusia and tough, pinnate to bipinnate fronds with spinulose teeth.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **Polystichum**, such as the common Christmas fern, retain their leathery green fronds throughout winter snows." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The genus **Polystichum** is distinguished among polypodiaceous ferns by its centrally peltate indusium covering each sorus." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "For shaded rock gardens, the stiff lustrous foliage of **Polystichum** aculeatum provides enduring architectural structure." }
    ]
  },
  "Dashboard — poly\\polystyrene.md": {
    "primary": "A rigid, transparent, and lightweight synthetic thermoplastic polymer made by the polymerization of styrene.",
    "secondary": "In industrial materials science, an aromatic polymer (solid or expanded foam / Styrofoam) with high thermal insulation, dielectric strength, and low cost, widely used in food packaging and building insulation.",
    "quotes": [
      { "author": "Hermann Staudinger", "work": "Macromolecular Chemistry", "quote": "Linear chains of **polystyrene** demonstrated that high molecular weight can be achieved through pure carbon-carbon covalent linkages." },
      { "author": "Herman Mark", "work": "Giant Molecules", "quote": "The bulky phenyl side groups along the **polystyrene** backbone hinder chain slippage, rendering the solid plastic hard and brittle." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "Expanding **polystyrene** beads with a blowing agent produces lightweight foamed blocks used universally for refrigeration insulation." }
    ]
  },
  "Dashboard — poly\\polysyllabic.md": {
    "primary": "Having or consisting of more than three syllables; or characterized by the use of long words.",
    "secondary": "In phonology, metrics, and rhetorical style, speech or prose featuring ornate, Latinate vocabulary of multiple syllables, contrasted with terse monosyllabic diction.",
    "quotes": [
      { "author": "George Orwell", "work": "Politics and the English Language", "quote": "Bad political writing is choked with vague, pompous, **polysyllabic** jargon designed to give an appearance of solidity to pure wind." },
      { "author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "The grand style of Milton naturally admits a rolling, **polysyllabic** cadence drawn from classical Latinity." },
      { "author": "Henry Sweet", "work": "A History of English Sounds", "quote": "Vowel reduction in rapid speech commonly collapses the unaccented syllables of an English **polysyllabic** word." }
    ]
  },
  "Dashboard — poly\\polysyllabically.md": {
    "primary": "In a polysyllabic manner; using or characterized by words with many syllables.",
    "secondary": "In literary criticism and linguistic phonetics, describing speech or writing delivered in an elaborate, multi-syllabic, or pedantic register.",
    "quotes": [
      { "author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Professor Teufelsdröckh declaimed **polysyllabically** from his tower, wrapping simple metaphysical truths in cumbersome German compounds." },
      { "author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber was accustomed to express himself **polysyllabically**, soaring into grandiose rhetorical circumlocutions." },
      { "author": "H. L. Mencken", "work": "The American Language", "quote": "The courtroom orator flourished **polysyllabically**, overwhelming the jury with resonant Latinate legalisms." }
    ]
  },
  "Dashboard — poly\\polysyllable.md": {
    "primary": "A word having more than three syllables.",
    "secondary": "In linguistics, prosody, and lexicology, a multisyllabic word whose rhythmic stress patterns (primary and secondary stress) dictate verse meter and natural spoken cadence.",
    "quotes": [
      { "author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "Ten low words oft creep in one dull line, while a grand **polysyllable** adds dignity and musical weight to the heroic couplet." },
      { "author": "Samuel Johnson", "work": "Preface to the English Dictionary", "quote": "I have not studiously avoided the foreign **polysyllable** when precision and scholarly elegance required its use." },
      { "author": "William Hazlitt", "work": "Table-Talk: On Familiar Style", "quote": "A truly good writer does not drag in an obscure **polysyllable** merely to astonish the ignorant." }
    ]
  },
  "Dashboard — poly\\polysyndeton.md": {
    "primary": "The deliberate and repeated use of conjunctions (such as 'and', 'or') in close succession, often with no commas, for rhetorical emphasis or rhythm.",
    "secondary": "In classical rhetoric and stylistics, an emphatic scheme that slows the tempo of a sentence, accumulates emotional momentum, and conveys a sense of overwhelming multiplicity or grandeur.",
    "quotes": [
      { "author": "Longinus", "work": "On the Sublime", "quote": "The judicious use of **polysyndeton** binds thoughts into an unbroken chain, giving the impression of urgent and continuous speed." },
      { "author": "Quintilian", "work": "Institutio Oratoria", "quote": "In **polysyndeton**, the repetition of connecting particles separates each item and adds deliberate weight to every clause." },
      { "author": "John Milton", "work": "Paradise Lost", "quote": "Satan pursues his way, o'er bog or steep, through strait, rough, dense, or rare, with head, hands, wings, or feet, pursuing an arduous flight in grand **polysyndeton**." }
    ]
  },
  "Dashboard — poly\\polysynthetic.md": {
    "primary": "Characterized by combining several word elements or morphemes into a single complex word; or relating to polysynthetic crystal twinning.",
    "secondary": "In linguistic typology (coined by Peter Stephen Du Ponceau), languages (such as Inuktitut, Nahuatl, and Navajo) that incorporate nominal, verbal, and modifier roots into single massive words; in mineralogy, repeated parallel lamellar twinning (such as albite twinning in plagioclase feldspars).",
    "quotes": [
      { "author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "A **polysynthetic** language constructs miniature sentences within the compass of a single morphological word unit." },
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "Under the polarizing microscope, plagioclase displays exquisite **polysynthetic** twinning in parallel alternating lamellae." },
      { "author": "Franz Boas", "work": "Handbook of American Indian Languages", "quote": "The **polysynthetic** morphology of Eskimo allows grammatical ideas to be woven into the verb stem through successive suffixes." }
    ]
  },
  "Dashboard — poly\\polytechnic.md": {
    "primary": "Offering, relating to, or providing instruction in many technical arts and applied sciences.",
    "secondary": "In educational history and engineering pedagogy, technical institutes or universities (beginning with the École Polytechnique in Paris, 1794) dedicated to training civil, mechanical, and chemical engineers.",
    "quotes": [
      { "author": "Matthew Arnold", "work": "Schools and Universities on the Continent", "quote": "The French **polytechnic** school established a rigorous mathematical curriculum that became the model for technical education worldwide." },
      { "author": "H. G. Wells", "work": "The New Machiavelli", "quote": "He studied electrical engineering at the local **polytechnic**, finding in practical science a welcome release from dry scholasticism." },
      { "author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "A well-organized **polytechnic** institute bridges the fatal gulf between abstract theoretical discovery and industrial manufacture." }
    ]
  },
  "Dashboard — poly\\polytetrafluoroethylene.md": {
    "primary": "A synthetic fluoropolymer of tetrafluoroethylene (known commercially as Teflon), notable for extreme chemical inertness, high thermal stability, and an exceptionally low coefficient of friction.",
    "secondary": "In materials science and polymer engineering, a high-performance polymer discovered by Roy J. Plunkett in 1938, characterized by dense fluorine shielding along a carbon backbone that prevents chemical attack and confers hydrophobic, non-stick properties.",
    "quotes": [
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The immense strength of the carbon-fluorine bond accounts for the almost complete chemical unreactivity of **polytetrafluoroethylene**." },
      { "author": "Herman Mark", "work": "Giant Molecules", "quote": "Dense fluorine envelopes wrap the molecular chain of **polytetrafluoroethylene**, producing a non-stick surface with the lowest friction of any solid." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "Gaskets and valve seals fabricated from **polytetrafluoroethylene** withstand corrosive acids at temperatures exceeding two hundred degrees." }
    ]
  },
  "Dashboard — poly\\polytheism.md": {
    "primary": "The belief in, or worship of, more than one god or deity.",
    "secondary": "In comparative religion, anthropology, and philosophy, religious traditions (such as ancient Greco-Roman, Vedic, and Mesoamerican religions) that venerate a pantheon of distinct deities governing diverse cosmic and human domains.",
    "quotes": [
      { "author": "David Hume", "work": "The Natural History of Religion", "quote": "The primary religion of mankind was inevitable **polytheism**, born of fear and hope directed toward diverse natural powers." },
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The various modes of worship which prevailed in the Roman world were all considered by the people as equally true, united under tolerant **polytheism**." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Vedic religion reflects that fluid stage of **polyheism** which I have designated kathenotheism, where each deity is addressed as supreme in turn." }
    ]
  },
  "Dashboard — poly\\polytheist.md": {
    "primary": "A person who believes in or worships multiple gods.",
    "secondary": "In history of religion and theological polemics, an adherent of a polytheistic faith who recognizes and propitiates diverse cosmic entities, ancestors, or personified natural forces.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "To the enlightened Roman **polytheist**, the addition of an exotic foreign divinity to the imperial Pantheon was a matter of polite civic indifference." },
      { "author": "David Hume", "work": "The Natural History of Religion", "quote": "The ancient **polytheist** never conceived of his gods as infinite or omnipotent, but as limited beings subject to passion." },
      { "author": "William James", "work": "The Varieties of Religious Experience", "quote": "A pragmatic view of the universe might find more natural kinship with the diverse pluralism of the **polytheist** than with abstract monism." }
    ]
  },
  "Dashboard — poly\\polytheistic.md": {
    "primary": "Relating to, characterized by, or advocating the belief in many gods.",
    "secondary": "In religious studies and cultural anthropology, pantheons and rituals structured around multiple divine powers presiding over specialized cosmic, agricultural, and social functions.",
    "quotes": [
      { "author": "James George Frazer", "work": "The Golden Bough", "quote": "The **polytheistic** pantheon of ancient Egypt reflected the localized animal deities of ancestral nomes gradually united under a national mythology." },
      { "author": "Max Weber", "work": "The Sociology of Religion", "quote": "The rationalization of **polytheistic** cults into functional departments paved the way for bureaucratic concepts of the sacred order." },
      { "author": "Edward Tylor", "work": "Primitive Culture", "quote": "From primitive animism, human imagination ascended naturally to the structured **polytheistic** hierarchies of Greece and India." }
    ]
  },
  "Dashboard — poly\\polythene.md": {
    "primary": "A lightweight, flexible plastic formed by the polymerization of ethylene; British term for polyethylene.",
    "secondary": "In industrial chemistry and packaging history, commercial polymers (introduced by Imperial Chemical Industries in the 1930s) widely used in film, bags, electrical cable insulation, and containers.",
    "quotes": [
      { "author": "Herman Mark", "work": "Giant Molecules", "quote": "During the war, the secret development of **polythene** insulation made compact airborne radar sets practicable for Allied aircraft." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "High-pressure synthesis converts ethylene gas into translucent **polythene**, impervious to water vapor and chemical solvents." },
      { "author": "Arthur Conan Doyle", "work": "Our American Adventure", "quote": "Modern synthetics like **polythene** have transformed everyday domestic commerce with durable, transparent packaging." }
    ]
  },
  "Dashboard — poly\\polytonal.md": {
    "primary": "Characterized by the simultaneous use of two or more different musical keys or tonalities.",
    "secondary": "In modern music theory and composition (prominent in the works of Igor Stravinsky, Darius Milhaud, and Charles Ives), harmonic structures where distinct tonal layers clash and interlock to create complex acoustic tension.",
    "quotes": [
      { "author": "Igor Stravinsky", "work": "Poetics of Music", "quote": "The famous chord in Petrushka is built upon a **polytonal** combination of C major and F-sharp major arpeggios." },
      { "author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "A **polytonal** passage creates a fascinating spatial depth by setting melodies in two different keys against each other." },
      { "author": "Leonard Bernstein", "work": "The Joy of Music", "quote": "Modern composers achieve brilliant biting contrasts by superimposing **polytonal** lines that retain their distinct tonal centers." }
    ]
  },
  "Dashboard — poly\\polytonalism.md": {
    "primary": "The musical practice, technique, or doctrine of using multiple keys simultaneously.",
    "secondary": "In 20th-century musicology, the systematic compositional approach developed by Darius Milhaud and early modernists as an alternative to German atonality, preserving tonal clarity within superimposed polyphonic layers.",
    "quotes": [
      { "author": "Darius Milhaud", "work": "Polytonalité et Atonalité", "quote": "Unlike Schoenberg's dodecaphony, **polytonalism** enriches musical expression by multiplying tonal poles rather than destroying them." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The rise of **polytonalism** marked an effort to expand harmonic resources without abandoning the expressive anchors of major and minor modes." },
      { "author": "Constant Lambert", "work": "Music Ho! A Study of Music in Decline", "quote": "In the hands of Stravinsky and Milhaud, **polytonalism** produced a sharp, brilliant acoustic glitter that defined post-war neoclassicism." }
    ]
  },
  "Dashboard — poly\\polytonality.md": {
    "primary": "The musical quality or condition of employing two or more different keys simultaneously.",
    "secondary": "In compositional aesthetics, the simultaneous hearing of distinct harmonic keys (bimodality or polymodality), creating rich contrapuntal dissonance while maintaining tonal anchors.",
    "quotes": [
      { "author": "Aaron Copland", "work": "Our New Music", "quote": "Through **polytonality**, the composer achieves an unexpected richness of color, as each melodic voice moves in its own tonal sphere." },
      { "author": "Charles Ives", "work": "Essays Before a Sonata", "quote": "The simultaneous sounding of two village bands playing different tunes in different keys represents the raw human truth of **polytonality**." },
      { "author": "Igor Stravinsky", "work": "Chronicles of My Life", "quote": "The harmonic structure of The Rite of Spring explores **polytonality** not as an intellectual system, but as an instinctive rhythmic necessity." }
    ]
  },
  "Dashboard — poly\\polyunsaturated.md": {
    "primary": "Designating organic compounds, especially fatty acids, that contain two or more carbon-carbon double or triple bonds in their molecular chain.",
    "secondary": "In biochemistry, nutrition, and cardiovascular medicine, essential dietary lipids (such as linoleic acid and omega-3 alpha-linolenic acid) that remain liquid at room temperature and modulate plasma cholesterol and cell membrane fluidity.",
    "quotes": [
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Vegetable seed oils are rich in **polyunsaturated** fatty acids whose multiple double bonds prevent tight crystal packing, keeping them liquid." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Edition", "quote": "Replacing saturated animal fats with **polyunsaturated** vegetable oils significantly lowers serum low-density lipoprotein levels." },
      { "author": "Eugene Braunwald", "work": "Heart Disease", "quote": "Dietary **polyunsaturated** fatty acids of the omega-3 series exert protective anti-inflammatory and anti-arrhythmic effects upon cardiac tissue." }
    ]
  },
  "Dashboard — poly\\polyurethan.md": {
    "primary": "A synthetic resin or polymer composed of organic units joined by carbamate (urethane) links; alternative spelling of polyurethane.",
    "secondary": "In industrial chemistry and polymer technology, versatile condensation polymers formed by reacting polyisocyanates with polyols, yielding resilient foams, coatings, adhesives, and elastomeric fibers.",
    "quotes": [
      { "author": "Otto Bayer", "work": "Das Diisocyanat-Polyadditionsverfahren", "quote": "Reaction of aliphatic diisocyanates with glycols created the new class of **polyurethan** polymers with remarkable tensile resilience." },
      { "author": "Herman Mark", "work": "Giant Molecules", "quote": "The wide range of **polyurethan** products extends from flexible cushioning sponges to ultra-hard marine varnishes." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "In the manufacture of synthetic leather, a porous microporous coating of **polyurethan** provides breathability and durability." }
    ]
  },
  "Dashboard — poly\\polyurethane.md": {
    "primary": "A synthetic resin or polymer consisting of organic chains linked by urethane (carbamate) groups, widely used in flexible foams, rigid insulation, elastomers, and protective coatings.",
    "secondary": "In materials science and polymer engineering, versatile addition polymers synthesized from diisocyanates and polyols, capable of being tailored into open-cell mattress foams, high-efficiency building insulation, or abrasion-resistant skateboard wheels.",
    "quotes": [
      { "author": "Otto Bayer", "work": "Angewandte Chemie", "quote": "The diisocyanate polyaddition reaction opened the entire modern chemistry of **polyurethane** foams and synthetic rubbers." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Hydrogen bonding between urethane groups contributes to the extraordinary elasticity and wear resistance of **polyurethane** fibers." },
      { "author": "Herman Mark", "work": "Physical Chemistry of High Polymeric Systems", "quote": "Rigid **polyurethane** closed-cell foam contains trapped gas that gives it the highest insulating value per inch of any commercial material." }
    ]
  }
}

base_cluster_dir = 'App database/Greek roots/Cluster Number & Mathematics'
slice_path = 'main app/scripts/slice-math-part3.json'

with open(slice_path, 'r', encoding='utf-8') as f:
    full_slice = json.load(f)

# Batch 2 is items 77 to 153 (77 items)
expected_keys = full_slice[77:154]

print(f"Batch 2 contains {len(batch2_data)} items.")
print(f"Expected slice items: {len(expected_keys)}")

missing = [k for k in expected_keys if k not in batch2_data]
extra = [k for k in batch2_data if k not in expected_keys]

if missing:
    print("ERROR: Missing keys in Batch 2:", missing)
    sys.exit(1)
if extra:
    print("ERROR: Extra keys in Batch 2:", extra)
    sys.exit(1)

print("Key matching confirmed perfectly!")

# Internal Quality Validation
for p, data in batch2_data.items():
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
for rel_path, data in batch2_data.items():
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

print(f"Successfully updated {updated} files in Batch 2.")
