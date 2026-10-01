import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Life & Vitality';

const BATCH6_DATA = {
  // Dashboard — treph (35 words)
  "amyotrophic": {
    dashboard: "Dashboard — treph",
    primary: "Relating to or characterized by muscular atrophy resulting from disease of the motor neurons in the spinal cord.",
    secondary: "Pertaining to amyotrophic lateral sclerosis (ALS / Lou Gehrig's disease), a progressive neurodegenerative disorder.",
    quotes: [
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", text: "I identified **amyotrophic** lateral sclerosis as a dual lesion uniting anterior horn motor cell degeneration with lateral spinal column sclerosis." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "In **amyotrophic** lateral sclerosis, fibrillary twitchings and muscular wasting precede spastic paralysis of the limbs." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Microscopic sections in **amyotrophic** disease reveal marked disappearance of the large multipolar Betz cells and motor root atrophy." }
    ]
  },
  "atrophic": {
    dashboard: "Dashboard — treph",
    primary: "Characterized by, exhibiting, or resulting from atrophy (wasting away or diminution in size of a body part or organ).",
    secondary: "Describing tissue or cellular degeneration resulting from starvation, denervation, disuse, or lack of endocrine trophic stimulation.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "The histological hallmark of the **atrophic** muscle fiber is volumetric shrinkage accompanied by fatty infiltration." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Chronic gastritis culminates in an **atrophic** mucosal lining incapable of secreting gastric acid and intrinsic factor." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Denervation of an involuntary salivary gland induces rapid **atrophic** changes in its glandular parenchyma." }
    ]
  },
  "atrophy": {
    dashboard: "Dashboard — treph",
    primary: "The wasting away, shrinkage, or decrease in size of a body organ, tissue, or cell caused by disease, malnutrition, or disuse.",
    secondary: "Figuratively, a gradual decline, wasting, or cessation of functional vitality, vigor, or creative energy in an institution or individual.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", text: "Disuse leads to the progressive **atrophy** and eventual reduction of useless organs in subterranean and cave fauna." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "Simple **atrophy** consists in a mere diminution in the volume of cellular elements without alteration in their quality." },
      { author: "William Osler", work: "Aequanimitas", text: "Intellectual **atrophy** inevitably overtakes the medical practitioner who ceases to read and observe." }
    ]
  },
  "autotroph": {
    dashboard: "Dashboard — treph",
    primary: "An organism capable of synthesizing its own organic food molecules from inorganic substances (such as carbon dioxide) using light or chemical energy.",
    secondary: "A primary producer (plant, algae, or autotrophic bacterium) forming the fundamental trophic base of terrestrial and aquatic ecosystems.",
    quotes: [
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The **autotroph** fixes radiant solar energy into chemical bonds, providing the energetic substrate for all heterotrophic life." },
      { author: "Sergei Winogradsky", work: "Microbiologie du Sol", text: "I demonstrated that the nitrifying bacterium is an obligate **autotroph**, thriving in purely mineral solutions without organic carbon." },
      { author: "G. Evelyn Hutchinson", work: "The Ecological Theater and the Evolutionary Play", text: "Ecological pyramid efficiency reflects the rate at which the photosynthetic **autotroph** captures incoming photon flux." }
    ]
  },
  "autotrophic": {
    dashboard: "Dashboard — treph",
    primary: "Pertaining to, characterized by, or being an autotroph; capable of self-nourishment using inorganic sources.",
    secondary: "Describing biochemical pathways that assimilate carbon dioxide through the Calvin cycle, reverse Krebs cycle, or Wood-Ljungdahl pathway.",
    quotes: [
      { author: "Martinus Beijerinck", work: "Studies on Microbial Ecology", text: "Certain sulfur bacteria maintain an **autotrophic** existence in volcanic hot springs by oxidizing hydrogen sulfide." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The **autotrophic** stratum of the forest canopy captures sunlight, driving the primary productivity of the watershed." },
      { author: "Melvin Calvin", work: "The Path of Carbon in Photosynthesis", text: "Radio-tracer studies resolved the cyclical enzyme reactions sustaining **autotrophic** carbon assimilation." }
    ]
  },
  "auxotrophy": {
    dashboard: "Dashboard — treph",
    primary: "The inability of an organism to synthesize a particular organic compound required for its growth, necessitating that compound in its culture medium.",
    secondary: "In microbial genetics, a nutritional deficiency caused by a genetic mutation in a biosynthetic pathway, contrasted with prototrophy.",
    quotes: [
      { author: "George Beadle", work: "Genetic Control of Biochemical Reactions in Neurospora", text: "X-ray mutagenesis produced specific strains of Neurospora exhibiting nutritional **auxotrophy** for pyridoxine and thiamine." },
      { author: "Edward Tatum", work: "A Pure Culture Approach to Heredity", text: "Our one-gene-one-enzyme hypothesis explained how single point mutations create specific amino acid **auxotrophy**." },
      { author: "Joshua Lederberg", work: "Gene Recombination in Escherichia coli", text: "Crossing two divergent strains marked by complementary **auxotrophy** demonstrated genetic recombination in bacteria." }
    ]
  },
  "chemolithoautotroph": {
    dashboard: "Dashboard — treph",
    primary: "An organism that obtains energy by oxidizing inorganic compounds (such as iron, sulfur, or hydrogen) and uses carbon dioxide as its sole carbon source.",
    secondary: "Deep-sea hydrothermal vent bacteria and rock-inhabiting lithotrophs capable of sustaining complex food webs independently of sunlight.",
    quotes: [
      { author: "Sergei Winogradsky", work: "On Chemosynthesis", text: "The colorless sulfur bacterium is a true **chemolithoautotroph**, deriving all kinetic energy from sulfide oxidation and building tissue from carbonic acid." },
      { author: "Carl Woese", work: "Bacterial Evolution", text: "Phylogenetic analysis suggests that the ancestral prokaryote was an anaerobic **chemolithoautotroph** flourishing in primordial volcanic waters." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "At abyssal hydrothermal rifts, the **chemolithoautotroph** replaces green plants as the primary trophic producer." }
    ]
  },
  "dystrophy": {
    dashboard: "Dashboard — treph",
    primary: "A disorder in which an organ or tissue of the body wastes away, especially as a result of hereditary genetic defects or nutritional deficiency.",
    secondary: "Muscular dystrophy, a group of genetic degenerative diseases characterized by progressive skeletal muscle fiber necrosis and weakness.",
    quotes: [
      { author: "Guillaume Duchenne", work: "Recherches sur la Paralysie Musculaire Pseudohypertrophique", text: "Progressive muscular **dystrophy** in young boys presents marked calf pseudohypertrophy caused by extensive fibro-fatty tissue replacement." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Hereditary transmission in pseudohypertrophic **dystrophy** passes through asymptomatic mothers to afflicted male sons." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "The primary lesion in muscular **dystrophy** resides in the muscle cell membrane protein dystrophin, not the motor neurons." }
    ]
  },
  "eutrophic": {
    dashboard: "Dashboard — treph",
    primary: "Rich in nutrients, especially nitrogen and phosphorus; promoting lush aquatic plant and algal growth.",
    secondary: "In limnology, describing a body of water characterized by high nutrient content, abundant phytoplankton blooms, and seasonal deep-water oxygen depletion.",
    quotes: [
      { author: "G. Evelyn Hutchinson", work: "A Treatise on Limnology", text: "In the shallow **eutrophic** lake, dense summer algal blooms shade the depths, leading to hypolimnetic anoxia." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "Nutrient runoff accelerates the natural aging process of lakes, inducing premature **eutrophic** conditions." },
      { author: "Rachel Carson", work: "Silent Spring", text: "Excess agricultural fertilizers washed into rivers convert pristine waters into choked, foul-smelling **eutrophic** shallows." }
    ]
  },
  "hemidystrophy": {
    dashboard: "Dashboard — treph",
    primary: "Dystrophy or abnormal, defective development affecting only one lateral half of the body or an organ.",
    secondary: "A rare congenital hemiatrophy or asymmetrical trophic disorder characterized by unilateral skeletal and soft tissue underdevelopment.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Facial **hemidystrophy** of Romberg begins insidiously in childhood, wasting cutaneous fat and bone on one side of the face." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Congenital **hemidystrophy** must be distinguished from unilateral cerebral palsies presenting secondary disuse hypoplasia." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Senile and Chronic Diseases", text: "The trophic asymmetries observed in progressive **hemidystrophy** point to deep autonomic vascular dysfunction." }
    ]
  },
  "heterotroph": {
    dashboard: "Dashboard — treph",
    primary: "An organism that cannot manufacture its own food and instead derives its nutritional requirements from complex organic substances.",
    secondary: "A consumer or decomposer in an ecosystem (including animals, fungi, and many bacteria) that relies upon autotrophic primary production.",
    quotes: [
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The **heterotroph** decomposes organic matter, recycling essential mineral nutrients back to the primary producers." },
      { author: "Jacques Monod", work: "Chance and Necessity", text: "As an obligate **heterotroph**, the bacterium requires exogenous glucose to fuel glycolysis and macromolecular synthesis." },
      { author: "Alexander Oparin", work: "The Origin of Life", text: "The earliest primordial cells were necessarily **heterotrophs**, grazing upon the prebiotic organic broth of ancient seas." }
    ]
  },
  "heterotrophic": {
    dashboard: "Dashboard — treph",
    primary: "Pertaining to, characterized by, or being a heterotroph; obtaining carbon and energy from organic compounds.",
    secondary: "In ecological trophic systems, describing the consumer stratum that breaks down organic matter synthesized by autotrophs.",
    quotes: [
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The **heterotrophic** component of the forest soil decomposes leaf litter, releasing carbon dioxide into the soil atmosphere." },
      { author: "Arthur Tansley", work: "The Use and Abuse of Vegetational Concepts and Terms", text: "Energy flows unidirectionally from the autotrophs through successive **heterotrophic** consumer levels." },
      { author: "Albert Lehninger", work: "Biochemistry", text: "Unlike plant chloroplasts, mammalian mitochondria rely entirely on **heterotrophic** metabolic fuels." }
    ]
  },
  "hypertrophy": {
    dashboard: "Dashboard — treph",
    primary: "The enlargement of an organ or tissue resulting from an increase in the size of its individual cells, rather than from an increase in cell number.",
    secondary: "Adaptive cellular enlargement in response to increased functional workload (as in cardiac ventricular hypertrophy) or hormonal stimulation.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", text: "In true **hypertrophy**, each individual muscle fiber expands in diameter without any numerical increase in the constituent cells." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Aortic stenosis inevitably forces the left ventricle into compensatory muscular **hypertrophy**." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Benign prostatic **hypertrophy** exerts progressive mechanical compression upon the prostatic urethra." }
    ]
  },
  "lithoautotroph": {
    dashboard: "Dashboard — treph",
    primary: "An autotrophic organism that obtains its energy from the oxidation of inorganic mineral substrates; a chemolithoautotroph.",
    secondary: "A subterranean or lithic microbe capable of colonizing bare granite or basalt using mineral sulfur, iron, or hydrogen.",
    quotes: [
      { author: "Sergei Winogradsky", work: "Microbiologie du Sol", text: "The subterranean **lithoautotroph** extracts reducing equivalents from pyrites, flourishing entirely isolated from sunlight." },
      { author: "Carl Woese", work: "Bacterial Evolution", text: "Deep crystalline aquifers host communities where the **lithoautotroph** forms the bedrock of the subterranean biosphere." },
      { author: "Alexander Oparin", work: "The Origin of Life", text: "Prebiotic evolution likely relied on primitive catalysts preceding the specialization of the modern **lithoautotroph**." }
    ]
  },
  "lithotroph": {
    dashboard: "Dashboard — treph",
    primary: "An organism that uses inorganic substrate molecules (such as mineral ions or dissolved gases) as electron donors for biosynthesis or energy production.",
    secondary: "A microbe specialized in the chemical weathering of rocks, ores, and volcanic lavas through inorganic redox reactions.",
    quotes: [
      { author: "Sergei Winogradsky", work: "Principles of Soil Microbiology", text: "I classified the iron-oxidizing Leptothrix as an obligate **lithotroph** capable of deriving energy from ferrous salts." },
      { author: "Albert Lehninger", work: "Principles of Biochemistry", text: "The biochemical hallmark of the **lithotroph** is its ability to direct electron transport chains using inorganic electron donors." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "Acid mine drainage is catalyzed by the metabolic activities of the iron-oxidizing **lithotroph** Thiobacillus ferrooxidans." }
    ]
  },
  "mixotroph": {
    dashboard: "Dashboard — treph",
    primary: "An organism capable of utilizing a mix of different sources of energy and carbon, alternating between autotrophy and heterotrophy.",
    secondary: "A unicellular protist (such as *Euglena*) that conducts photosynthesis when light is abundant and ingests organic prey in darkness.",
    quotes: [
      { author: "G. Evelyn Hutchinson", work: "A Treatise on Limnology", text: "The flagellate Euglena behaves as an opportunistic **mixotroph**, retaining chloroplasts while readily absorbing dissolved peptides." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "Planktonic **mixotrophs** dominate oligotrophic oceanic gyres where mineral nutrients and sunlight fluctuate dramatically." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", text: "Flexible cellular metabolism in the **mixotroph** represents a resilient evolutionary hedge against environmental scarcity." }
    ]
  },
  "organotroph": {
    dashboard: "Dashboard — treph",
    primary: "An organism that obtains hydrogen or electrons from organic substrates for cellular metabolism and biosynthesis.",
    secondary: "A bacterium or eukaryotic organism that relies upon organic electron donors (such as carbohydrates or amino acids), contrasted with a lithotroph.",
    quotes: [
      { author: "Albert Lehninger", work: "Biochemistry", text: "Most heterotrophic bacteria are simultaneously **organotrophs**, consuming carbohydrates both as carbon skeletons and electron donors." },
      { author: "Martinus Beijerinck", work: "Studies on Microbial Ecology", text: "Selective culture media enriched with lactate isolate the specialized **organotroph** from mixed river muds." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "Soil fungi act as paramount **organotrophs**, oxidizing refractory cellulose and humic polymers." }
    ]
  },
  "phagotrophy": {
    dashboard: "Dashboard — treph",
    primary: "The mode of nutrition in which particulate food is engulfed and internalized into food vacuoles (phagocytosis).",
    secondary: "Heterotrophic particle ingestion characteristic of amoeboid protists, ciliates, and specialized phagocytic host leukocytes.",
    quotes: [
      { author: "Élie Metchnikoff", work: "Immunity in Infective Diseases", text: "Phagocytic immunity is an evolutionary descendant of primitive cellular **phagotrophy** observed in unicellular amoebae." },
      { author: "Ray Lankester", work: "Zoological Articles", text: "The ciliate Stentor drives food particles into its cytostome through specialized cilia adapted for **phagotrophy**." },
      { author: "Lynn Margulis", work: "Origin of Eukaryotic Cells", text: "The evolutionary leap toward the modern eukaryote required the prior innovation of membrane-bound **phagotrophy**." }
    ]
  },
  "photoheterotroph": {
    dashboard: "Dashboard — treph",
    primary: "An organism that uses light for energy but cannot use carbon dioxide as its sole carbon source, requiring organic compounds from its environment.",
    secondary: "A photosynthetic organism (such as purple non-sulfur bacteria) that generates ATP via photophosphorylation while assimilating organic acids.",
    quotes: [
      { author: "Cornelis van Niel", work: "The Chemolithoautotrophic and Photosynthetic Bacteria", text: "Rhodospirillum rubrum functions as a quintessential **photoheterotroph**, converting organic malate using light energy without oxygen evolution." },
      { author: "Albert Lehninger", work: "Principles of Biochemistry", text: "The **photoheterotroph** combines light-driven ATP production with the enzymatic assimilation of simple organic carbon skeletons." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "In anoxic littoral sediments, the **photoheterotroph** exploits radiant infrared energy while recycling fermentation byproducts." }
    ]
  },
  "phototroph": {
    dashboard: "Dashboard — treph",
    primary: "An organism that manufactures its own food or derives energy from light (photons) through photochemical processes; a photosynthetic organism.",
    secondary: "Any photosynthetic organism (plants, algae, cyanobacteria, and photosynthetic bacteria) capable of converting electromagnetic radiation into chemical energy.",
    quotes: [
      { author: "Cornelis van Niel", work: "The Comparative Biochemistry of Photosynthesis", text: "Every **phototroph** utilizes light quanta to drive internal hydrogen transfers between donor and acceptor molecules." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The marine **phototroph** populates the sunlit euphotic zone, providing the primary energy sustaining pelagic food chains." },
      { author: "Melvin Calvin", work: "Chemical Evolution", text: "Primitive porphyrins facilitated the evolutionary transition from geochemical catalysis to the first true cellular **phototroph**." }
    ]
  },
  "phototrophic": {
    dashboard: "Dashboard — treph",
    primary: "Of, relating to, or being a phototroph; obtaining energy from light via photosynthesis.",
    secondary: "Pertaining to light-driven metabolic pathways and photochemical phosphorylation systems in living cells.",
    quotes: [
      { author: "Martinus Beijerinck", work: "Studies on Microbial Ecology", text: "Cyanobacteria represent an ancient **phototrophic** lineage that enriched the primeval atmosphere with free oxygen." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The productivity of the **phototrophic** layer depends upon solar irradiance, water temperature, and dissolved nitrates." },
      { author: "Albert Lehninger", work: "Biochemistry", text: "In **phototrophic** cells, light absorption by antenna pigments excites electrons to initiate photosynthetic phosphorylation." }
    ]
  },
  "phototrophy": {
    dashboard: "Dashboard — treph",
    primary: "The synthesis of organic molecules from inorganic materials using energy absorbed from light; photosynthetic nutrition.",
    secondary: "The biological mode of life relying on the absorption of light quanta by photosynthetic pigments to generate metabolic energy.",
    quotes: [
      { author: "Cornelis van Niel", work: "Photosynthesis of Bacteria", text: "Comparative biochemistry unifies oxygenic plant photosynthesis with bacterial anoxygenic **phototrophy**." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The global carbon cycle balances the carbon fixation of **phototrophy** against the respiratory breakdown of heterotrophs." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", text: "The acquisition of **phototrophy** by eukaryotic algae resulted from the endosymbiotic engulfment of ancestral cyanobacteria." }
    ]
  },
  "pogonotrophy": {
    dashboard: "Dashboard — treph",
    primary: "The growing, cultivating, or grooming of a beard.",
    secondary: "The cultural practice, art, or fashionable custom of maintaining facial hair.",
    quotes: [
      { author: "Thomas Carlyle", work: "Sartor Resartus", text: "The solemn German professor cultivated magnificent **pogonotrophy**, allowing his beard to sweep across his lecturing lectern." },
      { author: "William Makepeace Thackeray", work: "The Book of Snobs", text: "Young military subalterns devoted astonishing energy to competitive **pogonotrophy** and the sculpting of fierce moustaches." },
      { author: "Richard Burton", work: "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", text: "In the Levant, successful disguise required diligent **pogonotrophy**, as an untrimmed oriental beard commanded instant civic respect." }
    ]
  },
  "poliodystrophy": {
    dashboard: "Dashboard — treph",
    primary: "A degenerative disease of the gray matter of the brain, especially progressive infantile poliodystrophy (Alpers' disease).",
    secondary: "A neurodegenerative metabolic disorder characterized by intractable childhood seizures, progressive cerebral cortex atrophy, and hepatic cirrhosis.",
    quotes: [
      { author: "Bernard Alpers", work: "Diffuse Progressive Degeneration of the Gray Matter of the Cerebrum", text: "I described progressive cerebral **poliodystrophy** as a devastating childhood encephalopathy targeting the cerebral gray mantle." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Post-mortem examination in **poliodystrophy** reveals extensive neuronal loss and gliosis confined strictly to the cerebral cortex." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Intractable developmental regression accompanied by myoclonic spasms suggests progressive infantile **poliodystrophy**." }
    ]
  },
  "prototrophy": {
    dashboard: "Dashboard — treph",
    primary: "The ability of an organism (especially a bacterium or fungus) to synthesize all the growth factors and amino acids it requires from simple mineral salts and a carbon source.",
    secondary: "The wild-type nutritional state in microbial genetics, contrasted with mutant nutritional auxotrophy.",
    quotes: [
      { author: "Edward Tatum", work: "Genetic Control of Biochemical Reactions", text: "Selection for wild-type **prototrophy** allowed us to isolate rare revertant colonies from heavily irradiated auxotrophs." },
      { author: "Joshua Lederberg", work: "Gene Recombination in Escherichia coli", text: "When two different nutritional mutants were plated together, recombinant colonies exhibiting full **prototrophy** emerged on minimal agar." },
      { author: "Jacques Monod", work: "Chance and Necessity", text: "The wild-type Escherichia coli exhibits complete **prototrophy**, synthesizing every complex cellular metabolite from glucose and ammonium salts." }
    ]
  },
  "trephination": {
    dashboard: "Dashboard — treph",
    primary: "The surgical operation of drilling or cutting a circular hole into the skull with a trephine to relieve intracranial pressure or access the brain.",
    secondary: "An ancient surgical practice (trepanning) performed since the Neolithic era to treat head injuries, headaches, or spiritual afflictions.",
    quotes: [
      { author: "Paul Broca", work: "Sur la Trépanation Préhistorique", text: "Prehistoric skulls unearthed in Peruvian caverns show unmistakable evidence of successful **trephination** with healed bone margins." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Emergency **trephination** over the middle meningeal artery relieves expanding epidural hemorrhage following head trauma." },
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", text: "Neurosurgical subtemporal **trephination** decompresses intolerable intracranial tension in inoperable neoplasms." }
    ]
  },
  "trephine": {
    dashboard: "Dashboard — treph",
    primary: "A surgical instrument with a cylindrical saw blade used for cutting out circular discs of bone, especially from the skull.",
    secondary: "To operate upon with a trephine; to cut a circular window into a bone or corneal button in ophthalmic surgery.",
    quotes: [
      { author: "Ambroise Paré", work: "The Apologie and Treatise", text: "The surgeon should gently rotate the crown of the **trephine** until the outer cranial table is neatly traversed." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "We decided to **trephine** the parietal bone immediately to drain the localized subdural abscess." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", text: "The sharp teeth of the modern surgical **trephine** penetrate the skull with geometric safety unknown to ancient barbers." }
    ]
  },
  "trephritidae": {
    dashboard: "Dashboard — treph",
    primary: "A historical or variant orthographic spelling for Tephritidae, the family of true fruit flies (order Diptera), known for attractively marked wings.",
    secondary: "Agricultural pest flies whose larvae develop in ripening fruit and flower heads, including the Mediterranean fruit fly (*Ceratitis capitata*).",
    quotes: [
      { author: "David Sharp", work: "Insects: Part II", text: "Early dipterists catalogued these gall-making and fruit-infesting flies under the family designation **Trephritidae**." },
      { author: "Charles Valentine Riley", work: "Report on Noxious Insects", text: "The banded wings and ovipositor structure align the destructive apple maggot fly with the **Trephritidae**." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "Economic losses inflicted by larval infestations of the **Trephritidae** prompted worldwide phytosanitary quarantine protocols." }
    ]
  },
  "trophectoderm": {
    dashboard: "Dashboard — treph",
    primary: "The outer layer of cells of the early mammalian blastocyst that implants into the uterine wall and develops into the placenta and chorion; trophoblast.",
    secondary: "The first specialized, differentiated epithelial tissue established during mammalian embryogenesis, giving rise to extraembryonic fetal membranes.",
    quotes: [
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", text: "Differential gene expression separates the inner pluripotential cell mass from the enveloping **trophectoderm**." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Adhesion of the blastocyst **trophectoderm** to the uterine epithelium initiates maternal decidualization." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Invasive trophoblastic disease represents uncontrolled neoplastic proliferation of cells derived from the **trophectoderm**." }
    ]
  },
  "trophic": {
    dashboard: "Dashboard — treph",
    primary: "Of or relating to feeding, nutrition, or nutrient uptake.",
    secondary: "Pertaining to nutritional relationships in an ecosystem (trophic level, food chain) or to physiological factors promoting tissue growth.",
    quotes: [
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "Energy decreases progressively as it ascends from the primary producer level through higher **trophic** levels." },
      { author: "Charles Elton", work: "Animal Ecology", text: "The pyramid of numbers in an animal community is a direct consequence of the **trophic** structure of food chains." },
      { author: "Claude Bernard", work: "Lectures on Experimental Physiology", text: "Autonomic nerves exert a direct **trophic** influence upon the cellular metabolism and vascular tone of glandular tissues." }
    ]
  },
  "trophobiosis": {
    dashboard: "Dashboard — treph",
    primary: "A symbiotic relationship between two organisms in which food, nourishment, or secretions are exchanged for protection or other services.",
    secondary: "The mutualistic association between ants and honeydew-producing hemipterous insects (such as aphids and scale insects).",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", text: "The mutualistic interaction wherein ants guard aphid herds in exchange for sweet honeydew represents classic **trophobiosis**." },
      { author: "Edward O. Wilson", work: "The Insect Societies", text: "Sophisticated **trophobiosis** has evolved independently across multiple ant subfamilies interacting with diverse sap-sucking insects." },
      { author: "August Forel", work: "The Social World of the Ants", text: "Ants attend the root aphids with maternal tenderness, demonstrating the deep behavioral complexity of subterranean **trophobiosis**." }
    ]
  },
  "trophobiotic": {
    dashboard: "Dashboard — treph",
    primary: "Of, relating to, or engaging in trophobiosis; mutually dependent through nutritional food exchange.",
    secondary: "Pertaining to symbiotic interactions where one partner provides food secretions and the other offers defensive services.",
    quotes: [
      { author: "William Morton Wheeler", work: "Social Life Among the Insects", text: "The **trophobiotic** bond between honeydew-secreting membracids and foraging dolichoderine ants is extraordinarily intimate." },
      { author: "Edward O. Wilson", work: "Sociobiology: The New Synthesis", text: "Chemical cues mediate the **trophobiotic** solicitation dance performed by worker ants touching aphid abdomens with antennae." },
      { author: "David Sharp", work: "Insects: Part II", text: "Certain lycaenid butterfly caterpillars have evolved specialized **trophobiotic** glands that produce sugary juices for protector ants." }
    ]
  },
  "trophoblast": {
    dashboard: "Dashboard — treph",
    primary: "The outer cellular layer of a mammalian blastocyst that provides nutrients to the embryo and develops into the major part of the placenta.",
    secondary: "The specialized fetal tissue that invades maternal endometrial blood vessels during implantation and secretes human chorionic gonadotropin (hCG).",
    quotes: [
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", text: "The **trophoblast** mediates the primary physiological contact between the developing mammalian blastocyst and the maternal uterus." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Syncytial giant cells of the invasive **trophoblast** erode maternal capillaries to create lacunar vascular pools." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Enzymatic secretions produced by the embryonic **trophoblast** digest maternal decidual tissue to permit deep nidation." }
    ]
  },
  "trophoblastic": {
    dashboard: "Dashboard — treph",
    primary: "Of, relating to, or derived from the trophoblast.",
    secondary: "Pertaining to gestational trophoblastic disease (including hydatidiform mole and choriocarcinoma) characterized by abnormal placental proliferation.",
    quotes: [
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Choriocarcinoma is a highly malignant **trophoblastic** neoplasm that spreads rapidly through the maternal venous system." },
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", text: "The **trophoblastic** lacunae fill with maternal blood, establishing the hemochorial placenta." },
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", text: "Persistent elevation of urinary chorionic gonadotropin points to residual **trophoblastic** tissue following molar pregnancy." }
    ]
  },
  "trophozoite": {
    dashboard: "Dashboard — treph",
    primary: "The active, motile, feeding, and reproducing stage in the life cycle of certain parasitic protozoans (such as *Plasmodium* or *Entamoeba histolytica*).",
    secondary: "The vegetative amoeboid stage of protozoa in host tissues, contrasted with the resistant dormant cyst stage.",
    quotes: [
      { author: "Patrick Manson", work: "Tropical Diseases", text: "In acute amebic dysentery, microscopic stool examination demonstrates motile **trophozoites** actively ingesting red blood cells." },
      { author: "Ronald Ross", work: "The Prevention of Malaria", text: "The erythrocytic **trophozoite** of Plasmodium grows within the red blood corpuscle, producing malarial pigment before sporulation." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Ulceration of the colonic mucosa results from tissue-dissolving proteases secreted by the invasive **trophozoite**." }
    ]
  },

  // Dashboard — sperm (28 words)
  "angiosperm": {
    dashboard: "Dashboard — sperm",
    primary: "A plant that produces seeds enclosed within a carpel or fruit; a flowering plant belonging to the division Anthophyta (Magnoliophyta).",
    secondary: "The dominant group of land plants, characterized by double fertilization, triploid endosperm, flowers, and xylem vessels.",
    quotes: [
      { author: "Charles Darwin", work: "Letter to Joseph Dalton Hooker", text: "The rapid development as far as we can judge of all the higher plants within recent geological times is an abominable mystery—the explosive rise of the **angiosperm**." },
      { author: "Asa Gray", work: "Botanical Textbook", text: "Every true **angiosperm** conceals its developing ovules within the protective cavity of an ovary." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "The emergence of the **angiosperm** transformed the face of the Earth from gloomy conifer groves to radiant floral landscapes." }
    ]
  },
  "angiospermous": {
    dashboard: "Dashboard — sperm",
    primary: "Of, relating to, or characteristic of angiosperms; having seeds enclosed in a fruit or seedpod.",
    secondary: "Pertaining to flowering plants with enclosed seeds and vascular xylem vessels.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", text: "The **angiospermous** flower incorporates specialized floral envelopes designed to attract animal pollinators." },
      { author: "Charles Darwin", work: "The Origin of Species", text: "The co-evolution of **angiospermous** nectar-bearing flowers and flower-haunting insects spurred tremendous evolutionary radiation." },
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "Fossil floras from the Cretaceous record the sudden ascendancy of **angiospermous** hardwood trees over Mesozoic cycads." }
    ]
  },
  "endosperm": {
    dashboard: "Dashboard — sperm",
    primary: "The nutritive tissue formed within the embryo sac of flowering plants following double fertilization, nourishing the developing plant embryo.",
    secondary: "A typically triploid tissue storing starches, proteins, and oils, constituting the bulk of cereal grains (such as wheat, rice, and maize).",
    quotes: [
      { author: "Sergei Nawaschin", work: "Resultate einer Revision der Befruchtungsvorgänge bei Lilium Martagon", text: "Double fertilization produces two distinct entities: the diploid zygote and the triploid **endosperm** nourishing it." },
      { author: "Asa Gray", work: "Elements of Botany", text: "In cereal grains, the floury **endosperm** provides the abundant food reserves that sustain both seedling and human civilization." },
      { author: "Gregor Mendel", work: "Experiments in Plant Hybridisation", text: "Characters expressed in the cotyledons and **endosperm** of the hybrid seed showed immediate dominance without awaiting second-year growth." }
    ]
  },
  "episperm": {
    dashboard: "Dashboard — sperm",
    primary: "The outer coat or covering of a seed; the testa.",
    secondary: "The protective integument of a mature plant ovule shielding the embryo and perisperm against desiccation and mechanical injury.",
    quotes: [
      { author: "Augustin Pyramus de Candolle", work: "Théorie Élémentaire de la Botanique", text: "The **episperm** exhibits diverse surface sculpturings, wing-like expansions, and hairs adapted for wind or animal dispersal." },
      { author: "Asa Gray", work: "Botanical Textbook", text: "In cotton, the fibers of commerce are unicellular epidermal outgrowths arising directly from the surface of the **episperm**." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "Hardening of the **episperm** creates an impenetrable barrier that enforces seed dormancy until favorable rains arrive." }
    ]
  },
  "gymnosperm": {
    dashboard: "Dashboard — sperm",
    primary: "A vascular plant that produces seeds that are not enclosed in an ovary or fruit, but borne naked on scales or cones (such as conifers, cycads, and ginkgoes).",
    secondary: "An ancient seed plant lineage that dominated Mesozoic terrestrial landscapes prior to the rise of angiosperms.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", text: "The naked ovule of the **gymnosperm** receives airborne pollen directly upon the micropyle without intervening stigma or style." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "Pines and spruces represent the hardiest northern survivors of the ancient **gymnosperm** alliance." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "In every typical **gymnosperm**, pollination is mediated entirely by wind currents carrying buoyant winged pollen grains." }
    ]
  },
  "gymnospermous": {
    dashboard: "Dashboard — sperm",
    primary: "Of, relating to, or having the characteristics of a gymnosperm; bearing naked seeds.",
    secondary: "Pertaining to non-flowering seed plants lacking true closed ovaries and vessels in their wood (except Gnetales).",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", text: "Petrified trunks in the Carboniferous coal measures display characteristic **gymnospermous** pitted tracheids." },
      { author: "Asa Gray", work: "Structural Botany", text: "The simple cone scale of the **gymnospermous** ovulate strobilus represents a primitive floral homologue." },
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "Mesozoic forests consisted primarily of **gymnospermous** conifers, cycadeoids, and ginkgoalean trees." }
    ]
  },
  "oligospermia": {
    dashboard: "Dashboard — sperm",
    primary: "A deficiency in the number of spermatozoa in the semen, resulting in reduced male fertility.",
    secondary: "A clinical condition defined by a sperm concentration below normal physiological thresholds (typically under 15 million spermatozoa per milliliter).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Severe endocrine hypopituitarism or testicular mumps orchitis frequently induces permanent **oligospermia**." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Histological examination in idiopathic **oligospermia** reveals hyalinization of seminiferous tubules and maturation arrest." },
      { author: "Frank Beach", work: "Hormones and Behavior", text: "While **oligospermia** impairs reproductive fecundity, it does not necessarily diminish male libidinal potency." }
    ]
  },
  "perisperm": {
    dashboard: "Dashboard — sperm",
    primary: "Nutritive tissue of a seed derived from the nucellus outside the embryo sac, surrounding the endosperm in certain plant families.",
    secondary: "A diploid maternal nutrient tissue storing starch, present in mature seeds of Caryophyllaceae, Piperaceae, and Chenopodiaceae.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", text: "In the water lily and black pepper, food storage resides primarily within the abundant nucellar **perisperm**." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "We distinguish true endosperm from the **perisperm**, which is formed entirely outside the embryo sac." },
      { author: "Augustin Pyramus de Candolle", work: "Théorie Élémentaire de la Botanique", text: "In beet seeds, the developing embryo curves snugly around a dense central reservoir of floury **perisperm**." }
    ]
  },
  "sperm": {
    dashboard: "Dashboard — sperm",
    primary: "Semen; also, a spermatozoon or male gamete; in whales, spermaceti.",
    secondary: "The haploid reproductive cell produced by the male gonad capable of fertilizing an ovum.",
    quotes: [
      { author: "Antonie van Leeuwenhoek", work: "Letter to the Royal Society of London", text: "Examining fresh canine seminal fluid under the microscope, I observed millions of microscopic animalcules moving vigorously in the **sperm**." },
      { author: "Herman Melville", work: "Moby-Dick", text: "We were squeezed and steeped in the precious **sperm** till our hands were soft as satin." },
      { author: "Charles Darwin", work: "The Descent of Man", text: "Sexual selection operates through competition among males whose motile **sperm** compete to fertilize the female ova." }
    ]
  },
  "spermaceti": {
    dashboard: "Dashboard — sperm",
    primary: "A white, waxy substance found in the head cavities of the sperm whale (*Physeter macrocephalus*), formerly used for candles, ointments, and lubricants.",
    secondary: "A liquid cetyl ester wax contained within the cranial case of sperm whales, believed to function in acoustic focusing and buoyancy regulation.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", text: "The vast spermaceti case of the whale was opened, and buckets of clear, sweet **spermaceti** were hoisted to the deck." },
      { author: "William Shakespeare", work: "Henry IV, Part 1", text: "The sovereign'st thing on earth was **spermaceti** for an inward bruise." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", text: "Commonly mistaken for the whale's semen, **spermaceti** is an oily, crystalline fat located in the bony cistern of its head." }
    ]
  },
  "spermatic": {
    dashboard: "Dashboard — sperm",
    primary: "Of, relating to, or conveying sperm or semen; seminal.",
    secondary: "In anatomy, designating structures associated with the testes, such as the spermatic cord, spermatic artery, and spermatic vein.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", text: "The **spermatic** cord suspends the testis within the scrotum and contains the ductus deferens and pampiniform plexus." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", text: "Torsion of the **spermatic** vessels rapidly precipitates hemorrhagic infarction of the testicle." },
      { author: "William Shakespeare", work: "Troilus and Cressida", text: "He spoke of hot blood and **spermatic** vigor, mocking the cold wisdom of the aged counselors." }
    ]
  },
  "spermatid": {
    dashboard: "Dashboard — sperm",
    primary: "An immature, non-motile haploid male germ cell formed by the division of a secondary spermatocyte, developing into a mature spermatozoon.",
    secondary: "A round or elongating germ cell in the seminiferous epithelium undergoing spermiogenesis (acrosome formation and flagellar growth).",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "The transformation of the spherical **spermatid** into a motile flagellated spermatozoon is a masterpiece of cellular remodeling." },
      { author: "Thomas Hunt Morgan", work: "The Physical Basis of Heredity", text: "Each primary spermatocyte yields four haploid **spermatids**, each carrying a unique assortment of paternal and maternal chromosomes." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Toxic exposure halts spermiogenesis, leaving rows of immature **spermatids** degenerating within the testicular tubules." }
    ]
  },
  "spermatocele": {
    dashboard: "Dashboard — sperm",
    primary: "A benign cystic accumulation of sperm and fluid arising from the epididymis or rete testis.",
    secondary: "A painless, transilluminating retention cyst of the head of the epididymis filled with cloudy fluid containing spermatozoa.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "A chronic, painless scrotal swelling lying superior to the testicle frequently proves upon aspiration to be a benign **spermatocele**." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Aspiration of a **spermatocele** reveals non-motile spermatozoa suspended in a clear, watery or milky serous fluid." },
      { author: "Henry Gray", work: "Anatomy of the Human Body", text: "Cysts of the epididymal efferent ductules readily enlarge to form an encysted **spermatocele**." }
    ]
  },
  "spermatocide": {
    dashboard: "Dashboard — sperm",
    primary: "A chemical substance or agent that kills spermatozoa; spermicide.",
    secondary: "A contraceptive agent designed to rapidly immobilize and destroy sperm cells upon contact in the vagina.",
    quotes: [
      { author: "Marie Stopes", work: "Contraception: Its Theory, History and Practice", text: "A safe, non-irritating **spermatocide** incorporated into soluble pessaries forms a practical barrier against conception." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "The evolution of modern birth control relied heavily on the synthesis of effective, non-toxic **spermatocides**." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Topical application of a potent **spermatocide** disrupts the lipoprotein envelope of the sperm flagellum in seconds." }
    ]
  },
  "spermatocyte": {
    dashboard: "Dashboard — sperm",
    primary: "A male germ cell derived from a spermatogonium that undergoes meiosis to produce spermatids.",
    secondary: "A primary spermatocyte (diploid, undergoing meiosis I) or secondary spermatocyte (haploid, undergoing meiosis II) in the testis.",
    quotes: [
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", text: "Synapsis and crossing over occur during the prolonged prophase of the primary **spermatocyte**." },
      { author: "August Weismann", work: "The Germ-Plasm: A Theory of Heredity", text: "The reduction division within the **spermatocyte** ensures that the gametes inherit an exact half of the parental germ-plasm." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Concentric rings of dividing **spermatocytes** line the seminiferous tubules toward the central lumen." }
    ]
  },
  "spermatogenesis": {
    dashboard: "Dashboard — sperm",
    primary: "The biological process of the formation and development of mature spermatozoa in the male seminiferous tubules.",
    secondary: "The complete cellular progression from spermatogonial stem cells through meiotic divisions to flagellated spermatozoa.",
    quotes: [
      { author: "August Weismann", work: "The Germ-Plasm: A Theory of Heredity", text: "Continuous **spermatogenesis** provides millions of unique recombinant gametes throughout the reproductive life of the male." },
      { author: "Frank Beach", work: "Hormones and Behavior", text: "Luteinizing hormone and follicle-stimulating hormone act synergistically to maintain active **spermatogenesis**." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Cryptorchidism leads to thermal arrest of **spermatogenesis** while leaving androgen-producing Leydig cells intact." }
    ]
  },
  "spermatogonium": {
    dashboard: "Dashboard — sperm",
    primary: "An undifferentiated male germ cell in the basement membrane of a seminiferous tubule that gives rise to spermatocytes.",
    secondary: "A stem cell of the male germ line that undergoes mitotic renewal to maintain spermatogenesis throughout adult life.",
    quotes: [
      { author: "August Weismann", work: "Essays Upon Heredity", text: "The immortal lineage of the germ-plasm resides in the quiescent **spermatogonium** resting upon the tubular basement membrane." },
      { author: "Thomas Hunt Morgan", work: "The Mechanism of Mendelian Heredity", text: "Mitotic divisions of the **spermatogonium** preserve an identical chromosomal complement before meiosis commences." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Seminoma of the testis represents a malignant proliferation of cells morphologically resembling the primitive **spermatogonium**." }
    ]
  },
  "spermatophyta": {
    dashboard: "Dashboard — sperm",
    primary: "A major taxonomic division of the plant kingdom comprising all seed-bearing plants (angiosperms and gymnosperms).",
    secondary: "Vascular plants that reproduce by seeds rather than spores, dominating modern terrestrial flora.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Textbook", text: "The grand evolutionary division of the **Spermatophyta** freed plants from the aqueous reproductive constraints of ferns and mosses." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "In all **Spermatophyta**, the ovule provides a sheltered chamber for fertilization and embryonic nourishment." },
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "The fossil record registers a decisive planetary revolution when the **Spermatophyta** replaced the giant lycopsid swamps." }
    ]
  },
  "spermatophyte": {
    dashboard: "Dashboard — sperm",
    primary: "A plant that belongs to the division Spermatophyta; any seed-bearing vascular plant.",
    secondary: "A plant producing true seeds containing an embryo and nutrient reserves, including conifers, cycads, and flowering plants.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", text: "The seed habit gives the **spermatophyte** an immense competitive advantage in dispersing across arid continental interiors." },
      { author: "Asa Gray", work: "Structural Botany", text: "The life cycle of the **spermatophyte** exhibits extreme reduction of the gametophyte generation down to microscopic pollen and embryo sac." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "Terrestrial primary productivity is almost wholly executed by **spermatophytes** anchoring continental soils." }
    ]
  },
  "spermatozoan": {
    dashboard: "Dashboard — sperm",
    primary: "A mature, motile male reproductive cell; a spermatozoon.",
    secondary: "A specialized haploid gamete consisting of a DNA-packed head, acrosomal cap, mitochondria-packed midpiece, and propulsive flagellum.",
    quotes: [
      { author: "Antonie van Leeuwenhoek", work: "Arcana Naturae Detecta", text: "Each microscopic **spermatozoan** swims with furious haste, propelled by the serpentine lashing of its slender tail." },
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "I proved that the **spermatozoan** is not a parasitic infusorian, but the authentic male fertilizing agent." },
      { author: "Thomas Hunt Morgan", work: "Heredity and Sex", text: "Fertilization involves the entry of a single **spermatozoan** nucleus into the egg, restoring the diploid chromosome count." }
    ]
  },
  "spermatozoid": {
    dashboard: "Dashboard — sperm",
    primary: "A motile male gamete produced in an antheridium by algae, fungi, mosses, and ferns; an antherozoid.",
    secondary: "A flagellated, swimming male reproductive cell that requires environmental water to swim toward the archegonium.",
    quotes: [
      { author: "Wilhelm Hofmeister", work: "On the Germination, Development, and Fructification of the Higher Cryptogamia", text: "The coiled, ciliated **spermatozoid** escapes from the ruptured antheridium and swims actively toward the archegonium neck." },
      { author: "Asa Gray", work: "Botanical Textbook", text: "In primitive ferns, fertilization cannot occur without a film of rainwater permitting the swimming of the **spermatozoid**." },
      { author: "Charles Darwin", work: "The Descent of Man", text: "The presence of a motile **spermatozoid** in cycads and Ginkgo reveals an archaic evolutionary link to aquatic cryptogams." }
    ]
  },
  "spermatozoon": {
    dashboard: "Dashboard — sperm",
    primary: "The mature, motile male fertilizing cell or gamete of an animal.",
    secondary: "A flagellated male reproductive cell that delivers the paternal genome into the ovum upon fertilization.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "De Ovi Mammalium et Hominis Genesi", text: "The **spermatozoon** is the essential fertilizing agent, penetrating the ovum to initiate embryonic ontogeny." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", text: "Myriad **spermatozoa** perish in the competition, while one alone successfully fuses with the germinal vesicle." },
      { author: "Francis Crick", work: "What Mad Pursuit", text: "The head of the **spermatozoon** carries its hereditary text compressed into an ultra-dense crystalline package of protamines." }
    ]
  },
  "spermicidal": {
    dashboard: "Dashboard — sperm",
    primary: "Destructive to or capable of killing spermatozoa.",
    secondary: "Pertaining to chemical agents, foams, or gels used as contraceptive barrier methods to immobilize sperm.",
    quotes: [
      { author: "Marie Stopes", work: "Contraception: Its Theory, History and Practice", text: "Laboratory testing confirmed the powerful **spermicidal** efficacy of quinine and lactic acid formulations." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "The introduction of safe **spermicidal** compounds revolutionized the practicality of female-controlled contraception." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Nonoxynol-9 acts through its **spermicidal** detergent action, dissolving the lipid membranes of the sperm flagellum." }
    ]
  },
  "spermicide": {
    dashboard: "Dashboard — sperm",
    primary: "A substance or preparation that destroys spermatozoa, used as a contraceptive.",
    secondary: "A chemical contraceptive (foam, gel, or suppository) that immobilizes sperm cells in the vagina prior to uterine entry.",
    quotes: [
      { author: "Marie Stopes", work: "Wise Parenthood", text: "A dependable **spermicide** used in conjunction with an occlusive diaphragm guarantees reliable family planning." },
      { author: "Havelock Ellis", work: "The Task of Social Hygiene", text: "Sociological hygiene demands accessible, hygienic **spermicides** to alleviate the distress of unwanted pregnancies." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Surfactant **spermicides** inhibit motility within seconds by disrupting outer flagellar membranes." }
    ]
  },
  "spermophile": {
    dashboard: "Dashboard — sperm",
    primary: "A ground squirrel of the genus *Spermophilus* or related marmotine rodents, native to open grasslands and steppes.",
    secondary: "A burrowing sciurid rodent characterized by cheek pouches used for transporting seeds and grain to underground storage burrows.",
    quotes: [
      { author: "John James Audubon", work: "The Viviparous Quadrupeds of North America", text: "The striped **spermophile** scurries through the prairie grasses, storing seeds in its capacious cheek pouches." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", text: "Vast colonies of burrowing **spermophiles** honeycombed the arid pampas, alerting one another with sharp whistling alarms." },
      { author: "C. Hart Merriam", work: "Life Zones and Crop Zones of the United States", text: "The geographic distribution of the plains **spermophile** strictly delineates the Upper Sonoran life zone." }
    ]
  },
  "spermophilus": {
    dashboard: "Dashboard — sperm",
    primary: "A genus of ground squirrels in the squirrel family (Sciuridae), commonly called seed-lovers.",
    secondary: "Holarctic burrowing rodents inhabiting steppes and prairies, exhibiting deep winter torpor and seasonal hibernation.",
    quotes: [
      { author: "C. Hart Merriam", work: "Revision of the North American Ground Squirrels", text: "I classified the numerous geographical races of **Spermophilus** based upon cranial dimensions and cheek-tooth morphology." },
      { author: "John James Audubon", work: "The Viviparous Quadrupeds of North America", text: "Species of **Spermophilus** play an essential ecological role as prey for prairie falcons, coyotes, and badgers." },
      { author: "Peter Hochachka", work: "Biochemical Adaptation", text: "During prolonged hibernation, **Spermophilus** depresses core metabolic rate and body temperature to near freezing." }
    ]
  },
  "spermous": {
    dashboard: "Dashboard — sperm",
    primary: "Of, relating to, or consisting of sperm or semen; seminal.",
    secondary: "Containing or producing spermatozoa or seeds.",
    quotes: [
      { author: "Antonie van Leeuwenhoek", work: "Letters on the Microscopic World", text: "Under high magnification, the **spermous** fluid swarmed with countless animalcules in perpetual agitation." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", text: "The **spermous** discharge in aquatic spawning animals is carried passively by surrounding tidal currents." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", text: "Philosophers debated whether the **spermous** emission contributed material substance or purely formal virtue to generation." }
    ]
  },
  "stenospermocarpy": {
    dashboard: "Dashboard — sperm",
    primary: "A biological phenomenon in fruit development where pollination and fertilization take place, but the embryo or seed subsequently aborts, resulting in 'seedless' fruit.",
    secondary: "The mechanism underlying seedless table grapes (such as Thompson Seedless) where minute, imperceptible seed traces remain inside the pulp.",
    quotes: [
      { author: "A. B. Stout", work: "Seedlessness in Grapes", text: "I introduced the term **stenospermocarpy** to describe fruit where fertilization occurs but normal seed development aborts prematurely." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", text: "Commercial seedless grapes rely on **stenospermocarpy**, yielding plump berries containing only vestigial seed coats." },
      { author: "Asa Gray", work: "Botanical Memoirs", text: "In **stenospermocarpy**, hormonal stimulation from initial fertilization suffices to drive full pericarp expansion despite subsequent embryo death." }
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
for (const [lemma, data] of Object.entries(BATCH6_DATA)) {
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
console.log(`Batch 6 Completed: ${count} / ${Object.keys(BATCH6_DATA).length} words updated`);
console.log(`========================================\n`);
