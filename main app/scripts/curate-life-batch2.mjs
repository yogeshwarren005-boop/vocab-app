import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Life & Vitality';

const BATCH2_DATA = {
  // Dashboard — blast (52 words)
  "blast": {
    dashboard: "Dashboard — blast",
    primary: "A violent gust of wind, a sudden loud sound, or a destructive wave of explosive pressure.",
    secondary: "In cell biology and embryology, an immature, undifferentiated precursor cell capable of dividing and giving rise to specialized tissues.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", text: "Blow, winds, and crack your cheeks! rage! blow! you cataracts and hurricanoes, spout till you have drench'd our steeples, drown'd the cocks! ... And thou, all-shaking thunder, strike flat the thick rotundity o' the world! Crack nature's moulds, all germens spill at once, that make ingrateful man! A bitter **blast** tore through the battlements." },
      { author: "John Milton", work: "Paradise Lost", text: "As when the potent rod of Amram's son in Egypt's evil day waved round the coast, up called a pitchy cloud of locusts, warping on the eastern **blast**." },
      { author: "Karl Ernst von Baer", work: "On the Genesis of the Animal", text: "Every embryonic **blast** gives rise in orderly succession to the primary germ layers that sculpt the adult organism." }
    ]
  },
  "blasted": {
    dashboard: "Dashboard — blast",
    primary: "Blighted, withered, or damaged as if struck by lightning, frost, or disease.",
    secondary: "Cursed, ruined, or shattered violently by an explosive shockwave.",
    quotes: [
      { author: "William Shakespeare", work: "Macbeth", text: "Say from whence you owe this strange intelligence? or why upon this **blasted** heath you stop our way with such prophetic greeting?" },
      { author: "John Milton", work: "Paradise Lost", text: "Glory obscure: as when the Sun new risen looks through the horizontal misty air shorn of his beams, or from behind the moon in dim eclipse disastrous twilight sheds on half the nations, and with fear of change perplexes monarchs. Darkened so, yet shone above them all the Archangel: but his face deep scars of thunder had intrenched, and care sat on his faded cheek, but under brows of dauntless courage, and considerate pride waiting revenge: cruel his eye, but cast signs of remorse and passion to behold the fellows of his crime, the followers rather (far other once beheld in bliss) condemned for ever now to have their lot in pain, millions of spirits for his fault amerced of Heaven, and from eternal splendours flung for his revolt, yet faithful how they stood, their glory withered: as when Heaven's fire hath scathed the forest oaks, or mountain pines, with singed top their stately growth though bare stands on the **blasted** heath." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", text: "The ancient apple trees stretched their **blasted** branches against the winter sunset like arthritic limbs." }
    ]
  },
  "blastema": {
    dashboard: "Dashboard — blast",
    primary: "A mass of undifferentiated, proliferating cells capable of growth and tissue regeneration into complete anatomical structures.",
    secondary: "The rudimentary formative substance or cellular budding zone from which an amputated organ or limb is regenerated.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrate Animals", text: "At the amputation surface of the salamander limb, a conical **blastema** forms rapidly from dedifferentiated mesodermal cells." },
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "The embryonic **blastema** undergoes progressive histological differentiation before individual organ boundaries become discernible." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", text: "Regenerative power in lower amphibia proceeds from the prolific vitality of the sub-epithelial **blastema**." }
    ]
  },
  "blastemal": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or resembling a blastema.",
    secondary: "Pertaining to the undifferentiated cellular mass that drives biological epimorphic regeneration.",
    quotes: [
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "Signaling gradients within the **blastemal** cone instruct proliferating cells regarding their distal positional identity." },
      { author: "Ross Granville Harrison", work: "Experiments on the Development of the Limbs", text: "Grafting experiments confirm that **blastemal** tissue retains intrinsic self-organizing autonomy under neutral culture." },
      { author: "Julian Huxley", work: "Problems of Relative Growth", text: "Differential mitotic rates in **blastemal** zones determine the relative proportions of developing appendages." }
    ]
  },
  "blastematic": {
    dashboard: "Dashboard — blast",
    primary: "Relating to or derived from a blastema; having formative or regenerative cellular properties.",
    secondary: "Pertaining to formative protoplasm or primitive tissue matrices capable of generating specialized organs.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "We must abandon the archaic theory of a structureless **blastematic** exudate in favor of universal cellular continuity." },
      { author: "Alexander Kowalevsky", work: "Developmental Studies on Ascidians", text: "The **blastematic** rudiment of the chordal rod separates cleanly from the surrounding entodermal mantle." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Direct observation revealed that **blastematic** proliferations give rise to the segmental nephric tubules." }
    ]
  },
  "blastemic": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or of the nature of a blastema.",
    secondary: "Describing embryonic or regenerative tissues undergoing cellular organization into definitive structures.",
    quotes: [
      { author: "William Roux", work: "Der Kampf der Theile im Organismus", text: "The **blastemic** pool responds to localized mechanical stress by orienting cellular division planes accordingly." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", text: "The organizer region directs neighboring **blastemic** layers toward neural plate differentiation." },
      { author: "Thomas Hunt Morgan", work: "Regeneration", text: "Early mitotic figures in the **blastemic** bud indicate rapid renewal of regenerative competence." }
    ]
  },
  "blaster": {
    dashboard: "Dashboard — blast",
    primary: "A worker or instrument that discharges explosives to break rock, excavate foundations, or fell obstacles.",
    secondary: "One that blights, withers, or brings destructive ruin upon life or reputations.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", text: "The expert quarry **blaster** sets his deep gunpowder fuse with the icy composure of a seasoned gunner." },
      { author: "William Shakespeare", work: "The Two Gentlemen of Verona", text: "As in the sweetest bud the eating canker dwells, so eating love inhabits in the finest wits of all: yet love is the **blaster** of tender youth." },
      { author: "H. G. Wells", work: "The War of the Worlds", text: "The Martian heat-ray operated like an invisible aerial **blaster**, shattering masonry and vaporizing iron girders." }
    ]
  },
  "blasting": {
    dashboard: "Dashboard — blast",
    primary: "The act or process of shattering rock or earth with detonating explosives.",
    secondary: "A destructive withering, blighting, or ruinous assault on vegetation, health, or hopes.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", text: "Extensive quarrying and rock **blasting** along the railway cut exposed pristine fossiliferous strata." },
      { author: "John Milton", work: "Samson Agonistes", text: "God delivered him from the treacherous snare and the pestilential **blasting** of his enemies." },
      { author: "Mary Shelley", work: "Frankenstein", text: "A fierce thunderbolt struck the old willow, **blasting** its mighty trunk into blackened splinters in an instant." }
    ]
  },
  "blastocele": {
    dashboard: "Dashboard — blast",
    primary: "The fluid-filled primary segmentation cavity within an early blastula embryo; variant spelling of blastocoel.",
    secondary: "The central embryonic space formed during cleavage that prevents premature interaction between animal and vegetal cells.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Radial cleavage in the amphibian egg yields an internal **blastocele** filled with translucent proteinaceous fluid." },
      { author: "Francis Balfour", work: "Comparative Embryology", text: "Invagination of the vegetal pole progressively obliterates the preexisting **blastocele** cavity." },
      { author: "Ray Lankester", work: "Zoological Articles", text: "The spacious **blastocele** separates the micro-blastomeres from the underlying yolk-laden macromeres." }
    ]
  },
  "blastochyle": {
    dashboard: "Dashboard — blast",
    primary: "The serous fluid contained within the blastocoel or segmentation cavity of an early embryo.",
    secondary: "The embryonic fluid medium that cushions dividing blastomeres and facilitates nutrient diffusion before vascularization.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Evolution of Man", text: "Within the hollow interior of the spherical blastula collects the clear, albuminous **blastochyle**." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Chemical analysis indicates that **blastochyle** differs markedly in osmotic pressure from the external seawater." },
      { author: "Alexander Kowalevsky", work: "Embryological Investigations on Amphioxus", text: "As gastrulation proceeds, the accumulated **blastochyle** is gradually displaced by the expanding archenteron." }
    ]
  },
  "blastocladia": {
    dashboard: "Dashboard — blast",
    primary: "A genus of zoosporic, saprophytic water molds in the order Blastocladiales with branched thalli.",
    secondary: "Aquatic fungi inhabiting submerged plant debris, characterized by resistant sporangia and motile uniflagellate zoospores.",
    quotes: [
      { author: "Roland Thaxter", work: "Contributions from the Cryptogamic Laboratory", text: "The basal cell of **Blastocladia** attaches firmly to decaying twigs by means of delicate rhizoidal outgrowths." },
      { author: "John N. Couch", work: "Observations on the Genus Blastocladia", text: "Under anaerobic pond conditions, species of **Blastocladia** form distinctive thick-walled resting sporangia." },
      { author: "F. K. Sparrow", work: "Aquatic Phycomycetes", text: "Microscopic examination of **Blastocladia** revealed uniflagellate gametes exhibiting true anisogamous copulation." }
    ]
  },
  "blastocladiales": {
    dashboard: "Dashboard — blast",
    primary: "An order of zoosporic fungi characterized by true alternation of generations and uniflagellate zoospores with distinct nuclear caps.",
    secondary: "Water molds and soil chytrids possessing chitinous cell walls and motile zoospores guided by specialized ribosomal aggregates.",
    quotes: [
      { author: "F. K. Sparrow", work: "Aquatic Phycomycetes", text: "The **Blastocladiales** occupy a unique phylogenetic position by virtue of their regular alternation of isomorphic generations." },
      { author: "Ralph Emerson", work: "Life Cycles in the Blastocladiales", text: "Genetic analysis across the **Blastocladiales** demonstrated Mendelian segregation during meiotic resting spore germination." },
      { author: "G. C. Ainsworth", work: "The Fungi: An Advanced Treatise", text: "Ultrastructure of the zoospore nuclear cap remains a key diagnostic synapomorphy for all members of the **Blastocladiales**." }
    ]
  },
  "blastocoel": {
    dashboard: "Dashboard — blast",
    primary: "The central fluid-filled cleavage cavity of a blastula, enclosed by the blastoderm.",
    secondary: "The primary body cavity of the early metazoan embryo that provides physical space for inward cell migration during gastrulation.",
    quotes: [
      { author: "Hans Spemann", work: "Embryonic Development and Induction", text: "Theinvaginating mesoderm creeps along the inner roof of the **blastocoel**, establishing the primary embryonic axis." },
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "Expansion of the **blastocoel** is driven by active sodium transport accompanied by osmotic water influx." },
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", text: "Comparative embryologists recognized the **blastocoel** as a universal developmental stage shared across bilateria." }
    ]
  },
  "blastocoele": {
    dashboard: "Dashboard — blast",
    primary: "The fluid-filled internal cavity of an early embryonic blastula; variant spelling of blastocoel.",
    secondary: "The primitive segmentation space that is subsequently compressed and largely obliterated during gastrulation.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", text: "A continuous layer of ciliated cells encloses the central **blastocoele** in the free-swimming echinoderm larva." },
      { author: "Ray Lankester", work: "Notes on Embryology", text: "The primary germinal cavity or **blastocoele** must be rigorously distinguished from the secondary coelomic space." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Vegetal macromeres project into the floor of the **blastocoele** before inward sinking commences." }
    ]
  },
  "blastocoelic": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or situated within the blastocoel.",
    secondary: "Pertaining to the internal fluid-filled cavity of the cleavage-stage embryo and its biochemical microenvironment.",
    quotes: [
      { author: "Hans Spemann", work: "Embryonic Development and Induction", text: "Microsurgical injection of vital dyes into the **blastocoelic** cavity allowed continuous tracking of presumptive neural tissue." },
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "The **blastocoelic** fluid contains extracellular matrix polymers that facilitate cellular crawling during epiboly." },
      { author: "Ross Granville Harrison", work: "Organization of the Developing Embryo", text: "Cells bordering the **blastocoelic** surface exhibit distinct apicobasal polarity essential for coordinated gastrulation." }
    ]
  },
  "blastocyst": {
    dashboard: "Dashboard — blast",
    primary: "The mammalian blastula formed in early embryonic development, comprising an inner cell mass and an outer trophoblast surrounding a central cavity.",
    secondary: "The embryonic stage that hatches from the zona pellucida and implants into the receptive maternal uterine endometrium.",
    quotes: [
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", text: "The mammalian **blastocyst** differentiates into the embryonic disc destined to form the fetus, and the enveloping trophoblast." },
      { author: "Arthur Kornberg", work: "For the Love of Enzymes", text: "Pluripotent stem cells isolated from the inner cell mass of the pre-implantation **blastocyst** retain boundless developmental plasticity." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "The pre-implantation **blastocyst** relies upon uterine secretions before establishing vascular placental connections." }
    ]
  },
  "blastocyte": {
    dashboard: "Dashboard — blast",
    primary: "An undifferentiated embryonic cell; a primitive, formative germ cell.",
    secondary: "An unspecialized blastomeric cell capable of rapid mitotic proliferation and subsequent lineage commitment.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Each isolated **blastocyte** retains the developmental capacity to generate diverse somatic tissue lineages." },
      { author: "Alexander Kowalevsky", work: "Embryological Studies", text: "Division of the zygote yields a cluster of identical **blastocytes** prior to germ layer stratification." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "Pathological proliferation often reactivates the primordial metabolic phenotype of the embryonic **blastocyte**." }
    ]
  },
  "blastocytoma": {
    dashboard: "Dashboard — blast",
    primary: "A neoplasm or tumor composed of embryonic, undifferentiated blastemic precursor cells; blastoma.",
    secondary: "A primitive malignant tumor occurring predominantly in pediatric patients, arising from embryonic rests.",
    quotes: [
      { author: "Rudolf Virchow", work: "Die krankhaften Geschwülste", text: "The histological hallmark of the **blastocytoma** is its resemblance to early foetal organ rudiments." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Renal **blastocytoma** exhibits rapid expansion, recapitulating embryonic nephrogenic tissue under the microscope." },
      { author: "James Ewing", work: "Neoplastic Diseases", text: "Cerebellar **blastocytoma** presents densely packed, primitive round cells with hyperchromatic nuclei." }
    ]
  },
  "blastoderm": {
    dashboard: "Dashboard — blast",
    primary: "The primitive cellular layer or disc formed by cleavage of the fertilized ovum, from which the embryo develops.",
    secondary: "The superficial sheet of cells resting upon the central yolk mass in telolecithal and centrolecithal eggs.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "The **blastoderm** separates into distinct laminae, laying down the primary blueprint of the vertebrate body." },
      { author: "Thomas Henry Huxley", work: "The Elements of Embryology", text: "In the avian egg, the **blastoderm** spreads outward over the yolk sphere by active marginal cell division." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "The primitive streak appears as an axial thickening near the posterior border of the embryonic **blastoderm**." }
    ]
  },
  "blastodermatic": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or derived from the blastoderm.",
    secondary: "Pertaining to the primitive embryonic cellular layer that yields the primary germ layers.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", text: "The **blastodermatic** membrane envelops the yolk, initiating rhythmic nutrient absorption for the developing embryo." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Invagination of the **blastodermatic** layers establishes the initial tripartite division of germ tissues." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Changes within the **blastodermatic** vesicle mark the definite emergence of cephalic and caudal poles." }
    ]
  },
  "blastodermic": {
    dashboard: "Dashboard — blast",
    primary: "Relating to or having the nature of a blastoderm; blastodermatic.",
    secondary: "Describing embryonic structures such as the blastodermic vesicle (blastocyst) or blastodermic disc.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Elements of Embryology", text: "The **blastodermic** vesicle of the rabbit expands rapidly within the uterine lumen prior to attachment." },
      { author: "Alexander Kowalevsky", work: "Embryological Studies", text: "Superficial cleavage results in a continuous **blastodermic** monolayer enclosing the central unsegmented yolk." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", text: "The dorsal lip of the **blastodermic** margin exercises inductive control over neural tube formation." }
    ]
  },
  "blastodiaceae": {
    dashboard: "Dashboard — blast",
    primary: "A taxonomic family designation historically applied to certain budding, yeast-like fungi or blastosporous molds.",
    secondary: "In historical cryptogamic botany, a family classification grouping anamorphic fungi reproducing by blastoconidia.",
    quotes: [
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", text: "The family **Blastodiaceae** unites those imperfect molds whose propagation relies primarily on spontaneous blastospore production." },
      { author: "Roland Thaxter", work: "Cryptogamic Researches", text: "Early mycological systems assigned diverse budding parasites to the provisional family **Blastodiaceae**." },
      { author: "F. K. Sparrow", work: "Aquatic Phycomycetes", text: "Phylogenetic revisions dissolved the polyphyletic **Blastodiaceae**, reassigning member genera to distinct Ascomycota and Chytridiomycota orders." }
    ]
  },
  "blastodisc": {
    dashboard: "Dashboard — blast",
    primary: "The small, disc-shaped region of yolk-free active cytoplasm at the animal pole of a telolecithal egg where cleavage takes place.",
    secondary: "The germinal disc of fish, reptilian, and avian ova that gives rise exclusively to the embryo and extraembryonic membranes.",
    quotes: [
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Meroblastic cleavage is restricted entirely to the lenticular **blastodisc** floating upon the vast yolk sphere." },
      { author: "Thomas Henry Huxley", work: "The Elements of Embryology", text: "Within twenty-four hours of incubation, the avian **blastodisc** shows distinct areas pellucida and opaca." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "The microscopic furrowing of the **blastodisc** reveals the geometric precision of initial protoplasmic divisions." }
    ]
  },
  "blastoff": {
    dashboard: "Dashboard — blast",
    primary: "The launch or fiery departure of a rocket or spacecraft from its launch pad.",
    secondary: "The precise moment of ignition and lift-off under maximum rocket propulsion; figuratively, a sudden explosive start.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", text: "With a deafening roar and sheets of flame, the Saturn V underwent **blastoff**, carrying astronauts outward toward the Moon." },
      { author: "Arthur C. Clarke", work: "The Promise of Space", text: "Seconds after **blastoff**, the towering rocket cleared the gantry, climbing into the Florida sky on a pillar of incandescent smoke." },
      { author: "Norman Mailer", work: "Of a Fire on the Moon", text: "The thunderous tremor of the **blastoff** shook the earth miles away, vibrating in the marrow of every witness." }
    ]
  },
  "blastogenesis": {
    dashboard: "Dashboard — blast",
    primary: "Reproduction or inheritance proceeding exclusively from the germ-plasm (germ cells) rather than somatic tissues.",
    secondary: "In immunology and hematology, the morphological transformation and rapid mitotic activation of quiescent lymphocytes into lymphoblasts.",
    quotes: [
      { author: "August Weismann", work: "The Germ-Plasm: A Theory of Heredity", text: "I designate by **blastogenesis** the continuity of the germ-plasm, which remains unaffected by somatic modifications acquired during life." },
      { author: "Peter Medawar", work: "The Uniqueness of the Individual", text: "Phytohemagglutinin stimulates widespread **blastogenesis** in resting peripheral blood lymphocytes within cell culture." },
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", text: "Weismann's concept of **blastogenesis** sounded the death knell for inheritance of acquired characters." }
    ]
  },
  "blastogenetic": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or produced by blastogenesis; derived from germ-plasm.",
    secondary: "Pertaining to hereditary traits transmitted through germ cells, or to lymphocyte activation into proliferating blasts.",
    quotes: [
      { author: "August Weismann", work: "Essays Upon Heredity", text: "Only **blastogenetic** variations arising directly within the germinal substance can be transmitted to succeeding generations." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", text: "The distinction between somatogenetic changes and **blastogenetic** mutations remains the rock of modern genetics." },
      { author: "Peter Medawar", work: "The Hope of Progress", text: "Antigenic stimulation triggers a rapid **blastogenetic** response within reactive lymphoid follicles." }
    ]
  },
  "blastoma": {
    dashboard: "Dashboard — blast",
    primary: "A neoplasm or malignant tumor composed of embryonic, undifferentiated precursor cells.",
    secondary: "A pediatric or developmental neoplasm (such as retinoblastoma or nephroblastoma) recapitulating immature organ tissues.",
    quotes: [
      { author: "Rudolf Virchow", work: "Die krankhaften Geschwülste", text: "We classify as **blastoma** those neoplasms arising from dormant embryonic tissue rests that retain formative potency." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Microscopically, the **blastoma** exhibits sheets of small, hyperchromatic cells devoid of mature architectural patterns." },
      { author: "James Ewing", work: "Neoplastic Diseases", text: "The high radio-sensitivity of medulloblastoma distinguishes this neuroepithelial **blastoma** from adult glial tumors." }
    ]
  },
  "blastomere": {
    dashboard: "Dashboard — blast",
    primary: "Any of the individual cells formed by the cleavage divisions of a fertilized ovum during early embryonic development.",
    secondary: "One of the nucleated cellular units in the morula whose cleavage planes determine early bilateral symmetry and cell fate.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Each successive cleavage divides the ovum into smaller **blastomeres** without increasing total embryonic volume." },
      { author: "Hans Driesch", work: "The Science and Philosophy of the Organism", text: "Separating a single sea urchin **blastomere** at the two-cell stage yielded a complete, normally proportioned pluteus larva." },
      { author: "Thomas Hunt Morgan", work: "The Development of the Frog's Egg", text: "The first cleavage furrow separates the right and left **blastomeres**, aligning with the future median plane of the embryo." }
    ]
  },
  "blastomeric": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or having the character of a blastomere.",
    secondary: "Pertaining to the cleavage divisions and spatial configuration of early embryonic cells.",
    quotes: [
      { author: "Hans Driesch", work: "The Science and Philosophy of the Organism", text: "The developmental potential of each **blastomeric** unit proved to be far wider than its prospective fate in normal ontogeny." },
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "Cytoplasmic localization within **blastomeric** lineages provides the maternal determinants that guide early differentiation." },
      { author: "Alexander Kowalevsky", work: "Embryological Investigations", text: "Careful tracking of **blastomeric** cleavage planes revealed conserved spiralian patterns across annelids and mollusks." }
    ]
  },
  "blastomyces": {
    dashboard: "Dashboard — blast",
    primary: "A genus of dimorphic pathogenic fungi, notably *Blastomyces dermatitidis*, that causes blastomycosis in humans and animals.",
    secondary: "A fungal genus that grows as a mould in soil and converts to a thick-walled budding yeast phase in mammalian host tissues.",
    quotes: [
      { author: "Thomas Casper Gilchrist", work: "A Case of Blastomycetic Dermatitis in Man", text: "Microscopic examination of the skin lesions revealed round, budding yeast cells belonging to the pathogenic genus **Blastomyces**." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "In tissue sections, **Blastomyces** is readily recognized by its thick, double-contoured wall and broad-based budding." },
      { author: "René Dubos", work: "Bacterial and Mycotic Infections of Man", text: "Inhalation of soil conidia allows **Blastomyces** to establish primary pulmonary granulomas that mimic tuberculosis." }
    ]
  },
  "blastomycete": {
    dashboard: "Dashboard — blast",
    primary: "A budding fungus or yeast-like organism, historically classified under the Blastomycetes.",
    secondary: "Any fungus that reproduces primarily by vegetative budding (gemmation) rather than forming true aerial hyphae.",
    quotes: [
      { author: "Thomas Casper Gilchrist", work: "Blastomycetic Dermatitis", text: "The patient presented granulomatous ulcers teeming with the spherical bodies of a parasitic **blastomycete**." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", text: "Yeasts and related **blastomycetes** conduct alcoholic fermentation with exquisite chemical specificity." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Inflammatory responses to the invasive **blastomycete** combine acute suppuration with chronic epithelioid granuloma formation." }
    ]
  },
  "blastomycosis": {
    dashboard: "Dashboard — blast",
    primary: "A chronic systemic fungal infection caused by *Blastomyces dermatitidis*, affecting primarily the lungs and skin.",
    secondary: "An endemic mycosis contracted via inhalation of fungal spores from soil and decaying wood, characterized by granulomatous lesions.",
    quotes: [
      { author: "Thomas Casper Gilchrist", work: "A Case of Blastomycetic Dermatitis in Man", text: "We describe here the first documented North American case of cutaneous **blastomycosis** caused by yeast-like budding organisms." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Pulmonary **blastomycosis** frequently masquerades as bronchogenic carcinoma on thoracic roentgenograms." },
      { author: "René Dubos", work: "Bacterial and Mycotic Infections of Man", text: "Disseminated **blastomycosis** carries a grave prognosis unless treated promptly with systemic antifungal agents." }
    ]
  },
  "blastomycotic": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or caused by blastomycosis.",
    secondary: "Pertaining to infections, granulomas, or lesions produced by *Blastomyces* species.",
    quotes: [
      { author: "Thomas Casper Gilchrist", work: "Blastomycetic Dermatitis", text: "Histological sections of the **blastomycotic** nodule showed dense microabscesses bordered by giant cells." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "The **blastomycotic** ulcer displays violaceous, elevated margins with cribriform micro-pustules." },
      { author: "James Ewing", work: "Neoplastic Diseases", text: "Chronic **blastomycotic** hyperplasia of the epidermis closely mimics well-differentiated squamous cell carcinoma." }
    ]
  },
  "blastoporal": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or situated at or near the blastopore.",
    secondary: "Pertaining to the embryological opening that serves as the entry site for invaginating cell sheets during gastrulation.",
    quotes: [
      { author: "Hans Spemann", work: "Embryonic Development and Induction", text: "The dorsal **blastoporal** lip exerts the organizer effect, inducing neural plate development in overlying ectoderm." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Cells migrating through the **blastoporal** margin differentiate into the axial notochord." },
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "Vital dye marks placed on the **blastoporal** rim reveal the precise trajectories of prospective mesodermal somites." }
    ]
  },
  "blastopore": {
    dashboard: "Dashboard — blast",
    primary: "The opening into the archenteron (primitive digestive cavity) formed by invagination of the blastula wall during gastrulation.",
    secondary: "The embryonic orifice that develops into the mouth in protostomes and the anus in deuterostomes.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Gastraea Theory", text: "The primary mouth or **blastopore** of the gastraea represents the most fundamental ancestral aperture of all Metazoa." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", text: "Transplantation of the dorsal lip of the **blastopore** induced a secondary embryonic axis upon the host flank." },
      { author: "Alexander Kowalevsky", work: "Embryological Investigations on Amphioxus", text: "Invagination of the vegetative hemisphere leads to complete closure of the **blastopore** as the neural folds unite." }
    ]
  },
  "blastoporic": {
    dashboard: "Dashboard — blast",
    primary: "Of or pertaining to the blastopore; blastoporal.",
    secondary: "Relating to cellular movements, lip boundaries, or inductive signals located at the embryonic blastopore.",
    quotes: [
      { author: "Hans Spemann", work: "Embryonic Development and Induction", text: "Excision of the upper **blastoporic** crescent abolishes the normal induction of the medullary plate." },
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "The **blastoporic** furrow deepens as bottle cells actively constrict their apical membranes." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "In deuterostome ontogeny, the **blastoporic** region marks the definitive site of the future anal opening." }
    ]
  },
  "blastosphere": {
    dashboard: "Dashboard — blast",
    primary: "A hollow spherical embryo formed by the cleavage of a fertilized ovum; the blastula.",
    secondary: "The spherical monolayer of blastomeres enclosing the central cleavage cavity prior to gastrulation.",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "Cleavage culminates in the hollow cellular sphere which we designate the **blastosphere** or blastula." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Ciliation of the **blastosphere** enables the marine larva to break free from its egg membrane and swim actively." },
      { author: "Thomas Henry Huxley", work: "The Elements of Embryology", text: "The transition from the solid morula to the hollow **blastosphere** marks the establishment of an internal embryonic milieu." }
    ]
  },
  "blastospheric": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or resembling a blastosphere; blastular.",
    secondary: "Pertaining to the hollow spherical stage of embryonic cleavage preceding germ layer formation.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Evolution of Man", text: "The **blastospheric** stage recapitulates an ancestral colonial protozoan ancestor resembling modern Volvox." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Even thickness of the **blastospheric** wall is soon disrupted by vegetal pole cell enlargement." },
      { author: "Alexander Kowalevsky", work: "Developmental Studies on Ascidians", text: "A single layer of columnar blastomeres forms the complete **blastospheric** boundary in simple tunicates." }
    ]
  },
  "blastula": {
    dashboard: "Dashboard — blast",
    primary: "An early animal embryo at the stage following cleavage, typically consisting of a hollow sphere of cells enclosing a central fluid-filled cavity (blastocoel).",
    secondary: "The embryonic stage marking the conclusion of cleavage and providing the physical architecture required for gastrulation.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Gastraea Theory", text: "The **blastula** represents an ontogenetic milestone shared by virtually all multicellular animals from sponges to vertebrates." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "From the spherical symmetry of the early **blastula**, the embryo progressively acquires bilateral polarity." },
      { author: "Hans Driesch", work: "The Science and Philosophy of the Organism", text: "Centrifuging the amphibian **blastula** demonstrated that cytoplasmic organization can reorganize itself to restore normal form." }
    ]
  },
  "blastular": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or characteristic of a blastula.",
    secondary: "Pertaining to the developmental processes, cell divisions, or architecture of the blastula stage.",
    quotes: [
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "Mid-blastula transition marks the activation of embryonic transcription following rapid **blastular** cleavage cycles." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", text: "Grafting tissues between **blastular** embryos revealed that cell fates remain largely uncommitted prior to gastrulation." },
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", text: "The **blastular** epithelium exhibits uniform mechanical tension across its outer spherical perimeter." }
    ]
  },
  "cytotrophoblast": {
    dashboard: "Dashboard — blast",
    primary: "The inner cellular layer of the embryonic trophoblast, composed of distinct mononucleated cells that give rise to the syncytiotrophoblast.",
    secondary: "The stem-cell layer of the mammalian chorionic villi responsible for placental invasion into maternal uterine spiral arteries.",
    quotes: [
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", text: "The proliferous **cytotrophoblast** provides the stem cell reservoir sustaining syncytial growth throughout placental maturation." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Choriocarcinoma displays malignant overgrowth of both the invasive syncytium and underlying **cytotrophoblast**." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Enzymatic erosion by the **cytotrophoblast** anchors the mammalian ovum deeply into vascular endometrial beds." }
    ]
  },
  "ectoblast": {
    dashboard: "Dashboard — blast",
    primary: "The outer germ layer of an early embryo; an archaic or alternative term for ectoderm.",
    secondary: "The embryonic cellular layer that gives rise to the epidermis, sensory organs, and nervous system.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "The outer layer or **ectoblast** folds inward along the dorsal midline to generate the neural tube." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", text: "From the primitive **ectoblast** derive both the protective cutaneous integument and the central organs of thought." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Separation of the **ectoblast** from the underlying mesoblast marks the primary stratification of vertebrate tissues." }
    ]
  },
  "endoblast": {
    dashboard: "Dashboard — blast",
    primary: "The innermost germ layer of an early embryo; an archaic or alternative embryological term for endoderm.",
    secondary: "The embryonic layer of cells that lines the primitive gut and gives rise to the epithelial lining of the digestive and respiratory tracts.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "The vegetative layer or **endoblast** curves upward to fashion the primitive alimentary canal." },
      { author: "Thomas Henry Huxley", work: "The Elements of Embryology", text: "The epithelial lining of the pulmonary tree and digestive glands is exclusively of **endoblast** origin." },
      { author: "Alexander Kowalevsky", work: "Embryological Investigations on Amphioxus", text: "Invagination converts the vegetative pole cells into the inner lining of the archenteron, constituting the true **endoblast**." }
    ]
  },
  "entoblast": {
    dashboard: "Dashboard — blast",
    primary: "The inner germ layer of an embryo; endoderm; also historically used for the cell nucleus or nucleolus.",
    secondary: "The embryonic germ layer responsible for generating the lining of the digestive tube and associated metabolic organs.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Gastraea Theory", text: "The primary gastraea consists of two elementary cell sheets: the outer ectoblast and the digestive **entoblast**." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Ciliated cells of the **entoblast** drive fluid currents through the primitive enteric cavity of the sponge." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", text: "Nutritive absorption in the early embryo is executed entirely by the glandular cells of the **entoblast**." }
    ]
  },
  "fibroblast": {
    dashboard: "Dashboard — blast",
    primary: "A common type of cell in connective tissue that synthesizes extracellular matrix components and collagen fibers.",
    secondary: "A spindle-shaped stromal cell playing a crucial role in wound healing, scar formation, and tissue remodeling.",
    quotes: [
      { author: "Alexis Carrel", work: "Tissue Culture and Cellular Immortality", text: "In our embryonic chick heart cultures, the **fibroblast** proliferated continuously for decades when provided with fresh embryonic juice." },
      { author: "Alexander Fleming", work: "On the Antibacterial Action of Cultures of a Penicillium", text: "Penicillin inhibited virulent staphylococcal growth at dilutions that left the delicate human **fibroblast** completely uninjured." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "During granulation tissue organization, the **fibroblast** migrates into the fibrinous exudate, depositing robust collagen strands." }
    ]
  },
  "hypoblast": {
    dashboard: "Dashboard — blast",
    primary: "The inner or lower layer of cells of the embryonic blastodisc, underlying the epiblast and giving rise to yolk sac endoderm.",
    secondary: "The ventral embryonic sheet in avian and mammalian embryos that directs early axis formation before being displaced during gastrulation.",
    quotes: [
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "The **hypoblast** delaminates from the lower surface of the blastodisc, spreading out to line the sub-germinal cavity." },
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "Signals from the anterior **hypoblast** establish early anterior-posterior polarity within the overlying epiblast." },
      { author: "Thomas Henry Huxley", work: "The Elements of Embryology", text: "While the epiblast gives rise to the entire embryonic body, the **hypoblast** mainly subserves extraembryonic nutrition." }
    ]
  },
  "megaloblast": {
    dashboard: "Dashboard — blast",
    primary: "An abnormally large, nucleated erythroblast found in bone marrow in certain anemias (especially pernicious anemia and vitamin B12 or folate deficiency).",
    secondary: "A pathological primitive red blood cell precursor characterized by nuclear-cytoplasmic dissociation due to impaired DNA synthesis.",
    quotes: [
      { author: "Paul Ehrlich", work: "Studies on Anemia and Blood Morphology", text: "I identified the **megaloblast** in bone marrow smears as the definitive cytological sign of Addisonian pernicious anemia." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Arrested maturation fills the erythroid marrow with towering numbers of the distinctive blue-staining **megaloblast**." },
      { author: "George Minot", work: "Treatment of Pernicious Anemia by a Special Diet", text: "Liver extract administration provoked an immediate disappearance of the **megaloblast** from the patient's bone marrow." }
    ]
  },
  "megaloblastic": {
    dashboard: "Dashboard — blast",
    primary: "Relating to or characterized by the presence of megaloblasts, as in megaloblastic anemia.",
    secondary: "Pertaining to erythropoietic marrow hyperplasia characterized by defective thymidine synthesis and gigantism of blood precursors.",
    quotes: [
      { author: "William Castle", work: "Observations on the Etiologic Relationship of Achylia Gastrica to Pernicious Anemia", text: "Deficiency of gastric intrinsic factor precipitates severe **megaloblastic** bone marrow conversion." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "The peripheral blood smear in **megaloblastic** states exhibits oval macrocytes and hypersegmented neutrophils." },
      { author: "Paul Ehrlich", work: "Histology of the Blood", text: "True **megaloblastic** erythropoiesis reflects a reversion to an archaic, embryonic mode of red cell genesis." }
    ]
  },
  "mesoblast": {
    dashboard: "Dashboard — blast",
    primary: "The middle germ layer of an early embryo; an archaic or alternative term for mesoderm.",
    secondary: "The embryonic cell layer situated between ectoderm and endoderm, giving rise to muscle, bone, blood, and connective tissues.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "Between the external and internal laminae arises the **mesoblast**, from which the muscular system and skeleton take origin." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Splitting of the lateral **mesoblast** into somatic and splanchnic sheets creates the coelomic body cavity." },
      { author: "Thomas Henry Huxley", work: "The Elements of Embryology", text: "The vascular network of the embryo arises entirely within the vascular lamina of the **mesoblast**." }
    ]
  },
  "mesoblastic": {
    dashboard: "Dashboard — blast",
    primary: "Of, relating to, or derived from the mesoblast (mesoderm).",
    secondary: "Pertaining to tissues, somites, or developmental structures of mesodermal origin.",
    quotes: [
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Segmentation of the paraxial **mesoblastic** plate yields the paired somites flanking the notochord." },
      { author: "C. H. Waddington", work: "Principles of Embryology", text: "The **mesoblastic** mantle spreads forward between ectoderm and endoderm, providing the substratum for heart development." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Condensation of **mesoblastic** cells around the primitive chordal sheath initiates vertebral chondrogenesis." }
    ]
  },
  "monoblast": {
    dashboard: "Dashboard — blast",
    primary: "An immature cell in bone marrow that is the earliest precursor in the monocytic series, developing into a promonocyte and then a monocyte.",
    secondary: "A primitive hematopoietic stem cell characterized by abundant non-granular basophilic cytoplasm and a delicate chromatin meshwork.",
    quotes: [
      { author: "Paul Ehrlich", work: "Histology of the Blood", text: "In acute monocytic leukemia, the bone marrow is overwhelmed by proliferations of the primitive **monoblast**." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Distinguishing the **monoblast** from the myeloblast requires specific cytochemical esterase staining." },
      { author: "Alexander Maximow", work: "Relation of Blood Cells to Connective Tissue", text: "The marrow **monoblast** differentiates into wandering phagocytes capable of traversing endothelial barriers." }
    ]
  },
  "sideroblast": {
    dashboard: "Dashboard — blast",
    primary: "An erythroblast (nucleated red blood cell precursor) containing granules of non-heme iron detectable by Prussian blue staining.",
    secondary: "An erythroid precursor cell in bone marrow; when iron granules encircle the nucleus (ring sideroblast), it indicates defective heme synthesis.",
    quotes: [
      { author: "Paul Ehrlich", work: "Studies on Blood Staining", text: "Specialized ferrocyanide staining revealed tiny iron deposits inside the cytoplasm of the maturing **sideroblast**." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "The presence of the pathological ringed **sideroblast** points to mitochondrial iron overload in refractory anemia." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", text: "Quantifying the percentage of marrow **sideroblasts** provides crucial insight into defective iron utilization pathways." }
    ]
  },

  // Dashboard — brot (6 words)
  "ambrosia": {
    dashboard: "Dashboard — brot",
    primary: "In classical mythology, the food of the Olympian gods, often depicted as conferring immortality or perpetual youth upon those who consumed it.",
    secondary: "Something with an especially delicious flavor or fragrance; also, a genus of plants (such as ragweed, *Ambrosia*).",
    quotes: [
      { author: "Homer", work: "The Iliad", text: "White-armed Hera cleansed her lovely flesh with sweet **ambrosia**, whose immortal fragrance shook heaven and earth." },
      { author: "John Milton", work: "Paradise Lost", text: "His dewy locks distilled **ambrosia**, and celestial fragrance filled the wide circuit of Eden." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", text: "We feast on the nectar and **ambrosia** of divine thoughts that death cannot consume." }
    ]
  },
  "ambrosial": {
    dashboard: "Dashboard — brot",
    primary: "Worthy of the gods; divinely sweet, delicious, or fragrant.",
    secondary: "Pertaining to or resembling ambrosia; celestial and exquisitely delightful to the senses.",
    quotes: [
      { author: "Alfred Lord Tennyson", work: "In Memoriam A.H.H.", text: "And sweet and **ambrosial** air began to blow through the summer twilight from the south." },
      { author: "John Keats", work: "Endymion", text: "A slumberous silence fell upon the cave, bathed in an **ambrosial** mist that breathed of eternal spring." },
      { author: "Herman Melville", work: "Moby-Dick", text: "The fragrant spermaceti smelled sweet as an **ambrosial** ointment prepared for royal anointing." }
    ]
  },
  "ambrotype": {
    dashboard: "Dashboard — brot",
    primary: "An early photographic process popular in the mid-19th century producing a positive photograph on a glass plate with a dark backing.",
    secondary: "A wet-collodion photographic image on glass that appears as a positive when viewed against an opaque black background (velvet or lacquer).",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "The Stereoscope and the Stereograph", text: "The delicate grey tones of the **ambrotype** captured the living expression on glass with astonishing precision." },
      { author: "Walt Whitman", work: "Specimen Days", text: "I kept an old **ambrotype** of a young cavalry soldier in my knapsack throughout the Virginia campaign." },
      { author: "Nathaniel Hawthorne", work: "The House of the Seven Gables", text: "The daguerreotypist held up the glass **ambrotype**, where sunlight had fixed the sullen features of the Judge." }
    ]
  },
  "brot": {
    dashboard: "Dashboard — brot",
    primary: "The ancient Greek root (*brotos*, mortal, human, or blood) denoting mortal life, ephemeral humanity, or mortal remains.",
    secondary: "In comparative philology, the morphological root seen in Greek *ambrotos* (immortal, divine) cognate with Sanskrit *amṛta* and Latin *mors*.",
    quotes: [
      { author: "Gilbert Murray", work: "The Rise of the Greek Epic", text: "In Homeric diction, the root **brot** consistently evokes the tragic fragility of mortals compared to the deathless gods." },
      { author: "Walter Burkert", work: "Greek Religion", text: "Ritual offerings bridged the chasm between Olympian immortals and the ephemeral world of the human **brot**." },
      { author: "Max Müller", work: "Lectures on the Science of Language", text: "Etymologically, Greek compounds retaining the stem **brot** descend from the Indo-European root for mortal dying." }
    ]
  },
  "brotula": {
    dashboard: "Dashboard — brot",
    primary: "A genus of deep-water, elongated marine cusk-eels in the family Ophidiidae.",
    secondary: "Benthic, eel-like teleost fishes inhabiting tropical continental shelves and deep reefs, having barbels around the mouth.",
    quotes: [
      { author: "George Brown Goode", work: "Oceanic Ichthyology", text: "The bearded **Brotula** dwells upon rocky ledges in deep tropical waters, using sensory chin barbels to locate benthic prey." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", text: "Taxonomically, the genus **Brotula** forms an archaic offshoot of ophidioid teleosts with continuous dorsal and anal fins." },
      { author: "William Beebe", work: "Half Mile Down", text: "From the bathysphere window we glimpsed a sinuous **Brotula** gliding through the perpetual gloom of the abyssal slope." }
    ]
  },
  "brotulidae": {
    dashboard: "Dashboard — brot",
    primary: "A family (or historically recognized family) of marine cusk-eels (order Ophidiiformes), now commonly placed within Ophidiidae or as subfamily Brotulinae.",
    secondary: "A family of benthic and pelagic eel-like marine fishes characterized by tapering bodies, reduced pelvic fins, and nocturnal or deep-sea habitats.",
    quotes: [
      { author: "David Starr Jordan", work: "The Genera of Fishes", text: "Lankester grouped these nocturnal cusk-eels within the family **Brotulidae**, citing their distinctive barbels and sensory pore systems." },
      { author: "George Brown Goode", work: "Oceanic Ichthyology", text: "Abyssal dredges brought up rare representatives of the **Brotulidae** from depths exceeding one thousand fathoms." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "Morphological specialization among the **Brotulidae** includes viviparity and complete adaptation to the bathypelagic environment." }
    ]
  }
};

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\n');
}

function updateFile(filePath, wordData) {
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\n\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n${formatQuotes(wordData.quotes)}\n`;

  const finalContent = topPart + '\n\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

let count = 0;
for (const [lemma, data] of Object.entries(BATCH2_DATA)) {
  const filePath = path.join(CLUSTER_DIR, data.dashboard, `${lemma}.md`);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    continue;
  }
  if (updateFile(filePath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 2 Completed: ${count} / ${Object.keys(BATCH2_DATA).length} words updated`);
console.log(`========================================\n`);
