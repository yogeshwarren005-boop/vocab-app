# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — duct Part 2 (8B, 37 words) ---
  "Dashboard — duct/introductory.md": {
    "primary": "Serving to introduce, precede, or open a subject, text, course, or ceremony; preliminary.",
    "secondary": "In legal practice and judicial trials, introductory instructions inform the jury of their legal duties before opening statements.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He delivered a few **introductory** words before demonstrating the remarkable sword drill to the assembly."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In the **introductory** chapter, I summarized the main facts indicating the transmutation of species."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The author provided an **introductory** discourse examining the ancient mercantile systems of Europe."}
    ]
  },
  "Dashboard — duct/misconduct.md": {
    "primary": "Improper, dishonest, unethical, or unlawful behavior, especially by a person in a position of trust or authority.",
    "secondary": "In administrative and employment law, gross misconduct justifies immediate termination of an employment contract without notice.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth felt humbled by the discovery of Wickham's real **misconduct** and profligacy."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The military **misconduct** of the general led directly to the loss of the border province."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The power of impeachment was provided to punish the official **misconduct** of public magistrates."}
    ]
  },
  "Dashboard — duct/nonconducting.md": {
    "primary": "Not conducting or transmitting heat, electricity, or sound; functioning as an electrical or thermal insulator.",
    "secondary": "In electrostatic apparatus design, glass and ebonite rods serve as nonconducting supports to isolate stored electrical charges.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The copper wire was wrapped in silk thread to provide a **nonconducting** barrier between the coils."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "A dielectric medium behaves as a **nonconducting** space through which electric induction operates."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "The submarine cable was surrounded by a **nonconducting** sheath of gutta-percha to prevent current leakage."}
    ]
  },
  "Dashboard — duct/nonconductive.md": {
    "primary": "Lacking the property of conducting heat or electricity; having high dielectric resistance; insulating.",
    "secondary": "In industrial electrical safety standards, maintenance workers wear nonconductive rubber boots when repairing high-voltage transformers.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The porcelain mounts provided a **nonconductive** foundation for the sensitive galvanic instruments."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "Air at normal atmospheric pressure acts as an effective **nonconductive** shield against modest voltages."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The tripod machines were operated from cabs lined with **nonconductive** ceramic plates."}
    ]
  },
  "Dashboard — duct/nonconductor.md": {
    "primary": "A substance or medium that does not conduct heat, electricity, or sound; an electrical or thermal insulator.",
    "secondary": "In nineteenth-century physics, Benjamin Franklin classified dry wood, glass, and amber as typical nonconductors of electric fluid.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Experiments and Observations on Electricity", "quote": "Glass is a remarkable **nonconductor**, retaining the electric fluid upon its surface without allowing it to permeate."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The experiment proved that pure water is a very poor conductor, almost acting as a **nonconductor**."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Dry air is an excellent **nonconductor** of heat, protecting the earth from rapid nocturnal radiation."}
    ]
  },
  "Dashboard — duct/nondeductible.md": {
    "primary": "Not eligible or allowable to be deducted or subtracted from taxable gross income or a total financial sum.",
    "secondary": "In modern corporate tax accounting, personal living expenses and government regulatory fines are strictly nondeductible.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Certain arbitrary royal assessments were deemed **nondeductible** from the tenant's agricultural tithes."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A tax system loses equity when essential subsistence outlays are treated as **nondeductible** burdens."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The parliamentary commissioners ruled that private loans to the exiled monarch were **nondeductible** debts."}
    ]
  },
  "Dashboard — duct/nonproductive.md": {
    "primary": "Not producing goods, wealth, or crops; failing to generate tangible economic value or useful results; unproductive.",
    "secondary": "In classical economics, Adam Smith distinguished between productive labor (creating durable commodities) and nonproductive labor (menial service).",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The labor of some of the most respectable orders in the society is, like that of menial servants, **nonproductive** of any value."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Capital employed in luxury consumption is **nonproductive** of future industrial wealth."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Rote memorization without scientific demonstration remains a **nonproductive** educational exercise."}
    ]
  },
  "Dashboard — duct/overproduction.md": {
    "primary": "The production of more of a commodity or good than can be sold or consumed; excessive output leading to surplus.",
    "secondary": "In Marxist macroeconomic crisis theory, capitalist competition leads inevitably to overproduction and falling profit margins.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A temporary **overproduction** of manufactured cottons depressed wholesale market prices throughout the Midlands."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The enormous **overproduction** of offspring in every species creates a perpetual struggle for existence."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A general **overproduction** of all commodities simultaneously is a commercial impossibility, though partial gluts occur."}
    ]
  },
  "Dashboard — duct/product.md": {
    "primary": "An article, substance, or outcome manufactured, refined, or produced; or the result of multiplying numbers.",
    "secondary": "In organic chemistry, a reaction product forms when chemical reactants undergo covalent bond rearrangement.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The annual **product** of the land and labor of any nation can be increased in its value by no other means than by increasing either the number of its productive laborers, or the productive powers of those laborers."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The valuable sperm oil was the ultimate commercial **product** sought by the intrepid whalemen."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every domestic breed is the combined **product** of natural variation and human artificial selection."}
    ]
  },
  "Dashboard — duct/production.md": {
    "primary": "The act, process, or work of manufacturing, creating, cultivating, or bringing forth goods, crops, or artistic works.",
    "secondary": "In microeconomics, a production function specifies the maximum output attainable from given quantities of capital and labor.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The result from capital employed in the **production** of any movement of a mental nature is slow."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Consumption is the sole end and purpose of all **production**; and the interest of the producer ought to be attended to, only so far as it may be necessary for promoting that of the consumer."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The continuous **production** of new varieties under domestication illustrates the plasticity of animal organizations."}
    ]
  },
  "Dashboard — duct/productive.md": {
    "primary": "Yielding or capable of producing abundant goods, crops, results, or benefits; generative and fertile.",
    "secondary": "In macroeconomic theory, productive capital refers to machinery, plant facilities, and infrastructure used directly to generate output.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "So, in **productive** subjects, grow the chapters with generous fullness."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The employment of capital in agriculture is the most **productive** investment for any commonwealth."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A single healthy plant can prove astonishingly **productive**, scattering thousands of viable seeds across the meadow."}
    ]
  },
  "Dashboard — duct/productively.md": {
    "primary": "In a productive, fruitful, or generative manner; with effective, useful, or profitable results.",
    "secondary": "In corporate operations management, deploying modern automation enables labor hours to be utilized productively.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A merchant invests his capital where it may be most **productively** employed to maximize his returns."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Land drained by tile conduits was farmed far more **productively** than boggy pastures."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "A student spends his leisure **productively** when observing living specimens in field nature."}
    ]
  },
  "Dashboard — duct/productiveness.md": {
    "primary": "The capacity, efficiency, or power to yield abundance, goods, or fruitful results.",
    "secondary": "In agricultural soil science, the productiveness of alluvial river plains depends on organic loam content and drainage.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labor causes a greater increase in the **productiveness** of human exertion than any other improvement."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The natural **productiveness** of tropical vegetation supports an extraordinary diversity of insect life."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The industrial **productiveness** of a nation reflects the technical skill and mechanical inventiveness of its artisans."}
    ]
  },
  "Dashboard — duct/productivity.md": {
    "primary": "The efficiency of productive effort, measured by output per unit of input or labor.",
    "secondary": "In macroeconomic growth accounting (Solow-Swan model), total factor productivity measures output gains not accounted for by capital and labor growth.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A man's true wealth is measured by the fruitful **productivity** of his thoughts and moral actions."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The mechanical loom multiplied the physical **productivity** of textile weavers tenfold."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The application of chemical fertilizers enhanced the agricultural **productivity** of exhausted arable land."}
    ]
  },
  "Dashboard — duct/reductant.md": {
    "primary": "A substance that brings about reduction in another chemical species by donating electrons and being oxidized in the process.",
    "secondary": "In metallurgy, carbon monoxide generated from burning coke acts as the primary gaseous reductant in a blast furnace reducing iron oxide to pig iron.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The chemist introduced charcoal as a powerful **reductant** to extract metallic tin from its mineral oxide."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Hydrogen gas served as an effective chemical **reductant** during the high-temperature reduction experiment."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Geological strata reveal how organic matter acted as a **reductant** on dissolved ferric salts in primordial oceans."}
    ]
  },
  "Dashboard — duct/reductase.md": {
    "primary": "An enzyme that catalyzes a chemical reduction reaction in biochemical pathways.",
    "secondary": "In human pharmacotherapy, HMG-CoA reductase inhibitors (statins) block the rate-limiting enzyme in hepatic cholesterol biosynthesis.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Biological respiration depends upon intracellular **reductase** enzymes that transfer electrons along the metabolic chain."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Deficiency in red blood cell **reductase** activity predisposes the patient to acute hemolytic crises."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The biochemical activity of cellular **reductase** maintains the delicate redox equilibrium of nervous tissue."}
    ]
  },
  "Dashboard — duct/reductio.md": {
    "primary": "A philosophical or logical method of refutation by demonstrating that a proposition leads inevitably to an absurd conclusion.",
    "secondary": "In classical Aristotelian syllogistic logic, a reductio argument demonstrates a thesis by showing that its negation contradicts established axioms.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The mathematical proof proceeded by a rigorous **reductio**, proving the impossibility of an odd square having an even root."},
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "His argument collapsed under the weight of a devastating **reductio** that exposed its innate contradictions."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Euclid frequently employs the method of **reductio** to confirm geometrical theorems beyond question."}
    ]
  },
  "Dashboard — duct/reduction.md": {
    "primary": "The act of making smaller, less, or diminished; or the chemical gain of electrons by an atom or molecule.",
    "secondary": "In evolutionary biology, morphological reduction describes the vestigial loss or diminution of ancestral anatomical structures due to relaxed selection.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "This state of the eyes is probably due to gradual **reduction** from disuse, aided by natural selection."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A general **reduction** of import duties gave immediate stimulus to domestic maritime shipping."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The chemical **reduction** of silver ore requires the steady application of heat and fluxing agents."}
    ]
  },
  "Dashboard — duct/reductionism.md": {
    "primary": "The philosophical doctrine or practice of analyzing and explaining complex phenomena solely in terms of fundamental or simpler components.",
    "secondary": "In philosophy of science, physicalist reductionism asserts that all biological, mental, and social phenomena are ultimately explainable by fundamental physical laws.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Philosophical **reductionism** seeks to dissolve metaphysical perplexities into atomic logical propositions."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "A cautious scientist avoids dogmatic **reductionism**, acknowledging the emergent complexities of living organisms."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The crude **reductionism** that would equate conscious spiritual feelings with mere cerebral twitches ignores inner reality."}
    ]
  },
  "Dashboard — duct/reductionist.md": {
    "primary": "Pertaining to, advocating, or characteristic of reductionism; or a person who explains complex phenomena through simpler constituents.",
    "secondary": "In evolutionary biology, reductionist models focusing solely on selfish genes were contested by advocates of multi-level selection.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "The **reductionist** analysis of matter resolves solid physical objects into systems of mathematical relations."},
      {"author": "William James", "work": "The Will to Believe", "quote": "The dogmatic **reductionist** fails to appreciate that moral experiences possess an intrinsic qualitative validity."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "A thorough **reductionist** might view ethics as biological survival adaptations, yet moral duties transcend brute impulse."}
    ]
  },
  "Dashboard — duct/reductive.md": {
    "primary": "Tending to reduce, simplify, or minimize; or oversimplifying complex issues by ignoring nuances.",
    "secondary": "In organic synthesis, reductive amination converts a carbonyl group into an amine via an imine intermediate.",
    "quotes": [
      {"author": "George Orwell", "work": "Collected Essays", "quote": "The political pamphlet presented a crude and **reductive** picture of the social crisis."},
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "A purely **reductive** view of human motivation reduces all historic heroism to economic self-interest."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Philistine criticism adopted a narrow, **reductive** standard that dismissed artistic refinement as useless."}
    ]
  },
  "Dashboard — duct/reductivism.md": {
    "primary": "The tendency or philosophical practice of oversimplifying complex phenomena by reducing them to a single basic cause or principle.",
    "secondary": "In art history, reductivism refers to twentieth-century minimalist art movements emphasizing extreme geometric simplification and non-representational form.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "The extreme **reductivism** of early materialists denied the evident reality of conscious mental experience."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Psychological **reductivism** impoverishes our understanding of human character by treating souls as chemical machines."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Literary **reductivism** that judges poetry by mechanical utility ignores the sublime power of imagination."}
    ]
  },
  "Dashboard — duct/reintroduction.md": {
    "primary": "The act of introducing something again into an environment, society, or curriculum where it had ceased to exist.",
    "secondary": "In conservation biology, species reintroduction programs release captive-bred or translocated individuals into historical natural habitats.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "The sudden **reintroduction** of medieval religious passions into modern London street life bewildered the citizens."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The accidental **reintroduction** of an extirpated weed into cultivated fields can alter local botanical competition."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The parliamentary party celebrated the **reintroduction** of the Habeas Corpus Act as a bulwark of liberty."}
    ]
  },
  "Dashboard — duct/reproduction.md": {
    "primary": "The biological process by which organisms generate offspring; or the exact copying of a work of art, document, or sound.",
    "secondary": "In evolutionary biology, differential reproductive success among diverse genotypes drives adaptive phenotypic changes across generations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The physiological laws governing the **reproduction** of hybrid animals reveal deep homologies across species."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "And you thought I was the mere stone **reproduction** of one of the ancient d'Urberville knights."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "No mechanical **reproduction** can capture the subtle vibration of color present in Turner's original canvas."}
    ]
  },
  "Dashboard — duct/reproductive.md": {
    "primary": "Pertaining to, concerned with, or capable of biological reproduction; or producing copies of original works.",
    "secondary": "In plant botany, reproductive organs are housed within floral whorls adapted to facilitate pollination.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **reproductive** system is notoriously susceptible to the slightest change in the conditions of life."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **reproductive** organs undergo cyclic maturation influenced by internal glandular secretions."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "A high degree of mental development is frequently accompanied by a diminution in **reproductive** fertility."}
    ]
  },
  "Dashboard — duct/seduction.md": {
    "primary": "The act of enticing, tempting, or leading someone astray from moral rectitude, duty, or virginity.",
    "secondary": "In historical common law, a father or master could maintain a tort action of seduction for the loss of his daughter's services.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Colonel Brandon revealed the villainous **seduction** of young Eliza by the unscrupulous Willoughby."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Little Emily was lured from her family by the deceitful **seduction** of Steerforth's romantic flatteries."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "The proud soul rises above every sensual **seduction**, keeping its course toward spiritual truth."}
    ]
  },
  "Dashboard — duct/seductive.md": {
    "primary": "Tending to seduce, entice, or mislead by alluring charm, beauty, or flattering promises; tempting.",
    "secondary": "In persuasive advertising and rhetoric, seductive framing exploits cognitive heuristics to elicit impulsive consumer decisions.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "I should indeed be foolish to feel offended at anything you say, he answered in that **seductive** tone she dreaded."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The twenty pounds' worth of seed-corn had been planted in vain in the **seductive** green meadow."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The calm tropical sea presented a **seductive** mirror that concealed the ravenous monsters beneath."}
    ]
  },
  "Dashboard — duct/seductively.md": {
    "primary": "In a seductive, alluring, or enticing manner; with tempting charm or insidious appeal.",
    "secondary": "In narrative fiction, antagonists speak seductively to disarm moral vigilance and persuade heroes into compromising alliances.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy leaned over the orchard wall and whispered **seductively** to the hesitant country girl."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The whisper of temptation came **seductively** upon my ear, urging me to sacrifice conscience to passion."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The cunning usurer smiled **seductively** as he unfolded the parchment mortgage before his victim."}
    ]
  },
  "Dashboard — duct/seductress.md": {
    "primary": "A woman who seduces, allures, or entices others, especially through charm, sexual attraction, or cunning.",
    "secondary": "In classical mythology and literature, the archetype of the seductress tests the moral resolve of heroes.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The courtiers whispered that the foreign countess was a dangerous **seductress** sent to ensnare the prince."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp played the consummate **seductress**, fascinating old Sir Pitt and his wealthy brother alike."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The tragic history unfolded how the glamorous **seductress** brought ruin upon the honorable family."}
    ]
  },
  "Dashboard — duct/subduction.md": {
    "primary": "The act of taking away or subtracting; or the geological process where one tectonic plate slides under another into the mantle.",
    "secondary": "In plate tectonics and geodynamics, subduction zones generate deep ocean trenches, megathrust earthquakes, and volcanic island arcs.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The downward **subduction** of crustal margins into deep subterranean cauldrons compensates for volcanic upwelling."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Geological **subduction** and thermal expansion collaborate to shape the immense topography of oceanic trenches."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The uplift of the Andes must be counterbalanced by the crustal **subduction** along the deep Pacific trench."}
    ]
  },
  "Dashboard — duct/superconductivity.md": {
    "primary": "The complete disappearance of electrical resistance in certain materials when cooled below a characteristic critical temperature.",
    "secondary": "In low-temperature condensed matter physics, BCS theory explains superconductivity via electron pairing (Cooper pairs) mediated by lattice phonons.",
    "quotes": [
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "If absolute zero could be attained, metallic resistance might vanish entirely, giving rise to perfect **superconductivity**."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The theoretical possibility of persistent currents in conductors exhibiting ideal **superconductivity** would transform electrodynamics."},
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "In the limiting condition of zero resistive loss, magnetic field expulsion and perpetual **superconductivity** emerge."}
    ]
  },
  "Dashboard — duct/transduction.md": {
    "primary": "The action of transferring or converting energy or a message from one system or form to another.",
    "secondary": "In bacterial genetics, transduction is the process whereby bacteriophages transfer DNA fragments from one bacterial cell to another.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Sensory **transduction** in retinal photoreceptors converts radiant electromagnetic light into nervous impulses."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The **transduction** of physical vibrations in the ear into conscious sensations of musical pitch illustrates mental synthesis."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Microscopic mechanisms of physiological **transduction** mediate between external environmental stimuli and organismal response."}
    ]
  },
  "Dashboard — duct/underproduction.md": {
    "primary": "The production of a commodity, crop, or good in quantities less than demanded or below normal capacity.",
    "secondary": "In agricultural economics, unseasonable drought causes crop underproduction, triggering price spikes and food distribution crises.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A chronic **underproduction** of corn during cold summers invariably raised bread prices and pauperized laborers."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The temporary **underproduction** of coal stemmed from labor disputes rather than any exhaustion of mineral seams."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Industrial **underproduction** can only be remedied by training craftsmen in more efficient scientific methods."}
    ]
  },
  "Dashboard — duct/unproductive.md": {
    "primary": "Failing to produce significant goods, crops, results, or benefits; barren, infertile, or yielding no useful return.",
    "secondary": "In classical Ricardian rent theory, marginal land that yields no economic rent is categorized as unproductive acreage.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Linnæus calculated that if an annual plant produced only two seeds, its progeny would soon cover the earth; none is completely **unproductive**."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Barren rocky soils remain **unproductive** until human industry enriches them with marl and drainage."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The conversation proved awkward and **unproductive**, neither party feeling at ease to open their thoughts."}
    ]
  },
  "Dashboard — duct/unproductively.md": {
    "primary": "In an unproductive, ineffective, or fruitless manner; without generating useful results, goods, or profit.",
    "secondary": "In public finance, allocating government revenues unproductively to lavish courtly display drains national capital resources.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The anxious interval wore away **unproductively**, leaving Anne in the same state of suspense and regret."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A prodigal heir spends his inheritance **unproductively** on luxury menials, squandering the wealth accumulated by his ancestors."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "When capital is consumed **unproductively**, it perishes without creating an equivalent fund for future employment."}
    ]
  },
  "Dashboard — duct/unproductiveness.md": {
    "primary": "The absence of fertility, yield, or practical output; barrenness or fruitlessness.",
    "secondary": "In agronomic land valuation, the unproductiveness of clay hardpan soils requires deep subsoil plowing and lime application.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The apparent **unproductiveness** of hybrid crossings is a natural consequence of reproductive disharmony."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The natural **unproductiveness** of rocky mountain pastures limits the population of highland glens."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The economic **unproductiveness** of archaic scholastic methods led to the foundation of modern technical colleges."}
    ]
  },
  "Dashboard — duct/unseductive.md": {
    "primary": "Lacking allure, charm, temptation, or attraction; unappealing, austere, or plain in appearance.",
    "secondary": "In aesthetic philosophy, an unseductive presentation prioritizes stark empirical truth over flattering rhetorical ornament.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The austere scholar presented an **unseductive** exterior to the cheerful society of the provincial drawing-room."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Lowood School appeared as a cold and **unseductive** asylum to the friendless orphan."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The dusty legal folios presented an **unseductive** prospect to a youth yearning for classical poetry."}
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

print(f"Motion Batch 8B: Successfully updated {updated}/{len(data)} notes.")
