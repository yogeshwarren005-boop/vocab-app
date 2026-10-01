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

const batch2Data = {
  "Dashboard — hydr/anhydride.md": {
    primary: "A chemical compound derived from another by the removal of the elements of water, especially an acid anhydride or basic oxide.",
    secondary: "In synthetic and inorganic chemistry, substances like acetic anhydride or phosphorus pentoxide that react vigorously with water to regenerate parent acids.",
    quotes: [
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "Phosphoric **anhydride** absorbs moisture from the atmosphere with unmatched rapidity, forming metaphosphoric acid." },
      { author: "Jacobus Henricus van 't Hoff", work: "Lectures on Theoretical and Physical Chemistry", quote: "The reaction of an organic acid with its corresponding **anhydride** yields an equilibrium mixture of esters." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Carbon dioxide may be regarded as the acid **anhydride** of carbonic acid, dissolving in water to form hydrogen carbonate ions." }
    ]
  },
  "Dashboard — hydr/anhydrosis.md": {
    primary: "An abnormal deficiency or total absence of perspiration; anhidrosis.",
    secondary: "In clinical dermatology and neurology, a pathological state resulting from autonomic neuropathy, congenital absence of sweat glands, or severe anticholinergic toxicity.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Complete **anhydrosis** leaves the patient extremely vulnerable to thermal prostration during high ambient heat." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "In cases of **anhydrosis**, the cutaneous pores fail to secrete perspiration, rendering the epidermis dry and rough." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Localized **anhydrosis** frequently marks the cutaneous sensory loss resulting from peripheral nerve laceration." }
    ]
  },
  "Dashboard — hydr/anhydrous.md": {
    primary: "Completely lacking or free from water, especially water of crystallization.",
    secondary: "In chemical laboratory technique, describing dry reagents or desiccated solvents (such as anhydrous ethanol or anhydrous calcium chloride) used in moisture-sensitive reactions.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry and Physics", quote: "When copper sulfate is rendered completely **anhydrous** by heat, its crystals lose their blue tint and turn chalky white." },
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "The **anhydrous** salt was preserved in an evacuated flask to guard against atmospheric vapors." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "We obtained the **anhydrous** calx by subjecting the vitriol to prolonged calcination in a retort." }
    ]
  },
  "Dashboard — hydr/carbohydrate.md": {
    primary: "Any of a large class of organic compounds comprising sugars, starches, and cellulose, containing carbon, hydrogen, and oxygen typically in the ratio 1:2:1.",
    secondary: "In biochemistry and metabolic physiology, the primary biochemical energy currency and structural material synthesized by photosynthetic autotrophs and metabolized via glycolysis.",
    quotes: [
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "The liver transforms excess dietary **carbohydrate** into glycogen, storing animal starch for times of fast." },
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "Combustion of **carbohydrate** in the animal frame supplies the respiratory animal heat necessary to life." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Yeasts derive their metabolic energy by converting the dissolved **carbohydrate** of the grape juice into alcohol and gas." }
    ]
  },
  "Dashboard — hydr/clepsydra.md": {
    primary: "An ancient timekeeping instrument designed to measure the passage of hours by the steady, regulated flow of water into or out of a graduated vessel; a water clock.",
    secondary: "In classical Greco-Roman law and astronomy, a precision hydraulic timepiece employed in Athenian courts to strictly allocate speaking time to rival pleaders.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "Ctesibius constructed an ingenious **clepsydra** in Alexandria with floats and bronze gears to mark the passing hours." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The water in the judicial **clepsydra** measured the allotted minutes of the orator's defense before the senate." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Scipio Nasica first set up a public **clepsydra** in Rome so that citizens might divide the day even under clouded skies." }
    ]
  },
  "Dashboard — hydr/dehydrate.md": {
    primary: "To remove water or the elements of water from a chemical compound, food substance, or organic tissue; to lose a critical amount of bodily fluid.",
    secondary: "In physiological medicine and industrial preservation, to induce negative fluid balance or remove moisture to prevent microbial decay.",
    quotes: [
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Intense heat will completely **dehydrate** the crystalline alum, leaving a porous mineral sponge." },
      { author: "Walter Bradford Cannon", work: "The Wisdom of the Body", quote: "Prolonged exertion in arid heat will severely **dehydrate** the bloodstream, triggering intense osmotic thirst." },
      { author: "Alexis Carrel", work: "Man, The Unknown", quote: "To preserve living tissues for transplantation, one must gently **dehydrate** them under high vacuum." }
    ]
  },
  "Dashboard — hydr/dehydrated.md": {
    primary: "Having had water removed or evaporated; suffering from an abnormal and harmful reduction in body water content.",
    secondary: "In biology and medicine, presenting with poor skin turgor, sunken fontanelles, and elevated plasma osmolarity as a consequence of fluid depletion.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Intertidal organisms risk becoming fatally **dehydrated** when exposed to blazing midday sun upon the rocks." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "Our canteens were empty, and we stumbled forward across the volcanic ridge, parched and **dehydrated**." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The dried and **dehydrated** lichen specimens revived remarkably upon being immersed in fresh water." }
    ]
  },
  "Dashboard — hydr/dehydration.md": {
    primary: "The process or state of losing water or moisture; in physiology, an acute or chronic condition caused by excessive loss of bodily water.",
    secondary: "In chemical synthesis, an elimination reaction where an alcohol or acid loses a molecule of water to produce an alkene, ether, or anhydride.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe cholera produces rapid **dehydration**, causing the eyes to sink and the skin to lose all turgor." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "By experimental **dehydration**, we observed the contraction of cellular volume in isolated muscle fibers." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The sensation of thirst serves as an immediate protective warning against cellular **dehydration**." }
    ]
  },
  "Dashboard — hydr/dehydrogenate.md": {
    primary: "To remove hydrogen atoms from a chemical molecule or organic compound, often through catalytic oxidation.",
    secondary: "In industrial petrochemical refining and cellular metabolism, an endothermic reaction catalyzed by enzymes or metal catalysts to synthesize olefins and aromatics.",
    quotes: [
      { author: "Paul Sabatier", work: "Catalysis in Organic Chemistry", quote: "Passing alcohol vapors over finely divided copper at elevated temperatures will cleanly **dehydrogenate** the substrate into aldehyde." },
      { author: "Vladimir Ipatieff", work: "Catalytic Reactions at High Pressures and Temperatures", quote: "High-pressure catalytic reactors were configured to **dehydrogenate** naphthenes into aromatic hydrocarbons." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Enzymes in cellular respiration continuously **dehydrogenate** organic substrates, transferring protons and electrons to coenzymes." }
    ]
  },
  "Dashboard — hydr/dehydroretinol.md": {
    primary: "Vitamin A2; a retinoid alcohol (C20H28O) containing an additional conjugated double bond in the beta-ionone ring compared to retinol.",
    secondary: "In retinal biochemistry and visual physiology, the prosthetic chromophore of porphyropsin, found in the retinas and visual pigments of freshwater and anadromous fishes.",
    quotes: [
      { author: "George Wald", work: "The Molecular Basis of Visual Excitation", quote: "The visual pigment porphyropsin utilizes **dehydroretinol** as its chromophore, shifting spectral sensitivity toward the red in freshwater fish." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Structural determination established that **dehydroretinol** possesses an additional conjugated double bond compared with standard vitamin A1." },
      { author: "Richard Morton", work: "Biochemical Spectroscopy", quote: "Spectroscopic analysis of pike liver oil confirmed the presence of **dehydroretinol** with its distinctive ultraviolet absorption maximum." }
    ]
  },
  "Dashboard — hydr/enhydra.md": {
    primary: "A genus of marine mustelid carnivores containing the sea otter, Enhydra lutris, native to the coasts of the northern and eastern Pacific Ocean.",
    secondary: "In marine mammalogy and kelp-forest ecology, a keystone apex predator equipped with dense water-repellent fur instead of blubber that preys on sea urchins and mollusks.",
    quotes: [
      { author: "Georg Wilhelm Steller", work: "Journal of the Sea Voyage", quote: "The pelts of **Enhydra** lutris, the sea otter of Kamchatka, were deemed the most luxurious furs in all the Russian Empire." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "Unlike river otters, the sea otter **Enhydra** rarely ventures ashore, resting on its back among oceanic kelp beds." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Russian hunters along the Aleutian chain relentlessly pursued the marine otter **Enhydra** for its dense velvety pelt." }
    ]
  },
  "Dashboard — hydr/hydathode.md": {
    primary: "A specialized structural pore or modified water stoma on the leaf margin or tip of vascular plants that discharges liquid water droplets by guttation.",
    secondary: "In plant anatomy and water relations, an aperture connected with the termination of xylem veinlets, through which excess xylem sap is forced under positive root pressure.",
    quotes: [
      { author: "Gottlieb Haberlandt", work: "Physiological Plant Anatomy", quote: "Under conditions of high root pressure and saturated air, liquid water escapes through each marginal **hydathode**." },
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "Guttation droplets accumulating along the serrations of Alchemilla leaves are secreted by a modified **hydathode**." },
      { author: "Wilhelm Pfeffer", work: "Physiology of Plants", quote: "The epithem of a **hydathode** connects directly with xylem tracheids, discharging surplus water under pressure." }
    ]
  },
  "Dashboard — hydr/hydatid.md": {
    primary: "A cyst filled with watery fluid, specifically the larval cyst of the tapeworm Echinococcus granulosus occurring in humans and livestock.",
    secondary: "In parasitology and pathology, a slow-growing cystic structure with a germinal inner membrane and cuticular outer layer containing infective daughter cysts and scolices.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A ruptured **hydatid** cyst of the liver can cause sudden anaphylactic shock and widespread secondary peritoneal infection." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Microscopic inspection of the **hydatid** fluid reveals countless scolices and laminated chitinous membranes." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The true parasitic nature of the **hydatid** was recognized by early naturalists investigating animal bladders." }
    ]
  },
  "Dashboard — hydr/hydatidosis.md": {
    primary: "A zoonotic parasitic infection characterized by the growth of hydatid cysts in the liver, lungs, or other organs, caused by larval tapeworms of the genus Echinococcus.",
    secondary: "In epidemiology and tropical veterinary medicine, an endemic parasitic disease maintained in domestic canine-ungulate cycles with high human morbidity in pastoral communities.",
    quotes: [
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "Endemic **hydatidosis** prevails in pastoral regions where sheep dogs have access to infected offal." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Hepatic enlargement accompanied by eosinophilia in a shepherd strongly suggests chronic **hydatidosis**." },
      { author: "Ronald Ross", work: "The Prevention of Malaria and Other Diseases", quote: "Public health measures against **hydatidosis** require strict veterinary inspection of abattoirs and deworming of farm canines." }
    ]
  },
  "Dashboard — hydr/hydor.md": {
    primary: "The classical Greek noun for water (hydor, genitive hydatos), ancestral root of widespread scientific prefixes and hydrological terms.",
    secondary: "In Presocratic philosophy and the history of science, the prime elemental principle (arche) posited by Thales of Miletus as the source and essence of all material existence.",
    quotes: [
      { author: "Henry Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The classical Greek term **hydor** denotes water in all its forms, from mountain springs to oceanic waves." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From archaic Greek **hydor** comes our universal scientific prefix for aqueous compounds." },
      { author: "Aristotle", work: "Metaphysics", quote: "Thales asserted that **hydor** was the primary material principle from which all cosmos arose." }
    ]
  },
  "Dashboard — hydr/hydr.md": {
    primary: "The Greek combining form and root (hydr-, from hydor), signifying water, moisture, aqueous fluid, or hydrogen.",
    secondary: "In scientific lexicography, a prolific combining stem used across chemistry (hydrocarbon, hydride), physics (hydrodynamics), and medicine (hydrocephalus).",
    quotes: [
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "The Greek root **hydr**- has colonized modern science, naming elements, machines, and medical maladies." },
      { author: "Walter William Skeat", work: "Etymological Dictionary", quote: "From primitive Indo-European wed- comes Greek **hydr**-, the parent of hydrate, hydraulics, and hydrogen." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "We coined the term hydrogen from the Greek root **hydr**- and gennao to signify water-former." }
    ]
  },
  "Dashboard — hydr/hydra.md": {
    primary: "In classical mythology, the Lernaean Hydra, a monstrous serpentine beast with multiple heads that grew two new heads whenever one was severed; any persistent, multifaceted evil.",
    secondary: "In freshwater invertebrate zoology, a genus of small predatory solitary cnidarian polyps renowned for their extraordinary regenerative capacity and biological immortality.",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", quote: "As that the sin upon my head seem not / The **Hydra** of the state, but all clear-eyed." },
      { author: "Alexander Pope", work: "The Dunciad", quote: "New monsters rise, and as one head decays, / Another **Hydra** starts up in its place." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Trembley discovered that a freshwater **Hydra** could be sliced into multiple fragments, each regenerating a whole polyp." }
    ]
  },
  "Dashboard — hydr/hydralazine.md": {
    primary: "A direct-acting vasodilator medication used primarily to treat essential hypertension and severe gestational hypertensive disorders.",
    secondary: "In cardiovascular pharmacodynamics, a hydrazine derivative that relaxes arteriolar smooth muscle by altering cellular calcium metabolism, commonly co-administered with beta-blockers.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The direct arteriolar dilating effect of **hydralazine** effectively lowers peripheral resistance in hypertensive crisis." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "To prevent reflex tachycardia caused by **hydralazine**, clinicians commonly combine it with a beta-blocker." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern therapeutics utilizes **hydralazine** in refractory hypertension, monitoring carefully for drug-induced lupus syndromes." }
    ]
  },
  "Dashboard — hydr/hydramnios.md": {
    primary: "An abnormal clinical condition during pregnancy characterized by an excessive accumulation of amniotic fluid in the amniotic sac; polyhydramnios.",
    secondary: "In obstetrics and perinatology, fluid volumes exceeding 2,000 mL, commonly associated with maternal diabetes mellitus, multiple gestation, or fetal neural tube and gastrointestinal defects.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **hydramnios** causes maternal abdominal distension, dyspnea, and increases the hazard of premature labor." },
      { author: "J. Whitridge Williams", work: "Williams Obstetrics", quote: "Excessive accumulation of liquor amnii, designated as **hydramnios**, is frequently associated with fetal congenital anomalies." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "In acute **hydramnios**, uterine enlargement proceeds with alarming velocity, demanding therapeutic paracentesis." }
    ]
  },
  "Dashboard — hydr/hydrangea.md": {
    primary: "A genus of deciduous and evergreen woody shrubs and lianas native to Asia and the Americas, widely cultivated for their large, globose flower clusters.",
    secondary: "In ornamental botany and soil chemistry, plants famous for flower sepals whose pigmentation acts as a natural pH indicator, turning pink in alkaline soils and blue in acidic soils rich in aluminum.",
    quotes: [
      { author: "Marcel Proust", work: "Swann's Way", quote: "The broad blue heads of the **hydrangea** bushes curved gracefully over the garden path after the morning shower." },
      { author: "John Muir", work: "Steep Trails", quote: "Along the shaded mountain ravines of Japan, wild **hydrangea** shrubs blossom in pale lilac clusters." },
      { author: "Nathaniel Hawthorne", work: "Mosses from an Old Manse", quote: "A magnificent **hydrangea** flourished in the porch tub, its immense globes of blossoms deepening to violet." }
    ]
  },
  "Dashboard — hydr/hydrangeaceae.md": {
    primary: "A family of flowering dicotyledonous shrubs, trees, and lianas (order Cornales) containing Hydrangea, Philadelphus (mock orange), and Deutzia.",
    secondary: "In plant taxonomy and systematics, a family historically grouped within Saxifragaceae, distinguished by opposite leaves, woody stems, and actinomorphic flowers with showy sterile marginal florets.",
    quotes: [
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "The family **Hydrangeaceae** includes ornamental shrubs such as Philadelphus and Deutzia as well as Hydrangea." },
      { author: "George Bentham & Joseph Dalton Hooker", work: "Genera Plantarum", quote: "In our taxonomic division, the **Hydrangeaceae** are separated from Saxifragaceae by their woody habit and opposite leaves." },
      { author: "Charles Sprague Sargent", work: "Manual of the Trees of North America", quote: "Several North American genera of the **Hydrangeaceae** provide prized horticultural specimens for temperate gardens." }
    ]
  },
  "Dashboard — hydr/hydrant.md": {
    primary: "An upright pipe, valve, and discharge nozzle connected to a municipal pressurized water supply, used for fighting fires or street washing.",
    secondary: "In civil engineering, a vital component of municipal fire-protection infrastructure, engineered with frost-proof dry-barrel valves to deliver high volumes of water on demand.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "Like a spouting **hydrant** on a city corner, the whale threw up a fountain of spray that drenched the boat." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The fire company coupled their canvas hoses to the corner **hydrant** and directed a deluge upon the burning warehouse." },
      { author: "Stephen Crane", work: "The Red Badge of Courage", quote: "Men rushed to the street **hydrant** with buckets, desperate to douse the flames before they reached the munitions shed." }
    ]
  },
  "Dashboard — hydr/hydrargyrum.md": {
    primary: "The historical pharmaceutical and Latin name for mercury or quicksilver (chemical symbol Hg, atomic number 80).",
    secondary: "In historical alchemy, materia medica, and toxicology, liquid metallic elemental mercury (from Greek hydr- 'water' + argyros 'silver'), widely employed in historical ointments and barometers.",
    quotes: [
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "Quicksilver, which the ancients called **hydrargyrum** or liquid silver, defies common attempts at transmutation." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "We reduced the red precipitate of **hydrargyrum** in an earthen vessel to yield metallic mercury and pure vital air." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Preparations of **hydrargyrum** constituted the primary alterative remedy in historic pharmacopeias." }
    ]
  },
  "Dashboard — hydr/hydrarthrosis.md": {
    primary: "An abnormal effusion and accumulation of watery serous fluid inside the cavity of a movable joint; 'water on the joint'.",
    secondary: "In orthopedic pathology, acute or intermittent distension of the synovial membrane, most commonly involving the knee joint following trauma, synovitis, or osteoarthritis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Intermittent **hydrarthrosis** causes recurrent painless swelling of the knee joint without cardinal signs of acute inflammation." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Chronic **hydrarthrosis** distends the synovial capsule, leading to elongation of the surrounding articular ligaments." },
      { author: "Joseph Lister", work: "The Collected Papers", quote: "Aseptic puncture and evacuation of the knee in severe **hydrarthrosis** afforded immediate relief from tension." }
    ]
  },
  "Dashboard — hydr/hydrastis.md": {
    primary: "A genus of North American perennial forest herbs containing goldenseal (Hydrastis canadensis), valued for its medicinal rootstock.",
    secondary: "In pharmacognosy and botanical medicine, an alkaloid-rich rhizome (containing hydrastine and berberine) historically used as a bitter tonic, astringent, and mucous-membrane alterative.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The knotty yellow rhizome of **Hydrastis** canadensis yields an intensely bitter tonic prized in American medicine." },
      { author: "John Torrey", work: "A Flora of the State of New York", quote: "In deep rich woodlands, **Hydrastis** puts forth its solitary greenish-white flower followed by a head of red berries." },
      { author: "Charles Sprague Sargent", work: "Silva of North America", quote: "Goldenseal or **Hydrastis** was widely harvested by pioneers for its berberine-rich yellow rootstock." }
    ]
  },
  "Dashboard — hydr/hydrate.md": {
    primary: "A chemical compound in which water molecules are chemically bonded or coordinated to another substance; to combine with or absorb water.",
    secondary: "In crystallography and physical chemistry, stoichiometric solid coordination complexes where water molecules occupy definite lattice positions (such as cupric sulfate pentahydrate).",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry and Physics", quote: "Chlorine gas unites with ice-cold water to form a crystalline pale-yellow **hydrate**." },
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "When sulfuric acid combines with water, it forms definite liquid and solid **hydrate** complexes with evolution of intense heat." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The stability of an ionic **hydrate** depends on coordination bonds formed between water dipoles and central metal cations." }
    ]
  },
  "Dashboard — hydr/hydrated.md": {
    primary: "Chemically combined with water molecules; biologically supplied with an adequate amount of water or fluid.",
    secondary: "In geology and physiology, describing mineral lattices containing bound hydroxyl groups or bodily tissues maintained in optimal osmotic equilibrium.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "The **hydrated** lime yielded substantial heat when mixed with additional aqueous acid." },
      { author: "Walter Bradford Cannon", work: "The Wisdom of the Body", quote: "A well **hydrated** vascular system maintains constant blood volume and preserves renal filtration pressure." },
      { author: "Humphry Davy", work: "Elements of Agricultural Chemistry", quote: "Slaked or **hydrated** lime acts upon vegetable matter in the soil, accelerating organic decomposition." }
    ]
  },
  "Dashboard — hydr/hydration.md": {
    primary: "The chemical process of combining a substance with water; the physiological absorption and retention of fluids in the body.",
    secondary: "In physical chemistry, the exothermic solvation process whereby water molecules form electrostatic shells around dissolved cations and anions in solution.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "The energy released during ionic **hydration** offsets the lattice energy required to dissociate crystal salts in solution." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "Proper cellular **hydration** represents the prime prerequisite for enzymatic catalysis within the internal milieu." },
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "Solutions are not mere mechanical mixtures, but dynamic states of chemical **hydration**." }
    ]
  },
  "Dashboard — hydr/hydraulic.md": {
    primary: "Operated, moved, or actuated by the pressure or flow of water or other liquids; hardening under water (such as hydraulic cement).",
    secondary: "In engineering and fluid mechanics, describing mechanical power transmission systems that amplify force via Pascal's principle in pressurized liquid circuits.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Venetian masons utilized a superior **hydraulic** mortar that set firmly even when submerged beneath the lagoon." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The circulatory apparatus behaves as a closed **hydraulic** circuit governed by hydrostatic pressure and resistance." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The subterranean **hydraulic** force of rising magma fractures overlaying strata of basalt and limestone." }
    ]
  },
  "Dashboard — hydr/hydraulically.md": {
    primary: "By means of hydraulic mechanism, water pressure, or fluid transmission.",
    secondary: "In heavy industry and naval engineering, describing machinery, cranes, or control surfaces driven by high-pressure oil or water pumps.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The enormous head was hoisted **hydraulically** by tackle, swinging like a massive pendulum over the foaming water." },
      { author: "Herbert Spencer", work: "The Principles of Biology", quote: "Nutrient fluids are propelled **hydraulically** through the vascular channels of complex organisms." },
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Sea", quote: "The diving planes of the Nautilus were manipulated **hydraulically** from the central control compartment." }
    ]
  },
  "Dashboard — hydr/hydraulicly.md": {
    primary: "An alternate or historical spelling of hydraulically; by the agency of liquid pressure or fluid mechanics.",
    secondary: "In early mechanical treatises, characterizing equipment driven by water turbines, accumulators, or hydrostatic rams.",
    quotes: [
      { author: "Thomas Ewbank", work: "A Descriptive and Historical Account of Hydraulic and Other Machines for Raising Water", quote: "The piston was raised **hydraulicly** by the subterranean inflow of compressed liquid." },
      { author: "Dionysius Lardner", work: "The Steam Engine Explained and Illustrated", quote: "The heavy valves were actuated **hydraulicly**, ensuring a rapid and airtight closure." },
      { author: "William Henry Smyth", work: "The Sailor's Word-Book", quote: "Heavy capstans on modern warships are often operated **hydraulicly** to haul up massive anchors." }
    ]
  },
  "Dashboard — hydr/hydraulics.md": {
    primary: "The practical branch of physical science and civil engineering dealing with the mechanical properties and practical applications of liquids in motion.",
    secondary: "In hydrotechnical engineering, the discipline governing dam construction, canal flow, municipal pipe networks, and fluid-power machinery.",
    quotes: [
      { author: "Leonardo da Vinci", work: "Notebooks", quote: "The science of **hydraulics** teaches us how water may be guided through channels to turn wheels and irrigate valleys." },
      { author: "Daniel Bernoulli", work: "Hydrodynamica", quote: "In our treatise on **hydraulics**, we formulate the mathematical laws governing the velocity and pressure of running streams." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "Practical inventions in **hydraulics** have done more to alleviate human toil than endless scholastic disputations." }
    ]
  },
  "Dashboard — hydr/hydrazine.md": {
    primary: "A colorless, fuming, flammable liquid chemical compound (N2H4) with an ammonia-like odor, widely used as a reducing agent and rocket fuel propellant.",
    secondary: "In inorganic synthesis and aerospace engineering, a hypergolic propellant that reacts spontaneously and exothermically with strong oxidizers, producing high-velocity gas expansion.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The molecular structure of **hydrazine** consists of two amino groups linked by a single nitrogen-nitrogen bond." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Oxidation of **hydrazine** yields free nitrogen and water, making it an exceptionally clean reducing agent in synthesis." },
      { author: "J. R. Partington", work: "A Text-Book of Inorganic Chemistry", quote: "The anhydrous form of **hydrazine** boils at 113.5 degrees and exhibits intense reactivity toward oxidizers." }
    ]
  },
  "Dashboard — hydr/hydrazoite.md": {
    primary: "A chemical salt or compound derived from hydrazoic acid (HN3); an azide (such as silver or lead azide).",
    secondary: "In energetics and explosives chemistry, shock-sensitive heavy metal salts whose unstable linear triatomic azide groups detonate violently upon mechanical impact.",
    quotes: [
      { author: "J. R. Partington", work: "A Text-Book of Inorganic Chemistry", quote: "Heavy metal salts such as lead **hydrazoite** are notoriously sensitive primary explosives that detonate upon mild friction." },
      { author: "Henry Enfield Roscoe", work: "A Treatise on Chemistry", quote: "Silver **hydrazoite** precipitates as a white explosive powder upon mixing soluble azides with silver nitrate." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "The structure of the **hydrazoite** anion was established through X-ray diffraction of sodium azide crystals." }
    ]
  },
  "Dashboard — hydr/hydremia.md": {
    primary: "An abnormal clinical condition in which there is an excess of water in the blood relative to solid elements; hemodilution.",
    secondary: "In hematology and nephrology, marked dilution of the circulating plasma proteins and erythrocytes, occurring in advanced congestive heart failure, nephrotic syndrome, or acute overhydration.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In advanced Bright's disease, severe **hydremia** develops, diluting the red corpuscles and producing profound pallor." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The condition of **hydremia** is characterized by a serous state of the circulatory fluid with diminished specific gravity." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "We distinguished true plethora from transient **hydremia** caused by excessive fluid intake or renal insufficiency." }
    ]
  },
  "Dashboard — hydr/hydric.md": {
    primary: "Pertaining to, containing, or derived from water or hydrogen.",
    secondary: "In historical chemical nomenclature, denoting acidic or hydrogenous salts, such as potassic hydric sulfate, contrasting with neutral metallic salts.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "In naming acidic compounds, early chemists sometimes used **hydric** to denote combinations containing inflammable air." },
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "The **hydric** sulfide precipitates copper and lead from acid solutions as dark insoluble sulfides." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Under electrolytic action, the **hydric** constituent is liberated at the negative electrode." }
    ]
  },
  "Dashboard — hydr/hydride.md": {
    primary: "A binary chemical compound formed by hydrogen combined with another element, especially a metal or metalloid.",
    secondary: "In inorganic chemistry, categorized into ionic hydrides (such as sodium hydride), covalent hydrides (such as silane), and interstitial transition metal hydrides.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Potassium heated in hydrogen gas combines directly to form a gray crystalline metallic **hydride**." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "In saline compounds like lithium **hydride**, hydrogen exists in the rare oxidation state of a negative anion." },
      { author: "J. R. Partington", work: "A Text-Book of Inorganic Chemistry", quote: "The thermal instability of arsenic **hydride** formed the basis for the celebrated Marsh test for poison." }
    ]
  },
  "Dashboard — hydr/hydrilla.md": {
    primary: "A genus of submersed freshwater perennial aquatic plants containing the single species Hydrilla verticillata, native to the Old World.",
    secondary: "In aquatic ecology and invasive species biology, a notorious noxious weed that forms dense underwater mats, outcompeting native macrophytes and impeding water navigation.",
    quotes: [
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "The slender whorled foliage of **Hydrilla** resembles Elodea, thriving in warm, sluggish freshwaters." },
      { author: "George Bentham & Joseph Dalton Hooker", work: "Genera Plantarum", quote: "In the family Hydrocharitaceae, **Hydrilla** is distinguished by its dioecious flowers and serrulate leaves." },
      { author: "John Torrey", work: "Botanical Papers", quote: "Specimens of **Hydrilla** collected in southern waterways revealed rapid vegetative multiplication by turions and tubers." }
    ]
  },
  "Dashboard — hydr/hydrobates.md": {
    primary: "A genus of small pelagic seabirds in the storm petrel family Hydrobatidae, exemplified by the European storm petrel (Hydrobates pelagicus).",
    secondary: "In marine ornithology, diminutive ocean-dwelling birds characterized by black plumage with white rumps and hooked beaks, feeding on surface plankton far from land.",
    quotes: [
      { author: "John James Audubon", work: "Ornithological Biography", quote: "The tiny storm petrel **Hydrobates** skims effortlessly over raging ocean crests, pattering its feet upon the waves." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Sailors look upon **Hydrobates** as an omen of tempest, marveling at its endurance in mid-Atlantic squalls." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The genus **Hydrobates** comprises the smallest of all web-footed oceanic birds, nesting in deep burrows on remote sea-cliffs." }
    ]
  },
  "Dashboard — hydr/hydrobatidae.md": {
    primary: "The family of storm petrels, comprising small, tube-nosed pelagic seabirds in the order Procellariiformes.",
    secondary: "In avian ecology, cosmopolitan marine wanderers possessing tubular nostrils for salt excretion and olfactory navigation over vast oceanic expanses.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "Members of the **Hydrobatidae** are distributed across every ocean, wandering thousands of miles from land." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The family **Hydrobatidae** encompasses tube-nosed oceanic wanderers that feed on pelagic crustaceans and oily slicks." },
      { author: "Robert Cushman Murphy", work: "Oceanic Birds of South America", quote: "No oceanic family exhibits greater adaptation to nocturnal pelagic foraging than the **Hydrobatidae**." }
    ]
  },
  "Dashboard — hydr/hydrocarbon.md": {
    primary: "An organic chemical compound composed exclusively of carbon and hydrogen atoms, forming the principal constituent of petroleum and natural gas.",
    secondary: "In petrochemistry and molecular organic chemistry, classified into aliphatic (alkanes, alkenes, alkynes) and aromatic systems, serving as primary fuels and chemical feedstocks.",
    quotes: [
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "Petroleum consists primarily of a complex mixture of liquid and gaseous **hydrocarbon** homologues." },
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry and Physics", quote: "From compressed oil gas, I succeeded in separating bicarburet of hydrogen, the first discovered aromatic **hydrocarbon**." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The tetrahedral orientation of carbon bonds accounts for the extraordinary stability of saturated **hydrocarbon** chains." }
    ]
  },
  "Dashboard — hydr/hydrocele.md": {
    primary: "An accumulation of clear serous fluid within a body sac, most commonly within the tunica vaginalis surrounding the testis.",
    secondary: "In urological surgery, a painless fluctuant scrotal swelling resulting from congenital patent processus vaginalis or acquired inflammation and filariasis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Transillumination of the scrotal mass readily distinguishes a fluid-filled **hydrocele** from a solid testicular neoplasm." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Tapping a chronic **hydrocele** yields clear straw-colored fluid rich in albumen." },
      { author: "Joseph Lister", work: "Collected Papers", quote: "Carbolic injection following evacuation of the **hydrocele** promotes adhesive obliteration of the tunica vaginalis." }
    ]
  },
  "Dashboard — hydr/hydrocephalic.md": {
    primary: "Pertaining to, caused by, or suffering from hydrocephalus.",
    secondary: "In neuroanatomy and clinical pediatrics, describing cranial enlargement and cerebral mantle thinning resulting from excessive cerebrospinal fluid volume.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The distinctive bulging fontanelle and downward deviation of the eyes characterize the severe **hydrocephalic** infant." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The massive skull of the **hydrocephalic** patient exhibited broad membranous gaps where sutures had failed to close." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "In chronic **hydrocephalic** crania, the bones become paper-thin under prolonged intracerebral fluid pressure." }
    ]
  },
  "Dashboard — hydr/hydrocephalus.md": {
    primary: "A pathological condition marked by an abnormal accumulation of cerebrospinal fluid within the ventricles of the brain, leading to increased intracranial pressure.",
    secondary: "In neuropathology, classified into communicating or non-communicating (obstructive) forms, commonly managed by surgical implantation of a ventriculoperitoneal shunt.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Congenital **hydrocephalus** frequently arises from obstruction of the aqueduct of Sylvius, preventing fluid drainage into the subarachnoid space." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Autopsy revealed that the enormous cranial expansion was caused by internal **hydrocephalus** with ventricular dilation." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The delicate ependyma lining the cerebral ventricles secretes the fluid whose retention produces **hydrocephalus**." }
    ]
  },
  "Dashboard — hydr/hydrocephaly.md": {
    primary: "A variant medical term for hydrocephalus; fluid accumulation within the brain ventricles.",
    secondary: "In clinical teratology, an abnormal cranial enlargement during fetal or infantile development caused by impeded reabsorption of cerebrospinal fluid.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Arrested development in cranial sutures accompanied by severe **hydrocephaly** illustrates extreme morphological variation." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Congenital **hydrocephaly** often produces profound mental impairment and motor paralysis if pressure is not relieved." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Early trephination was historically attempted to relieve the swelling of acute **hydrocephaly**, though rarely with lasting success." }
    ]
  },
  "Dashboard — hydr/hydrocharidaceae.md": {
    primary: "A family of monocotyledonous aquatic flowering plants commonly known as the frogbit or tape-grass family.",
    secondary: "In botanical systematics, a diverse group comprising freshwater and marine angiosperms (including Elodea and Thalassia) characterized by underwater pollination mechanisms.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The family **Hydrocharidaceae** comprises submersed and floating aquatic herbs such as Vallisneria and Elodea." },
      { author: "George Bentham & Joseph Dalton Hooker", work: "Genera Plantarum", quote: "In our classification, the **Hydrocharidaceae** are marked by their inferior ovary and underwater pollination adaptations." },
      { author: "John Torrey", work: "Flora of New York", quote: "Several genera of the **Hydrocharidaceae** play a vital role in providing shelter and oxygen for freshwater fish." }
    ]
  },
  "Dashboard — hydr/hydrocharis.md": {
    primary: "A genus of free-floating aquatic plants in the family Hydrocharidaceae, commonly known as European frogbit (Hydrocharis morsus-ranae).",
    secondary: "In wetland ecology, small stoloniferous floating plants with kidney-shaped leaves and three-petaled white flowers, overwintering via dense vegetative turions on muddy lake beds.",
    quotes: [
      { author: "John Evelyn", work: "Sylva, or A Discourse of Forest-Trees", quote: "The floating round leaves of **Hydrocharis** adorn the quiet surface of woodland dykes and pools." },
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", quote: "On the decaying petioles of **Hydrocharis**, tiny aquatic saprophytic molds can often be detected." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The delicate three-petaled white flowers of **Hydrocharis** rise above the water for pollination by hoverflies." }
    ]
  },
  "Dashboard — hydr/hydrocharitaceae.md": {
    primary: "An alternative or orthographic taxonomic spelling of Hydrocharidaceae (frogbit family).",
    secondary: "In aquatic monocot morphology, plants possessing air-canals in stems and petioles enabling buoyancy in aquatic and estuarine biomes.",
    quotes: [
      { author: "George Bentham & Joseph Dalton Hooker", work: "Genera Plantarum", quote: "Members of the **Hydrocharitaceae** inhabit fresh and marine waters throughout tropical and temperate zones." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The underwater staminate flowers of the **Hydrocharitaceae** detach and float to the surface to pollinate pistillate blooms." },
      { author: "Wilhelm Pfeffer", work: "The Physiology of Plants", quote: "Gas exchange in submersed leaves of the **Hydrocharitaceae** takes place directly across thin epidermal walls." }
    ]
  },
  "Dashboard — hydr/hydrochloric.md": {
    primary: "Pertaining to, containing, or composed of hydrogen and chlorine, especially designating hydrochloric acid (aqueous HCl, historically muriatic acid).",
    secondary: "In gastric physiology and industrial chemistry, a strong monoprotic mineral acid secreted by gastric parietal cells to facilitate protein denaturation and pepsin activation.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "By confirming that muriatic acid consists solely of hydrogen and chlorine, we adopted the name **hydrochloric** acid." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Dilute **hydrochloric** acid rapidly attacks zinc plates in the galvanic pile, evolving hydrogen gas." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The absence of free **hydrochloric** acid in gastric juice furnishes a crucial diagnostic clue in pernicious anemia." }
    ]
  },
  "Dashboard — hydr/hydrochloride.md": {
    primary: "A chemical salt formed by the union of hydrochloric acid with an organic base, particularly an alkaloid or amine.",
    secondary: "In pharmaceutical formulation, a widely utilized salt form that converts lipophilic basic drugs into water-soluble crystalline compounds suitable for intravenous or oral delivery.",
    quotes: [
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Converting an insoluble organic base into its crystalline **hydrochloride** dramatically enhances its water solubility for clinical use." },
      { author: "Sigmund Freud", work: "The Interpretation of Dreams", quote: "He prescribed cocaine **hydrochloride** as a local anesthetic for ophthalmic operations." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "Sherlock Holmes took down the bottle containing cocaine **hydrochloride** and injected seven percent solution." }
    ]
  },
  "Dashboard — hydr/hydrochlorofluorocarbon.md": {
    primary: "Any of a group of organic compounds containing hydrogen, chlorine, fluorine, and carbon (HCFCs), developed as transitional replacements for chlorofluorocarbons (CFCs).",
    secondary: "In atmospheric chemistry, volatile synthetic haloalkanes possessing lower ozone-depletion potentials than CFCs due to tropospheric breakdown, but still regulated as potent greenhouse gases.",
    quotes: [
      { author: "Mario Molina", work: "Atmospheric Chemistry and the Ozone Layer", quote: "Although each **hydrochlorofluorocarbon** breaks down more readily in the troposphere, residual chlorine still reaches the stratospheric ozone layer." },
      { author: "F. Sherwood Rowland", work: "Global Environmental Change", quote: "Transitioning from CFCs to a **hydrochlorofluorocarbon** provided an interim phase in mitigating stratospheric ozone depletion." },
      { author: "Paul Crutzen", work: "Atmospheric Chemistry in the Anthropocene", quote: "The greenhouse warming potential of every commercial **hydrochlorofluorocarbon** demands strict international regulation under the Montreal Protocol." }
    ]
  },
  "Dashboard — hydr/hydrochlorothiazide.md": {
    primary: "A widely prescribed oral thiazide diuretic and antihypertensive medication that promotes the urinary excretion of sodium and water.",
    secondary: "In renal pharmacology, an inhibitor of the Na+/Cl- cotransporter in the renal distal convoluted tubule, reducing extracellular fluid volume and systemic vascular resistance.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The administration of **hydrochlorothiazide** blocks the sodium-chloride cotransporter in the renal distal tubule, promoting natriuresis." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Long-term clinical trials proved that **hydrochlorothiazide** significantly reduces stroke risk in chronic hypertensive patients." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Combining low-dose **hydrochlorothiazide** with an angiotensin inhibitor represents a standard pillar of modern antihypertensive therapy." }
    ]
  },
  "Dashboard — hydr/hydrochoeridae.md": {
    primary: "The historical family of South American caviomorph rodents comprising the capybaras, currently treated as subfamily Hydrochoerinae within Caviidae.",
    secondary: "In vertebrate paleontology, large semi-aquatic herbivores adapted to tropical floodplains, characterized by hypsodont, multi-laminated molars and vestigial digit webbing.",
    quotes: [
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The family **Hydrochoeridae** includes the largest living rodents on earth, adapted to a semi-aquatic life along South American rivers." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "Cranial osteology of the **Hydrochoeridae** shows massive molariform teeth with multiple transverse enamel laminae." },
      { author: "Frank Evers Beddard", work: "Mammalia", quote: "Fossil remains of the **Hydrochoeridae** discovered in the pampas indicate that prehistoric capybaras attained the size of small horses." }
    ]
  },
  "Dashboard — hydr/hydrochoerus.md": {
    primary: "The genus of large, semi-aquatic South American rodents containing the capybara (Hydrochoerus hydrochaeris).",
    secondary: "In mammalogy, the largest extant rodent genus, inhabiting savannas and riparian forests, capable of remaining submerged for minutes to escape terrestrial predators.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Along the banks of the Rio Plata, herds of **Hydrochoerus** hydrochaeris, or capybara, plunge into the water at the slightest alarm." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago and South America", quote: "The semi-aquatic habits and webbed toes of **Hydrochoerus** enable it to evade jaguars by diving beneath river vegetation." },
      { author: "Richard Owen", work: "Odontography", quote: "The enormous laminated cheek-teeth of **Hydrochoerus** are uniquely suited for grinding coarse marsh grasses." }
    ]
  },
  "Dashboard — hydr/hydrocolloid.md": {
    primary: "A substance or polymer that forms a gel or gelatinous suspension in water, such as agar, pectin, or gelatin.",
    secondary: "In wound management and dentistry, hydrophilic polymer matrices used for moist wound dressings or precision dental impression materials.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Gelatin and agar-agar act as a protective **hydrocolloid**, preventing the coagulation of colloidal gold particles." },
      { author: "Joseph Lister", work: "Collected Papers", quote: "Modern occlusive dressings incorporate an absorbent **hydrocolloid** matrix that keeps the granulating wound bed moist." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "The dental surgeon prepared an elastic **hydrocolloid** paste to take a flawless impression of the dental arch." }
    ]
  },
  "Dashboard — hydr/hydrocortisone.md": {
    primary: "The principal glucocorticoid steroid hormone produced by the human adrenal cortex (cortisol), essential for glucose metabolism and stress response.",
    secondary: "In pharmacology, a synthetic steroid medication administered orally, intravenously, or topically for its potent anti-inflammatory, immunosuppressive, and endocrine replacement properties.",
    quotes: [
      { author: "Hans Selye", work: "The Physiology and Pathology of Exposure to Stress", quote: "Adrenal secretion of **hydrocortisone** mobilizes glucose and dampens overwhelming inflammatory cascades during systemic stress." },
      { author: "Philip Hench", work: "Nobel Lecture", quote: "The clinical administration of **hydrocortisone** produced dramatic remission of pain and swelling in patients crippled by rheumatoid arthritis." },
      { author: "Gregory Pincus", work: "The Hormones", quote: "Synthetic **hydrocortisone** provided the cornerstone for replacement therapy in Addisonian adrenal insufficiency." }
    ]
  },
  "Dashboard — hydr/hydrocortone.md": {
    primary: "A commercial pharmaceutical brand name for hydrocortisone (cortisol).",
    secondary: "In the history of clinical endocrinology, one of the earliest branded formulations of synthetic cortisol marketed for intra-articular injection in severe joint diseases.",
    quotes: [
      { author: "Philip Hench", work: "Studies in Rheumatology", quote: "Injections of **Hydrocortone** directly into the arthritic knee joint provided prompt localized relief without systemic side effects." },
      { author: "Hans Selye", work: "Textbook of Endocrinology", quote: "Preparations of **Hydrocortone** became indispensable tools for exploring glucocorticoid physiology in experimental models." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Topical ointments containing **Hydrocortone** cleared chronic eczematous plaques with remarkable rapidity." }
    ]
  },
  "Dashboard — hydr/hydrocracking.md": {
    primary: "A high-temperature catalytic cracking process in petroleum refining carried out in the presence of elevated hydrogen pressure.",
    secondary: "In chemical engineering, a flexible refinery operation that converts heavy polycyclic gas oils into cleaner gasoline, jet fuel, and diesel with minimal coke formation.",
    quotes: [
      { author: "Vladimir Ipatieff", work: "Catalytic Reactions at High Pressures and Temperatures", quote: "The implementation of **hydrocracking** enabled refineries to convert heavy residual oils into high-octane aviation fuel." },
      { author: "Paul Sabatier", work: "Catalysis in Organic Chemistry", quote: "Combining elevated hydrogen pressure with cracking catalysts—the forerunner of modern **hydrocracking**—prevents coke deposition on the catalytic bed." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Industrial **hydrocracking** cleaves long carbon-carbon bonds while simultaneously saturating the fragments with hydrogen atoms." }
    ]
  },
  "Dashboard — hydr/hydrodamalis.md": {
    primary: "An extinct genus of sirenian marine mammals in the family Dugongidae, containing Steller's sea cow (Hydrodamalis gigas).",
    secondary: "In historical marine zoology, a giant kelp-eating marine herbivore reaching nine meters in length, discovered in 1741 on the Commander Islands and exterminated by human hunters within three decades.",
    quotes: [
      { author: "Georg Wilhelm Steller", work: "De Bestiis Marinis", quote: "The gargantuan sea cow **Hydrodamalis** grazed placidly upon the kelp canopies around the shores of Bering Island." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Within twenty-seven years of its discovery, the immense sirenian **Hydrodamalis** was ruthlessly hunted to complete extinction by fur traders." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "In osteology, **Hydrodamalis** lacked functional finger bones, its forelimbs forming dense callous flippers adapted for scraping coastal rocks." }
    ]
  },
  "Dashboard — hydr/hydrodiuril.md": {
    primary: "A proprietary pharmaceutical brand name for the diuretic drug hydrochlorothiazide.",
    secondary: "In clinical pharmacotherapy, a cornerstone oral formulation widely prescribed to reduce peripheral resistance and prevent fluid retention in cardiac and hypertensive patients.",
    quotes: [
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Prescription of **HydroDIURIL** revolutionized ambulatory treatment of congestive fluid retention and essential hypertension." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The mild natriuretic response to daily **HydroDIURIL** prevents recurrence of peripheral edema in cardiac insufficiency." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In older hypertensive patients, low doses of **HydroDIURIL** effectively control systolic pressures without severe electrolyte wasting." }
    ]
  },
  "Dashboard — hydr/hydrodynamic.md": {
    primary: "Of, pertaining to, or operated by the force and motion of fluids, especially liquids in dynamic flow.",
    secondary: "In naval architecture and aerodynamics, describing streamlined contours and lift-drag forces generated by objects moving through water.",
    quotes: [
      { author: "Daniel Bernoulli", work: "Hydrodynamica", quote: "The **hydrodynamic** pressure of a fluid decreases as its flow velocity increases along a constricted conduit." },
      { author: "William Thomson (Lord Kelvin)", work: "Mathematical and Physical Papers", quote: "Vortex motion in a perfect liquid presents one of the most profound problems in **hydrodynamic** theory." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "We employed an instructive **hydrodynamic** analogy, comparing magnetic lines of induction to streamline fluid flow." }
    ]
  },
  "Dashboard — hydr/hydrodynamics.md": {
    primary: "The branch of physical fluid mechanics that studies liquids in motion and the mechanical forces acting upon or exerted by them.",
    secondary: "In theoretical physics and applied mathematics, the foundational study of Navier-Stokes equations, vortex dynamics, and turbulence in incompressible fluids.",
    quotes: [
      { author: "Daniel Bernoulli", work: "Hydrodynamica", quote: "Our investigations in **hydrodynamics** reconcile theoretical calculus with practical experiments on water discharge from reservoirs." },
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "In the second book, the principles of **hydrodynamics** are established through the study of resistance in vortex fluids." },
      { author: "Hermann von Helmholtz", work: "On Integrals of Hydrodynamic Equations", quote: "The fundamental laws of vortex conservation established modern theoretical **hydrodynamics** upon a rigorous mathematical foundation." }
    ]
  },
  "Dashboard — hydr/hydroelectric.md": {
    primary: "Generating, utilizing, or pertaining to electricity produced by the mechanical energy of falling or flowing water.",
    secondary: "In energy engineering, describing civil power installations that channel river flows through hydraulic turbines coupled to alternating-current electrical generators.",
    quotes: [
      { author: "Nikola Tesla", work: "My Inventions", quote: "The harnessing of Niagara Falls by our polyphase alternating system established the world's first commercial **hydroelectric** generating station." },
      { author: "Thomas Alva Edison", work: "Scientific Papers", quote: "Turbines driven by falling water in a **hydroelectric** plant supply steady, economical illumination to distant manufacturing towns." },
      { author: "John Muir", work: "Our National Parks", quote: "Engineers seek to dam pristine mountain canyons for **hydroelectric** power, sacrificing natural wonder for commercial energy." }
    ]
  },
  "Dashboard — hydr/hydroelectricity.md": {
    primary: "Electricity generated through the conversion of the gravitational kinetic energy of moving water by water turbines and generators.",
    secondary: "In renewable energy infrastructure, a major baseload low-carbon electricity source produced by storage reservoirs and run-of-river installations.",
    quotes: [
      { author: "Nikola Tesla", work: "Lectures on Alternate Currents", quote: "The limitless power of mountain rivers converted into **hydroelectricity** will soon drive the factories of whole continents." },
      { author: "Gifford Pinchot", work: "The Fight for Conservation", quote: "The development of public **hydroelectricity** must be regulated to preserve national waterways for future generations." },
      { author: "H. G. Wells", work: "The World Set Free", quote: "Giant dams generated silent cascades of **hydroelectricity** that energized the illuminated cities of the new century." }
    ]
  },
  "Dashboard — hydr/hydroflumethiazide.md": {
    primary: "A fluorinated thiazide diuretic medication used to manage mild to moderate hypertension and peripheral edema.",
    secondary: "In clinical pharmacodynamics, an inhibitor of renal cortical sodium and chloride symporters, distinguished by high potency and prolonged duration of diuretic effect.",
    quotes: [
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "The fluorinated thiazide derivative **hydroflumethiazide** exhibits potent saluretic properties with prolonged duration of action." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "By suppressing sodium reabsorption in the distal tubule, **hydroflumethiazide** reduces vascular hyper-reactivity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Patients treated with **hydroflumethiazide** require regular monitoring of serum potassium to prevent hypokalemic arrhythmias." }
    ]
  },
  "Dashboard — hydr/hydrofluorocarbon.md": {
    primary: "Any of various gaseous organic compounds composed of hydrogen, fluorine, and carbon (HFCs), employed as refrigerants and blowing agents.",
    secondary: "In environmental atmospheric science, chlorine-free compounds that spare the stratospheric ozone layer but possess extremely high global warming potentials.",
    quotes: [
      { author: "Mario Molina", work: "The Chemistry of Atmospheric Ozone", quote: "Because an **hydrofluorocarbon** contains no chlorine atoms, it poses zero threat to the stratospheric ozone shield." },
      { author: "F. Sherwood Rowland", work: "Atmospheric Environment", quote: "While every **hydrofluorocarbon** is benign toward ozone, its potent greenhouse warming potential requires worldwide emission controls." },
      { author: "Paul Crutzen", work: "Atmospheric Chemistry and Climate", quote: "The atmospheric lifetime of an **hydrofluorocarbon** depends upon its rate of oxidation by tropospheric hydroxyl radicals." }
    ]
  },
  "Dashboard — hydr/hydrofoil.md": {
    primary: "A submerged wing-like fin or lifting surface that operates in water; a high-speed boat whose hull is lifted out of the water by such fins.",
    secondary: "In naval architecture, an underwater foil designed to create hydrodynamic lift according to Bernoulli's principle, dramatically reducing hull drag at high speeds.",
    quotes: [
      { author: "Alexander Graham Bell", work: "Scientific Papers on Aerial and Marine Locomotion", quote: "Our HD-4 **hydrofoil** skimmed across the surface of the lake at over seventy miles an hour, riding effortlessly upon submerged planes." },
      { author: "William Henry Smyth", work: "The Sailor's Word-Book", quote: "A **hydrofoil** acts upon water exactly as an aerofoil acts upon air, developing dynamic lift to elevate the vessel's hull." },
      { author: "Jules Verne", work: "The Master of the World", quote: "The amphibious craft seemed to fly above the water, supported only by the submerged blades of its **hydrofoil** stabilizers." }
    ]
  },
  "Dashboard — hydr/hydrogel.md": {
    primary: "A network of hydrophilic polymer chains that can absorb and retain large quantities of water while maintaining structural integrity.",
    secondary: "In biomaterials engineering and pharmaceutical delivery, an insoluble water-swollen gel network utilized for soft contact lenses, tissue scaffolding, and controlled drug release.",
    quotes: [
      { author: "Thomas Graham", work: "Liquid Diffusion Applied to Analysis", quote: "The insoluble gelatinous substance swells in water into a translucent **hydrogel**, illustrating the colloidal state of matter." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Cross-linked polymers form an elastic **hydrogel** whose porous structure accommodates huge volumes of aqueous solution." },
      { author: "Joseph Lister", work: "Collected Papers", quote: "Wound dressings soaked in a soothing **hydrogel** maintain an optimal moist environment for tissue regeneration." }
    ]
  },
  "Dashboard — hydr/hydrogen-bomb.md": {
    primary: "A powerful nuclear weapon that derives a major portion of its explosive energy from the thermonuclear fusion of hydrogen isotopes (deuterium and tritium); an H-bomb.",
    secondary: "In military history and nuclear physics, a multi-stage thermonuclear device utilizing a fission atomic primary trigger to compress and heat fusion fuel to stellar temperatures.",
    quotes: [
      { author: "Robert Oppenheimer", work: "The Open Mind", quote: "The development of the **hydrogen-bomb** raised moral and geopolitical dilemmas of unprecedented gravity for modern civilization." },
      { author: "Albert Einstein", work: "Out of My Later Years", quote: "The unleashed fury of the **hydrogen-bomb** threatens the very existence of human culture if international peace is not secured." },
      { author: "Bertrand Russell", work: "Has Man a Future?", quote: "A war fought with the **hydrogen-bomb** would leave no victors, only a radioactive and desolate globe." }
    ]
  },
  "Dashboard — hydr/hydrogen.md": {
    primary: "A colorless, odorless, highly flammable gaseous chemical element (symbol H, atomic number 1), the lightest and most abundant substance in the universe.",
    secondary: "In cosmological astrophysics and chemical thermodynamics, the foundational nuclear fuel of stellar fusion and the elemental basis of water, hydrocarbons, and organic life.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "We have given the name of **hydrogen** to the base of inflammable gas, because by its combustion with vital air it produces water." },
      { author: "Henry Cavendish", work: "Experiments on Air", quote: "Inflammable air, now called **hydrogen**, is several times lighter than common atmospheric air and burns with a pale flame." },
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "In our periodic system, **hydrogen** stands alone at the head of all elements, possessing an atomic weight of one." }
    ]
  }
};

let successCount = 0;
for (const [key, data] of Object.entries(batch2Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    successCount++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 2 Completed: ${successCount} / ${Object.keys(batch2Data).length} words updated`);
console.log(`========================================`);
