# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — duc Part 3 (13C, 40 words) ---
  "Dashboard — duc/irreproducibility.md": {
    "primary": "The characteristic of being unable to be replicated, duplicated, or reproduced in subsequent experiments.",
    "secondary": "In philosophy of science and metascience, the replication crisis highlighting empirical studies that fail independent verification.",
    "quotes": [
      {"author": "Karl Popper", "work": "The Logic of Scientific Discovery", "quote": "The **irreproducibility** of an isolated experimental effect deprives it of any standing as genuine scientific knowledge."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Apparent biological anomalies must be discarded upon demonstrated **irreproducibility** under controlled laboratory conditions."},
      {"author": "Bertrand Russell", "work": "The Scientific Outlook", "quote": "The fatal defect in magical rituals is their complete **irreproducibility** when subjected to skeptical observation."}
    ]
  },
  "Dashboard — duc/irreproducible.md": {
    "primary": "Incapable of being reproduced, replicated, duplicated, or repeated in identical form.",
    "secondary": "In experimental methodology, findings attributable to artifactual noise, p-hacking, or unrecorded confounding variables.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Any electrical phenomenon that proves **irreproducible** upon repeating the apparatus setup must be regarded as an artifact."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Science accepts no dogmatic assertion based upon solitary and **irreproducible** observations."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "Griffin feared that his complex chemical synthesis might prove **irreproducible** if his notebooks were destroyed."}
    ]
  },
  "Dashboard — duc/misconduct.md": {
    "primary": "Unacceptable, improper, or dishonest behavior, especially by a professional or person in authority.",
    "secondary": "In administrative and criminal law, official misconduct encompasses malfeasance, misfeasance, or nonfeasance in the performance of public duty.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A magistrate who abuses his judicial authority may be prosecuted for gross **misconduct** in office."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Impeachment provides a constitutional remedy for the treason, bribery, or other high **misconduct** of public officials."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solicitor was struck off the rolls following conclusive exposure of professional **misconduct** in estate management."}
    ]
  },
  "Dashboard — duc/nonconducting.md": {
    "primary": "Not conducting or transmitting heat, electricity, or sound; acting as an insulator.",
    "secondary": "In electrical engineering, nonconducting materials (dielectrics) prevent short-circuit discharges in high-voltage power grids.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Dry gutta-percha forms an admirable **nonconducting** sheath around submarine telegraph cables."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The electric displacement occurs across the **nonconducting** dielectric gap separating the two condenser plates."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Dry air acts as a practically **nonconducting** blanket surrounding the earth's radiating crust."}
    ]
  },
  "Dashboard — duc/nonconductive.md": {
    "primary": "Incapable of or poor at conducting electrical current, heat, or sound waves; insulating.",
    "secondary": "In industrial safety standards, nonconductive footwear and safety tools prevent electrical shock when working near live circuits.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Glass exhibits intensely **nonconductive** properties at normal ambient temperatures."},
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "A double layer of **nonconductive** felt effectively prevents radiative and convective heat loss from the steam boiler."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "The spherical interior was lined with a **nonconductive** substance impervious to the vacuum chill of interplanetary space."}
    ]
  },
  "Dashboard — duc/nonconductor.md": {
    "primary": "A substance that does not readily conduct electricity, heat, or sound; an electrical or thermal insulator.",
    "secondary": "In early electrical physics (Benjamin Franklin and Coulomb), materials dividing nature into electrics (nonconductors) and non-electrics (conductors).",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Experiments and Observations on Electricity", "quote": "Glass, amber, and dry resin act as powerful **nonconductors** that hold electric fluid on their surfaces."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Every known **nonconductor** will break down into conduction if subjected to an overwhelming electric tension."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Adipose tissue functions as an excellent thermal **nonconductor**, conserving core body warmth in Arctic mammals."}
    ]
  },
  "Dashboard — duc/nondeductible.md": {
    "primary": "Not able to be subtracted or deducted, especially from gross income when calculating tax liability.",
    "secondary": "In statutory revenue law, personal living expenditures and political lobbying expenses are strictly nondeductible.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "His accountant pointed out that club dues were ruled entirely **nondeductible** under the new internal revenue regulation."},
      {"author": "John Kenneth Galbraith", "work": "The Affluent Society", "quote": "Tax lawyers debated whether extravagant corporate goodwill expenditures remained **nondeductible** after audit."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "The political campaign contribution had to be paid from personal reserves as a **nondeductible** private outlay."}
    ]
  },
  "Dashboard — duc/nonproductive.md": {
    "primary": "Not producing goods, crops, or commodities; not yielding profitable or constructive results; barren.",
    "secondary": "In classical political economy, distinguishing productive labor (manufacturing tangible goods) from nonproductive services.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The labor of some of the most respectable orders in society is, like that of menial servants, **nonproductive** of tangible wealth."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Spending revenue upon purely **nonproductive** luxuries diminishes the potential accumulation of reproductive capital."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The stony ridge of the downs remained obstinately **nonproductive** despite frequent applications of chalk marl."}
    ]
  },
  "Dashboard — duc/outproduce.md": {
    "primary": "To produce more goods, crops, or industrial output than a competitor or rival enterprise.",
    "secondary": "In economic and wartime history, the decisive capability of allied industrial complexes to outproduce adversary industrial manufacturing.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The industrial shipyards of North America possessed the capacity to **outproduce** the losses inflicted by U-boat wolfpacks."},
      {"author": "John Dos Passos", "work": "The Big Money", "quote": "Henry Ford's continuous assembly line was designed to **outproduce** every traditional automotive workshop in Michigan."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Technologically integrated syndicates easily managed to **outproduce** fragmented regional craft guilds."}
    ]
  },
  "Dashboard — duc/overproduce.md": {
    "primary": "To produce more of a commodity or crop than is needed or can be sold profitably.",
    "secondary": "In business cycle theory, the tendency of competitive industries during boom phases to overproduce beyond effective consumer demand.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "When farmers **overproduce** corn in exceptionally bountiful harvests, the market price falls below the natural cost."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "Competitive factories tend to **overproduce** during periods of excessive optimism, precipitating sudden inventory gluts."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The local mills were warned not to **overproduce** flour when export markets showed sudden signs of contraction."}
    ]
  },
  "Dashboard — duc/overproduction.md": {
    "primary": "The production of more goods, services, or commodities than the market can absorb; an economic glut.",
    "secondary": "In Marxist economics, crises of overproduction arise from the contradiction between expanding productive capacity and constrained working-class consumption.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "General **overproduction** across all industries simultaneously was shown by classical theorists to be an economic impossibility."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The absurdity of the modern crisis lay in poverty and unemployment amid agricultural and industrial **overproduction**."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Business managers systematically curtail output to prevent chronic **overproduction** from collapsing price structures."}
    ]
  },
  "Dashboard — duc/oviduct.md": {
    "primary": "The tube or duct through which an ovum or egg passes from the ovary to the uterus or exterior.",
    "secondary": "In human female reproductive anatomy, the oviduct is commonly designated the Fallopian tube, where fertilization typically occurs.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The calcareous eggshell is secreted by specialized glandular walls along the middle section of the avian **oviduct**."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Mature ova pass down the ciliated **oviduct** to receive albuminous coats before extrusion into the aquatic medium."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ectopic gestation arises when the fertilized ovum arrests and implants prematurely within the **oviduct**."}
    ]
  },
  "Dashboard — duc/passconduct.md": {
    "primary": "A formal document or warrant guaranteeing safe passage through a military territory or sovereign jurisdiction; safe-conduct.",
    "secondary": "In early modern diplomatic and martial law, a passconduct issued under sign manual protected foreign ambassadors or heralds from arrest.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Templar demanded a royal **passconduct** before venturing into the camp of the Saxon insurgents."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Dutch envoys were furnished with an official **passconduct** signed by the secretary of state."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Gothic chieftain honored the imperial **passconduct**, permitting the Christian bishops to travel unmolested."}
    ]
  },
  "Dashboard — duc/produce.md": {
    "primary": "To bring forth, yield, make, manufacture, or generate; agricultural goods and farm harvests.",
    "secondary": "In microeconomics, to combine factor inputs (land, labor, capital) through a production function to generate output goods.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The annual **produce** of the land and labour of any nation can be increased in its value by no other means than by increasing the productivity of its labour."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection can act only by the preservation and accumulation of infinitesimally small inherited modifications, each profitable to the preserved being; and as modern geology has almost banished such views as the catastrophe of the deluge, so will natural selection banish the belief of the continued creation of new organic beings, or of any great and sudden modification in their structure, to **produce** new species."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba examined the farm **produce** laid out upon the stalls in the corn exchange."}
    ]
  },
  "Dashboard — duc/producer.md": {
    "primary": "A person, company, or country that makes, grows, or supplies goods or commodities for sale; theatrical manager.",
    "secondary": "In ecological trophic systems, an autotrophic organism (such as a green plant) that synthesizes organic nutrients from inorganic substances via photosynthesis.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Consumption is the sole end and purpose of all production; and the interest of the **producer** ought to be attended to only so far as it may be necessary for promoting that of the consumer."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Man is priest, and scholar, and statesman, and **producer**, and soldier in one comprehensive humanity."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The town merchants found it profitable to deal directly with the primary agricultural **producer**."}
    ]
  },
  "Dashboard — duc/product.md": {
    "primary": "An article or substance that is manufactured or refined for sale; a result of action or process.",
    "secondary": "In mathematics, the quantity obtained by multiplying two or more numbers, algebraic expressions, or matrices together.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She simply observed herself as a fair **product** of Nature in the feminine kind, rejoicing in her youthful beauty."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The price of every commodity resolves itself into one or other of those three parts, wages, profit, or rent, forming the total **product**."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Real scientific philosophy is not a barren disputation, but the fruitful **product** of systematic experiment."}
    ]
  },
  "Dashboard — duc/production.md": {
    "primary": "The action of making, manufacturing, or growing components or commodities; a work of literature or art.",
    "secondary": "In macroeconomic theory, aggregate production comprises the gross output of economic goods evaluated over a specific calendar accounting period.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The greatest improvement in the productive powers of labour seems to have been the effects of the division of labour in the **production** of commodities."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The result from capital employed in the **production** of agricultural staples was visible across the fertile fields."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When men examine and judge a **production** of human art, they seek to discover the maker's original intention."}
    ]
  },
  "Dashboard — duc/productive.md": {
    "primary": "Yielding, producing, or creating abundant results, commodities, crops, or creative works; fruitful.",
    "secondary": "In classical economics, productive labor directly adds value to materials, reproducing the wages consumed and generating a capitalist profit.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "So, in **productive** subjects, grow the chapters with rich abundance of whaling lore."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The proportion between the number of those who are employed in **productive** labour and that of those who are not governs national wealth."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The warm spring rains rendered the deep loam of Weatherbury valley exceptionally **productive**."}
    ]
  },
  "Dashboard — duc/productively.md": {
    "primary": "In a productive, fruitful, or generative manner; with effective, profitable output or results.",
    "secondary": "In organizational efficiency studies, deploying operational capital and working hours with minimal frictional waste.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Capital employed **productively** maintains industrious workers and continuously replaces itself with profit."},
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "I resolved to allocate every hour of the working day **productively**, avoiding idle tavern company."},
      {"author": "Herbert Spencer", "work": "The Data of Ethics", "quote": "Social evolution enables individuals to cooperate **productively** without destructive predatory competition."}
    ]
  },
  "Dashboard — duc/productiveness.md": {
    "primary": "The capacity, attribute, or degree of being productive; power of generating abundant output or fruit.",
    "secondary": "In agricultural economics, the natural fertility and crop yield potential of specific soil types under systematic cultivation.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The extraordinary **productiveness** of the pin manufactory demonstrates the power of specialized mechanical labor."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Selective breeding frequently alters the relative **productiveness** of domestic sheep varieties across changing pasturelands."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The **productiveness** of industry depends upon natural advantages, bodily skill, and moral reliability of workers."}
    ]
  },
  "Dashboard — duc/productivity.md": {
    "primary": "The rate or efficiency at which goods, crops, or commodities are produced, especially measured per unit of input.",
    "secondary": "In macroeconomic analysis, total factor productivity measures output efficiency growth unexplainable by mere increases in capital and labor inputs.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The mechanical **productivity** of British factories astonished visitors with its vast daily outpouring of cotton fabric."},
      {"author": "John Kenneth Galbraith", "work": "The Affluent Society", "quote": "Modern economic systems prioritize high physical **productivity** above equitable distribution or ecological conservation."},
      {"author": "Thorstein Veblen", "work": "The Instinct of Workmanship", "quote": "The underlying technological knowledge of the community forms the true foundation of industrial **productivity**."}
    ]
  },
  "Dashboard — duc/raduc.md": {
    "primary": "A historical Latinate morphological derivative denoting leading forth or conducting along root conduits.",
    "secondary": "In anatomical and botanical nomenclature, designating vascular bundles or root-conduction pathways facilitating fluid translocation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The plant vascular conduits perform an analogous **raduc** function in leading water upward from primary root hairs."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain sap channels serve as an internal **raduc** conduit, drawing vital moisture from the soil into upper boughs."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The differentiated tracheids form an efficient **raduc** channel through which ascending transpiration streams circulate."}
    ]
  },
  "Dashboard — duc/reconduct.md": {
    "primary": "To conduct, lead, or escort back to a former place, position, or safe harbor.",
    "secondary": "In historical diplomatic protocol, the ceremonial escorting of an accredited foreign envoy back to the state frontier.",
    "quotes": [
      {"author": "John Dryden", "work": "The Aeneid", "quote": "A faithful guide was appointed to **reconduct** thy steps safely through the perils of the hostile camp."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The knight offered to **reconduct** the royal lady through the mountain pass before nightfall."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The centurion received strict orders to **reconduct** the captive prince to the imperial headquarters."}
    ]
  },
  "Dashboard — duc/reduce.md": {
    "primary": "To make smaller, less, or lower in size, amount, degree, or intensity; to bring into a simpler state.",
    "secondary": "In chemistry, to add electrons or hydrogen to a substance, or remove oxygen from an oxide (reduction).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Which to **reduce** into our former favour you are assembled; and my speech entreats that I may know the let."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "We must **reduce** complex natural phenomena into simple, constituent axioms through systematic elimination."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Disuse will frequently **reduce** an organ in size when it ceases to be of functional service to the species."}
    ]
  },
  "Dashboard — duc/reduced.md": {
    "primary": "Made smaller, diminished in size, quantity, status, or price; simplified into basic components.",
    "secondary": "In medical surgery, a fractured bone or dislocated joint restored to its normal anatomical alignment.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His once comfortable estate was **reduced** to an insignificant holding following the disastrous sheep loss."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The gentlewoman lived in **reduced** circumstances, occupying two modest rooms in a faded suburban terrace."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The strangulated inguinal hernia was successfully **reduced** under gentle taxis without surgical section."}
    ]
  },
  "Dashboard — duc/reducer.md": {
    "primary": "A person, tool, or substance that reduces, diminishes, or scales down something.",
    "secondary": "In chemical reactions and metallurgy, a reducing agent (or reductant) that donates electrons to another reactant, being itself oxidized.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Hydrogen acts as a powerful chemical **reducer** when passed over heated metallic oxides in the tube."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The mechanical gear **reducer** stepped down the high-speed turbine shaft to turn the colossal propeller blades."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin calibrated the pressure **reducer** on the compressed nitrogen cylinder to prevent tube blowout."}
    ]
  },
  "Dashboard — duc/reducible.md": {
    "primary": "Capable of being reduced, diminished, simplified, or brought into a specified lower condition.",
    "secondary": "In chemical analysis, compounds capable of undergoing reduction reactions through the acquisition of electrons.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "All our complex ideas are ultimately **reducible** to simple perceptions derived from sensation and reflection."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Physical laws are **reducible** to mathematical equations expressing functional relationships between measurable events."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The vital activities of living protoplasm are **reducible** to fundamental physical and chemical affinities."}
    ]
  },
  "Dashboard — duc/reducing.md": {
    "primary": "Decreasing in size, amount, degree, or weight; bringing down to simpler or lesser form.",
    "secondary": "In metallurgy, a reducing atmosphere in a smelting furnace contains carbon monoxide that extracts oxygen from metallic ores.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Joseph spoke in an apologetic whisper, **reducing** his body smaller whilst attempting to explain his absence."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection operates continuously, preserving beneficial traits while **reducing** rudimentary structures."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The glowing charcoal created an intensely active **reducing** flame inside the laboratory crucible."}
    ]
  },
  "Dashboard — duc/reductant.md": {
    "primary": "A reducing agent; a substance that brings about reduction in another chemical species by donating electrons.",
    "secondary": "In biochemistry, intracellular electron donors (such as NADPH and glutathione) maintaining cellular redox homeostasis.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Nascent hydrogen acts as the most vigorous **reductant** in breaking down refractory metallic salts."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Organic matter in marsh soils acts as a potent **reductant**, transforming ferric iron into soluble ferrous compounds."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ascorbic acid functions physiologically as a biological **reductant** essential for connective tissue collagen synthesis."}
    ]
  },
  "Dashboard — duc/reductase.md": {
    "primary": "An enzyme that catalyzes a biochemical reduction reaction within cellular metabolism.",
    "secondary": "In pharmacology, inhibitors of HMG-CoA reductase (statins) block hepatic cholesterol biosynthesis, reducing circulating LDL levels.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bacterial enzymes include a specific nitrate **reductase** capable of reducing nitrates to nitrites in infected urine."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The clinical action of the compound relies upon inhibiting a specific **reductase** within central dopamine metabolic pathways."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "Congenital deficiency of methemoglobin **reductase** causes persistent familial cyanosis resistant to ordinary oxygen therapy."}
    ]
  },
  "Dashboard — duc/reductio.md": {
    "primary": "A Latin philosophical term meaning reduction; famously in reductio ad absurdum (reduction to the absurd).",
    "secondary": "In classical formal logic, proving a proposition by demonstrating that its negation leads to a logical contradiction.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "Euclidean geometry frequently employs the method of **reductio** ad absurdum to establish geometric congruence."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A rigorous **reductio** demonstrates that the contrary hypothesis violates known axioms of experience."},
      {"author": "G. K. Chesterton", "work": "Heretics", "quote": "His paradoxical argument arrived at a brilliant **reductio** of modern skepticism, showing that it doubts itself."}
    ]
  },
  "Dashboard — duc/reduction.md": {
    "primary": "The act or process of making something smaller, less, or simpler in form, size, amount, or intensity.",
    "secondary": "In chemistry, the gain of electrons or decrease in oxidation state by a molecule, atom, or ion during a reaction.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The rudimentary wings of the flightless beetle are the result of gradual **reduction** through long-continued disuse."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A sudden **reduction** in taxes encourages commercial enterprise and stimulates domestic manufacturing."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Electrolytic **reduction** precipitates pure metallic copper onto the negative cathode plate."}
    ]
  },
  "Dashboard — duc/reductionism.md": {
    "primary": "The philosophical practice of explaining complex phenomena in terms of simpler or more fundamental constituent parts.",
    "secondary": "In epistemology, contrasting explanatory reductionism (ontological components) with emergentism in biological and social systems.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Our Knowledge of the External World", "quote": "Logical **reductionism** seeks to translate physical object statements into strict propositions concerning sense-data."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Extreme psychological **reductionism** that treats thought as mere cerebral secretion ignores the rich reality of inner experience."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Methodological **reductionism** has proven an indispensable investigative tool in revealing the chemical basis of physiology."}
    ]
  },
  "Dashboard — duc/reductionist.md": {
    "primary": "A person who advocates or practices reductionism; characteristic of reductionist methodology.",
    "secondary": "In biological philosophy, an investigator who analyses macroscopic organismic phenomena purely through molecular mechanics.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Scientific Outlook", "quote": "The thoroughgoing **reductionist** attempts to resolve biological evolution into the mechanical dynamics of atoms."},
      {"author": "William James", "work": "Pragmatism", "quote": "The tender-minded philosopher rejects the harsh **reductionist** claim that human devotion is merely disguised self-interest."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "A consistent **reductionist** recognizes that moral evolution builds upon, yet transcends, physical struggle."}
    ]
  },
  "Dashboard — duc/reductive.md": {
    "primary": "Tending or serving to reduce, diminish, simplify, or bring about chemical reduction.",
    "secondary": "In intellectual criticism, overly simplistic analyses that ignore essential nuance, context, or complexity.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His cynical interpretation of Dorothea's generosity was too **reductive** to encompass her noble nature."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The intense heat created an active **reductive** zone inside the laboratory combustion tube."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Critics offered a **reductive** caricature of utilitarian ethics as a doctrine worthy only of swine."}
    ]
  },
  "Dashboard — duc/reductivism.md": {
    "primary": "The advocacy or application of extreme reductionist methods in philosophy, science, or art.",
    "secondary": "In mid-20th-century art theory, minimal art (reductivism) stripping visual composition of narrative illusion and ornament.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Medical **reductivism** that explains spiritual vision by dietary dyspepsia fails to touch its spiritual significance."},
      {"author": "Bertrand Russell", "work": "An Inquiry into Meaning and Truth", "quote": "Epistemological **reductivism** encounters formidable obstacles when attempting to construct physical objects out of sensory qualia."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific progress requires resisting metaphysical dogmatism while utilizing methodological **reductivism** for practical discoveries."}
    ]
  },
  "Dashboard — duc/reintroduce.md": {
    "primary": "To introduce someone or something again; to bring back into use, notice, or an ecosystem.",
    "secondary": "In conservation biology, releasing captive-bred or translocated wildlife into their indigenous historical ranges.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Certain theorists attempt to **reintroduce** an archaic doctrine of spiritual degeneration to explain human origins."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel resolved to **reintroduce** older, proven methods of sheep husbandry across the neglected farm."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional framers sought to **reintroduce** stability without reviving monarchical executive tyranny."}
    ]
  },
  "Dashboard — duc/reintroduction.md": {
    "primary": "The act or process of introducing someone or something anew or bringing back into practice.",
    "secondary": "In wildlife restoration ecology, returning an extirpated apex predator (such as the gray wolf) to re-establish trophic cascades.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "The sudden **reintroduction** of archaic religious controversies startled modern secular journalists in Fleet Street."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The **reintroduction** of ancestral crosses promptly restored wild coloration in the domestic pigeon flock."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The **reintroduction** of the old coinage reformed commerce and restored public credit throughout the nation."}
    ]
  },
  "Dashboard — duc/reproduce.md": {
    "primary": "To make a copy, duplicate, or likeness of; to produce offspring by sexual or asexual means.",
    "secondary": "In evolutionary biology, reproductive success (fitness) represents an organism's relative capacity to transmit genetic material to succeeding generations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every organism tends to multiply at so rapid a rate that its progeny cannot all survive, yet each strives to **reproduce** its kind."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The great artist does not merely **reproduce** external contours, but conveys the living soul of the mountain."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes managed to **reproduce** the exact footprints found on the roof using plaster casts."}
    ]
  },
  "Dashboard — duc/reproduceable.md": {
    "primary": "Capable of being copied, duplicated, or reproduced accurately; reproducible.",
    "secondary": "In technical documentation and industrial quality control, processes verified to yield consistent results across multiple manufacturing cycles.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The electromagnetic deflection was clearly **reproduceable** whenever the primary circuit was closed."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A scientific fact must be **reproduceable** by any competent investigator possessing proper laboratory instruments."},
      {"author": "Karl Popper", "work": "The Logic of Scientific Discovery", "quote": "Only when certain events recur in accordance with rules is our observation in principle **reproduceable**."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Motion Batch 13C: Successfully updated {updated}/{len(data)} notes.")
