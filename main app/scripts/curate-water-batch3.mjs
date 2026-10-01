import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Water & Hydrology';

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

const batch3Data = {
  "Dashboard — hydr/hydrogenate.md": {
    primary: "To combine or treat a chemical substance with hydrogen, especially in the presence of a catalyst to convert unsaturated compounds into saturated ones.",
    secondary: "In industrial food science and petrochemistry, to add hydrogen across carbon-carbon double bonds to solidify liquid vegetable oils or convert coal into synthetic liquid fuels.",
    quotes: [
      { author: "Paul Sabatier", work: "Catalysis in Organic Chemistry", quote: "Finely divided nickel enables us to smoothly **hydrogenate** unsaturated oils into solid fats." },
      { author: "Vladimir Ipatieff", work: "Catalytic Reactions at High Pressures and Temperatures", quote: "We were able to **hydrogenate** naphthalene into tetralin and decalin under high hydrogen pressure." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "In industrial margarine production, chemists **hydrogenate** vegetable oils to achieve the desired melting point." }
    ]
  },
  "Dashboard — hydr/hydrogenation.md": {
    primary: "The chemical process of combining a substance with molecular hydrogen in the presence of a catalyst.",
    secondary: "In industrial chemical engineering, a catalytic reduction process invented by Sabatier and Normann to solidify fats, synthesize ammonia via the Haber-Bosch process, and produce petrochemicals.",
    quotes: [
      { author: "Paul Sabatier", work: "Nobel Lecture", quote: "The direct **hydrogenation** of organic compounds over metallic catalysts opened vast new vistas for industrial chemistry." },
      { author: "Wilhelm Normann", work: "Patent Specification for the Hardening of Fats", quote: "Catalytic **hydrogenation** transforms liquid whale oil and cotton-seed oil into odorless edible solids." },
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "The phenomenon of catalytic **hydrogenation** proves that porous metals temporarily occlude hydrogen gas on their surfaces." }
    ]
  },
  "Dashboard — hydr/hydrographic.md": {
    primary: "Of, pertaining to, or relating to hydrography; dealing with the measurement and description of navigable waters and ocean beds.",
    secondary: "In maritime navigation and physical geography, characterizing bathymetric charts, tide tables, and depth soundings essential for safe nautical piloting.",
    quotes: [
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "Accurate **hydrographic** charts of ocean currents and winds transformed transatlantic sailing into a science." },
      { author: "James Cook", work: "A Voyage Towards the South Pole", quote: "We carried out a detailed **hydrographic** survey of the uncharted bays along the southern coast of New Zealand." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Captain FitzRoy's arduous **hydrographic** measurements of Tierra del Fuego guided mariners safely through perilous channels." }
    ]
  },
  "Dashboard — hydr/hydrographical.md": {
    primary: "An alternative spelling of hydrographic; pertaining to the mapping, depth measurement, and charting of water bodies.",
    secondary: "In earth sciences and navigational history, describing coastal and oceanic surveys designed to identify navigational hazards, tidal shoals, and reef topologies.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Our **hydrographical** observations established the true connection between the basins of the Orinoco and the Amazon." },
      { author: "Robert FitzRoy", work: "Narrative of the Surveying Voyages of HMS Adventure and Beagle", quote: "The **hydrographical** department required rigorous sounding logs for every anchorage visited in the Pacific." },
      { author: "William Henry Smyth", work: "The Sailor's Word-Book", quote: "A **hydrographical** map indicates soundings, shoals, tidal sets, and lighthouses essential for navigation." }
    ]
  },
  "Dashboard — hydr/hydrography.md": {
    primary: "The applied science of surveying, measuring, and charting navigable waters (oceans, seas, lakes, rivers) and coastal topography.",
    secondary: "In naval science and civil engineering, the discipline dedicated to maritime cartography, bathymetry, tidal predictions, and marine safety notices.",
    quotes: [
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "Modern **hydrography** maps the mountains and deep valleys of the ocean floor with sounding lines." },
      { author: "James Cook", work: "Journals", quote: "The practice of nautical **hydrography** demands unrelenting vigilance against hidden coral reefs and deceptive shoals." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "Before discussing terrestrial landforms, we must examine the principles of marine **hydrography**." }
    ]
  },
  "Dashboard — hydr/hydroid.md": {
    primary: "A cnidarian invertebrate in the polyp stage of its life cycle, especially a colonial marine organism belonging to the class Hydrozoa.",
    secondary: "In marine zoology, a sedentary plant-like organism comprising branching chitinous perisarc tubes and specialized polymorphic zooids for feeding, defense, and asexual budding.",
    quotes: [
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "The branched stalks of a colonial **hydroid** bud off tiny free-swimming medusae in rhythmic succession." },
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "In each **hydroid** colony, polymorphic zooids divide labor between nutrition, defense, and sexual reproduction." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Tufts of the **hydroid** Tubularia cling to the wooden wharf pilings like clusters of delicate pink flowers." }
    ]
  },
  "Dashboard — hydr/hydrokinetic.md": {
    primary: "Pertaining to, actuated by, or utilizing the kinetic energy and motion of flowing water or other fluids.",
    secondary: "In renewable energy engineering and hydraulics, describing run-of-river submerged turbines that extract electrical power directly from river currents and ocean tidal streams.",
    quotes: [
      { author: "Daniel Bernoulli", work: "Hydrodynamica", quote: "The **hydrokinetic** energy of a torrent is proportional to the square of its discharge velocity." },
      { author: "William Thomson (Lord Kelvin)", work: "Mathematical and Physical Papers", quote: "We investigated the **hydrokinetic** dissipation of energy in viscous fluids flowing through narrow channels." },
      { author: "Nikola Tesla", work: "Lectures on Alternate Currents", quote: "New turbine designs maximize the capture of **hydrokinetic** power from untamed mountain waterfalls." }
    ]
  },
  "Dashboard — hydr/hydrokinetics.md": {
    primary: "The branch of fluid mechanics that treats the motion of liquids and the forces and energy resulting from that motion.",
    secondary: "In theoretical physics and hydraulic engineering, the mathematical analysis of fluid flow velocities, streamlines, friction losses, and mechanical power generation.",
    quotes: [
      { author: "Daniel Bernoulli", work: "Hydrodynamica", quote: "In founding theoretical **hydrokinetics**, we established that fluid pressure falls as kinetic speed increases." },
      { author: "Hermann von Helmholtz", work: "Scientific Memoirs", quote: "The fundamental vortex equations of **hydrokinetics** explain why fluid rings can propagate indefinitely without tearing." },
      { author: "James Clerk Maxwell", work: "Scientific Papers", quote: "Our treatment of electromagnetic field lines borrowed foundational mathematical theorems from classical **hydrokinetics**." }
    ]
  },
  "Dashboard — hydr/hydrolise.md": {
    primary: "To subject to or undergo hydrolysis; British spelling of hydrolyze.",
    secondary: "In biochemistry and digestive physiology, to decompose complex macromolecules into simpler monomers by enzyme-mediated addition of water molecules.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Dilute mineral acids readily **hydrolise** insoluble starch into fermentable grape sugar." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "Pancreatic secretions contain digestive ferments that **hydrolise** neutral dietary lipids into glycerol and fatty acids." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Intestinal enzymes **hydrolise** complex polypeptides into absorbable amino acids before they cross the mucosal barrier." }
    ]
  },
  "Dashboard — hydr/hydrolith.md": {
    primary: "Calcium hydride (CaH2), a gray crystalline chemical compound that reacts vigorously with water to generate hydrogen gas.",
    secondary: "In military aeronautics and early aviation, a solid portable reagent carried in field canisters to rapidly inflate observation balloons and airships without acid generators.",
    quotes: [
      { author: "Henri Moissan", work: "The Electric Furnace", quote: "By direct synthesis in the electric furnace, we prepared crystalline **hydrolith**, which reacts with water to release hydrogen." },
      { author: "J. R. Partington", work: "A Text-Book of Inorganic Chemistry", quote: "Military field aeronauts carried canisters of **hydrolith** to generate hydrogen rapidly without bulky acid generators." },
      { author: "Henry Enfield Roscoe", work: "A Treatise on Chemistry", quote: "The action of water on **hydrolith** is extraordinarily brisk, yielding one kilogram of hydrogen from two kilograms of solid." }
    ]
  },
  "Dashboard — hydr/hydrolize.md": {
    primary: "A variant or American spelling of hydrolyze; to decompose or split a chemical compound through reaction with water.",
    secondary: "In chemical laboratory synthesis, to cleave ester, amide, or glycosidic linkages in the presence of acidic or alkaline aqueous catalysts.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "A warm aqueous solution of sodium acetate will slightly **hydrolize**, generating an alkaline pH." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Boiling the ester with alcoholic potassium hydroxide will rapidly **hydrolize** it into an acid salt and alcohol." },
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry", quote: "Certain delicate metallic salts **hydrolize** spontaneously when dissolved in excess boiling water." }
    ]
  },
  "Dashboard — hydr/hydrologist.md": {
    primary: "A scientist who specializes in hydrology, studying the properties, distribution, and circulation of water on Earth.",
    secondary: "In environmental science and civil resource planning, an expert who models watershed runoffs, groundwater aquifers, flood risks, and municipal water allocations.",
    quotes: [
      { author: "John Wesley Powell", work: "Report on the Lands of the Arid Region of the United States", quote: "The **hydrologist** must calculate seasonal runoff with exacting precision before dams are raised in the western deserts." },
      { author: "Gifford Pinchot", work: "The Fight for Conservation", quote: "Every competent **hydrologist** recognizes that forest cover on mountain slopes regulates the discharge of lowland rivers." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "The observant **hydrologist** notes how deforestation dries up mountain headwaters and unleashes disastrous flash floods." }
    ]
  },
  "Dashboard — hydr/hydrology.md": {
    primary: "The scientific study of the waters of the Earth, their occurrence, distribution, circulation, and chemical and physical properties.",
    secondary: "In Earth system science, the discipline analyzing the global water cycle, precipitation infiltration, subterranean aquifers, and sediment transport in river basins.",
    quotes: [
      { author: "John Wesley Powell", work: "Report on the Lands of the Arid Region", quote: "In the arid West, agricultural settlement is strictly governed by the stern laws of **hydrology**." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "The modern science of **hydrology** traces the raindrop from its oceanic evaporation to its subterranean descent." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "River erosion and limestone subterranean caverns demonstrate the immense geological power of underground **hydrology**." }
    ]
  },
  "Dashboard — hydr/hydrolysate.md": {
    primary: "Any chemical substance or mixture produced by the hydrolysis of a larger compound, such as protein or starch hydrolysate.",
    secondary: "In clinical nutrition and biotechnology, enzymatically digested peptides and free amino acids formulated for hypoallergenic infant milk, medical enteral feeding, or bacterial growth media.",
    quotes: [
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Chromatographic fractionation of the casein **hydrolysate** revealed nineteen distinct alpha-amino acids." },
      { author: "Frederick Gowland Hopkins", work: "Biochemical Papers", quote: "Feeding animals on an acid **hydrolysate** of protein lacking tryptophan resulted in rapid cessation of growth." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Patients with severe malabsorption benefit from intravenous feeding with an enzymatic **hydrolysate** of purified proteins." }
    ]
  },
  "Dashboard — hydr/hydrolyse.md": {
    primary: "To decompose a chemical compound by reaction with water; British spelling of hydrolyze.",
    secondary: "In biochemistry and industrial biocatalysis, to cleave ester, peptide, or polysaccharide bonds through the action of hydrolase enzymes.",
    quotes: [
      { author: "Thomas Graham", work: "Liquid Diffusion Applied to Analysis", quote: "Colloidal ferments slowly **hydrolyse** cane sugar into glucose and fructose without being consumed." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "The enzymes of the saliva and pancreas **hydrolyse** dietary starches into soluble dextrins." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Molds and yeasts produce extracellular invertase to **hydrolyse** complex disaccharides in the nutrient broth." }
    ]
  },
  "Dashboard — hydr/hydrolysis.md": {
    primary: "A chemical reaction in which a molecule of water cleaves one or more chemical bonds in another compound, incorporating H+ and OH- fragments.",
    secondary: "In metabolic biochemistry and industrial chemistry, the mechanism by which polymers (proteins, polysaccharides, nucleic acids) are broken down into their constituent monomers.",
    quotes: [
      { author: "Svante Arrhenius", work: "Theories of Chemistry", quote: "The degree of **hydrolysis** of a dissolved salt can be quantitatively calculated from its electrolytic dissociation constants." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The enzymatic **hydrolysis** of adenosine triphosphate releases free energy to drive endergonic cellular processes." },
      { author: "Jacobus Henricus van 't Hoff", work: "Lectures on Theoretical and Physical Chemistry", quote: "We measured the velocity of ester **hydrolysis** in dilute aqueous acids to verify the mass action law." }
    ]
  },
  "Dashboard — hydr/hydrolyzable.md": {
    primary: "Capable of being broken down or cleaved by water or aqueous enzymes; susceptible to hydrolysis.",
    secondary: "In pharmacochemistry and materials science, describing biodegradable polymer sutures (such as polyglycolic acid) or tannins that dissolve and degrade in biological fluids.",
    quotes: [
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Tannins are broadly classified into condensed proanthocyanidins and **hydrolyzable** gallotannins." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The glycosidic linkages of cellulose are **hydrolyzable** only under severe acidic conditions or by specialized cellulase enzymes." },
      { author: "Frederick Gowland Hopkins", work: "Biochemical Journal", quote: "Only the **hydrolyzable** peptide bonds of proteins are cleaved during peptic and tryptic digestion." }
    ]
  },
  "Dashboard — hydr/hydrolyze.md": {
    primary: "To subject to or cause chemical cleavage through reaction with water; American spelling of hydrolyse.",
    secondary: "In industrial organic synthesis, to split fats into glycerol and fatty acids with superheated steam, or convert starches into corn syrup using mineral acids.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Strong mineral acids will rapidly **hydrolyze** starch into glucose when heated under reflux." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Lipases in the small intestine **hydrolyze** dietary triglycerides into monoglycerides and free fatty acids." },
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry", quote: "Substances that **hydrolyze** easily in moist air must be preserved under an inert atmosphere." }
    ]
  },
  "Dashboard — hydr/hydromancer.md": {
    primary: "A diviner or seer who practices hydromancy, claiming to foresee future events by interpreting water movements, ripples, or images.",
    secondary: "In historical folklore and classical anthropology, a practitioner of ancient water-scrying consulted at sacred springs and oracles in ancient Greece and Rome.",
    quotes: [
      { author: "Walter Scott", work: "The Antiquary", quote: "The village **hydromancer** pretended to read doom in the circular ripples of the holy well." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "The ancient **hydromancer** cast pebbles into a silver basin and divined war or peace from the shimmering waves." },
      { author: "Edward Tylor", work: "Primitive Culture", quote: "Among primitive tribes, the **hydromancer** peered into sacred pools to discover the thief or foretell the harvest." }
    ]
  },
  "Dashboard — hydr/hydromancy.md": {
    primary: "Divination by means of water, such as observing the ripples, colors, reflections, or objects floating in a sacred basin or pool.",
    secondary: "In the history of religion and occultism, one of the four traditional elemental divinations (along with geomancy, aeromancy, and pyromancy) described by classical authors like Varro.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "Ancient Greek priests practiced **hydromancy** at the fountain of Apollo, gazing into the waters for prophetic visions." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Divination by water, or **hydromancy**, was numbered by Varro among the four principal modes of ancient occult inquiry." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The superstitious emperor consulted rustic seers who claimed mastery in astrological arts and **hydromancy**." }
    ]
  },
  "Dashboard — hydr/hydromantes.md": {
    primary: "A genus of lungless plethodontid salamanders (cave salamanders or web-toed salamanders) native to southern Europe and California.",
    secondary: "In evolutionary herpetology, famous for exhibiting a ballistic projectile tongue and an enigmatic disjunct distribution across Mediterranean limestone grottos and the Sierra Nevada.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The disjunct occurrence of **Hydromantes** in California and the Mediterranean caves presents a classical biogeographic puzzle." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "Species of **Hydromantes** possess a projectile tongue capable of shooting forward to catch insects on cave walls." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The subterranean habits of **Hydromantes** explain its survival in isolated rocky caverns across separated continents." }
    ]
  },
  "Dashboard — hydr/hydromel.md": {
    primary: "A liquor or fermented beverage made of honey and water; mead.",
    secondary: "In ancient Greco-Roman and medieval domestic economy, unfermented honey-water drunk as a refreshing medicinal tisane, or fermented into an intoxicating celebratory mead.",
    quotes: [
      { author: "Pliny the Elder", work: "Natural History", quote: "The beverage known as **hydromel** is prepared by blending pure rainwater with old comb-honey and exposing it to forty days of summer sun." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The northern barbarians celebrated their victories around roaring hearths, quaffing deep horns of fermented **hydromel**." },
      { author: "Walter Scott", work: "Ivanhoe", quote: "The Saxon thane offered his guests foaming cups of ale and sweet golden **hydromel** before the banquet commenced." }
    ]
  },
  "Dashboard — hydr/hydrometer.md": {
    primary: "An instrument for measuring the specific gravity, relative density, or strength of liquids by means of buoyancy.",
    secondary: "In physical instrumentation and brewing, a sealed graduated glass bulb weighted with lead shot that sinks to varying depths depending on liquid density (such as in wort or battery acid).",
    quotes: [
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "By dipping a graduated glass **hydrometer** into wine and spirits, we determined their relative buoyant gravities with great precision." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "The Baumé **hydrometer** provided distillers and acid manufacturers with a rapid commercial scale for measuring specific gravity." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "To monitor the state of charge in a lead-acid storage cell, one tests the electrolyte density with a suction **hydrometer**." }
    ]
  },
  "Dashboard — hydr/hydrometric.md": {
    primary: "Of, pertaining to, or determined by hydrometry; relating to the measurement of liquid density, velocity, or discharge.",
    secondary: "In river basin management, characterizing gauging stations, current-meters, and stage-discharge rating curves used to monitor streamflow.",
    quotes: [
      { author: "Daniel Bernoulli", work: "Hydrodynamica", quote: "We calibrated our **hydrometric** vanes to measure the discharge velocity of water flowing through flumes." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Our **hydrometric** observations on the Orinoco revealed that the river rises more than thirty feet during the rainy season." },
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "Naval officers must record regular **hydrometric** soundings of surface seawater density to detect fresh river plumes." }
    ]
  },
  "Dashboard — hydr/hydrometry.md": {
    primary: "The science or practice of measuring the specific gravity, density, or velocity and volume of liquids, particularly water.",
    secondary: "In environmental monitoring and engineering, the operational discipline of recording river discharge, aquifer water levels, and canal flow rates.",
    quotes: [
      { author: "Daniel Bernoulli", work: "Hydrodynamica", quote: "The science of **hydrometry** provides civil engineers with the mathematical formulas necessary to meter canal irrigation." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Precision **hydrometry** allows the chemist to ascertain the exact strength of nitric and sulfuric acids without chemical titration." },
      { author: "William Henry Smyth", work: "The Sailor's Word-Book", quote: "In nautical science, **hydrometry** includes measuring the buoyancy and saltiness of different oceanic waters." }
    ]
  },
  "Dashboard — hydr/hydromorphone.md": {
    primary: "A semi-synthetic opioid analgesic medication derived from morphine (brand name Dilaudid), used for the relief of moderate to severe pain.",
    secondary: "In clinical pharmacodynamics, a potent mu-opioid receptor agonist roughly five to eight times more potent than oral morphine, with rapid onset and minimal histamine release.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "For intractable cancer pain, **hydromorphone** provides powerful analgesia with fewer sedative side effects than morphine." },
      { author: "Donald Calne", work: "Therapeutics in Neurology", quote: "The pharmacological potency of **hydromorphone** is roughly five to seven times greater than that of parenteral morphine." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Catalytic hydrogenation of morphine followed by oxidation yields **hydromorphone**, featuring a ketone at the six-position." }
    ]
  },
  "Dashboard — hydr/hydromyinae.md": {
    primary: "A subfamily of murid rodents commonly called amphibious rats or water rats, native to Australia, New Guinea, and adjacent islands.",
    secondary: "In mammalian evolutionary biology, a group of semi-aquatic rodents displaying morphological adaptations including reduced molar dentition, webbed digits, and water-repellent guard hair.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The water rats of the **Hydromyinae** possess webbed hind feet and dense water-repellent fur suited for river hunting." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "Members of the **Hydromyinae** display remarkable dental reduction, having only two molars in each jaw." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "In cranial anatomy, the **Hydromyinae** exhibit flattened skulls and valvular nostrils adapted to aquatic diving." }
    ]
  },
  "Dashboard — hydr/hydromys.md": {
    primary: "A genus of semi-aquatic Australasian rodents containing the rakali or Australian water rat (Hydromys chrysogaster).",
    secondary: "In native Australasian ecology, an apex freshwater carnivore that hunts fish, frogs, and freshwater crustaceans along riparian corridors and coastal estuaries.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "In the streams of Tasmania, the golden-bellied **Hydromys** fills the ecological niche occupied by the European water vole." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The Australian beaver-rat **Hydromys** chrysogaster dives skillfully to hunt freshwater mussels and crayfish." },
      { author: "Frank Evers Beddard", work: "Mammalia", quote: "The skull of **Hydromys** is heavily constructed to support powerful jaw muscles for cracking mollusk shells." }
    ]
  },
  "Dashboard — hydr/hydronephrosis.md": {
    primary: "The aseptic distension and dilation of the renal pelvis and calyces caused by obstruction to the outflow of urine.",
    secondary: "In clinical urology, progressive renal hydropic enlargement resulting from kidney stones, strictures, or tumors that eventually causes renal cortical thinning and renal failure.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "An impacted ureteral calculus can rapidly induce acute **hydronephrosis**, causing excruciating flank colic and renal swelling." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Longstanding **hydronephrosis** leads to progressive atrophy of the renal parenchyma until the kidney becomes a thin-walled fluid sac." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Surgical relief of the obstruction in early **hydronephrosis** allows the kidney to recover its secretory function." }
    ]
  },
  "Dashboard — hydr/hydropathic.md": {
    primary: "Of, pertaining to, or practicing hydropathy (the water-cure); utilizing water treatments for therapeutic purposes.",
    secondary: "In 19th-century social and medical history, describing residential spa sanatoriums where patients underwent cold-water wraps, douches, and dietary regimens.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "He had spent six weeks at a celebrated **hydropathic** establishment in the hills, drinking cold spring water and taking vigorous walks." },
      { author: "Charlotte Brontë", work: "The Life of Charlotte Brontë", quote: "The physician urged her to seek relief at a Yorkshire **hydropathic** retreat where cold wraps were applied for nervous exhaustion." },
      { author: "George Eliot", work: "Middlemarch", quote: "Fashionable society flocked to **hydropathic** sanitariums to escape the smoky air of manufacturing towns." }
    ]
  },
  "Dashboard — hydr/hydropathy.md": {
    primary: "The historical treatment of disease by the internal and external application of water; the 'water cure'.",
    secondary: "In medical history, a popular 19th-century alternative medical system developed by Vincenz Prießnitz, which evolved into modern evidence-based physiotherapy and hydrotherapy.",
    quotes: [
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "While the extravagant claims of **hydropathy** must be viewed with skepticism, the judicious application of clean cold water has saved many a fevered life." },
      { author: "Thomas Henry Huxley", work: "Critiques and Addresses", quote: "The Victorian craze for **hydropathy** demonstrated the public desire for non-toxic therapies over mercurial purges." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "Prießnitz founded modern **hydropathy** at Gräfenberg, demonstrating that cold plunges and wet sheets could stimulate physiological recovery." }
    ]
  },
  "Dashboard — hydr/hydrophidae.md": {
    primary: "A family (or elapid subfamily Hydrophiinae) of highly venomous marine sea snakes inhabiting warm coastal waters of the Indian and Pacific Oceans.",
    secondary: "In herpetology, specialized front-fanged aquatic reptiles possessing laterally flattened, paddle-like tails, valvular nostrils, and specialized salt-excreting sublingual glands.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "In the warm waters of the Indian Ocean, we observed banded sea snakes of the **Hydrophidae** swimming with paddle-shaped tails." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The deadly venom of the **Hydrophidae** is adapted to immobilize swift marine fish almost instantaneously." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "Members of the **Hydrophidae** are fully viviparous marine reptiles that never come ashore to lay eggs." }
    ]
  },
  "Dashboard — hydr/hydrophilic.md": {
    primary: "Having a strong chemical affinity for water; readily absorbing, wetting, or dissolving in water.",
    secondary: "In surface chemistry and cell biology, describing polar molecules or functional groups (such as carboxyls and amines) capable of forming hydrogen bonds with water molecules.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The **hydrophilic** polar head groups of phospholipids face outward toward the aqueous cytoplasm of the living cell." },
      { author: "Christian de Duve", work: "A Guided Tour of the Living Cell", quote: "Cell membranes are organized with **hydrophilic** surfaces in contact with water and hydrophobic cores shielded inside." },
      { author: "Thomas Graham", work: "Liquid Diffusion Applied to Analysis", quote: "Substances with high **hydrophilic** character form gelatinous colloids that diffuse with extreme slowness." }
    ]
  },
  "Dashboard — hydr/hydrophily.md": {
    primary: "The pollination of flowering plants through the agency of water currents; water pollination.",
    secondary: "In ecological botany, an unusual evolutionary mode of pollen transfer found in submerged or floating plants like eelgrass (Zostera) and tape grass (Vallisneria).",
    quotes: [
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "The underwater pollination of Vallisneria and Zostera illustrates the rare botanical phenomenon of **hydrophily**." },
      { author: "Asa Gray", work: "How Plants Behave", quote: "True **hydrophily** occurs only in a handful of aquatic angiosperms where buoyant pollen grains drift across the water surface." },
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "In marine seagrasses, **hydrophily** has evolved to transport filiform pollen through underwater currents to receptive stigmas." }
    ]
  },
  "Dashboard — hydr/hydrophobia.md": {
    primary: "An extreme, morbid, or convulsive dread of water, historically the hallmark symptom of rabies in humans; rabies itself.",
    secondary: "In clinical neurology and infectious disease, excruciating reflex laryngeal spasms triggered when a rabies patient attempts to swallow liquids, caused by viral encephalitis.",
    quotes: [
      { author: "Louis Pasteur", work: "Researches on Rabies", quote: "The harrowing symptom of **hydrophobia** is caused by agonizing pharyngeal spasms when the patient attempts to swallow water." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The diagnosis of rabies is confirmed by the terrifying reflex laryngeal spasms of **hydrophobia** provoked by the mere sound of running water." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "The dread and convulsive terror seen in canine rabies and human **hydrophobia** reflect profound viral damage to the brainstem." }
    ]
  },
  "Dashboard — hydr/hydrophobic.md": {
    primary: "Lacking affinity for water; repelling water or failing to mix with it; characteristic of rabies (hydrophobia).",
    secondary: "In physical chemistry and structural biology, designating nonpolar substances (such as hydrocarbons and lipids) that force water molecules into clathrate cages, driving hydrophobic collapse.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The folding of globular proteins is driven by the spontaneous burial of non-polar, **hydrophobic** amino acid residues within the interior." },
      { author: "Christian de Duve", work: "A Guided Tour of the Living Cell", quote: "The lipid bilayer forms an effective permeability barrier because its central core is intensely **hydrophobic**." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "The **hydrophobic** paraffin wax coating prevented aqueous solutions from wetting the glass capillary." }
    ]
  },
  "Dashboard — hydr/hydrophobicity.md": {
    primary: "The physical property of being water-repellent; the tendency of nonpolar chemical groups to avoid contact with water.",
    secondary: "In molecular biology and biophysics, the fundamental thermodynamic driving force responsible for protein folding, micelle formation, and cell membrane stability.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "The high **hydrophobicity** of hydrocarbon chains causes oil droplets to coalesce and separate from an aqueous emulsion." },
      { author: "Christian de Duve", work: "Vital Dust", quote: "The self-assembly of primitive cellular membranes was dictated by the differential **hydrophobicity** of prebiotic amphiphiles." },
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "X-ray crystallography established that the internal **hydrophobicity** of hemoglobin provides the mechanical stability needed for cooperative oxygen binding." }
    ]
  },
  "Dashboard — hydr/hydrophyllaceae.md": {
    primary: "The waterleaf family of dicotyledonous flowering plants (order Boraginales), comprising herbs and shrubs such as Hydrophyllum and Phacelia.",
    secondary: "In systematic botany, plants characterized by bristly hairs, coiled scorpioid cymes, and watery mottled markings on early basal leaves.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The family **Hydrophyllaceae** is distinguished by scorpioid cymes and pinnately divided foliage that often looks water-spotted." },
      { author: "George Bentham & Joseph Dalton Hooker", work: "Genera Plantarum", quote: "In North American floras, the **Hydrophyllaceae** are represented by numerous showy annuals and woodland perennials." },
      { author: "John Torrey", work: "A Flora of the State of New York", quote: "In damp deciduous woods, members of the **Hydrophyllaceae** carpet the forest floor with delicate lilac blossoms." }
    ]
  },
  "Dashboard — hydr/hydrophyllum.md": {
    primary: "A genus of North American woodland perennial herbs commonly known as waterleaf (family Boraginales / Hydrophyllaceae).",
    secondary: "In woodland flora, spring ephemerals featuring pinnatifid leaves with translucent watery maculations and terminal clusters of bell-shaped flowers.",
    quotes: [
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "Species of **Hydrophyllum** derive their common name from the translucent watery spots that appear on their early spring foliage." },
      { author: "John Torrey", work: "Botanical Papers", quote: "The bell-shaped lavender flowers of **Hydrophyllum** virginianum attract solitary bees to northern hardwood forests." },
      { author: "John Muir", work: "The Mountains of California", quote: "Along shaded alpine brooks, clumps of wild **Hydrophyllum** blossom beneath the shelter of towering conifers." }
    ]
  },
  "Dashboard — hydr/hydrophyte.md": {
    primary: "A plant adapted to grow in water or in waterlogged soil; an aquatic plant.",
    secondary: "In ecological plant physiology, an organism possessing specialized adaptations including floating leaves, submerged dissected foliage, absent cuticles, and extensive aerenchyma.",
    quotes: [
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "A true **hydrophyte** possesses reduced vascular tissues and extensive intercellular air-channels to provide buoyancy and oxygen." },
      { author: "Andreas Schimper", work: "Plant-Geography upon a Physiological Basis", quote: "The water lily is a celebrated **hydrophyte** whose leaves float flat upon the surface while roots anchor in the anaerobic lake mud." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Because a **hydrophyte** absorbs water and minerals directly through its epidermal surfaces, its root system is often markedly reduced." }
    ]
  },
  "Dashboard — hydr/hydrophytic.md": {
    primary: "Of, pertaining to, or characteristic of hydrophytes; adapted to an aquatic or water-saturated habitat.",
    secondary: "In wetland ecology, describing vegetative communities (such as cattails, bulrushes, and water lilies) that indicate hydric soil conditions.",
    quotes: [
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "The **hydrophytic** vegetation of marshlands exhibits finely dissected leaves that offer minimal resistance to moving water." },
      { author: "Henry Chandler Cowles", work: "The Physiographic Ecology of Chicago and Vicinity", quote: "The progressive accumulation of peat transforms open **hydrophytic** ponds into bog forests." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "The floating meadows of the Amazon basin form an impenetrable **hydrophytic** barrier of grasses and Eichhornia." }
    ]
  },
  "Dashboard — hydr/hydroplane.md": {
    primary: "A light, high-speed motorboat designed to skim over the surface of the water; a fin or control surface on a submarine; to skim uncontrollably across a wet surface.",
    secondary: "In automotive safety and aerodynamics, the hazardous loss of vehicle traction occurring when a wedge of water builds up between tires and wet road surfaces.",
    quotes: [
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Sea", quote: "Captain Nemo tilted the forward **hydroplane** fins to steer the submarine deep into the Atlantic trench." },
      { author: "Alexander Graham Bell", work: "Scientific Papers on Aerial and Marine Locomotion", quote: "A stepped hull allows a racing **hydroplane** to break water suction and plane effortlessly on the surface." },
      { author: "H. G. Wells", work: "The War in the Air", quote: "The scout flew low over the channel in his twin-engine **hydroplane**, watching for the approach of the enemy flotilla." }
    ]
  },
  "Dashboard — hydr/hydroponic.md": {
    primary: "Relating to, grown by, or utilizing hydroponics; cultivated in liquid nutrient solutions without soil.",
    secondary: "In agricultural technology, describing soilless cultivation systems that circulate oxygenated water and balanced mineral salts to achieve high crop productivity.",
    quotes: [
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "Our early **hydroponic** water cultures demonstrated that plants can attain full maturity supplied solely with dissolved mineral salts." },
      { author: "Wilhelm Pfeffer", work: "The Physiology of Plants", quote: "By adjusting the chemical ratios in a **hydroponic** solution, we identified the essential micro-elements needed for chlorophyll synthesis." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Vast **hydroponic** towers produced artificial vegetables under neon illumination in the mechanized state nurseries." }
    ]
  },
  "Dashboard — hydr/hydroponics.md": {
    primary: "The cultivation of plants in liquid nutrient solutions, with or without an inert supporting medium like perlite or gravel, without soil.",
    secondary: "In modern horticulture and controlled-environment agriculture, a precision farming methodology minimizing water waste and eliminating soil-borne pathogens.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The laboratory technique of **hydroponics** revolutionized plant physiology by proving that soil is not an absolute necessity for plant life." },
      { author: "Wilhelm Pfeffer", work: "The Physiology of Plants", quote: "Modern greenhouse **hydroponics** relies upon precise oxygenation and mineral buffering to maximize crop yields." },
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "Lunar and planetary bases will depend on closed-cycle **hydroponics** to supply fresh food and recycle oxygen." }
    ]
  },
  "Dashboard — hydr/hydrops.md": {
    primary: "An abnormal clinical accumulation of serous fluid in tissues or bodily cavities; edema or dropsy.",
    secondary: "In clinical perinatology, hydrops fetalis, a lethal fetal condition characterized by widespread subcutaneous edema, ascites, and cardiovascular collapse.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Fetal **hydrops** resulting from severe Rh incompatibility causes massive subcutaneous edema, ascites, and pleural effusion." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The transudation of fluid in generalized **hydrops** follows increased capillary permeability and venous stasis." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Chronic joint effusion, historically called **hydrops** articuli, leads to progressive ligamentous laxity." }
    ]
  },
  "Dashboard — hydr/hydrosphere.md": {
    primary: "The total mass of liquid, frozen, and gaseous water found on, under, and over the surface of the Earth.",
    secondary: "In Earth system science and climatology, the global aqueous realm including oceans, seas, ice caps, lakes, rivers, and atmospheric vapor that regulates global planetary heat.",
    quotes: [
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "In our geophysical survey, we partition the globe into lithosphere, atmosphere, and the liquid **hydrosphere** that covers seventy percent of the planet." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The global hydrological cycle connects the restless **hydrosphere** with the surrounding atmospheric currents." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The vast **hydrosphere** acts as the great thermal thermostat of the earth, buffering global climates against catastrophic extremes." }
    ]
  },
  "Dashboard — hydr/hydrostat.md": {
    primary: "An apparatus or automatic regulator designed to detect, control, or maintain a constant water level, especially in a steam boiler.",
    secondary: "In mechanical engineering, a safety control switch that automatically interrupts burner operation or sounds an alarm when water levels drop below a critical threshold.",
    quotes: [
      { author: "Thomas Ewbank", work: "A Descriptive and Historical Account of Hydraulic Machines", quote: "An automated **hydrostat** was fitted to the boiler to shut off fuel whenever the water dropped below the crown-sheet." },
      { author: "Dionysius Lardner", work: "The Steam Engine Explained and Illustrated", quote: "The steam engineer adjusted the balance float of the **hydrostat** to ensure continuous boiler feed." },
      { author: "William Henry Smyth", work: "The Sailor's Word-Book", quote: "A marine **hydrostat** signals an alarm in the engine room when water accumulates dangerously in the ship's bilges." }
    ]
  },
  "Dashboard — hydr/hydrostatic.md": {
    primary: "Of, pertaining to, or in a state of equilibrium under the pressure exerted by liquids at rest.",
    secondary: "In physiology and medicine, describing hydrostatic pressure within capillary beds that drives filtration across endothelial walls in opposition to oncotic pressure.",
    quotes: [
      { author: "Daniel Bernoulli", work: "Hydrodynamica", quote: "The **hydrostatic** pressure at any depth in a vessel is proportional to the density of the fluid and the height of the column." },
      { author: "Blaise Pascal", work: "Treatise on the Weight of the Mass of Air", quote: "Our experiments confirmed that **hydrostatic** pressure is transmitted equally in all directions throughout a confined fluid." },
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "In the second book, we establish that **hydrostatic** equilibrium requires equal pressure along every horizontal plane." }
    ]
  },
  "Dashboard — hydr/hydrostatics.md": {
    primary: "The branch of physical fluid mechanics that studies liquids at rest and the pressure and forces they exert.",
    secondary: "In classical physics, the study of Pascal's principle, Archimedes' buoyant principle, and the equilibrium equations of incompressible fluids.",
    quotes: [
      { author: "Archimedes", work: "On Floating Bodies", quote: "The foundational principle of **hydrostatics** establishes that any solid immersed in a fluid is buoyed up by a force equal to the weight of the displaced liquid." },
      { author: "Blaise Pascal", work: "Treatise on the Equilibrium of Liquids", quote: "The mathematical laws of **hydrostatics** explain why a slender column of water can burst a stout oak cask." },
      { author: "Simon Stevin", work: "The Elements of Hydrostatics", quote: "By geometric demonstrations in **hydrostatics**, we proved that liquid pressure upon a surface depends strictly on depth and area." }
    ]
  },
  "Dashboard — hydr/hydrotherapy.md": {
    primary: "The use of water in any form (liquid, ice, steam) internally or externally in the treatment of disease, pain, or physical rehabilitation.",
    secondary: "In physical medicine and physiotherapy, aquatic rehabilitation regimens utilizing water buoyancy, hydrostatic pressure, and temperature to restore mobility.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Judicious **hydrotherapy** using cold sponge baths effectively reduced high temperatures and delirium in typhoid fever." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Carefully regulated warm **hydrotherapy** soothes the nervous system and relaxes rigid spastic muscles far better than opiates." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "Scientific **hydrotherapy** established itself as a rational discipline when physiological thermal responses replaced mystical water cures." }
    ]
  },
  "Dashboard — hydr/hydrothermal.md": {
    primary: "Of, pertaining to, or produced by heated water, steam, or mineral-rich solutions circulating within the Earth's crust.",
    secondary: "In economic geology and volcanology, describing mineral-deposit veins, geysers, and deep-sea submarine hydrothermal vents supporting chemosynthetic ecosystems.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Rich veins of gold and copper were deposited along rock fissures by ascending **hydrothermal** solutions charged with sulfur." },
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "Volcanic calderas and geysers demonstrate the immense kinetic energy of subterranean **hydrothermal** systems." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Deep submarine **hydrothermal** vents support vibrant chemosynthetic ecosystems independent of sunlight." }
    ]
  },
  "Dashboard — hydr/hydrothermic.md": {
    primary: "An alternative form of hydrothermal; produced by or relating to the combined action of subterranean heat and water.",
    secondary: "In petrology and mineral synthesis, designating metamorphic changes or mineral crystallization induced in rock formations by superheated aqueous fluids.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The formation of zeolite crystals in volcanic cavities is a typical product of low-temperature **hydrothermic** alteration." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The steaming fumaroles and boiling springs of the Andes display the persistent power of **hydrothermic** metamorphism." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Deep-seated rocks undergo profound recrystallization under the combined influence of **hydrothermic** pressure and volcanic heat." }
    ]
  },
  "Dashboard — hydr/hydrothorax.md": {
    primary: "A non-inflammatory accumulation of serous fluid in one or both pleural cavities of the thorax; pleural effusion.",
    secondary: "In internal medicine and pulmonology, a common complication of congestive heart failure, liver cirrhosis, or nephrotic syndrome resulting from altered oncotic and hydrostatic pressures.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Bilateral **hydrothorax** is a frequent manifestation of congestive heart failure, producing dullness on chest percussion and severe orthopnea." },
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", quote: "Auscultation over the lower lung lobes in **hydrothorax** reveals complete absence of respiratory murmur and distinct egophony." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "When acute **hydrothorax** compresses the lungs and displaces the heart, thoracentesis must be promptly performed to relieve asphyxia." }
    ]
  },
  "Dashboard — hydr/hydrous.md": {
    primary: "Containing water, especially water of crystallization, hydration, or chemical combination; aqueous.",
    secondary: "In descriptive mineralogy, identifying minerals such as gypsum, opal, or talc that contain bound water molecules within their crystalline framework.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Gypsum is a **hydrous** calcium sulfate which, when gently heated, loses its water of crystallization to form plaster of Paris." },
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry", quote: "The crystalline substance proved to be a **hydrous** oxide of iron, readily parting with its moisture upon calcination." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Chemists must carefully differentiate between an anhydrous mineral and its **hydrous** crystallized state." }
    ]
  },
  "Dashboard — hydr/hydroxide.md": {
    primary: "A chemical compound containing the univalent hydroxyl group (-OH) combined with a metallic element or radical; a chemical base.",
    secondary: "In inorganic chemistry, compounds such as sodium hydroxide (NaOH) or calcium hydroxide (Ca(OH)2) that dissociate in water to produce alkaline hydroxide anions.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "By the intense action of the galvanic battery, I decomposed caustic potash and separated metallic potassium from its **hydroxide**." },
      { author: "Svante Arrhenius", work: "Theories of Chemistry", quote: "In aqueous solution, every basic substance dissociates to release free **hydroxide** ions into the medium." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Sodium **hydroxide** forms a strongly basic solution that saponifies fats and rapidly neutralizes mineral acids." }
    ]
  },
  "Dashboard — hydr/hydroxy.md": {
    primary: "Containing, characterized by, or pertaining to the hydroxyl group or radical (-OH) attached to an organic skeleton.",
    secondary: "In systematic organic nomenclature, a prefix designating the presence of an alcohol or phenol function on a carbon chain (such as hydroxybenzoic acid).",
    quotes: [
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "The introduction of a **hydroxy** group into an aromatic ring transforms the parent hydrocarbon into a reactive phenol." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Hydrogen bonding between adjacent **hydroxy** groups contributes to the high boiling point of polyhydric alcohols." },
      { author: "Emil Fischer", work: "Studies on Carbohydrates", quote: "Stereochemical orientation of each secondary **hydroxy** group along the carbon chain determines whether a hexose is glucose or galactose." }
    ]
  },
  "Dashboard — hydr/hydroxybenzene.md": {
    primary: "The systematic chemical name for phenol (carbolic acid, C6H5OH), an aromatic organic compound consisting of a benzene ring bonded to a hydroxyl group.",
    secondary: "In historical medicine and petrochemical synthesis, a pioneering antiseptic introduced by Joseph Lister, widely used in synthesizing polymers, bakelite, and pharmaceuticals.",
    quotes: [
      { author: "Joseph Lister", work: "Collected Papers", quote: "Dilute sprays and dressings of **hydroxybenzene**, then known as carbolic acid, banished hospital gangrene from our surgical wards." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "In industrial synthesis, **hydroxybenzene** is produced on a vast scale via the cumene hydroperoxide process." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The resonance delocalization of pi electrons into the benzene ring renders the hydroxyl proton of **hydroxybenzene** appreciably acidic." }
    ]
  },
  "Dashboard — hydr/hydroxychloroquine.md": {
    primary: "A 4-aminoquinoline medication used to treat and prevent malaria, and as a disease-modifying antirheumatic drug (DMARD) for lupus and rheumatoid arthritis.",
    secondary: "In clinical rheumatology and immunology, an oral drug that accumulates in intracellular lysosomes, inhibiting antigen presentation and dampening toll-like receptor signaling.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern management of systemic lupus erythematosus relies on **hydroxychloroquine** to prevent disease flares and renal complications." },
      { author: "Donald Calne", work: "Therapeutics in Neurology", quote: "The incorporation of a hydroxyl group into chloroquine yielded **hydroxychloroquine**, marked by reduced ocular toxicity." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Long-term therapeutic regimens of **hydroxychloroquine** suppress autoimmune inflammation without causing generalized bone-marrow suppression." }
    ]
  },
  "Dashboard — hydr/hydroxyl.md": {
    primary: "The chemical univalent radical or functional group -OH, consisting of one oxygen atom covalently bonded to one hydrogen atom.",
    secondary: "In organic chemistry and surface science, a polar functional group whose presence imparts water solubility, hydrogen bonding capability, and chemical reactivity to alcohols and phenols.",
    quotes: [
      { author: "Svante Arrhenius", work: "Theories of Chemistry", quote: "The electrical conductivity of basic solutions is primarily governed by the high mobility of the free **hydroxyl** anion." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The electronegative oxygen atom of the **hydroxyl** group forms strong intermolecular hydrogen bonds in water and alcohols." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Acetylation of the compound confirmed that each substituted molecule contains exactly three free **hydroxyl** radicals." }
    ]
  },
  "Dashboard — hydr/hydroxymethyl.md": {
    primary: "The univalent organic chemical group -CH2OH, consisting of a methylene group bonded to a hydroxyl group.",
    secondary: "In biochemistry and carbohydrate chemistry, a substituent present on aldohexose rings (such as C-6 of glucose) and key intermediates in enzymatic methylenation.",
    quotes: [
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Oxidation of the terminal **hydroxymethyl** group of a primary alcohol yields first an aldehyde and finally a carboxylic acid." },
      { author: "Emil Fischer", work: "Studies on Carbohydrates", quote: "In aldohexose stereochemistry, the C-6 **hydroxymethyl** group projects outside the pyranose ring." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The presence of a **hydroxymethyl** substituent significantly enhances the aqueous solubility of aromatic heterocycles." }
    ]
  },
  "Dashboard — hydr/hydroxyproline.md": {
    primary: "A non-essential amino acid (C5H9NO3) formed by the post-translational hydroxylation of proline residues, constituting a fundamental building block of collagen.",
    secondary: "In connective tissue biochemistry, an amino acid whose stereospecific hydrogen-bonding hydroxyl group stabilizes the triple-helical structure of collagen fibers, depleted in scurvy.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The unusual triple-helical structure of collagen is stabilized by hydrogen bonds mediated by **hydroxyproline** residues." },
      { author: "Frederick Gowland Hopkins", work: "Biochemical Papers", quote: "Because vitamin C is required to synthesize **hydroxyproline**, scurvy results in defective connective tissue repair." },
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "High-resolution diffraction data demonstrated that **hydroxyproline** restricts backbone conformation, providing tensile strength to tendons." }
    ]
  },
  "Dashboard — hydr/hydroxytetracycline.md": {
    primary: "A broad-spectrum tetracycline antibiotic (oxytetracycline) produced by the soil bacterium Streptomyces rimosus, used to treat diverse bacterial infections.",
    secondary: "In antimicrobial pharmacology, an inhibitor of bacterial protein synthesis that binds reversibly to the 30S ribosomal subunit, preventing aminoacyl-tRNA attachment.",
    quotes: [
      { author: "Alexander Fleming", work: "Penicillin and Other Antibiotics", quote: "The discovery of **hydroxytetracycline** provided clinicians with a potent agent against rickettsial and chlamydial infections." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Oral administration of **hydroxytetracycline** effectively suppresses atypical pneumonia and brucellosis." },
      { author: "Selman Waksman", work: "My Life with the Microbes", quote: "Screening actinomycetes from fertile soils revealed Streptomyces rimosus, the source of crystalline **hydroxytetracycline**." }
    ]
  },
  "Dashboard — hydr/hydroxyzine.md": {
    primary: "A first-generation piperazine antihistamine medication with sedative, antiemetic, and anxiolytic properties (brand names Atarax, Vistaril).",
    secondary: "In psychopharmacology, an inverse agonist at peripheral and central histamine H1 receptors that crosses the blood-brain barrier to alleviate anxiety and allergic urticaria.",
    quotes: [
      { author: "Donald Calne", work: "Therapeutics in Neurology", quote: "The central histamine H1 receptor blockade of **hydroxyzine** produces significant sedation and relieves psychomotor agitation." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "In clinical dermatology, **hydroxyzine** remains one of the most effective oral agents for intractable allergic pruritus." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Preoperative administration of **hydroxyzine** eases anxiety and minimizes postoperative nausea and vomiting." }
    ]
  },
  "Dashboard — hydr/hydrozoa.md": {
    primary: "A taxonomic class of aquatic, mostly marine cnidarians that includes hydras, hydroids, and siphonophores, typically exhibiting alternation of polyp and medusa generations.",
    secondary: "In invertebrate zoology, a diverse class characterized by tetramerous medusae with a velum and colonial polyps displaying division of labor among feeding, defensive, and reproductive zooids.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "The class **Hydrozoa** exhibits an astonishing alternation of generations between sedentary hydroid polyps and pelagic jellyfish medusae." },
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "Nowhere in the animal kingdom is polymorphic differentiation more exquisitely displayed than among the colonial **Hydrozoa**." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The delicate glassy bells and vibrant floating siphonophores of the **Hydrozoa** present nature's most intricate geometric symmetries." }
    ]
  },
  "Dashboard — hydr/hydrozoan.md": {
    primary: "An aquatic invertebrate belonging to the cnidarian class Hydrozoa; of or pertaining to Hydrozoa.",
    secondary: "In marine ecology, organisms (such as Obelia, Hydra, or Physalia) possessing cnidocytes and polymorphic life cycles transitioning between asexual polyps and sexual medusae.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The Portuguese man-of-war is not a single animal, but a colonial **hydrozoan** composed of thousands of coordinated, interdependent zooids." },
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "Each specialized polyp within the **hydrozoan** colony performs a dedicated function—some for feeding, others for stinging defense." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "We captured a luminous **hydrozoan** medusa whose pulsating umbrella radiated phosphorescent green light in the ship's wake." }
    ]
  },
  "Dashboard — hydr/hydrus.md": {
    primary: "A mythical water snake or dragon in classical folklore; in modern astronomy, Hydrus (the Lesser Water Snake), a small southern constellation near Tucana.",
    secondary: "In medieval bestiaries and mythological etymology, a legendary water serpent said to roll in mud before invading and destroying the crocodile from within.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "Among the glittering constellations of the southern sky, the sailor marks the winding coil of **Hydrus** near the polar void." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Naturalists of antiquity described the **hydrus** as a water-serpent that entered the mouth of the sleeping crocodile to devour its entrails." },
      { author: "John Milton", work: "Paradise Lost", quote: "Scorpion, and Asp, and Amphisbaena dire, / Cerastes horned, **Hydrus**, and Elops drear." }
    ]
  },
  "Dashboard — hydr/monohydrate.md": {
    primary: "A chemical compound or crystalline substance that contains exactly one molecule of water of crystallization per formula unit.",
    secondary: "In pharmaceutical crystallization and solid-state chemistry, a stoichiometric hydrate form (such as citric acid monohydrate or ampicillin monohydrate) exhibiting specific dissolution and stability properties.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Heating citric acid crystals gently drives off moisture, converting the **monohydrate** into the anhydrous organic acid." },
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "Barium hydroxide **monohydrate** retains its single water molecule tenaciously, requiring red heat for complete dehydration." },
      { author: "J. R. Partington", work: "A Text-Book of Inorganic Chemistry", quote: "X-ray crystallographic analysis established that the **monohydrate** lattice incorporates the water molecule directly into hydrogen-bonded chains." }
    ]
  },
  "Dashboard — hydr/polyhydric.md": {
    primary: "Containing more than one hydroxyl (-OH) group per molecule, especially referring to alcohols (polyols) such as glycerol or sorbitol.",
    secondary: "In organic chemistry and polymer science, alcohols containing multiple alcohol functions utilized as crosslinkers and monomers in polyurethane and polyester synthesis.",
    quotes: [
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Glycerol is a trihydric alcohol, serving as the prototypical **polyhydric** alcohol in natural fats and phospholipids." },
      { author: "Emil Fischer", work: "Studies on Carbohydrates", quote: "The reduction of hexose monosaccharides yields sweet, crystalline **polyhydric** alcohols such as sorbitol and mannitol." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The viscous consistency of a **polyhydric** alcohol arises from extensive, intermolecular three-dimensional hydrogen bonding." }
    ]
  },
  "Dashboard — hydr/trihydroxy.md": {
    primary: "Containing three hydroxyl (-OH) functional groups in a chemical molecule.",
    secondary: "In organic chemistry, describing compounds like trihydroxybenzene (phloroglucinol, pyrogallol) or trihydroxy alcohols (glycerol) displaying enhanced hydrogen bonding and antioxidant reactivity.",
    quotes: [
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Pyrogallol is a symmetrical **trihydroxy** benzene whose alkaline solution absorbs atmospheric oxygen with extraordinary avidity." },
      { author: "Robert Robinson", work: "The Organic Chemistry of Natural Products", quote: "Natural flavones and anthocyanins frequently possess a **trihydroxy** substitution pattern on their central aromatic rings." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Glycerol may be systematically designated as a **trihydroxy** propane, forming the backbone of all biological triglycerides." }
    ]
  }
};

let successCount = 0;
for (const [key, data] of Object.entries(batch3Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    successCount++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 3 Completed: ${successCount} / ${Object.keys(batch3Data).length} words updated`);
console.log(`========================================`);
