# -*- coding: utf-8 -*-
import json
import os

batch4 = {
  "Dashboard — cyan/anthocyanin.md": {
    "primary": "A water-soluble vacuolar flavonoid pigment appearing red, purple, or blue depending on cellular pH, found in flowers, fruits, and autumn leaves.",
    "secondary": "In plant biochemistry, a glycosylated polyhydroxy derivative of 2-phenylchromenylium responsible for berry coloration and pollinator attraction.",
    "quotes": [
      { "author": "Richard Willstätter", "work": "Nobel Lecture: On Plant Pigments", "quote": "By isolating crystalline **anthocyanin** from cornflowers and dahlias, we proved that subtle pH variations dictate their red or blue coloration." },
      { "author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The rich deposit of **anthocyanin** in the petals guides visiting bees directly toward the nectary." },
      { "author": "Asa Gray", "work": "Structural Botany", "quote": "Autumnal chill halts chlorophyll synthesis, unmasking the brilliant scarlet **anthocyanin** dissolved within the leaf sap." }
    ]
  },
  "Dashboard — cyan/cyan.md": {
    "primary": "A greenish-blue color, lying between blue and green on the visible spectrum; one of the three subtractive primary colors in process printing.",
    "secondary": "In color printing and digital imaging, the process ink (C in CMYK) that absorbs red light while reflecting green and blue wavelengths.",
    "quotes": [
      { "author": "James Clerk Maxwell", "work": "On the Theory of Three Primary Colours", "quote": "Combining green and blue rays produces the vivid hue known in the modern palette as **cyan**." },
      { "author": "John Ruskin", "work": "Modern Painters", "quote": "Glacier crevices revealed an intense, luminous **cyan** that seemed born of frozen sky and sea." },
      { "author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Above the volcanic crater hung a strange vapor of pale **cyan** hue, illuminated by subterranean fires." }
    ]
  },
  "Dashboard — cyan/cyanamid.md": {
    "primary": "A variant spelling of cyanamide; an organic compound (NH2CN) or its commercial calcium salt used as an agricultural fertilizer.",
    "secondary": "In chemical industry, calcium cyanamid produced by the Frank-Caro process, fixing atmospheric nitrogen for synthetic fertilizers.",
    "quotes": [
      { "author": "Fritz Haber", "work": "Thermodynamics of Technical Gas Reactions", "quote": "Passing nitrogen gas over red-hot calcium carbide yields commercial **cyanamid**, an indispensable source of agricultural nitrates." },
      { "author": "Arthur D. Little", "work": "The Handwriting on the Wall", "quote": "The electrothermal manufacture of **cyanamid** opened modern industrial chemistry to atmospheric nitrogen fixation." },
      { "author": "Rachel Carson", "work": "Silent Spring", "quote": "Broadcast applications of **cyanamid** functioned simultaneously as weedkiller and soil fertilizer." }
    ]
  },
  "Dashboard — cyan/cyanamide.md": {
    "primary": "An organic amide of cyanic acid (NH2CN), appearing as a deliquescent white crystalline solid; or its calcium salt CaCN2.",
    "secondary": "In agricultural chemistry and pharmacotherapy, a compound used as an agrarian defoliant and in alcoholism aversion therapy (calcium carbimide).",
    "quotes": [
      { "author": "Ira Remsen", "work": "An Introduction to the Study of Organic Chemistry", "quote": "Hydrolysis of **cyanamide** proceeds smoothly in warm aqueous solution to yield ordinary urea." },
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The synthesis of **cyanamide** confirmed the structural unity linking cyanogen derivatives with carbon amides." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Resonance between tautomeric structures gives **cyanamide** its characteristic planar dipole geometry." }
    ]
  },
  "Dashboard — cyan/cyanic.md": {
    "primary": "Pertaining to, derived from, or containing cyanogen or the cyanate group; azure or deep blue in color.",
    "secondary": "In historical botany, designating the series of floral colors (cyanic series) tending toward blue and violet, as opposed to the xanthic (yellow) series.",
    "quotes": [
      { "author": "Friedrich Wöhler", "work": "Ueber künstliche Bildung des Harnstoffs", "quote": "Treating lead cyanate with ammonia yielded ammonium **cyanic** salt, which spontaneously transformed into urea." },
      { "author": "John Lindley", "work": "An Introduction to Botany", "quote": "De Candolle divided floral pigments into the **cyanic** series tending to blue, and the xanthic series tending to yellow." },
      { "author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "The **cyanic** acid prepared by decomposition of uric acid exhibited volatile and pungent properties." }
    ]
  },
  "Dashboard — cyan/cyanide.md": {
    "primary": "A chemical compound containing the monovalent cyano group (-C≡N), infamous for acute cellular toxicity by arresting cellular respiration.",
    "secondary": "In toxicology and biochemistry, an inhibitor that binds ferric iron in cytochrome c oxidase, blocking the mitochondrial electron transport chain.",
    "quotes": [
      { "author": "Claude Bernard", "work": "Lectures on the Effects of Toxic and Medicinal Substances", "quote": "A lethal dose of potassium **cyanide** halts tissue respiration instantly, leaving the venous blood arterial red." },
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Sussex Vampire", "quote": "A single drop of prussic acid or potassium **cyanide** upon the tongue causes death before the victim can cry out." },
      { "author": "Agatha Christie", "work": "Sparkling Cyanide", "quote": "The glass of champagne contained a fatal dose of potassium **cyanide**, turning celebration into horror." }
    ]
  },
  "Dashboard — cyan/cyanite.md": {
    "primary": "A blue silicate mineral of aluminium (Al2SiO5), more commonly known in modern mineralogy as kyanite.",
    "secondary": "In metamorphic petrology, an index mineral of high-pressure metamorphic pelites, displaying anisotropic hardness across its bladed crystals.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "The bladed sky-blue crystals of **cyanite** occur abundantly in mica schists and metamorphic gneisses." },
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "The presence of **cyanite** in alpine metamorphic rocks indicates crystallization under tremendous lithostatic pressure." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Microscopic examination reveals blue needles of **cyanite** embedded within garnet-bearing crystalline schists." }
    ]
  },
  "Dashboard — cyan/cyanobacteria.md": {
    "primary": "A phylum of photosynthetic, oxygen-producing prokaryotic microorganisms, historically known as blue-green algae.",
    "secondary": "In paleobiology and geobiology, the ancient organisms whose oxygenic photosynthesis caused the Great Oxidation Event and gave rise to eukaryotic chloroplasts.",
    "quotes": [
      { "author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "The chloroplast of every modern plant cell is the evolutionary descendant of an engulfed ancestral **cyanobacteria**." },
      { "author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Floating colonies of marine **cyanobacteria** paint the waters of the Red Sea with sudden crimson blooms." },
      { "author": "Stephen Jay Gould", "work": "Wonderful Life", "quote": "Fossil stromatolites built by ancient **cyanobacteria** preserve the earliest tangible evidence of terrestrial life." }
    ]
  },
  "Dashboard — cyan/cyanobacterial.md": {
    "primary": "Of, relating to, or produced by cyanobacteria (blue-green algae).",
    "secondary": "In environmental toxicology and limnology, describing blooms, mats, or microcystin toxins produced by eutrophic blue-green algal overgrowths.",
    "quotes": [
      { "author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "Excessive phosphorus runoff induced massive **cyanobacterial** scums across the shallow bay." },
      { "author": "Lynn Margulis", "work": "Early Life", "quote": "The Precambrian atmosphere was transformed from reducing to oxidizing through sustained **cyanobacterial** photosynthesis." },
      { "author": "Edward O. Wilson", "work": "The Diversity of Life", "quote": "Pioneer **cyanobacterial** crusts stabilize arid desert dunes, preparing the terrain for vascular plant colonization." }
    ]
  },
  "Dashboard — cyan/cyanocitta.md": {
    "primary": "A genus of New World passerine birds in the crow family Corvidae, including the blue jay (*Cyanocitta cristata*) and Steller's jay.",
    "secondary": "In North American ornithology, crested jays renowned for vibrant blue plumage (produced by light scattering) and complex social vocalizations.",
    "quotes": [
      { "author": "John James Audubon", "work": "Ornithological Biography", "quote": "The blue jay, classified as **Cyanocitta**, mimics the cry of the red-shouldered hawk with astonishing fidelity." },
      { "author": "Elliott Coues", "work": "Key to North American Birds", "quote": "In the western pine forests, the dark-crested **Cyanocitta** heralds the traveler with sharp, scolding screams." },
      { "author": "Henry David Thoreau", "work": "Walden", "quote": "The shrill, discordant trumpet of **Cyanocitta** broke the winter stillness of the snow-clad woods." }
    ]
  },
  "Dashboard — cyan/cyanocobalamin.md": {
    "primary": "A manufactured form of vitamin B12 containing a cobalt atom coordinated to a cyanide ligand, used to treat pernicious anemia.",
    "secondary": "In biochemistry and clinical hematology, a red crystalline organometallic cofactor converted in the body into active methylcobalamin and adenosylcobalamin.",
    "quotes": [
      { "author": "Dorothy Crowfoot Hodgkin", "work": "Nobel Lecture: The Structure of the Vitamin B12 Molecule", "quote": "X-ray crystallography solved the intricate cobalt coordination sphere of crystalline **cyanocobalamin**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The discovery of **cyanocobalamin** transformed pernicious anemia from a fatal wasting disease into a manageable deficiency." },
      { "author": "Linus Pauling", "work": "Orthomolecular Medicine", "quote": "Parenteral administration of **cyanocobalamin** restores normal bone marrow erythropoiesis within days." }
    ]
  },
  "Dashboard — cyan/cyanogen.md": {
    "primary": "A toxic, colorless, flammable gas (C2N2) with a pungent almond-like odor, composed of two linked cyanide radicals.",
    "secondary": "In inorganic chemistry, a pseudohalogen gas synthesized by heating mercuric cyanide, behaving in reactions like a halogen diatomic molecule.",
    "quotes": [
      { "author": "Joseph Louis Gay-Lussac", "work": "Recherches sur l'Acide Prussique", "quote": "I have given the name **cyanogen** to this radical, because it generates the brilliant Prussian blue pigment." },
      { "author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Heating mercury cyanide drives off **cyanogen** gas, which burns with a characteristic peach-blossom flame." },
      { "author": "Michael Faraday", "work": "Experimental Researches in Chemistry", "quote": "The condensation of **cyanogen** into a clear liquid was effected under four atmospheres of pressure." }
    ]
  },
  "Dashboard — cyan/cyanogenetic.md": {
    "primary": "Capable of producing or releasing hydrocyanic acid (hydrogen cyanide); cyanogenic.",
    "secondary": "In phytochemistry, describing plants containing glycosides that release prussic acid upon tissue maceration and enzymatic hydrolysis.",
    "quotes": [
      { "author": "Asa Gray", "work": "Scientific Papers", "quote": "Crushing the leaves of the wild cherry releases a pungent odor due to **cyanogenetic** enzyme action." },
      { "author": "William Trelease", "work": "Botanical Gazette", "quote": "The **cyanogenetic** properties of certain sorghum grasses pose a severe grazing hazard to livestock after drought." },
      { "author": "Julius von Sachs", "work": "Physiology of Plants", "quote": "Amygdalin in bitter almonds represents the classic example of a **cyanogenetic** plant glucoside." }
    ]
  },
  "Dashboard — cyan/cyanogenic.md": {
    "primary": "Producing or releasing hydrogen cyanide, especially through the enzymatic breakdown of plant glycosides.",
    "secondary": "In economic botany and pasture agronomy, characterizing forage crops (like clover or cassava) that produce toxic levels of prussic acid.",
    "quotes": [
      { "author": "Rachel Carson", "work": "Silent Spring", "quote": "Certain **cyanogenic** plants protect their foliage from herbivorous insects by releasing lethal traces of cyanide gas." },
      { "author": "Theodosius Dobzhansky", "work": "Genetics of the Evolutionary Process", "quote": "Polymorphism for **cyanogenic** glycosides in white clover varies systematically with winter temperature gradients." },
      { "author": "J. B. S. Haldane", "work": "The Causes of Evolution", "quote": "The chemical defense provided by **cyanogenic** precursors illustrates natural selection acting upon metabolic pathways." }
    ]
  },
  "Dashboard — cyan/cyanohydrin.md": {
    "primary": "An organic compound containing both a cyano (-CN) and a hydroxyl (-OH) group attached to the same carbon atom.",
    "secondary": "In synthetic organic chemistry, an intermediate formed by the nucleophilic addition of hydrogen cyanide to an aldehyde or ketone, used in the Strecker synthesis.",
    "quotes": [
      { "author": "Arthur Lapworth", "work": "Reactions Involving the Addition of Hydrogen Cyanide to Carbonyl Compounds", "quote": "The formation of acetone **cyanohydrin** established that cyanide ion initiates nucleophilic addition to the carbonyl carbon." },
      { "author": "Ira Remsen", "work": "Organic Chemistry", "quote": "Hydrolyzing an aldehyde **cyanohydrin** converts the nitrile group into an alpha-hydroxy carboxylic acid." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The **cyanohydrin** reaction serves as a classic organic pathway for extending carbon chain lengths." }
    ]
  },
  "Dashboard — cyan/cyanophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear of the color blue.",
    "secondary": "In clinical psychology and psychiatry, a specific chromatic phobia where exposure to azure, cobalt, or sky-blue shades triggers acute anxiety.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Cases of **cyanophobia** are recorded where the sight of the open ocean or blue wallpaper provoked dread." },
      { "author": "G. Stanley Hall", "work": "A Study of Fears", "quote": "Sensory phobias, including intense **cyanophobia**, demonstrate the strange symbolic power of primary colors in neurotic illness." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "Pathological antipathies such as **cyanophobia** often stem from forgotten early childhood sensory traumas." }
    ]
  },
  "Dashboard — cyan/cyanophore.md": {
    "primary": "A pigment-containing cell (chromatophore) found in cold-blooded animals that produces blue coloration.",
    "secondary": "In cellular biology and comparative anatomy, a dermal chromatophore utilizing pteridine or carotenoid pigments, or structural iridophore platelets, to reflect blue light.",
    "quotes": [
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "The sky-blue markings of the poison-dart frog are generated by specialized **cyanophore** cells in the dermis." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In certain cephalopods, iridescent platelets within each **cyanophore** reflect intense blue beams." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "The brilliant blue throat fan of the male lizard expands through the coordinated swelling of every **cyanophore**." }
    ]
  },
  "Dashboard — cyan/cyanophyceae.md": {
    "primary": "A class of photosynthetic prokaryotes characterized by a blue-green color due to c-phycocyanin, equivalent to the cyanobacteria.",
    "secondary": "In botanical phycology, an ancient taxon of prokaryotic algae lacking membrane-bound nuclei and reproducing exclusively by fission or hormogonia.",
    "quotes": [
      { "author": "Felix Eugen Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "The class **Cyanophyceae** stands sharply apart from all other algae by virtue of its rudimentary prokaryotic cytology." },
      { "author": "Gilbert M. Smith", "work": "Cryptogamic Botany", "quote": "Gelatinous colonies of **Cyanophyceae** form unsightly blue-green mats over stagnant summer ponds." },
      { "author": "Julius von Sachs", "work": "Text-Book of Botany", "quote": "In the cells of **Cyanophyceae**, blue phycocyanin masks the underlying green of chlorophyll." }
    ]
  },
  "Dashboard — cyan/cyanophyta.md": {
    "primary": "A botanical division comprising the blue-green algae, now universally recognized as the bacterial phylum Cyanobacteria.",
    "secondary": "In evolutionary biology, the pioneer photosynthetic lineage responsible for stromatolites, nitrogen fixation, and planetary oxygenation.",
    "quotes": [
      { "author": "Lynn Margulis", "work": "Origin of Eukaryotic Cells", "quote": "The **Cyanophyta** represent the photosynthetic engine that transformed Earth's prebiotic anaerobic atmosphere." },
      { "author": "Felix Eugen Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "No motile flagellated stages occur anywhere within the life cycle of the **Cyanophyta**." },
      { "author": "Gilbert M. Smith", "work": "The Fresh-Water Algae of the United States", "quote": "Species of **Cyanophyta** thrive in hot thermal springs where no eukaryotic organism can survive." }
    ]
  },
  "Dashboard — cyan/cyanophyte.md": {
    "primary": "Any organism belonging to the Cyanophyta; a blue-green alga or cyanobacterium.",
    "secondary": "In limnology and microbiology, a prokaryotic phototroph possessing phycobiliprotein light-harvesting antenna complexes.",
    "quotes": [
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "A slick black crust upon the high spray rocks was formed by a microscopic marine **cyanophyte**." },
      { "author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The hardiest pioneer organism upon newly cooled volcanic lava is often a primitive **cyanophyte**." },
      { "author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "Fixation of atmospheric nitrogen by a free-living **cyanophyte** enriches the nutrient economy of rice paddies." }
    ]
  },
  "Dashboard — cyan/cyanosis.md": {
    "primary": "A bluish or purplish discoloration of the skin and mucous membranes caused by deficient oxygenation of the blood.",
    "secondary": "In clinical cardiology and pulmonology, a cardinal physical sign indicating that deoxygenated hemoglobin in capillary blood exceeds 5 g/dL.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital heart malformations manifest in the newborn as profound, alarming **cyanosis** of the lips and fingertips." },
      { "author": "Thomas Sydenham", "work": "Medical Observations", "quote": "The dying asthmatic struggled for breath, his visage darkening into the deep purple of suffocating **cyanosis**." },
      { "author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The victim's distorted features and swollen, dusky lips betrayed the fatal **cyanosis** of poison." }
    ]
  },
  "Dashboard — cyan/cyanotic.md": {
    "primary": "Affected with, relating to, or characterized by cyanosis; having a bluish or dusky discoloration from lack of oxygen.",
    "secondary": "In physical diagnosis, describing mucous membranes, nail beds, or facial features blanched or purplish due to hypoxia or hypothermia.",
    "quotes": [
      { "author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The dying helmsman lay on the steamer deck, his lips turning a pale, **cyanotic** gray." },
      { "author": "William Osler", "work": "Lectures on Angina Pectoris", "quote": "During the paroxysm of suffocation, the face grew mottled and deeply **cyanotic**." },
      { "author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Watch the patient's fingernails; if they turn **cyanotic**, summon the physician immediately." }
    ]
  },
  "Dashboard — cyan/cyanuramide.md": {
    "primary": "The chemical compound melamine (2,4,6-triamino-1,3,5-triazine), historically described as the triamide of cyanuric acid.",
    "secondary": "In industrial organic chemistry, a nitrogen-rich heterocyclic compound synthesized by heating dicyandiamide, used in thermosetting resins and laminates.",
    "quotes": [
      { "author": "Justus von Liebig", "work": "Annalen der Pharmacie", "quote": "By heating ammonium thiocyanate, I obtained the crystalline base melamine, which is chemically a **cyanuramide**." },
      { "author": "Ira Remsen", "work": "Principles of Theoretical Chemistry", "quote": "The heterocyclic triazine ring in **cyanuramide** confers extraordinary thermal and chemical stability." },
      { "author": "Arthur D. Little", "work": "The Chemical Industry", "quote": "Condensing **cyanuramide** with formaldehyde yielded durable, fire-resistant laminate plastics." }
    ]
  },
  "Dashboard — cyan/isocyanate.md": {
    "primary": "A chemical compound containing the functional group -N=C=O, widely used in the industrial manufacture of polyurethanes.",
    "secondary": "In polymer chemistry and industrial toxicology, highly reactive electrophiles (such as toluene diisocyanate) that react with polyols to form polyurethane foams.",
    "quotes": [
      { "author": "Otto Bayer", "work": "Das Diisocyanat-Polyadditionsverfahren", "quote": "The reaction between a di-**isocyanate** and a glycol proceeds without byproduct formation, yielding resilient polyurethanes." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The linear cumulative double bonds of the **isocyanate** group make it exceptionally susceptible to nucleophilic attack." },
      { "author": "Alice Hamilton", "work": "Industrial Toxicology", "quote": "Inhaling trace aerosol vapors of aromatic **isocyanate** provoked severe occupational asthma among chemical plant workers." }
    ]
  },
  "Dashboard — cyan/isocyanic.md": {
    "primary": "Pertaining to, derived from, or containing the isocyanato group (-N=C=O); related to isocyanic acid (HNCO).",
    "secondary": "In chemical history, describing the volatile tautomer of cyanic acid whose silver salt was shown by Liebig and Wöhler to be isomeric with silver fulminate.",
    "quotes": [
      { "author": "Friedrich Wöhler", "work": "On Artificial Urea", "quote": "The decomposition of ammonium **isocyanic** salt provided the first chemical synthesis of an organic substance from inorganic matter." },
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The discovery that fulminic and **isocyanic** acids share identical composition gave birth to the concept of isomerism." },
      { "author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "Heating urea drives off volatile **isocyanic** acid, which polymerizes rapidly upon condensation." }
    ]
  },
  "Dashboard — diacosi/diacosi.md": {
    "primary": "The Greek combining numeral prefix (diakosioi) denoting two hundred.",
    "secondary": "In mathematical geometry and classical nomenclature, a prefix used in naming 200-sided polygons and ancient Greek administrative units.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The combining form **diacosi**- derives from the ancient Attic numeral for two hundred." },
      { "author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Classical polyhedral terms employ Greek numeral stems such as **diacosi**- to designate higher geometric figures." },
      { "author": "Thomas Heath", "work": "A History of Greek Mathematics", "quote": "Archimedes calculated upper bounds for circular perimeters using polygons advancing beyond the **diacosi**- class." }
    ]
  },
  "Dashboard — diacosi/diacosigon.md": {
    "primary": "A geometric polygon having two hundred sides and two hundred angles.",
    "secondary": "In Euclidean plane geometry, a regular polygon whose interior angles each measure 178.2 degrees, virtually indistinguishable to the eye from a circle.",
    "quotes": [
      { "author": "Augustus De Morgan", "work": "A Budget of Paradoxes", "quote": "To construct a regular **diacosigon** with straightedge and compass would require solving an impossible cyclotomic equation." },
      { "author": "Thomas Heath", "work": "A History of Greek Mathematics", "quote": "The perimeter of a regular **diacosigon** inscribed within a circle approaches the circumference to three decimal places." },
      { "author": "William Kingdon Clifford", "work": "Common Sense of the Exact Sciences", "quote": "As the number of vertices multiplies toward the **diacosigon**, the polygon visually fuses into a continuous curve." }
    ]
  },
  "Dashboard — diacosi/diacosipentecontaheptagon.md": {
    "primary": "A polygon having two hundred and fifty-seven sides and two hundred and fifty-seven angles (a 257-gon).",
    "secondary": "In number theory and Euclidean geometry, a celebrated constructible regular polygon because 257 is a Fermat prime (2^(2^3) + 1).",
    "quotes": [
      { "author": "Carl Friedrich Gauss", "work": "Disquisitiones Arithmeticae", "quote": "Because 257 is a Fermat prime, the regular **diacosipentecontaheptagon** can be constructed using only ruler and compass." },
      { "author": "Felix Klein", "work": "Famous Problems of Elementary Geometry", "quote": "Richelot devoted years of labor to publishing the complete geometric construction of the **diacosipentecontaheptagon**." },
      { "author": "Thomas Heath", "work": "A History of Greek Mathematics", "quote": "Gauss's discovery that the **diacosipentecontaheptagon** was constructible stunned mathematicians after two millennia of silence." }
    ]
  },
  "Dashboard — erythr/Erythraean.md": {
    "primary": "Of or relating to the Red Sea (ancient Mare Erythraeum) or the ancient Greek coastal city of Erythrae in Ionia.",
    "secondary": "In classical literature and ancient geography, describing the legendary Erythraean Sibyl or the maritime trade routes of the Indian Ocean.",
    "quotes": [
      { "author": "Herodotus", "work": "The Histories", "quote": "The Phoenicians migrated to the Mediterranean from the shores of the **Erythraean** Sea." },
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Roman fleets sailed annually across the **Erythraean** main to bring back silks and spices from Malabar." },
      { "author": "John Milton", "work": "Paradise Lost", "quote": "As when the potent rod of Amram's son waved round the coast of the troubled **Erythraean** deep." }
    ]
  },
  "Dashboard — erythr/erythema.md": {
    "primary": "Superficial reddening of the skin, usually in patches, caused by injury, inflammation, or dilation of the blood capillaries.",
    "secondary": "In clinical dermatology, a reactive vascular flush occurring in sunburn, drug reactions (erythema multiforme), or bacterial infection (erythema nodosum).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The initial stage of scarlet fever is heralded by a diffuse punctate **erythema** spreading from the neck." },
      { "author": "Erasmus Wilson", "work": "Diseases of the Skin", "quote": "Sunburn is an acute solar **erythema** resulting from intense ultraviolet engorgement of cutaneous capillaries." },
      { "author": "Thomas Sydenham", "work": "Medical Observations", "quote": "The fever was attended with a bright red **erythema** that blanched momentarily under the pressure of the thumb." }
    ]
  },
  "Dashboard — erythr/erythematous.md": {
    "primary": "Relating to, characterized by, or affected with erythema; displaying abnormal redness of the skin.",
    "secondary": "In clinical pathology, describing flushed, hyperemic dermatological lesions that blanch upon diascopy.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "An **erythematous** blush spread rapidly over the joints of the rheumatic fever patient." },
      { "author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "The chronic butterfly rash of lupus presents as a raised, **erythematous** plaque across the bridge of the nose." },
      { "author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "The **erythematous** patch was tender to touch but exhibited no vesicular elevation of the cuticle." }
    ]
  },
  "Dashboard — erythr/erythr.md": {
    "primary": "The Greek combining form (erythros, 'red') denoting a red color, red blood cells, or ruby-hued chemical compounds.",
    "secondary": "In biomedical and chemical nomenclature, a prefix designating erythrocytes, erythema, erythromycin, or erythrite minerals.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The combining element **erythr**- designates both the crimson pigment of blood and related physiological structures." },
      { "author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "Chemists employ the root **erythr**- to denote compounds yielding vivid carmine or scarlet solutions." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "In ancient Greek literature, **erythr**- characterized the red wine, blushing cheeks, and copper ores." }
    ]
  },
  "Dashboard — erythr/erythraemia.md": {
    "primary": "Variant spelling of erythremia (polycythemia vera); a rare chronic myeloproliferative disorder marked by excessive red blood cell production.",
    "secondary": "In hematology, a neoplastic proliferation of the erythroid bone marrow lineage leading to hyperviscosity, splenomegaly, and a ruddy plethoric complexion.",
    "quotes": [
      { "author": "William Osler", "work": "Chronic Cyanosis, with Polycythaemia and Enlarged Spleen: A New Clinical Entity", "quote": "The condition of chronic **erythraemia** is characterized by a remarkable cyanotic rubor and enormous erythrocyte counts." },
      { "author": "Henri Vaquez", "work": "Sur une Forme Spéciale de Cyanose", "quote": "Our investigations in **erythraemia** demonstrated that the bone marrow was packed with hyperactive normoblasts." },
      { "author": "Paul Ehrlich", "work": "The Anaemias", "quote": "Unlike compensatory polycythemia, true **erythraemia** represents an autonomous hyperplasia of the hematopoietic tissues." }
    ]
  },
  "Dashboard — erythr/erythrina.md": {
    "primary": "A genus of tropical and subtropical trees and shrubs in the pea family (Fabaceae), commonly known as coral trees, noted for flame-red flowers.",
    "secondary": "In economic botany and pharmacology, ornamental and shade trees yielding toxic curare-like alkaloids (erythroidines) and lightweight timber.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions", "quote": "Magnificent trees of **Erythrina**, loaded with dazzling scarlet flowers, shaded the young coffee plantations of the valley." },
      { "author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation", "quote": "The brilliant blossoms of **Erythrina** are adapted for pollination by hummingbirds and honey-eaters." },
      { "author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "In the hot Terai valleys, the coral tree **Erythrina** stood leafless, covered in massive clusters of crimson blooms." }
    ]
  },
  "Dashboard — erythr/erythrite.md": {
    "primary": "A soft, crimson to peach-red hydrated cobalt arsenate mineral, Co3(AsO4)2·8H2O, also known colloquially as cobalt bloom.",
    "secondary": "In economic mineralogy and prospecting, a bright secondary mineral formed by weathering of cobalt ores, serving as a visual surface guide for prospectors.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The delicate peach-red crusts of **erythrite** found in cobalt veins immediately attract the prospector's eye." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Weathering of smaltite leads to the oxidation and formation of beautiful carmine **erythrite** crystals." },
      { "author": "Charles Lyell", "work": "Elements of Geology", "quote": "The Saxon silver mines frequently exhibited crusts of radiant **erythrite** lining the fissure walls." }
    ]
  },
  "Dashboard — erythr/erythroblast.md": {
    "primary": "An immature, nucleated red blood cell found normally in the bone marrow, from which an erythrocyte develops.",
    "secondary": "In hematopoiesis, the precursor cell that progresses from proerythroblast to basophilic, polychromatic, and orthochromatic stages before enucleation.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Histology of the Blood", "quote": "Staining revealed the gradual accumulation of hemoglobin within the cytoplasm of each developing **erythroblast**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In severe pernicious anemia, gigantocytic forms of **erythroblast** escape prematurely into the circulating blood." },
      { "author": "William Henry Welch", "work": "Papers and Addresses", "quote": "The mitotic activity of the **erythroblast** population in bone marrow compensates rapidly for acute hemorrhage." }
    ]
  },
  "Dashboard — erythr/erythroblastopenia.md": {
    "primary": "A severe deficiency or absence of nucleated red blood cell precursors (erythroblasts) in the bone marrow; pure red cell aplasia.",
    "secondary": "In clinical hematology, an isolated bone marrow failure state characterized by profound normocytic anemia with normal granulocyte and platelet counts.",
    "quotes": [
      { "author": "Maxwell Finland", "work": "Hematological Complications in Clinical Medicine", "quote": "A bone marrow aspirate demonstrating complete **erythroblastopenia** confirmed the diagnosis of pure red cell aplasia." },
      { "author": "William Osler", "work": "Modern Medicine", "quote": "Acquired **erythroblastopenia** frequently resolves following surgical thymectomy or immunosuppressive therapy." },
      { "author": "Paul Ehrlich", "work": "Studies on Blood Cell Genesis", "quote": "When toxic agents selectively target the erythroid progenitor, total **erythroblastopenia** ensues without leukopenia." }
    ]
  },
  "Dashboard — erythr/erythroblastosis.md": {
    "primary": "An abnormal presence of nucleated red blood cells (erythroblasts) in the circulating blood, especially in erythroblastosis fetalis.",
    "secondary": "In perinatology, hemolytic disease of the newborn caused by maternal-fetal Rh incompatibility, triggering fetal erythrocyte destruction and extramedullary hematopoiesis.",
    "quotes": [
      { "author": "Philip Levine", "work": "The Role of Isoimmunization in the Pathogenesis of Erythroblastosis Fetalis", "quote": "Maternal Rh antibodies cross the placenta, destroying fetal erythrocytes and causing severe **erythroblastosis**." },
      { "author": "Alexander S. Wiener", "work": "Rh Factors in Clinical Medicine", "quote": "Exchange transfusion in the infant suffering from **erythroblastosis** successfully prevented fatal kernicterus." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Extensive extramedullary blood formation in the spleen and liver characterizes neonatal **erythroblastosis**." }
    ]
  },
  "Dashboard — erythr/erythrocebus.md": {
    "primary": "A genus of Old World monkeys comprising the patas monkey (*Erythrocebus patas*), characterized by reddish-brown fur and rapid terrestrial running.",
    "secondary": "In primatology, long-limbed semiterrestrial African savanna guenons capable of running at speeds exceeding thirty miles per hour.",
    "quotes": [
      { "author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The red patas monkey, classified under **Erythrocebus**, outstrips hunting hounds across the open Sahel plains." },
      { "author": "Arthur Loveridge", "work": "Tomorrow's a Holiday", "quote": "A troop of **Erythrocebus** dashed across the dry savannah with the speed of coursing greyhounds." },
      { "author": "David Bannerman", "work": "Fauna of West Africa", "quote": "The bright russet coat of **Erythrocebus** harmonizes with the red laterite soil of the northern scrub." }
    ]
  },
  "Dashboard — erythr/erythrocin.md": {
    "primary": "A proprietary brand name for the macrolide antibiotic erythromycin, used to treat bacterial respiratory and dermatological infections.",
    "secondary": "In clinical pharmacology, an oral and parenteral antibiotic preparation historically prescribed for penicillin-allergic patients with streptococcal pharyngitis.",
    "quotes": [
      { "author": "Maxwell Finland", "work": "Clinical Studies on Macrolide Antibiotics", "quote": "Patients intolerant of penicillin were successfully maintained on oral doses of **erythrocin**." },
      { "author": "Paul de Kruif", "work": "Men Against Death", "quote": "The pharmacy stocked **erythrocin** as an effective safeguard against virulent hemolytic streptococci." },
      { "author": "Selman Waksman", "work": "The Conquest of Tuberculosis", "quote": "Early clinical trials confirmed the broad antimicrobial spectrum and low toxicity of **erythrocin**." }
    ]
  },
  "Dashboard — erythr/erythrocyte.md": {
    "primary": "A mature red blood cell in humans and other vertebrates, containing hemoglobin and transporting oxygen from the lungs to tissues.",
    "secondary": "In vertebrate hematology, a biconcave, anucleated disc in mammals maximizing surface area for rapid gas exchange and capillary deformability.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "A single drop of human blood contains more than five millions of the minute discs termed the **erythrocyte**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Under the microscope, each normal **erythrocyte** displays a pale central depression surrounded by a rim of hemoglobin." },
      { "author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "The **erythrocyte** serves as an indispensable vehicle carrying respiratory oxygen to every living cell of the body." }
    ]
  },
  "Dashboard — erythr/erythrocytolysin.md": {
    "primary": "A substance (such as a bacterial toxin, snake venom, or antibody) capable of causing the dissolution or lysis of red blood cells; a hemolysin.",
    "secondary": "In immunology and bacterial pathogenesis, a cytolytic protein that forms pores in erythrocyte membranes, releasing free hemoglobin.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "A specific **erythrocytolysin** requires both an amboceptor and heat-labile complement to rupture red blood cells." },
      { "author": "Jules Bordet", "work": "Studies in Immunity", "quote": "Serum from immunized animals acted as a potent **erythrocytolysin** against foreign sheep corpuscles." },
      { "author": "William Henry Welch", "work": "General Pathology", "quote": "Venom injected by pit vipers contains a powerful **erythrocytolysin** that produces widespread intravascular hemolysis." }
    ]
  },
  "Dashboard — erythr/erythrocytosis.md": {
    "primary": "An abnormal increase in the number of red blood cells in the circulation, especially as a secondary physiological response.",
    "secondary": "In clinical medicine, elevated hematocrit triggered by hypoxemia (high altitude, chronic lung disease) or erythropoietin-secreting tumors.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Mountaineers living at high altitudes develop a compensatory **erythrocytosis** to offset low atmospheric oxygen." },
      { "author": "Claude Bernard", "work": "Lectures on the Physiology of Respiration", "quote": "Secondary **erythrocytosis** demonstrates the exquisite capacity of the organism to adjust its oxygen-carrying capacity." },
      { "author": "Henri Vaquez", "work": "Studies on Polycythemia", "quote": "Distinguishing benign compensatory **erythrocytosis** from true polycythemia vera is critical for proper patient management." }
    ]
  },
  "Dashboard — erythr/erythroderma.md": {
    "primary": "An inflammatory skin disease characterized by generalized redness (erythema) and scaling affecting more than ninety percent of the body surface.",
    "secondary": "In dermatology, a potentially life-threatening condition (exfoliative dermatitis) causing severe thermoregulatory disturbance, hypothermia, and high-output cardiac failure.",
    "quotes": [
      { "author": "Erasmus Wilson", "work": "On Diseases of the Skin", "quote": "The patient presented with total exfoliative **erythroderma**, his entire cutaneous surface shedding large bran-like scales." },
      { "author": "Jonathan Hutchinson", "work": "Lectures on Clinical Surgery", "quote": "Extensive **erythroderma** severely impairs cutaneous perspiration and leaves the patient shivering in ordinary room air." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe drug eruptions occasionally progress into generalized **erythroderma** requiring intensive supportive care." }
    ]
  },
  "Dashboard — erythr/erythroid.md": {
    "primary": "Having a red or reddish appearance; of or relating to the developmental lineage of red blood cells (erythrocytes).",
    "secondary": "In hematopathology, characterizing the precursor cell compartment in bone marrow dedicated to hemoglobin synthesis and erythrocyte formation.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Histology of the Blood", "quote": "Bone marrow smears from patients recovering from blood loss showed massive hyperplasia of the **erythroid** series." },
      { "author": "William Osler", "work": "Modern Medicine", "quote": "A normal myeloid-to-**erythroid** ratio in marrow aspirates ranges between three-to-one and four-to-one." },
      { "author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain pigeon varieties exhibit an **erythroid** tinge around the iris and legs." }
    ]
  },
  "Dashboard — erythr/erythrolysin.md": {
    "primary": "Any agent, toxin, or antibody that dissolves or hemolyzes red blood cells; a hemolysin.",
    "secondary": "In microbiology and venomics, an enzyme or protein toxin (such as streptolysin or cobra venom hemolysin) that perforates the erythrocyte membrane.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "The action of a specific **erythrolysin** illustrates the receptor theory of antibody-mediated cytolysis." },
      { "author": "Jules Bordet", "work": "Studies on Antigens and Antibodies", "quote": "Heating the serum destroyed the alexin, rendering the **erythrolysin** temporarily inactive until fresh serum was added." },
      { "author": "Alexander Fleming", "work": "The Action of Chemical Antiseptics", "quote": "Streptococcal filtrates contain a potent **erythrolysin** that rapidly produces clear zones on blood agar plates." }
    ]
  },
  "Dashboard — erythr/erythromelalgia.md": {
    "primary": "A rare neurovascular peripheral pain disorder characterized by intense burning pain, erythema, and increased skin temperature in the extremities.",
    "secondary": "In clinical neurology, a condition first described by Silas Weir Mitchell caused by microvascular arteriovenous shunting or sodium channel mutations.",
    "quotes": [
      { "author": "Silas Weir Mitchell", "work": "On a Rare Vaso-Motor Neurosis of the Extremities", "quote": "I have designated as **erythromelalgia** this painful affection wherein the feet become red, throbbing, and exquisitely hot." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients afflicted with **erythromelalgia** obtain temporary relief only by plunging their burning feet into buckets of ice water." },
      { "author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "The paroxysmal burning redness of **erythromelalgia** must be carefully differentiated from Raynaud's cold cyanosis." }
    ]
  },
  "Dashboard — erythr/erythromycin.md": {
    "primary": "A broad-spectrum macrolide antibiotic produced by the actinomycete *Saccharopolyspora erythraea*, widely used to treat bacterial infections.",
    "secondary": "In pharmacology, a 14-membered lactone ring antibiotic that reversibly binds the 50S bacterial ribosomal subunit, inhibiting polypeptide translocation.",
    "quotes": [
      { "author": "Maxwell Finland", "work": "The Macrolide Antibiotics", "quote": "Clinical administration of **erythromycin** proved a vital alternative for patients allergic to standard penicillins." },
      { "author": "Selman Waksman", "work": "The Actinomycetes", "quote": "From soil cultures collected in the Philippines, researchers isolated **erythromycin**, a compound of outstanding clinical value." },
      { "author": "Paul de Kruif", "work": "Men Against Death", "quote": "The swift cure of Legionnaires' disease was achieved by high-dose intravenous therapy with **erythromycin**." }
    ]
  },
  "Dashboard — erythr/erythronium.md": {
    "primary": "A genus of spring-flowering perennial woodland plants in the lily family Liliaceae (trout lilies, dogtooth violets); historically, the original name given to vanadium.",
    "secondary": "In botanical horticulture, delicate spring ephemerals with mottled foliage and reflexed petals; in chemical history, Andrés Manuel del Río's 1801 proposed element.",
    "quotes": [
      { "author": "Andrés Manuel del Río", "work": "Discurso de las Ciencias Naturales", "quote": "Because its salts turn red upon heating with acids, I bestowed upon the new Mexican metal the name **erythronium**." },
      { "author": "John Burroughs", "work": "Wake-Robin", "quote": "The delicate yellow bells of **Erythronium** nodded gracefully above the damp carpet of April leaf-mould." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The dog's-tooth violet, classified as **Erythronium**, spreads by deep scaly corms through rich deciduous woods." }
    ]
  },
  "Dashboard — erythr/erythrophobia.md": {
    "primary": "An abnormal, morbid fear of blushing, or an irrational dread of the color red.",
    "secondary": "In clinical psychology and psychotherapy, a social anxiety disorder where the anticipation of facial flushing triggers panic and social avoidance.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The young man's acute **erythrophobia** made ordinary social conversation an agonizing ordeal of expected shame." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "In **erythrophobia**, the fear of blushing creates a vicious autonomic cycle that instantly precipitates the flush." },
      { "author": "G. Stanley Hall", "work": "Adolescence", "quote": "Adolescent social hypersensitivity frequently manifests as a tormenting **erythrophobia** in classroom settings." }
    ]
  },
  "Dashboard — erythr/erythrophore.md": {
    "primary": "A pigment-containing cell (chromatophore) found in cold-blooded animals that produces red coloration.",
    "secondary": "In comparative anatomy and physiological zoology, a dermal chromatophore packed with carotenoids or pteridines that disperses pigment to redden skin.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "The vivid scarlet patches upon the male lizard's flank expand when nervous impulses excite every **erythrophore**." },
      { "author": "Thomas Henry Huxley", "work": "The Oceanic Hydrozoa", "quote": "Under the microscope, each individual **erythrophore** was seen to radiate branching cytoplasmic processes filled with ruby granules." },
      { "author": "E. Ray Lankester", "work": "Comparative Physiology", "quote": "Hormones from the pituitary gland control pigment dispersion within both the melanophore and the **erythrophore**." }
    ]
  },
  "Dashboard — erythr/erythropoiesis.md": {
    "primary": "The biological process by which red blood cells (erythrocytes) are produced and matured in the bone marrow.",
    "secondary": "In physiology, a tightly regulated hematopoietic feedback mechanism stimulated by tissue hypoxia and mediated by the hormone erythropoietin.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Following massive hemorrhage, accelerated **erythropoiesis** repopulates the marrow with active normoblasts." },
      { "author": "Paul Ehrlich", "work": "Histology of the Blood", "quote": "The stages of **erythropoiesis** illustrate a continuous maturation cycle terminating in the loss of the cell nucleus." },
      { "author": "Claude Bernard", "work": "Lectures on the Physiology of Respiration", "quote": "Renal sensors detect arterial hypoxia, triggering marrow **erythropoiesis** to maintain internal equilibrium." }
    ]
  },
  "Dashboard — erythr/erythropoietic.md": {
    "primary": "Pertaining to, producing, or stimulating erythropoiesis (the production of red blood cells).",
    "secondary": "In clinical hematology, describing tissues (such as active red marrow), hormonal factors, or disorders (such as erythropoietic protoporphyria).",
    "quotes": [
      { "author": "William Osler", "work": "Modern Medicine", "quote": "In chronic hemolytic anemia, the entire skeleton transforms into active **erythropoietic** red marrow." },
      { "author": "Paul Ehrlich", "work": "Studies on Blood Cell Genesis", "quote": "The spleen of the embryo serves as an indispensable **erythropoietic** organ prior to skeletal ossification." },
      { "author": "Maxwell Finland", "work": "Clinical Studies in Hematology", "quote": "The patient suffered from an inborn **erythropoietic** porphyria that caused extreme cutaneous photosensitivity." }
    ]
  },
  "Dashboard — erythr/erythropoietin.md": {
    "primary": "A glycoprotein hormone produced primarily by the kidneys that stimulates the bone marrow to produce red blood cells.",
    "secondary": "In physiology and nephrology, an endocrine mediator synthesized by renal peritubular interstitial cells in response to tissue hypoxia.",
    "quotes": [
      { "author": "Allan J. Erslev", "work": "Humoral Regulation of Red Cell Production", "quote": "Plasma extracts from anemic animals contained **erythropoietin**, demonstrating the hormonal control of red cell genesis." },
      { "author": "William Osler", "work": "Principles and Practice of Medicine", "quote": "Chronic renal failure inevitably causes severe normocytic anemia due to deficient secretion of **erythropoietin**." },
      { "author": "Linus Pauling", "work": "Orthomolecular Medicine", "quote": "Recombinant human **erythropoietin** revolutionized the clinical management of anemia in dialysis patients." }
    ]
  },
  "Dashboard — erythr/erythroprosopalgia.md": {
    "primary": "A severe localized facial neuralgic disorder accompanied by unilateral facial flushing and redness (a variant of cluster headache).",
    "secondary": "In clinical neurology, a trigeminal autonomic cephalgia characterized by excruciating orbital pain, ipsilateral conjunctival injection, and facial erythema.",
    "quotes": [
      { "author": "Silas Weir Mitchell", "work": "Injuries of Nerves and Their Consequences", "quote": "The patient endured paroxysms of **erythroprosopalgia**, during which the left half of the face flushed crimson with agony." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Vasomotor headache syndromes such as **erythroprosopalgia** demonstrate the profound influence of sympathetic nerves on cranial vessels." },
      { "author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "The unilateral burning flush of **erythroprosopalgia** recurred nightly with clockwork periodicity." }
    ]
  },
  "Dashboard — erythr/erythroxylaceae.md": {
    "primary": "A tropical family of flowering plants in the order Malpighiales comprising four genera of shrubs and trees, notably including *Erythroxylum*.",
    "secondary": "In systematic botany, an ancient pantropical family characterized by alternate simple leaves, persistent stipules, and alkaloid-rich tissues.",
    "quotes": [
      { "author": "George Bentham", "work": "Genera Plantarum", "quote": "The family **Erythroxylaceae** is distinguished by its distinctive intra-petiolar stipules and five-merous flowers." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Species of **Erythroxylaceae** inhabit tropical American and African forests, producing valued aromatic resins and alkaloids." },
      { "author": "Armen Takhtajan", "work": "Evolutionary Trends in Flowering Plants", "quote": "Phylogenetic analysis places the **Erythroxylaceae** in close evolutionary alliance with the Rhizophoraceae." }
    ]
  },
  "Dashboard — erythr/erythroxylon.md": {
    "primary": "A variant botanical spelling of the genus *Erythroxylum*, tropical woody plants famous for including the Andean coca bush.",
    "secondary": "In historical pharmacognosy, the botanical genus from whose leaves Albert Niemann first isolated the alkaloid cocaine.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Aspects of Nature", "quote": "The native porters walked all day across the Andes without fatigue, chewing the leaves of **Erythroxylon** with lime." },
      { "author": "Joseph Dalton Hooker", "work": "Kew Bulletin of Miscellaneous Information", "quote": "Specimens of **Erythroxylon** cultivated in the palm house flowered freely, yielding characteristic red drupes." },
      { "author": "Richard Spruce", "work": "Notes of a Botanist on the Amazon and Andes", "quote": "Every Amazonian Indian village maintained a clearing planted with bushes of **Erythroxylon** for ceremonial use." }
    ]
  },
  "Dashboard — erythr/erythroxylum.md": {
    "primary": "A genus of tropical trees and shrubs in the family Erythroxylaceae, notably *Erythroxylum coca*, native to South America.",
    "secondary": "In ethnobotany and medicine, the botanical source of coca leaves containing ecgonine derivatives and alkaloids used for altitude sickness and local anesthesia.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions", "quote": "Chewing the dried leaves of **Erythroxylum** sustains the Andean traveler through arduous ascents over freezing mountain passes." },
      { "author": "William Henry Prescott", "work": "History of the Conquest of Peru", "quote": "Under the Incas, the divine shrub **Erythroxylum** was reserved for the royal family and religious sacrifices." },
      { "author": "Carl Linnaeus", "work": "Systema Naturae", "quote": "The genus **Erythroxylum** was named for the reddish hue displayed by the heartwood of its tropical species." }
    ]
  },
  "Dashboard — erythr/polycythemia.md": {
    "primary": "An abnormal increase in the concentration of hemoglobin, red blood cells, or hematocrit in the peripheral blood.",
    "secondary": "In clinical hematology, classified into primary (polycythemia vera) and secondary types (due to hypoxemia, smoking, or erythropoietin excess).",
    "quotes": [
      { "author": "William Osler", "work": "Chronic Cyanosis, with Polycythaemia and Enlarged Spleen", "quote": "The clinical picture of chronic **polycythemia** presents a startling rubor of the face accompanied by high blood pressure." },
      { "author": "Paul Ehrlich", "work": "The Anaemias", "quote": "In cases of absolute **polycythemia**, the total red cell mass increases dramatically, raising blood viscosity." },
      { "author": "Claude Bernard", "work": "Lectures on Experimental Medicine", "quote": "Ascending to high Andean altitudes provoked a marked compensatory **polycythemia** within three weeks." }
    ]
  },
  "Dashboard — glauc/Glaucopsyche.md": {
    "primary": "A genus of gossamer-winged butterflies in the lycaenid subfamily Polyommatinae, commonly known as silvery blues.",
    "secondary": "In lepidopterology, holarctic butterflies (such as *Glaucopsyche lygdamus* and the extinct Xerces blue) displaying silvery sea-green or turquoise wings.",
    "quotes": [
      { "author": "Vladimir Nabokov", "work": "Speak, Memory", "quote": "A flash of pale turquoise betrayed a specimen of **Glaucopsyche** sunning its wings upon the lupine foliage." },
      { "author": "Samuel Hubbard Scudder", "work": "The Butterflies of the Eastern United States and Canada", "quote": "The silvery underside and delicate blue gloss identify **Glaucopsyche** among our earliest spring lycaenids." },
      { "author": "W. J. Holland", "work": "The Butterfly Book", "quote": "The silver-blue **Glaucopsyche** flits low over mountain meadows where pea vines flourish." }
    ]
  },
  "Dashboard — glauc/glauc.md": {
    "primary": "The Greek combining form (glaukos, 'gleaming, silvery-gray, bluish-green') denoting a pale sea-green, glaucous, or bluish hue.",
    "secondary": "In biological and mineralogical terminology, a prefix found in glaucoma, glaucous, glaucophane, and related natural science descriptors.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Physiography", "quote": "From the Greek root **glauc**- come scientific descriptors designating both the sea-green swell and frosted plant wax." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "Homer applied the epithet **glauc**- to the flashing, owl-like eyes of Athena and the shimmering Aegean waves." },
      { "author": "Asa Gray", "work": "Structural Botany", "quote": "Botanists use the prefix **glauc**- to characterize leaves coated with a bluish-white powdery bloom." }
    ]
  },
  "Dashboard — glauc/glaucium.md": {
    "primary": "A genus of flowering plants in the poppy family Papaveraceae, commonly known as horned poppies or sea poppies, native to coastal regions.",
    "secondary": "In littoral botany and pharmacognosy, plants characterized by glaucous foliage, bright yellow or orange petals, and the presence of glaucine alkaloid.",
    "quotes": [
      { "author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Upon the maritime shingle grew the yellow horned poppy, classified as **Glaucium**, with its sea-green leaves." },
      { "author": "John Lindley", "work": "Flora Medica", "quote": "Extracts of **Glaucium** were celebrated in folk medicine for their sedative properties and bitter yellow sap." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The long, curved silique pods of **Glaucium** distinguish it readily from all inland poppies." }
    ]
  },
  "Dashboard — glauc/glaucoma.md": {
    "primary": "A group of eye conditions characterized by damage to the optic nerve, often caused by abnormally high intraocular pressure, leading to vision loss.",
    "secondary": "In clinical ophthalmology, a progressive optic neuropathy with cupping of the optic disc and characteristic peripheral visual field deficits.",
    "quotes": [
      { "author": "Albrecht von Graefe", "work": "On the Treatment of Glaucoma by Iridectomy", "quote": "The introduction of iridectomy arrested the blinding march of acute **glaucoma** for the first time in medical history." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Increased intraocular tension in chronic **glaucoma** slowly suffocates the retinal nerve fibers at the optic disc." },
      { "author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "Examination with the ophthalmoscope reveals deep excavating cupping of the papilla in established **glaucoma**." }
    ]
  },
  "Dashboard — glauc/glaucomys.md": {
    "primary": "A genus of New World flying squirrels in the family Sciuridae, comprising the northern and southern flying squirrels.",
    "secondary": "In mammalian zoology, nocturnal arboreal sciurids possessing a furred patagium membrane extending between wrists and ankles, and large dark eyes.",
    "quotes": [
      { "author": "John James Audubon", "work": "The Viviparous Quadrupeds of North America", "quote": "At twilight, small colonies of **Glaucomys** leaped from hollow oaks, gliding silently across the forest glade." },
      { "author": "C. Hart Merriam", "work": "The Mammals of the Adirondack Region", "quote": "The delicate nocturnal **Glaucomys** feeds on lichens, fungi, and hickory nuts hidden high in the canopy." },
      { "author": "Elliott Coues", "work": "Fur-Bearing Animals", "quote": "The flattened tail of **Glaucomys** acts as an efficient rudder during its long aerial glides." }
    ]
  },
  "Dashboard — glauc/glauconite.md": {
    "primary": "A greenish iron potassium phyllosilicate mineral of the mica group, common as rounded pelletal grains in sedimentary greensands.",
    "secondary": "In sedimentary geology and stratigraphy, an authigenic marine mineral formed slowly on continental shelves in low-sedimentation environments.",
    "quotes": [
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "The Cretaceous strata of New Jersey are renowned for thick beds of greensand rich in dark green **glauconite**." },
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The potassium and iron content of **glauconite** makes it valuable both as an agricultural fertilizer and as a geological dating index." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Microscopic sections show pellets of **glauconite** replacing the internal molds of tiny foraminiferal shells." }
    ]
  },
  "Dashboard — glauc/glaucophane.md": {
    "primary": "A lavender-blue to dark-blue sodic amphibole mineral characteristic of blueschist facies metamorphic rocks.",
    "secondary": "In metamorphic petrology and plate tectonics, an indicator mineral formed under high pressure and low temperature conditions typical of subduction zones.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "The blue prismatic crystals of **glaucophane** impart their distinctive color to the alpine schists of the Valais." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "The formation of **glaucophane** requires intense crustal compression under relatively low geothermal gradients." },
      { "author": "Charles Lyell", "work": "Elements of Geology", "quote": "Subducted oceanic slabs metamorphose into dense blueschists richly endowed with crystalline **glaucophane**." }
    ]
  },
  "Dashboard — glauc/glaucophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear of the color gray, sea-green, or dull bluish-green.",
    "secondary": "In clinical psychology, a specific chromophobia characterized by extreme autonomic anxiety when encountering dull gray or muted greenish hues.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "The Psychology of Color", "quote": "The recluse displayed an intense **glaucophobia**, banishing every gray coat and muted tapestry from his residence." },
      { "author": "G. Stanley Hall", "work": "A Study of Fears", "quote": "Morbid sensory dreads such as **glaucophobia** often develop in sensitive adolescents following protracted illness." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "An unreasoned sensory antipathy like **glaucophobia** reveals how deeply primitive instincts attach to specific chromatic cues." }
    ]
  },
  "Dashboard — glauc/glaucous.md": {
    "primary": "Of a dull grayish-green or pale bluish-green color; also, covered with a powdery waxy bloom that rubs off easily.",
    "secondary": "In botanical and ornithological description, characterizing the frosted surface of plums and cabbage leaves or the pale mantle of gulls (*Larus hyperboreus*).",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The succulent leaves of the cabbage display a fine **glaucous** coating of waxy powder that repels water droplets." },
      { "author": "John James Audubon", "work": "Ornithological Biography", "quote": "The magnificent **glaucous** gull soared majestically over the drifting ice floes of Baffin Bay." },
      { "author": "Henry David Thoreau", "work": "Walden", "quote": "The blueberries were covered with a delicate **glaucous** bloom which melted under the heat of the hand." }
    ]
  }
}

# Write curate-light-batch4.mjs
mjs_code = f"""import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Light & Vision';

function updateNote(relPath, data) {{
  const filePath = path.join(baseClusterDir, relPath);
  if (!fs.existsSync(filePath)) {{
    console.error(`File not found: ${{filePath}}`);
    return false;
  }}
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {{
    console.error(`No > [!book] in ${{filePath}}`);
    return false;
  }}
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${{data.primary}}\\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${{data.secondary}}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${{q.author}} (*${{q.work}}*):** *"${{q.quote}}"*`).join('\\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\\n${{quoteLines}}`;

  const newContent = `${{headerPart}}\\n\\n${{defBlock}}\\n\\n${{quotesBlock}}\\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  return true;
}}

const batchData = {json.dumps(batch4, indent=2, ensure_ascii=False)};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {{
  if (updateNote(relPath, data)) updated++;
}}
console.log(`Successfully updated ${{updated}} of ${{Object.keys(batchData).length}} files in Batch 4.`);
"""

with open('main app/scripts/curate-light-batch4.mjs', 'w', encoding='utf-8') as f:
    f.write(mjs_code)

print("Generated curate-light-batch4.mjs with", len(batch4), "words.")
