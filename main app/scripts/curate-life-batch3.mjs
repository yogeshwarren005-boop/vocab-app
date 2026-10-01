import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Life & Vitality';
const DASHBOARD = 'Dashboard — gen';

const BATCH3_DATA = {
  "abiogenesis": {
    primary: "The generation of living organisms from inanimate matter; spontaneous generation, or modern chemical origin of life theories.",
    secondary: "The evolutionary hypothesis that organic macromolecules and the first cellular organisms originated from inorganic compounds on the prebiotic Earth.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Biogenesis and Abiogenesis", text: "I shall call the doctrine that living matter may be produced by not living matter, the hypothesis of **abiogenesis**." },
      { author: "Alexander Oparin", work: "The Origin of Life", text: "Coacervate droplets represented an essential physical step in the gradual evolutionary process of terrestrial **abiogenesis**." },
      { author: "J. B. S. Haldane", work: "The Origin of Life", text: "Ultraviolet irradiation of a methane-ammonia atmosphere paved the energetic pathway for primordial **abiogenesis**." }
    ]
  },
  "abiogenetic": {
    primary: "Of, relating to, or produced by abiogenesis; non-biological in origin.",
    secondary: "Pertaining to chemical reactions and processes generating organic molecules without the involvement of living systems.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Critiques and Addresses", text: "Francesco Redi's classic experiments overthrew the ancient **abiogenetic** assumptions regarding maggots in meat." },
      { author: "Harold Urey", work: "The Planets: Their Origin and Development", text: "Electric discharges across reducing gas mixtures produced abundant **abiogenetic** amino acids and hydroxy acids." },
      { author: "Cyril Ponnamperuma", work: "The Origins of Life", text: "Interstellar dust clouds contain complex **abiogenetic** carbon molecules synthesized before planetary accretion." }
    ]
  },
  "agene": {
    primary: "Nitrogen trichloride (NCl3), historically utilized as an artificial bleaching and aging agent for commercial wheat flour.",
    secondary: "A toxic chemical flour improver withdrawn from commerce after Edward Mellanby proved it induced canine epileptiform running fits.",
    quotes: [
      { author: "Edward Mellanby", work: "Diet and Canine Hysteria", text: "Commercial flour treated with **agene** consistently produced running fits and severe neurotoxicity in experimental hounds." },
      { author: "E. V. McCollum", work: "A History of Nutrition", text: "The discovery of methionine sulfoximine in **agene**-bleached gluten prompted health authorities to ban its culinary use." },
      { author: "Lord Horder", work: "Fifty Years of Medicine", text: "Public health reformers campaigned vigorously to eliminate the **agene** process from the British bread supply." }
    ]
  },
  "agenesis": {
    primary: "The complete absence or failure of development of an organ, limb, or anatomical structure during embryonic ontogeny.",
    secondary: "Congenital failure of a primitive tissue primordium to form, as in renal agenesis or agenesis of the corpus callosum.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "We contrast developmental hypoplasia with total **agenesis**, where the cellular rudiment fails to appear in early embryogenesis." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Bilateral renal **agenesis** is incompatible with extrauterine life and results in the characteristic facies of Potter's syndrome." },
      { author: "James Ewing", work: "Neoplastic Diseases", text: "Congenital **agenesis** of endocrine tissue highlights the critical role of hormonal feedback loops during fetal life." }
    ]
  },
  "agonadal": {
    primary: "Lacking gonads (ovaries or testes); characterized by the congenital absence or surgical excision of reproductive organs.",
    secondary: "Describing developmental conditions such as pure gonadal dysgenesis or embryonic agonadism resulting in lack of gonadal steroids.",
    quotes: [
      { author: "William Boyd", work: "Pathology for the Physician", text: "In congenital **agonadal** states, sexual differentiation proceeds along default female phenotypic pathways in the absence of androgens." },
      { author: "Frank Beach", work: "Hormones and Behavior", text: "Experimental **agonadal** animals display a total suppression of sex-typical courtship displays and mating behaviors." },
      { author: "Robert Greenblatt", work: "Office Endocrinology", text: "Elevated gonadotropin levels confirm pituitary hypersecretion attempting to stimulate an **agonadal** pelvis." }
    ]
  },
  "allergen": {
    primary: "Any substance (such as pollen, venom, animal dander, or dust mites) capable of inducing an allergic or hypersensitivity reaction.",
    secondary: "An environmental antigen that selectively elicits immunoglobulin E (IgE) synthesis and mast cell degranulation in atopic individuals.",
    quotes: [
      { author: "Clemens von Pirquet", work: "Allergie", text: "I designate as an **allergen** any foreign substance that alters the reactivity of the organism upon repeated contact." },
      { author: "Bela Schick", work: "Serum Sickness", text: "Horse serum acts as a potent **allergen**, provoking urticaria and systemic shock upon second inoculation." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Cross-linking of surface-bound IgE by the invading **allergen** triggers explosive histamine release from mast cell granules." }
    ]
  },
  "allergenic": {
    primary: "Having the property of an allergen; capable of causing an allergic response.",
    secondary: "Characterized by specific antigenic epitopes that stimulate IgE-mediated immunological hypersensitivity in sensitized hosts.",
    quotes: [
      { author: "Clemens von Pirquet", work: "Clinical Studies on Allergy", text: "Fractionation of ragweed extract isolated its most potent **allergenic** protein component." },
      { author: "Bela Schick", work: "The Nature of Cutaneous Reactions", text: "Intradermal injection elicited an immediate wheal-and-flare confirming the **allergenic** potency of the test serum." },
      { author: "René Dubos", work: "The Bacterial Cell", text: "Certain capsular polysaccharides display negligible toxicity yet evoke violent **allergenic** responses upon reinfection." }
    ]
  },
  "anagenesis": {
    primary: "Progressive evolutionary change occurring within a single unbranching lineage over time; phyletic evolution.",
    secondary: "The evolutionary accumulation of morphological and physiological adaptations without speciation, contrasted with cladogenesis.",
    quotes: [
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", text: "We must distinguish between cladogenesis or branching, and **anagenesis** or directional advancement along a continuous phyletic lineage." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", text: "Speciation creates diversity, but progressive **anagenesis** builds overarching biological complexity across geological eras." },
      { author: "George Gaylord Simpson", work: "The Major Features of Evolution", text: "The fossil horse sequence long served as a classic textbook exemplar of sustained **anagenesis** in response to expanding grasslands." }
    ]
  },
  "antigen": {
    primary: "Any foreign substance that induces an immune response in the body, especially the production of specific antibodies.",
    secondary: "A macromolecule bearing distinct epitopes capable of binding specifically to T-cell receptors or B-cell surface immunoglobulins.",
    quotes: [
      { author: "Paul Ehrlich", work: "Studies on Immunity", text: "The receptors of the side-chain theory bind specifically to the toxophore and haptophore groups of the invading **antigen**." },
      { author: "Karl Landsteiner", work: "The Specificity of Serological Reactions", text: "Chemical alteration of a single hapten group fundamentally alters the serological specificity of the artificial **antigen**." },
      { author: "Peter Medawar", work: "The Uniqueness of the Individual", text: "Graft rejection is driven by cell-surface **antigen** disparities encoded by the major histocompatibility complex." }
    ]
  },
  "antigenic": {
    primary: "Relating to or having the properties of an antigen; capable of triggering an immune reaction.",
    secondary: "Exhibiting molecular features recognized by antibodies or immunocompetent lymphoid cells.",
    quotes: [
      { author: "Karl Landsteiner", work: "The Specificity of Serological Reactions", text: "Conjugating simple aromatic radicals to proteins creates novel **antigenic** determinants with exquisite binding precision." },
      { author: "Frank Macfarlane Burnet", work: "The Clonal Selection Theory of Acquired Immunity", text: "Clonal selection postulates that **antigenic** challenge selects and expands preexisting antibody-producing clones." },
      { author: "Alexander Fleming", work: "Chemotherapy and Serology", text: "The bacterial capsule conceals somatic **antigenic** sites, shielding the pathogen from phagocytic recognition." }
    ]
  },
  "autogenesis": {
    primary: "Spontaneous generation; origin or development within the organism itself without external influence.",
    secondary: "In philosophy and developmental biology, self-generation or intrinsic morphogenesis independent of external environmental triggers.",
    quotes: [
      { author: "Herbert Spencer", work: "The Principles of Biology", text: "The hypothesis of **autogenesis** presupposes that organic forms unfold under the impetus of purely internal physiological forces." },
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "He opposed dogmatic vitalism, seeking to explain cellular **autogenesis** through physicochemical self-organization." },
      { author: "Alexander Oparin", work: "The Origin of Life", text: "Ancient thinkers conflated modern evolutionary synthesis with naive folklore concerning the **autogenesis** of vermin." }
    ]
  },
  "autogenetic": {
    primary: "Originating within the self or system; self-generated; relating to autogenesis.",
    secondary: "Arising from endogenous biological processes rather than external pathogens, stimuli, or vectors.",
    quotes: [
      { author: "Herbert Spencer", work: "First Principles", text: "Evolutionary changes display an **autogenetic** rhythm, wherein internal tensions continually reconfigure structural equilibria." },
      { author: "William Roux", work: "Der Kampf der Theile im Organismus", text: "The early blastomere executes **autogenetic** cleavages guided by its own internal maternal cytoplasmic architecture." },
      { author: "C. H. Waddington", work: "The Strategy of the Genes", text: "Canalization ensures an **autogenetic** stability that buffers development against transient environmental perturbations." }
    ]
  },
  "autogenous": {
    primary: "Originating within an organism itself; self-produced; endogenous.",
    secondary: "In immunology and medicine, derived from the patient's own body (such as an autogenous skin graft or autogenous vaccine).",
    quotes: [
      { author: "Alexis Carrel", work: "The Preservation of Tissues", text: "The surgical survival of an **autogenous** vein graft far exceeds that achieved with homologous arterial transplants." },
      { author: "Almroth Wright", work: "Studies on Immunisation", text: "In intractable furunculosis, immunization with an **autogenous** bacterial vaccine provoked a decisive clinical cure." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", text: "The internal milieu possesses **autogenous** regulatory mechanisms that maintain thermal and chemical constancy." }
    ]
  },
  "biogenesis": {
    primary: "The principle that living organisms develop only from preexisting living matter (contrasted with spontaneous generation or abiogenesis).",
    secondary: "The synthesis of complex substances by living organisms; biosynthesis.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Biogenesis and Abiogenesis", text: "I have named the doctrine that living matter is always produced by preexisting living matter, the law of **biogenesis**." },
      { author: "Louis Pasteur", work: "Memoir on the Organized Corpuscles Existing in the Atmosphere", text: "Every rigorous test confirms the great principle of **biogenesis**: life never appears without parent life." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "The aphorism omnis cellula e cellula stands as the definitive cellular expression of universal **biogenesis**." }
    ]
  },
  "biogenetic": {
    primary: "Pertaining to biogenesis, or to the production of living organisms from preexisting life.",
    secondary: "Relating to Ernst Haeckel's 'biogenetic law' (ontogeny recapitulates phylogeny) in developmental and evolutionary morphology.",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "I formulated the fundamental **biogenetic** law: the brief ontogenesis of the individual recapitulates the slow phylogenesis of the race." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", text: "Haeckel's **biogenetic** law dominated late nineteenth-century biology, influencing psychology, anthropology, and education." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", text: "Physical forces modify developmental trajectories, circumscribing the dogmatic claims of strict **biogenetic** recapitulation." }
    ]
  },
  "biogenous": {
    primary: "Produced by living organisms; of organic or biological origin.",
    secondary: "In geology and sedimentology, designating deposits (such as coral reefs, chalk, or diatomaceous ooze) constructed by organisms.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", text: "Immense coral limestone formations provide striking testimony to the vast scale of **biogenous** rock building." },
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "Pelagic globigerina ooze represents a purely **biogenous** deposit covering vast expanses of the abyssal ocean floor." },
      { author: "Vladimir Vernadsky", work: "The Biosphere", text: "The atmosphere's oxygen is entirely **biogenous**, created and continuously replenished by photosynthetic vegetation." }
    ]
  },
  "dysgenesis": {
    primary: "Defective, abnormal, or impaired development of an organ, tissue, or physiological system.",
    secondary: "Infertility or impaired reproductive capacity between crossbred species or subspecies; also gonadal dysgenesis in chromosomal disorders.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", text: "Hybrid sterility between divergent varieties illustrates the physiological **dysgenesis** resulting from incompatible germ-plasms." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Ovarian **dysgenesis** in Turner syndrome manifests as fibrous streak ovaries devoid of primordial germ cells." },
      { author: "Francis Galton", work: "Hereditary Genius", text: "Social conditions that encourage disproportionate fertility among the least capable threaten racial **dysgenesis**." }
    ]
  },
  "dysgenic": {
    primary: "Exerting a detrimental effect on the genetic qualities or hereditary health of a population; biologically degrading.",
    secondary: "Tending toward the accumulation of disadvantageous mutations or the survival of less biologically fit individuals.",
    quotes: [
      { author: "Julian Huxley", work: "The Stream of Life", text: "Modern warfare operates as a catastrophically **dysgenic** filter, destroying physically vigorous youths on the battlefield." },
      { author: "Theodosius Dobzhansky", work: "Mankind Evolving", text: "Relaxed natural selection in civilized societies has prompted anxieties regarding potentially **dysgenic** mutational loads." },
      { author: "H. G. Wells", work: "The Work, Wealth and Happiness of Mankind", text: "Slum tenements and industrial malnutrition act as powerful **dysgenic** agents upon working-class populations." }
    ]
  },
  "dysgenics": {
    primary: "The study of factors that bring about the genetic degeneration or biological decline of a population; the opposite of eugenics.",
    secondary: "The social or evolutionary processes that result in an increase in deleterious genetic traits within a gene pool.",
    quotes: [
      { author: "Francis Galton", work: "Inquiries into Human Faculty and Its Development", text: "We must analyze both the benefits of positive eugenics and the perils of uncontrolled social **dysgenics**." },
      { author: "Theodosius Dobzhansky", work: "Genetic Diversity and Human Equality", text: "Pessimistic doctrines of **dysgenics** often overlook the buffering capacity of cultural institutions and modern medicine." },
      { author: "Julian Huxley", work: "Essays of a Biologist", text: "A society that ignores reproductive demographics risks institutionalizing biological **dysgenics** under the guise of welfare." }
    ]
  },
  "endogen": {
    primary: "A plant that grows from within, historically applied to monocotyledons (such as grasses, palms, and lilies) whose stems lack annual rings.",
    secondary: "A botanical class established by Augustin Pyramus de Candolle contrasting with exogens (dicotyledons) in stem morphology.",
    quotes: [
      { author: "Augustin Pyramus de Candolle", work: "Théorie Élémentaire de la Botanique", text: "I classified flowering plants into the **endogen** group with internal vascular bundles, and exogens with concentric growth." },
      { author: "Asa Gray", work: "Elements of Botany", text: "The stem of an **endogen** exhibits closed fibrovascular bundles scattered irregularly through cellular ground tissue." },
      { author: "Charles Darwin", work: "The Movement and Habits of Climbing Plants", text: "Climbing monocotyledons demonstrate that the anatomical constraints of the **endogen** stem do not prevent twining habits." }
    ]
  },
  "endogenetic": {
    primary: "Originating or produced from within; endogenous; relating to internal forces or causes.",
    secondary: "In geology and geomorphology, designating internal subterranean forces (vulcanism, tectonic uplift) that deform Earth's crust.",
    quotes: [
      { author: "Eduard Suess", work: "The Face of the Earth", text: "Mountain belts arise from colossal **endogenetic** forces generated by the contraction and thermal cooling of the globe." },
      { author: "Archibald Geikie", work: "The Scenery of Scotland", text: "The basaltic plateaus of Skye owe their monumental architecture to tertiary **endogenetic** volcanic eruptions." },
      { author: "William Morris Davis", work: "Geographical Essays", text: "Landforms result from a continuous struggle between **endogenetic** tectonic uplift and exogenetic denudation." }
    ]
  },
  "endogenic": {
    primary: "Formed, originating, or occurring beneath the surface of the Earth; generated by internal tectonic or volcanic activity.",
    secondary: "Arising from internal physiological or psychological causes within an organism; endogenous.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", text: "Earthquakes and plutonic intrusions represent primary **endogenic** agencies counteracting atmospheric erosion." },
      { author: "Alfred Wegener", work: "The Origin of Continents and Oceans", text: "Sub-crustal magmatic currents provide the dynamic **endogenic** engine driving continental drift." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", text: "Radioactive heat within the mantle fuels the massive **endogenic** convection cycles that uplift ocean ridges." }
    ]
  },
  "endogenous": {
    primary: "Growing, originating, or produced from within; having an internal cause or origin.",
    secondary: "In biochemistry and medicine, produced inside an organism or tissue (such as endogenous insulin or hormones) rather than ingested.",
    quotes: [
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Glycogen synthesis in the liver illustrates the capacity of internal organs for **endogenous** metabolic production." },
      { author: "Sigmund Freud", work: "The Ego and the Id", text: "Melancholia frequently arises from powerful **endogenous** psychological conflicts without an evident external bereavement." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", text: "Homeostatic mechanisms regulate **endogenous** body temperature against harsh external fluctuations." }
    ]
  },
  "endogenously": {
    primary: "From within; in an endogenous manner; originating from internal causes or physiological processes.",
    secondary: "Produced internally by cellular biosynthesis or synthesized within an organism's own tissues.",
    quotes: [
      { author: "Hans Krebs", work: "The Citric Acid Cycle", text: "Intermediates generated **endogenously** within mitochondria maintain the steady-state flux of cellular respiration." },
      { author: "Walter Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", text: "Adrenaline released **endogenously** into the bloodstream prepares the animal for immediate combat or flight." },
      { author: "Erwin Bünning", work: "The Physiological Clock", text: "The rhythm persists in total darkness because it is generated **endogenously** by cellular pacemakers." }
    ]
  },
  "epigene": {
    primary: "Formed, originating, or taking place at or near the surface of the Earth; surficial or sedimentary.",
    secondary: "In geology and mineralogy, designating metamorphic changes, mineralization, or weathering driven by surface meteoric waters.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "We divide geological forces into hypogene actions deep within the crust and **epigene** weathering at the surface." },
      { author: "Charles Lyell", work: "Principles of Geology", text: "Rain, frost, and running rivers constitute the paramount **epigene** agents carving continental landscapes." },
      { author: "Amadeus William Grabau", work: "Principles of Stratigraphy", text: "Secondary oxidation in copper veins proceeds via descending **epigene** solutions percolating from the surface." }
    ]
  },
  "epigenesis": {
    primary: "The embryological theory that an organism develops from an undifferentiated zygote through gradual differentiation and organ formation.",
    secondary: "The developmental doctrine (championed by Caspar Friedrich Wolff) that overthrew preformationism; also phenotypic changes during ontogeny.",
    quotes: [
      { author: "Caspar Friedrich Wolff", work: "Theoria Generationis", text: "Careful microscopic observation of the chick embryo demonstrates true **epigenesis**, not the unfolding of preformed miniatures." },
      { author: "Immanuel Kant", work: "Critique of Judgment", text: "The system of **epigenesis** alone does justice to the purposive, self-organizing power manifested in living nature." },
      { author: "William Harvey", work: "Exercitationes de Generatione Animalium", text: "Generation proceeds by **epigenesis**, wherein parts are added successively one after another from the maternal blood." }
    ]
  },
  "epigenetics": {
    primary: "The study of heritable changes in gene expression or cellular phenotype caused by mechanisms other than changes in the underlying DNA sequence.",
    secondary: "The scientific discipline investigating how histone modifications, DNA methylation, and non-coding RNAs regulate gene transcription across development.",
    quotes: [
      { author: "C. H. Waddington", work: "The Epigenetics of Birds", text: "I introduced the term **epigenetics** to describe the complex interactions between genes and their environment that realize the phenotype." },
      { author: "Robin Holliday", work: "The Inheritance of Epigenetic Defects", text: "DNA methylation patterns provide a molecular foundation for **epigenetics**, explaining cellular memory through cell divisions." },
      { author: "Mary Lyon", work: "Gene Action in the X-chromosome of the Mouse", text: "Inactivation of one female X-chromosome stands as a monumental paradigm of mammalian **epigenetics**." }
    ]
  },
  "epigone": {
    primary: "A less distinguished imitator, follower, or successor of a great artist, writer, philosopher, or movement.",
    secondary: "Historically, one of the sons of the seven heroes who made the second expedition against Thebes (the Epigonoi).",
    quotes: [
      { author: "Friedrich Nietzsche", work: "Untimely Meditations", text: "Nothing is more debilitating to creative culture than the complacency of the cultured **epigone** living off inherited glory." },
      { author: "Thomas Mann", work: "Doctor Faustus", text: "The aging composer feared becoming a mere **epigone** of romanticism, trapped in repetitive harmonic mannerisms." },
      { author: "George Steiner", work: "Language and Silence", text: "The late twentieth-century critic often appears as a melancholy **epigone** following the monumental achievements of high modernism." }
    ]
  },
  "erogenous": {
    primary: "Sensitive to sexual stimulation; giving rise to sexual excitement when stimulated.",
    secondary: "In psychoanalysis, designating specific anatomical bodily zones (oral, anal, genital) whose excitation yields libidinal pleasure.",
    quotes: [
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", text: "Infantile sexuality is characterized by the diffuse gratification yielded by diverse **erogenous** zones across the body." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "Cutaneous tactile sensitivity varies widely, transforming ordinary epidermal areas into intensely **erogenous** centers." },
      { author: "Carl Jung", work: "Symbols of Transformation", text: "Libidinal energy shifts across development, detaching from primitive **erogenous** attachments toward spiritual sublimations." }
    ]
  },
  "Eugene": {
    primary: "A masculine given name derived from the Greek *eugenēs*, meaning 'well-born', 'noble', or 'of good descent'.",
    secondary: "A prominent city in western Oregon, named in honor of its founder, the pioneer Eugene Skinner.",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Prince **Eugene** of Savoy proved himself one of the consummate military captains of the European Enlightenment." },
      { author: "Honoré de Balzac", work: "Père Goriot", text: "Young **Eugene** de Rastignac stood on the heights of Père Lachaise and hurled his desperate defiance at Parisian society." },
      { author: "John Wesley Powell", work: "Report on the Lands of the Arid Region", text: "Agricultural settlers in the Willamette Valley established prosperous farmsteads surrounding the young town of **Eugene**." }
    ]
  },
  "eugenic": {
    primary: "Relating to or promoting improvement in the hereditary qualities of a population or offspring.",
    secondary: "Advocating selective breeding or policies intended to enhance desirable genetic traits in human lineages.",
    quotes: [
      { author: "Francis Galton", work: "Inquiries into Human Faculty and Its Development", text: "We pursue **eugenic** inquiries with the aim of giving the more suitable races a better chance of prevailing over the less suitable." },
      { author: "Julian Huxley", work: "If I Were Dictator", text: "A truly **eugenic** society must eliminate squalor and provide universal education before evaluating innate genetic potential." },
      { author: "George Bernard Shaw", work: "Man and Superman", text: "The philosopher must look to conscious **eugenic** selection if mankind is to transcend its chronic political barbarism." }
    ]
  },
  "eugenics": {
    primary: "The social movement and philosophy advocating the improvement of human genetic qualities through selective reproduction.",
    secondary: "A historical scientific and ideological movement in the 19th and 20th centuries that promoted forced sterilization, institutionalization, and selective breeding.",
    quotes: [
      { author: "Francis Galton", work: "Memories of My Life", text: "I coined the word **eugenics** to express the science of improving stock, whether in animals or man." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", text: "The tragedy of American **eugenics** culminated in the Buck v. Bell ruling, legitimizing compulsory sterilization of the vulnerable." },
      { author: "G. K. Chesterton", work: "Eugenics and Other Evils", text: "Modern **eugenics** is not a science, but an arrogant terrorism wielded by self-appointed oligarchs over the poor." }
    ]
  },
  "exogen": {
    primary: "A plant that increases in size by successive external additions of wood (concentric rings), typical of dicotyledons and gymnosperms.",
    secondary: "A botanical division created by Augustin Pyramus de Candolle for plants with two cotyledons, net-veined leaves, and exogenous stem growth.",
    quotes: [
      { author: "Augustin Pyramus de Candolle", work: "Théorie Élémentaire de la Botanique", text: "The woody trunk of an **exogen** expands year by year through the outward activity of the cambium zone." },
      { author: "Asa Gray", work: "Botanical Textbook", text: "In every typical **exogen**, the vascular cylinders encircle a central pith and are protected externally by bark." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "The grand architectural divide of flowering plants opposes the structural mechanics of the **exogen** to that of the endogen." }
    ]
  },
  "exogenic": {
    primary: "Formed, occurring, or originating on the surface of the Earth; exogeneous.",
    secondary: "In geology, pertaining to external surface processes (weathering, erosion, glaciation, sedimentation) driven by solar energy and gravity.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "The physical relief of continents reflects the unrelenting destruction wrought by **exogenic** weathering agents." },
      { author: "William Morris Davis", work: "Geographical Essays", text: "The geographical cycle traces how **exogenic** fluvial erosion reduces elevated plateaus to peneplains." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", text: "Wind, water, and glacial transport represent the principal **exogenic** tools redistributing continental detritus." }
    ]
  },
  "exogenous": {
    primary: "Originating or produced from outside an organism or system; introduced from external sources.",
    secondary: "In medicine and biochemistry, designating substances (such as pharmaceutical toxins, vitamins, or hormones) introduced into the body.",
    quotes: [
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Toxic symptoms subsided rapidly once the animal was isolated from the **exogenous** poisonous fumes." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", text: "The kidney regulates blood volume by swiftly filtering out excess **exogenous** solutes consumed in food." },
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", text: "Neurotic symptoms frequently crystallize around an **exogenous** psychic trauma acting upon a vulnerable predisposition." }
    ]
  },
  "gametogenesis": {
    primary: "The biological process by which diploid precursor cells undergo meiotic division and differentiation to produce mature haploid gametes.",
    secondary: "The cellular and genetic events comprising spermatogenesis in males and oogenesis in females within reproductive gonadal tissues.",
    quotes: [
      { author: "August Weismann", work: "The Germ-Plasm: A Theory of Heredity", text: "During **gametogenesis**, the reduction division halves the chromosome number to preserve species constancy upon fertilization." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", text: "Crossing over during meiotic prophase of **gametogenesis** generates novel genetic recombinations on each chromosome." },
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", text: "Hormonal signals from the pituitary gland initiate and sustain the rhythmic cycles of mammalian **gametogenesis**." }
    ]
  },
  "gen": {
    primary: "Information, intelligence, or detailed facts (informal/British colloquial: 'the gen'); also the ancient Greek combining root for birth, race, or kind.",
    secondary: "In historical linguistics and etymology, the Proto-Indo-European and Greek root *gen-* signifying becoming, begetting, descent, or clan.",
    quotes: [
      { author: "George Orwell", work: "Keep the Aspidistra Flying", text: "The intelligence clerk leaned across the desk to give him the latest service **gen** on troop movements." },
      { author: "Max Müller", work: "The Science of Language", text: "From the primordial root **gen** spring our words for genus, gentle, genuine, and the entire vocabulary of birth." },
      { author: "C. S. Lewis", work: "Studies in Words", text: "Etymologists trace the conceptual history of kind and nature back to the versatile Greek stem **gen**." }
    ]
  },
  "gene": {
    primary: "A basic unit of heredity in living organisms; a specific sequence of nucleotides in DNA or RNA that encodes a functional RNA or protein.",
    secondary: "A Mendelian factor residing at a distinct locus on a chromosome that undergoes replication, mutation, and transcription.",
    quotes: [
      { author: "Wilhelm Johannsen", work: "Elemente der exakten Erblichkeitslehre", text: "I have proposed the word **gene** to designate the fundamental hereditary element underlying unit characters." },
      { author: "Thomas Hunt Morgan", work: "The Physical Basis of Heredity", text: "Our linkage maps prove that each **gene** occupies a definite linear locus along the chromosome of Drosophila." },
      { author: "Francis Crick", work: "What Mad Pursuit", text: "The central dogma asserted that sequence information flows unidirectionally from the **gene** to messenger RNA to protein." }
    ]
  },
  "genealogic": {
    primary: "Of or relating to genealogy; tracing family ancestry, descent, or lineage.",
    secondary: "Pertaining to pedigree records or phylogenetic branching trees; genealogical.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", text: "All true classification of organisms is inherently **genealogic**, reflecting real lines of common evolutionary descent." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The proud patrician displayed ancient wax busts to demonstrate an unbroken **genealogic** succession from the Republic." },
      { author: "Ernst Haeckel", work: "The History of Creation", text: "I constructed the first comprehensive **genealogic** tree of living organisms based on comparative embryology." }
    ]
  },
  "genealogical": {
    primary: "Relating to or based on the study of family lineages and the tracing of ancestors.",
    secondary: "In philosophy and evolutionary theory, analyzing concepts or organisms by uncovering their historical descent and origins.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "On the Genealogy of Morals", text: "A rigorous **genealogical** inquiry uncovers the sordid historical origins of our venerated moral values." },
      { author: "Charles Darwin", work: "The Descent of Man", text: "Man's **genealogical** tree must be placed alongside the Catarhine monkeys of the Old World." },
      { author: "Michel Foucault", work: "Language, Counter-Memory, Practice", text: "The **genealogical** method avoids metaphysical teleology, demonstrating how power relations construct human subjectivity." }
    ]
  },
  "genealogically": {
    primary: "In a genealogical manner; in terms of family descent, ancestry, or pedigree.",
    secondary: "With regard to phylogenetic lineage or historical lines of succession.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", text: "Organisms that are placed close together in our classification are **genealogically** related through common ancestors." },
      { author: "Edward Gibbon", work: "Memoirs of My Life", text: "I can trace my ancestors **genealogically** back to the fourteenth century with indisputable documentary evidence." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", text: "Cladistics attempts to classify taxa strictly **genealogically**, using shared derived characters alone." }
    ]
  },
  "genealogist": {
    primary: "A person who traces or studies lines of family descent, pedigrees, and historical ancestry.",
    secondary: "A scholar or researcher examining archival records, parish registers, and historical documents to reconstruct kin networks.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Custom-House", text: "The patient **genealogist** delves through moth-eaten parchment records to authenticate forgotten family lines." },
      { author: "Francis Galton", work: "Hereditary Genius", text: "I consulted the eminent **genealogist** to verify the family trees of lord chancellors and royal judges." },
      { author: "W. M. Thackeray", work: "Vanity Fair", text: "Sir Pitt Crawley employed an obsequious **genealogist** to fabricate an illustrious pedigree reaching back to William the Conqueror." }
    ]
  },
  "genealogy": {
    primary: "A record or account of the ancestry and line of descent of a person, family, or group.",
    secondary: "A historical critique or analytical method that traces the emergence and development of cultural concepts, values, or biological species.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "On the Genealogy of Morals", text: "We need a critique of moral values; the value of these values must itself be brought into question, and for this a **genealogy** is required." },
      { author: "Charles Darwin", work: "The Origin of Species", text: "Our classifications will come to be regarded as **genealogies**, tracing the real lines of physical kinship among species." },
      { author: "Michel Foucault", work: "Discipline and Punish", text: "A **genealogy** of the modern penal system reveals the hidden technologies of surveillance disciplining the body." }
    ]
  },
  "genesis": {
    primary: "The origin, coming into being, or mode of formation of something.",
    secondary: "The first book of the Hebrew Bible and Christian Old Testament; in philosophy, the causal emergence of forms in nature.",
    quotes: [
      { author: "Francis Bacon", work: "Novum Organum", text: "True understanding seeks the primary **genesis** of things in nature through systematic experimental induction." },
      { author: "Johann Wolfgang von Goethe", work: "Italian Journey", text: "In the botanical gardens of Palermo, I contemplated the primal plant and the **genesis** of all floral forms." },
      { author: "Karl Ernst von Baer", work: "On the Genesis of the Animal", text: "The **genesis** of the embryo proceeds from the homogeneous to the heterogeneous through progressive differentiation." }
    ]
  },
  "genetic": {
    primary: "Of, relating to, or produced by genes or heredity.",
    secondary: "Pertaining to origins, historical development, or causal emergence (as in genetic epistemology).",
    quotes: [
      { author: "Gregor Mendel", work: "Experiments in Plant Hybridisation", text: "The mathematical ratios observed in garden peas reflect constant **genetic** laws governing character segregation." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", text: "Linear arrangement of genes on the chromosome provides the physical foundation of **genetic** inheritance." },
      { author: "Jean Piaget", work: "Genetic Epistemology", text: "Our **genetic** approach examines how the child's understanding of space, time, and causality emerges over developmental stages." }
    ]
  },
  "genetical": {
    primary: "Of or pertaining to genetics; genetic.",
    secondary: "Relating to hereditary transmission and the mathematical analysis of biological variation.",
    quotes: [
      { author: "Ronald Fisher", work: "The Genetical Theory of Natural Selection", text: "The **genetical** theory of natural selection harmonizes Darwinian evolution with particulate Mendelian inheritance." },
      { author: "J. B. S. Haldane", work: "The Causes of Evolution", text: "A purely **genetical** treatment of population variance allows us to calculate rates of selective replacement." },
      { author: "William Bateson", work: "Mendel's Principles of Heredity", text: "We stand on the threshold of a new **genetical** science that will elucidate the physiological basis of species variation." }
    ]
  },
  "genetically": {
    primary: "In a genetic manner; with regard to genes, heredity, or biological origin.",
    secondary: "By means of genetic engineering, selective breeding, or hereditary transmission.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", text: "Geographic races of a single species are **genetically** differentiated systems adapted to local ecological regimes." },
      { author: "Richard Dawkins", work: "The Selfish Gene", text: "An organism acts to maximize the survival of copies of its own genes found **genetically** in kin." },
      { author: "James Watson", work: "The Double Helix", text: "Base pairing in DNA explains how genetic information is copied **genetically** with immaculate precision." }
    ]
  },
  "geneticism": {
    primary: "The doctrine or belief that human behaviors, social structures, and mental traits are determined primarily by genetic inheritance.",
    secondary: "Genetic determinism; an excessive or reductionist reliance on genetic explanations for cultural and psychological phenomena.",
    quotes: [
      { author: "Richard Lewontin", work: "Biology as Ideology", text: "Radical **geneticism** reduces complex political and economic inequalities to trivial differences in nucleotide sequences." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", text: "We must contest the fallacies of crude **geneticism**, which seek to naturalize racism and class oppression." },
      { author: "Mary Midgley", work: "Beast and Man", text: "Rejecting dogmatic **geneticism** does not require us to pretend that human beings have no biological nature at all." }
    ]
  },
  "geneticist": {
    primary: "A scientist who specializes in the study of genetics, heredity, and gene function.",
    secondary: "An investigator analyzing the molecular structure, mutation, expression, or population dynamics of genes.",
    quotes: [
      { author: "Thomas Hunt Morgan", work: "The Mechanism of Mendelian Heredity", text: "The experimental **geneticist** finds in Drosophila melanogaster an unrivaled instrument for chromosome mapping." },
      { author: "Barbara McClintock", work: "The Discovery of Transposable Elements", text: "As a maize **geneticist**, I observed mobile controlling elements moving dynamically within the plant genome." },
      { author: "Francois Jacob", work: "The Statue Within", text: "The molecular **geneticist** became a cryptographer deciphering the chemical message inscribed within the cell." }
    ]
  },
  "genetics": {
    primary: "The branch of biology concerned with the study of heredity, genes, and variation in living organisms.",
    secondary: "The molecular and population sciences investigating the inheritance, expression, and evolution of genomic sequences.",
    quotes: [
      { author: "William Bateson", work: "Letter to Adam Sedgwick", text: "I suggest the term **genetics** for the dedicated science of heredity and variation." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", text: "Evolutionary **genetics** bridged the divide between laboratory mutation studies and natural field populations." },
      { author: "Francis Crick", work: "Of Molecules and Men", text: "Modern molecular **genetics** showed that biological specificity is entirely encoded in linear digital sequences." }
    ]
  },
  "genic": {
    primary: "Of, relating to, or produced by genes; genetic.",
    secondary: "Pertaining to specific alleles or gene loci and their individual phenotypic effects.",
    quotes: [
      { author: "Sewall Wright", work: "Evolution in Mendelian Populations", text: "Selection acts upon interactive gene complexes rather than isolated, additive **genic** frequencies." },
      { author: "Theodosius Dobzhansky", work: "Genetics of the Evolutionary Process", text: "Balanced polymorphism maintains high levels of **genic** diversity within natural Drosophila populations." },
      { author: "George Gaylord Simpson", work: "Tempo and Mode in Evolution", text: "Macroevolutionary trends must ultimately harmonize with the microevolutionary dynamics of **genic** substitution." }
    ]
  },
  "genocide": {
    primary: "The deliberate and systematic destruction, in whole or in part, of an ethnic, racial, religious, or national group.",
    secondary: "A concept formulated in international law by Raphael Lemkin to define the crime of annihilating a collective human population.",
    quotes: [
      { author: "Raphael Lemkin", work: "Axis Rule in Occupied Europe", text: "By **genocide** we mean the destruction of an ethnic group; it signifies a coordinated plan aiming at the annihilation of a nation." },
      { author: "Hannah Arendt", work: "Eichmann in Jerusalem", text: "The crime of **genocide** is committed against the human diversity of the world, an attack upon humanity in the person of a group." },
      { author: "Primo Levi", work: "The Drowned and the Saved", text: "To deny the memory of state-sponsored **genocide** is to prepare the groundwork for its monstrous repetition." }
    ]
  },
  "genophobia": {
    primary: "An irrational, persistent, or excessive fear of sexual intercourse or sexual intimacy; erotophobia.",
    secondary: "A psychological anxiety disorder or phobia characterized by acute panic and avoidance of physical sexual contact.",
    quotes: [
      { author: "Sigmund Freud", work: "A General Introduction to Psychoanalysis", text: "Severe hysterical **genophobia** often masks deeply repressed trauma originating in childhood seduction fantasies." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "In cases of pronounced **genophobia**, moral revulsion is accompanied by somatic spasms and tachycardia." },
      { author: "Wilhelm Stekel", work: "Frigidity in Woman", text: "The therapist must gently unpack the superstitious terrors that convert normal desire into crippling **genophobia**." }
    ]
  },
  "genotype": {
    primary: "The genetic constitution of an individual organism, distinct from its observable physical properties (phenotype).",
    secondary: "The total collection of genes and alleles carried by an organism, or the specific allele pair at a designated gene locus.",
    quotes: [
      { author: "Wilhelm Johannsen", work: "The Genotype Conception of Heredity", text: "The **genotype** is the fundamental constitution of the zygote, remaining invariable through somatic life." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", text: "The individual **genotype** functions as an integrated, harmonious gene system buffered against selection." },
      { author: "Theodosius Dobzhansky", work: "Mankind Evolving", text: "Every human **genotype** is uniquely tailored by sexual recombination, ensuring incomparable individuality." }
    ]
  },
  "genotypic": {
    primary: "Of, relating to, or determined by the genotype.",
    secondary: "Pertaining to the underlying genetic constitution of an organism as opposed to its phenotypic manifestations.",
    quotes: [
      { author: "Wilhelm Johannsen", work: "Elemente der exakten Erblichkeitslehre", text: "Phenotypic variance within a pure line reflects environmental noise, not underlying **genotypic** differences." },
      { author: "Sewall Wright", work: "Systems of Mating", text: "Inbreeding increases **genotypic** homozygosity without necessarily reducing environmental phenotypic variation." },
      { author: "C. H. Waddington", work: "The Strategy of the Genes", text: "Canalized development ensures that organisms with differing **genotypic** backgrounds can express identical phenotypes." }
    ]
  },
  "genotypical": {
    primary: "Relating to or having the nature of a genotype; genotypic.",
    secondary: "Describing hereditary constitution or characteristics determined strictly by genetic inheritance.",
    quotes: [
      { author: "Wilhelm Johannsen", work: "The Genotype Conception of Heredity", text: "We must distinguish between transient modifications and permanent **genotypical** alterations." },
      { author: "Ronald Fisher", work: "The Genetical Theory of Natural Selection", text: "Selection alters the **genotypical** frequencies in a population according to the fitness differentials of the alleles." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", text: "A proper species diagnosis requires evaluating **genotypical** divergence rather than superficial plumage traits." }
    ]
  },
  "gonad": {
    primary: "An organ that produces gametes; an ovary or a testis.",
    secondary: "A primary reproductive gland producing sex hormones (androgens, estrogens, and progestins) as well as germ cells.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", text: "In primitive marine invertebrates, the **gonad** is a simple follicular aggregation discharging through body pores." },
      { author: "Claude Bernard", work: "Lectures on Experimental Physiology", text: "The endocrine secretion of the **gonad** coordinates the maturation of secondary sexual plumage in birds." },
      { author: "Thomas Hunt Morgan", work: "Sex and Heredity", text: "The embryonic **gonad** remains indifferent until sex-determining chromosomes dictate testicular or ovarian fate." }
    ]
  },
  "gonadal": {
    primary: "Of, relating to, or affecting the gonads (ovaries or testes).",
    secondary: "Pertaining to gamete-producing organs or to the synthesis of sex steroids within reproductive tissues.",
    quotes: [
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Defective **gonadal** development precipitates endocrine imbalances affecting skeletal elongation." },
      { author: "Frank Beach", work: "Hormones and Behavior", text: "Receptivity in female mammals is closely synchronized with cyclic **gonadal** hormone fluctuations." },
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", text: "Primordial germ cells migrate from extraembryonic endoderm into the developing **gonadal** ridge." }
    ]
  },
  "heterogenesis": {
    primary: "Spontaneous generation; the production of living organisms from matter of a different nature (non-living or disparate organic material).",
    secondary: "Alternation of generations, or the historical doctrine that offspring can differ fundamentally from parents (mutationism / saltationism).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Biogenesis and Abiogenesis", text: "The hypothesis of **heterogenesis** assumes that living matter can generate organisms differing totally from the parent stock." },
      { author: "Henry Charlton Bastian", work: "The Beginnings of Life", text: "I claimed that careful heating of organic infusions did not prevent the **heterogenesis** of viable microbes." },
      { author: "Louis Pasteur", work: "Studies on Spontaneous Generation", text: "Careful filtration proved that **heterogenesis** was a chimera born of unsterilized glassware and airborne dust." }
    ]
  },
  "homogenesis": {
    primary: "The reproduction of offspring that are similar to the parents in structure, life cycle, and developmental stages; biogenesis.",
    secondary: "The biological law that living organisms reproduce their own kind through successive generations, contrasted with heterogenesis.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Biogenesis and Abiogenesis", text: "In **homogenesis**, the progeny passes through the same developmental cycle as that which produced the parents." },
      { author: "Herbert Spencer", work: "The Principles of Biology", text: "The universal law of organic heredity is **homogenesis**, ensuring the faithful perpetuation of species characters." },
      { author: "Ernst Haeckel", work: "The History of Creation", text: "The principle of **homogenesis** forms the bedrock of evolutionary stability across thousands of generations." }
    ]
  },
  "homogenetic": {
    primary: "Pertaining to or characterized by homogenesis; of similar origin or descent.",
    secondary: "In embryology and genetics, having uniform genetic origin or derived from homologous structures.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", text: "The **homogenetic** continuity of the germ-cell lineage explains the constancy of specific vertebrate anatomy." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Embryos of related classes share **homogenetic** pathways before diverging into specialized adult forms." },
      { author: "August Weismann", work: "Essays Upon Heredity", text: "Strict **homogenetic** reproduction guarantees that parental determiners pass uncorrupted to the filial generation." }
    ]
  },
  "hypogenesis": {
    primary: "Defective, deficient, or arrested embryonic development; underdevelopment of an organ or tissue.",
    secondary: "In evolutionary biology, reproduction without alternation of generations or through simplified developmental cycles.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "Congenital **hypogenesis** of the thyroid produces the classic clinical picture of infantile myxedema." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Cerebellar **hypogenesis** manifests as severe motor ataxia and failure of Purkinje cell maturation." },
      { author: "Ray Lankester", work: "Degeneration: A Chapter in Darwinism", text: "Parasitic lifestyles frequently induce physiological **hypogenesis**, simplifying complex ancestral organ systems." }
    ]
  },
  "hypogenic": {
    primary: "Formed or occurring deep beneath the Earth's surface (hypogene); of plutonic or subterranean origin.",
    secondary: "Relating to or caused by hypogenesis; characterized by developmental deficiency or incomplete tissue formation.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "Plutonic granites and regional schists demonstrate the vast power of **hypogenic** heat and pressure." },
      { author: "Charles Lyell", work: "Principles of Geology", text: "We trace volcanic intrusions down to their **hypogenic** reservoirs within the Earth's molten interior." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Congenital **hypogenic** malformations of the heart arise during early truncal septation." }
    ]
  },
  "hypogenous": {
    primary: "Growing, originating, or situated on the lower or under side of an organ (especially of a leaf in botany).",
    secondary: "Describing fungal mycelia or fructifications that develop on the abaxial surface of foliage.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", text: "Stomata in broadleaf evergreen trees are almost exclusively **hypogenous**, located on the shaded undersurface of the leaf." },
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", text: "The parasitic rust produces dense, powdery **hypogenous** sori covering the ventral face of infected leaves." },
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "Conidiophores rupture the lower epidermis to display their **hypogenous** fruiting structures to the morning dew." }
    ]
  },
  "metagenesis": {
    primary: "Alternation of generations, especially between sexual and asexual reproductive phases in the life cycle of an organism.",
    secondary: "The life cycle characteristic of cnidarians (such as jellyfish), where a sessile asexual polyp alternates with a free-swimming sexual medusa.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Invertebrates", text: "I have proposed the term **metagenesis** for that alternation of sexual and non-sexual generations found in hydrozoans." },
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", text: "In the Aurelia life cycle, **metagenesis** links the scyphistoma polyp with the free-floating sexual medusa." },
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "The evolutionary advantage of **metagenesis** lies in combining benthic territorial tenacity with pelagic gene dispersal." }
    ]
  },
  "monogenesis": {
    primary: "The theory that all human races are descended from a single ancestral pair or origin (monogenism).",
    secondary: "The biological development of organisms from a single source or asexual parent; or the origin of a linguistic family from a single proto-language.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", text: "The evidence of comparative anatomy and embryology strongly supports the doctrine of human **monogenesis**." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", text: "Advocates of **monogenesis** rightly insisted upon the fundamental physical unity linking all varieties of mankind." },
      { author: "Max Müller", work: "Lectures on the Science of Language", text: "Comparative philology seeks to ascertain whether the linguistic families point back to primeval **monogenesis**." }
    ]
  },
  "monogenic": {
    primary: "Determined or controlled by a single gene locus, as in Mendelian single-gene traits or disorders.",
    secondary: "Reproducing asexually or having only a single stage in the life cycle without alternation of generations.",
    quotes: [
      { author: "Gregor Mendel", work: "Experiments in Plant Hybridisation", text: "The seed coat color segregated as a simple **monogenic** trait following clean three-to-one ratios." },
      { author: "William Bateson", work: "Mendel's Principles of Heredity", text: "Albinism in mammals represents a classic **monogenic** recessive defect in enzymatic melanin synthesis." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", text: "Natural selection operates swiftly upon **monogenic** differences where dominance determines clear phenotypic expression." }
    ]
  },
  "paragenesis": {
    primary: "The sequential or contemporaneous formation of associated minerals under characteristic geological, temperature, and pressure conditions.",
    secondary: "The study of the geochemical order and equilibrium associations of coexisting mineral phases in ore deposits and metamorphic rocks.",
    quotes: [
      { author: "August Breithaupt", work: "Die Paragenesis der Mineralien", text: "I established the term **paragenesis** to signify the lawful coexistence and sequence of minerals in natural ore veins." },
      { author: "Waldemar Lindgren", work: "Mineral Deposits", text: "Microscopic study of polished ore slabs unveils the detailed **paragenesis** of copper and silver sulfides." },
      { author: "Charles Lyell", work: "Principles of Geology", text: "The mineral **paragenesis** in granitic pegmatites reveals the cooling history of volatile magmatic residual fluids." }
    ]
  },
  "polygene": {
    primary: "A member of a group of non-allelic genes that together control a quantitative phenotypic character (such as height, skin color, or yield).",
    secondary: "A gene having a small, cumulative additive effect on a continuous phenotype in polygenic inheritance.",
    quotes: [
      { author: "Kenneth Mather", work: "Biometrical Genetics", text: "I introduced the concept of the **polygene** to account for continuous phenotypic variation governed by Mendelian principles." },
      { author: "Ronald Fisher", work: "The Correlation Between Relatives on the Supposition of Mendelian Inheritance", text: "The cumulative action of multiple **polygenes** generates normal bell-shaped frequency distributions in natural populations." },
      { author: "Sewall Wright", work: "Evolution and the Genetics of Populations", text: "Selection upon a vast **polygene** system permits steady phenotypic movement far beyond the original range of variation." }
    ]
  },
  "polygenic": {
    primary: "Controlled or influenced by multiple non-allelic genes acting together in an additive or interactive manner.",
    secondary: "Pertaining to quantitative traits (such as blood pressure, intelligence, or grain yield) governed by complex genetic networks.",
    quotes: [
      { author: "Kenneth Mather", work: "Polygenic Inheritance and Natural Selection", text: "Continuous variation in nature is overwhelmingly **polygenic**, mediated by scores of contributing loci." },
      { author: "Theodosius Dobzhansky", work: "Mankind Evolving", text: "Human stature and skin pigmentation are typical **polygenic** characteristics responsive to both genetics and climate." },
      { author: "Richard Lewontin", work: "The Genetic Basis of Evolutionary Change", text: "Mapping the specific loci underlying a **polygenic** trait remains one of the toughest challenges of quantitative genetics." }
    ]
  },
  "polygenous": {
    primary: "Having many origins, varieties, or kinds; composed of diverse elements.",
    secondary: "In historical ethnology or linguistics, originating from multiple independent ancestral stocks or evolutionary sources.",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The imperial army had become a **polygenous** host recruited from every barbarian tribe along the frontiers." },
      { author: "Thomas Henry Huxley", work: "Methods and Results of Ethnology", text: "The polygenist school asserted that human races were **polygenous** species created independently across continents." },
      { author: "Max Müller", work: "The Science of Language", text: "A **polygenous** vocabulary reflects centuries of conquest, maritime trade, and cultural borrowing." }
    ]
  },
  "progenesis": {
    primary: "A form of heterochrony in which an organism attains sexual maturity while still possessing juvenile or larval somatic morphology.",
    secondary: "The precocious acceleration of gonadal development relative to somatic growth, leading to truncated ontogeny.",
    quotes: [
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", text: "In **progenesis**, early sexual maturation halts somatic development, producing minute adult organisms with larval anatomy." },
      { author: "Julian Huxley", work: "Problems of Relative Growth", text: "The axolotl provides an evolutionary classic of neoteny, while certain gall midges display extreme reproductive **progenesis**." },
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", text: "Heterochronic shifts like **progenesis** offer rapid evolutionary routes to new ecological niches without complex genetic redesign." }
    ]
  },
  "pseudogene": {
    primary: "A section of DNA that closely resembles a functional gene but contains mutations (such as frameshifts or stop codons) that prevent its transcription or translation.",
    secondary: "A non-functional, decayed genomic relic resulting from gene duplication (unprocessed pseudogene) or retrotransposition (processed pseudogene).",
    quotes: [
      { author: "Richard Dawkins", work: "The Blind Watchmaker", text: "The genome is littered with **pseudogenes**, petrified genetic fossils of ancestral genes that have fallen into silence." },
      { author: "Francis Crick", work: "What Mad Pursuit", text: "Duplicated copies free from selective pressure rapidly accumulate disabling mutations, drifting into inert **pseudogenes**." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", text: "Shared non-functional **pseudogenes** in humans and chimpanzees furnish unanswerable proof of shared genealogical descent." }
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
for (const [lemma, data] of Object.entries(BATCH3_DATA)) {
  const filePath = path.join(CLUSTER_DIR, DASHBOARD, `${lemma}.md`);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    continue;
  }
  if (updateFile(filePath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Gen Batch 3 Completed: ${count} / ${Object.keys(BATCH3_DATA).length} words updated`);
console.log(`========================================\n`);
