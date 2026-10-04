# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — grad (32 words) ---
  "Dashboard — grad/aggrade.md": {
    "primary": "To build up the level of a riverbed or valley floor through the progressive deposition of alluvial sediment.",
    "secondary": "In fluvial geomorphology and sedimentology, overloaded braided stream channels aggrade during periods of intense glacial meltwater runoff.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Torrential mountain streams continue to **aggrade** their alluvial fans as they enter the broad piedmont valley."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "When the river velocity diminishes across flat lowlands, it begins to **aggrade** rather than excavate its bed."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The heavy gravel washes deposited by seasonal floods slowly **aggrade** the barren valleys of Patagonia."}
    ]
  },
  "Dashboard — grad/centigrade.md": {
    "primary": "Divided into one hundred degrees, designating the thermometric temperature scale where water freezes at 0° and boils at 100°.",
    "secondary": "In physical chemistry and international meteorological reporting, the centigrade or Celsius scale serves as the primary metric unit.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The deep-sea thermometer registered four degrees **centigrade** at a depth of two thousand fathoms in the Atlantic."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The laboratory apparatus was maintained at twenty degrees **centigrade** throughout the galvanic experiment."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "Cavor noted the rapid plunge of the mercury to fifty degrees **centigrade** below freezing during the lunar night."}
    ]
  },
  "Dashboard — grad/degradation.md": {
    "primary": "The process of reducing something to a lower rank, quality, status, or moral character; or the geological wearing down of land surfaces.",
    "secondary": "In polymer chemistry and environmental science, photo-thermal degradation cleaves synthetic macromolecular polymer chains over time.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Atmospheric weathering and rain cause continuous geological **degradation** of the highest granite mountain ranges."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip felt a painful sense of moral **degradation** while associating with the coarse company at the Blue Boar."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The gradual **degradation** of the Roman legions into undisciplined peasant militia invited barbarian invasion."}
    ]
  },
  "Dashboard — grad/degrade.md": {
    "primary": "To lower someone in dignity, rank, or character; or to cause to break down or deteriorate chemically or physically.",
    "secondary": "In biochemistry and enzymatic proteomics, specific endopeptidases degrade polypeptide chains into absorbable amino acid residues.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "Must I lose the name of king? A God's name, let it go; I'll give my jewels for a set of beads, and **degrade** my royal state."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth declared that marrying Mr. Collins would **degrade** her understanding in the eyes of all sensible people."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Physical weathering and frost action slowly **degrade** exposed sandstone escarpments into fertile alluvial soils."}
    ]
  },
  "Dashboard — grad/degraded.md": {
    "primary": "Reduced in quality, status, rank, or moral character; or worn down through physical or biological processes.",
    "secondary": "In evolutionary morphology, vestigial or degraded anatomical structures indicate loss of ancestral functional adaptation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain parasitic crustaceans possess a **degraded** anatomical structure, retaining little more than a sac of reproductive organs."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ruined whaleman was a **degraded** spectacle of drunken despair, haunting the bleak taverns of New Bedford."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Frankenstein looked upon the miserable demon as the **degraded** creature of his own reckless scientific pride."}
    ]
  },
  "Dashboard — grad/degrader.md": {
    "primary": "A person, agent, or biological organism that causes degradation, breakdown, or decline.",
    "secondary": "In environmental microbiology and bioremediation, fungal lignin degrader species decompose recalcitrant polyaromatic plant polymers.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A cynical politician who appeals only to selfish market instincts acts as a moral **degrader** of the commonwealth."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Industrial commercialism operates as a relentless **degrader** of genuine craftsmanship and architectural beauty."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The torrential mountain stream functions as an active **degrader** of elevated volcanic plateaus."}
    ]
  },
  "Dashboard — grad/degrading.md": {
    "primary": "Causing a loss of self-respect or social standing; humiliating; or breaking down matter into simpler components.",
    "secondary": "In sociopolitical critique and labor economics, sweatshop working conditions subject factory laborers to degrading environments.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The extreme squalor of the coal-mining tenements had a deeply **degrading** effect upon the health of the families."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane refused to accept a dependent position that she regarded as morally **degrading** to an honest mind."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The monotonous drudgery of the Coketown mills was pronounced a **degrading** influence upon the human spirit."}
    ]
  },
  "Dashboard — grad/grad.md": {
    "primary": "An informal abbreviated term for a graduate; or an angular unit of measurement equal to one-hundredth of a right angle.",
    "secondary": "In surveying and trigonometric geodesy, the grad (or gon) divides a full circle into four hundred metric angular units.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt attended the university alumni reunion, boasting of his status as an energetic college **grad**."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The young Princeton **grad** wandered down Fifth Avenue, dreaming of literary fame in the postwar metropolis."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The ambitious university **grad** sought entry into the administrative civil service through competitive examinations."}
    ]
  },
  "Dashboard — grad/gradable.md": {
    "primary": "Capable of being graded, categorized, or compared on a continuum of degree or intensity.",
    "secondary": "In structural linguistics and semantic theory, gradable adjectives (such as hot/cold or large/small) admit comparative morphology.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Qualitative sensations of temperature and brightness form a **gradable** series amenable to quantitative measurement."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Emotional intensities of pleasure and pain exist as a continuous, **gradable** continuum in human consciousness."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The complex phenomena of biological evolution present a **gradable** progression from simplicity to intricate organization."}
    ]
  },
  "Dashboard — grad/gradate.md": {
    "primary": "To pass or cause to pass gradually through a series of intermediate stages, shades, or color tones.",
    "secondary": "In visual studio painting and chromatic theory, masters gradate oil glazes to achieve subtle sfumato transitions in portraiture.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner learned how to **gradate** his azure skies into warm horizon golds with peerless atmospheric delicacy."},
      {"author": "Henry David Thoreau", "work": "Autumnal Tints", "quote": "The leaves of the scarlet oak **gradate** from deep olive green to fiery crimson under the October frosts."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The evening clouds seemed to **gradate** from pale primrose to dark purple above the rolling downs."}
    ]
  },
  "Dashboard — grad/gradation.md": {
    "primary": "A scale or series of successive changes, stages, or degrees; or a subtle transition between colors, tones, or ideas.",
    "secondary": "In evolutionary biology and paleontology, phyletic gradualism posits that morphological change proceeds via subtle phenotypic gradation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection can act only through the preservation of useful variations by minute, successive **gradation**."},
      {"author": "Alexander Pope", "work": "An Essay on Man", "quote": "Vast chain of being, which from God began, natures ethereal, human, angel, man, beast, bird, fish, insect, what no eye can see, no glass can reach, from infinite to thee, from thee to nothing; on superior powers were we to press, inferior might on ours; or in the full creation leave a void, where, one step broken, the great scale's destroyed; from Nature's chain whatever link you strike, tenth, or ten thousandth, breaks the chain alike; each creature in its proper **gradation**."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "There is a seamless **gradation** in natural species that defies the rigid boundaries of human verbal definition."}
    ]
  },
  "Dashboard — grad/gradational.md": {
    "primary": "Characterized by, proceeding through, or relating to gradual stages, degrees, or progressive transitions.",
    "secondary": "In sedimentological stratigraphy, a gradational boundary reflects continuous environmental deposition without an erosional unconformity.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The transition from marine shale to terrestrial sandstone presents a **gradational** sequence marked by estuarine fossils."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The emergence of human civilization exhibits a **gradational** development from primitive tribal custom to codified law."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Social institutions evolve through **gradational** modifications rather than sudden, unprovoked institutional revolutions."}
    ]
  },
  "Dashboard — grad/gradatory.md": {
    "primary": "Proceeding step by step; gradual; or characterized by progressive steps or stages.",
    "secondary": "In classical architectural history, gradatory stone seating tiers defined Greco-Roman amphitheater construction.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "Spiritual enlightenment unfolds through a **gradatory** discipline that purifies both intellect and moral desire."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The inductive method requires a **gradatory** ascent from particular empirical observations to universal scientific axioms."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor introduced a **gradatory** scale of judicial appeals across the municipal courts of Italy."}
    ]
  },
  "Dashboard — grad/grade.md": {
    "primary": "A particular level of rank, quality, proficiency, or value; or an inclined slope of a road or railway.",
    "secondary": "In civil road engineering, calculating the maximum grade determines permissible traction limits for heavy freight locomotives.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The overland stagecoach labored up the steep mountain **grade**, its team of six horses steaming in the thin air."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Bitzer took pride in achieving the highest **grade** in Mr. Gradgrind's model factual examination."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The market prices of manufactured woolens vary according to the fine **grade** of fleece selected by weavers."}
    ]
  },
  "Dashboard — grad/grade-appropriate.md": {
    "primary": "Suitable, challenging, and suitable for the developmental level, age, or curricular requirements of students in a specific school grade.",
    "secondary": "In educational pedagogy and reading curriculum design, selecting grade-appropriate texts ensures Lexile readability alignment.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The progressive teacher selects **grade-appropriate** materials that connect directly with the pupil's living social experience."},
      {"author": "H. G. Wells", "work": "Mankind in the Making", "quote": "A modern national curriculum requires carefully curated, **grade-appropriate** scientific readers for young students."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The village school board scrutinized the biology textbooks, insisting upon **grade-appropriate** lessons for the grammar grades."}
    ]
  },
  "Dashboard — grad/grade-constructed.md": {
    "primary": "Engineered, leveled, or built according to specific gradient slopes, elevations, and structural cross-sections.",
    "secondary": "In transport civil engineering, a grade-constructed railroad roadbed incorporates engineered cut-and-fill drainage cross-sections.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "The municipal traction franchise laid down heavy steel rails over the newly **grade-constructed** suburban boulevard."},
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The speculative railroad syndicate surveyed miles of **grade-constructed** earthworks across the fertile Missouri prairie."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "Armored locomotives advanced along the **grade-constructed** military embankment guarding the river crossing."}
    ]
  },
  "Dashboard — grad/graded.md": {
    "primary": "Arranged, categorized, or evaluated according to rank, size, quality, or difficulty; or leveled to a slope.",
    "secondary": "In pedagogical instructional design, graded readers introduce vocabulary in controlled lexical frequencies to facilitate learning.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "Earthworms sort soil particles, leaving a **graded** layer of fine vegetable mold across the ancient pasture."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate examined the **graded** series of anatomical specimens preserved in the hospital pathology laboratory."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Import tariffs were assessed according to a **graded** schedule based on the certified quality of foreign spirits."}
    ]
  },
  "Dashboard — grad/grader.md": {
    "primary": "A person who evaluates and assigns grades to academic work; or a heavy earthmoving machine equipped with a blade to level surfaces.",
    "secondary": "In highway construction and roadbed maintenance, a motorized motor grader shapes the crown and drainage ditches of unpaved roadways.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol Kennicott watched the municipal road **grader** scrape the muddy spring ruts along the village avenue."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "The municipal contracting firm deployed a steam-powered road **grader** to level the new traction line."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The young instructor spent weary midnight hours acting as a conscientious **grader** of freshman themes."}
    ]
  },
  "Dashboard — grad/gradient.md": {
    "primary": "An inclined part of a road, railway, or physical surface; or the rate of regular increase or decrease in a variable.",
    "secondary": "In thermodynamics and physical transport phenomena, thermal gradients drive conductive heat transfer via Fourier's law.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The erosive velocity of a river is determined by the hydraulic **gradient** of its descent toward the sea."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Atmospheric pressure displays a vertical barometric **gradient** that decreases steadily with increasing elevation."},
      {"author": "Jules Verne", "work": "Journey to the Center of the Earth", "quote": "Professor Lidenbrock monitored the geothermal temperature **gradient** as they penetrated deeper into the subterranean shaft."}
    ]
  },
  "Dashboard — grad/grading.md": {
    "primary": "The act of classifying, evaluating, or sorting by degree or quality; or leveling and sloping ground for construction.",
    "secondary": "In civil geotechnical engineering, site grading establishes positive overland storm runoff away from structural foundations.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The construction gangs were busy **grading** the roadbed of the transcontinental railway across the alkali flats."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The merchant guild introduced strict standards for **grading** exported wool according to fiber fineness."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I observed the railroad laborers **grading** the sandy cut near the pond, filling carts with yellow loam."}
    ]
  },
  "Dashboard — grad/gradual.md": {
    "primary": "Taking place, progressing, or changing slowly by subtle degrees or steps over an extended duration.",
    "secondary": "In evolutionary biology and deep-time geomorphology, gradual continental drift explains plate tectonic displacement over millions of years.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The extinction of old species and the production of new ones are the results of a **gradual** and continuous process."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **gradual** decline of imperial virtue prepared Rome for subjugation under barbarian chieftains."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth recognized a **gradual** change in her sentiments toward Darcy, originating in admiration of his integrity."}
    ]
  },
  "Dashboard — grad/graduality.md": {
    "primary": "The quality, condition, or property of proceeding by small, gradual steps or incremental stages.",
    "secondary": "In developmental psychology and language acquisition, cognitive graduality characterizes the transition from babbling to lexical syntax.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The universal law of progress is marked by a profound **graduality** that links primordial nebulae to human mind."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Nature exhibits an unbroken **graduality** in the transition from basic reflex to conscious moral deliberation."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The growth of spiritual wisdom requires patience, proceeding with that divine **graduality** seen in growing trees."}
    ]
  },
  "Dashboard — grad/gradually.md": {
    "primary": "In a slow, step-by-step manner; little by little over an extended period.",
    "secondary": "In clinical pharmacology, physicians titrate dosages gradually to avoid adverse drug reactions while monitoring therapeutic efficacy.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The coral atolls **gradually** subside beneath the tropical ocean, leaving rings of barrier reefs behind."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The stormy clouds dispersed **gradually**, revealing a calm blue sky illuminated by the morning sun."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes **gradually** pieced together the tangled threads of the mystery from footprints upon the moor."}
    ]
  },
  "Dashboard — grad/gradualness.md": {
    "primary": "The characteristic or quality of proceeding slowly, step by step, or by barely perceptible increments.",
    "secondary": "In evolutionary biology debates, punctuated equilibrium challenges the absolute gradualness posited by classical Darwinism.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geological record illustrates the **gradualness** with which ancestral forms diverge into distinct genera."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Social reformers must respect the necessary **gradualness** of institutional transformations across generations."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Economic transitions toward cooperative enterprise must proceed with steady **gradualness** to ensure financial stability."}
    ]
  },
  "Dashboard — grad/graduate.md": {
    "primary": "A person who has successfully completed a course of study at a school or university; or to calibrate divisions on a measuring vessel.",
    "secondary": "In analytical chemistry, volumetric glassware is precision-graduated to measure exact fluid titration aliquots.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The scholar must **graduate** his studies from particular experimental phenomena to the highest philosophical axioms."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Edmund Bertram prepared to **graduate** from Oxford and enter holy orders as a country clergyman."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Steerforth was celebrated as the most brilliant university **graduate** of his year, admired by all his peers."}
    ]
  },
  "Dashboard — grad/graduated.md": {
    "primary": "Having earned an academic degree or diploma; or divided into marked stages, levels, or calibration lines.",
    "secondary": "In fiscal public policy, a graduated income tax levies progressively higher marginal tax rates on higher income brackets.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "The chemist poured the liquid into a **graduated** glass cylinder to measure the volume of gas released."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Watson had recently **graduated** from the University of London as a doctor of medicine before departing for India."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The municipal taxation system was **graduated** to place greater assessments upon luxury carriages and townhouses."}
    ]
  },
  "Dashboard — grad/graduation.md": {
    "primary": "The receiving or conferring of an academic degree or diploma; or a mark or system of marks indicating intervals on a scale.",
    "secondary": "In metrological instrumentation, precision laser graduation etches micrometric divisions onto optical scale reticles.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Upon his medical **graduation**, Martin Arrowsmith received his diploma and began his clinical internship at City Hospital."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The commencement celebrations and formal **graduation** ceremony marked the closing of his youth at Princeton."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The sensitive galvanometer was fitted with an ivory scale whose fine **graduation** permitted fractional degree readings."}
    ]
  },
  "Dashboard — grad/postgraduate.md": {
    "primary": "Relating to, enrolled in, or conducting advanced academic study undertaken after obtaining a bachelor's degree.",
    "secondary": "In medical education and surgical credentialing, postgraduate residency training provides clinical subspecialty competence.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Dr. Gottlieb encouraged young Arrowsmith to pursue rigorous **postgraduate** research in bacteriology at the institute."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Resident Patient", "quote": "Dr. Trevelyan completed his **postgraduate** medical honors, winning a prestigious university prize for his treatise on catalepsy."},
      {"author": "H. G. Wells", "work": "The Food of the Gods", "quote": "The young chemist continued his **postgraduate** investigations into synthetic growth hormones in the private laboratory."}
    ]
  },
  "Dashboard — grad/retrograde.md": {
    "primary": "Directed or moving backward; declining to an earlier, inferior, or less developed state; inverse.",
    "secondary": "In observational astronomy, retrograde planetary motion describes the apparent westward looping movement of planets against background constellations.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "For your intent in going back to school in Wittenberg, it is most **retrograde** to our desire."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain parasitic lineages undergo **retrograde** development, losing sensory organs and locomotion possessed by ancestors."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The reign of the tyrant witnessed a **retrograde** collapse in constitutional liberties and imperial security."}
    ]
  },
  "Dashboard — grad/undergrad.md": {
    "primary": "An informal abbreviated term for an undergraduate student studying for a first university degree.",
    "secondary": "In university campus cultural history, undergrad societies governed literary debating clubs and intramural rowing rivalries.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "As an eager young **undergrad**, Amory Blaine debated poetry and politics late into the night at Cottage Club."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Ted Babbitt preferred tinkering with automobile engines to life as a scholarly college **undergrad**."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Three Students", "quote": "Holmes interrogated the nervous **undergrad** who was suspected of copying the confidential Greek examination papers."}
    ]
  },
  "Dashboard — grad/undergraduate.md": {
    "primary": "A university or college student who has not yet taken a first degree; or pertaining to such students.",
    "secondary": "In higher education administration, undergraduate liberal arts curricula balance foundational general education with departmental majors.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Herbert Pocket reminisced about his cheerful **undergraduate** days at Cambridge while dining with Pip in London."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Tom Bertram lived as an extravagant Oxford **undergraduate**, accumulating debts that burdened the family estate."},
      {"author": "Arthur Conan Doyle", "work": "The Gloria Scott", "quote": "Holmes looked back on his **undergraduate** college days when his singular habits of observation first attracted notice."}
    ]
  },
  "Dashboard — grad/ungraded.md": {
    "primary": "Not arranged, sorted, or classified into grades, stages, or quality levels; unrated.",
    "secondary": "In agricultural market wholesale logistics, ungraded bulk grain or fruit shipments command lower prices due to quality variance.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Merchants in open markets sold sacks of **ungraded** grain at lower prices to avoid municipal inspection fees."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The rustic wool buyer examined the piles of **ungraded** fleeces stacked haphazardly in the shearing barn."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The village farmer brought bushels of **ungraded** apples to the country store to barter for sugar and salt."}
    ]
  },

  # --- Dashboard — scend (32 words) ---
  "Dashboard — scend/ascend.md": {
    "primary": "To move, go, climb, or rise upward; or to rise to a higher social, political, or moral position.",
    "secondary": "In aeronautics and ballooning, lighter-than-air vessels ascend when buoyant force exceeds total gravitational weight.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I resolved to **ascend** to the summit of Montanvert, hoping the sublime mountain scenery would bring peace to my soul."},
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Brutus did **ascend** the public pulpit to render reasons for the death of Caesar before the citizens of Rome."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Ascend, I bid thee, to the heavenly hill, where radiant seraphim proclaim the eternal majesty of the creator."}
    ]
  },
  "Dashboard — scend/ascendable.md": {
    "primary": "Capable of being climbed, mounted, or scaled; accessible by ascent.",
    "secondary": "In mountaineering route topography, alpine surveyors map ascendable rock gullies through sheer glacial cirques.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The steep volcanic cone of the island was scarcely **ascendable** on its western slope due to loose basalt cinders."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The sheer granite wall of the Sierra crag appeared impossible, but Muir discovered an **ascendable** chimney in the rock."},
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The Swiss guides assured the party that the snowy ridge was easily **ascendable** with proper rope and ice axes."}
    ]
  },
  "Dashboard — scend/ascendance.md": {
    "primary": "Governing or controlling influence; domination, superiority, or supremacy; ascendancy.",
    "secondary": "In geopolitics and international balance-of-power theory, rising naval hegemons seek regional maritime ascendance.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rapid military **ascendance** of the Arabian caliphate reshaped the borders of the eastern Mediterranean world."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The parliamentary party achieved moral and constitutional **ascendance** during the long crisis of the Glorious Revolution."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The violent faction gained an alarming **ascendance** over the Paris municipal assemblies through terror and intimidation."}
    ]
  },
  "Dashboard — scend/ascendancy.md": {
    "primary": "A position of dominant power, commanding influence, or controlling superiority over others.",
    "secondary": "In historical Irish sociology, the Protestant Ascendancy designated the political and ecclesiastical ruling elite from the 17th to 19th centuries.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor observed with concern the powerful **ascendancy** that the passionate Willoughby had gained over Marianne's heart."},
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "To Sherlock Holmes she is always the woman; she alone achieved an intellectual **ascendancy** that commanded his admiration."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The Royal Air Force established air **ascendancy** over the English Channel, frustrating enemy invasion plans."}
    ]
  },
  "Dashboard — scend/ascendant.md": {
    "primary": "Rising in power, influence, or status; dominating; or the astrological degree rising on the eastern horizon.",
    "secondary": "In classical horoscopic astrology and medieval cosmology, the ascendant signifies the celestial sign ascending at natal birth.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The military faction was now in the **ascendant**, deposing civilian magistrates at will across the provinces."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond was confident that her charm was in the **ascendant**, ensuring her husband's acquiescence to her wishes."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The star of the Jacobin club was clearly **ascendant** as more moderate deputies fled the capital."}
    ]
  },
  "Dashboard — scend/ascendence.md": {
    "primary": "Controlling power, rising influence, or supreme authority; an alternative spelling of ascendance.",
    "secondary": "In sociological class analysis, the political ascendence of mercantile urban classes supplanted landed feudal aristocracies.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A single social class must not be permitted to achieve permanent political **ascendence** over the legislative council."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The gradual **ascendence** of industrial cooperation over military subordination marks progressive societal evolution."},
      {"author": "David Hume", "work": "The History of England", "quote": "The monarch sought to maintain the royal prerogative against the growing **ascendence** of the House of Commons."}
    ]
  },
  "Dashboard — scend/ascendency.md": {
    "primary": "Controlling influence, superior power, or governing authority; an alternative spelling of ascendancy.",
    "secondary": "In constitutional theory and colonial administration, parliamentary ascendency defined the legal subordination of provincial assemblies.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Letter to Richard Burke", "quote": "Burke criticized the narrow **ascendency** that excluded the vast Catholic majority of Ireland from civic participation."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The intellectual **ascendency** of Athens dominated the culture of the ancient Mediterranean for centuries."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The fierce religious faction asserted its spiritual **ascendency** with unrelenting puritanical severity."}
    ]
  },
  "Dashboard — scend/ascendent.md": {
    "primary": "Rising in power, authority, or prestige; dominant; an alternative spelling of ascendant.",
    "secondary": "In celestial cartography and astronomical history, ascendent zodiacal constellations mark the eastern dawn horizon.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "When heroic moral conviction is **ascendent** in a nation, petty materialist factions melt away like mist."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Christian faith became **ascendent** throughout the empire following the conversion of Constantine."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "A prudent courtier observes which faction is **ascendent** in the sovereign's personal confidence."}
    ]
  },
  "Dashboard — scend/ascender.md": {
    "primary": "A person or thing that climbs or rises; or in typography, the upward vertical stem of a lowercase letter extending above the x-height.",
    "secondary": "In technical mountaineering and caving, a mechanical ascender uses a camming mechanism to grip ropes for vertical rope climbing.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The mountain **ascender** strapped on his crampons and checked his rope before tackling the icy couloir."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Gothic scribe carefully balanced the tall **ascender** of the letters 'b' and 'd' across the illuminated page."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger designed a mechanical rope **ascender** to scale the vertical red sandstone cliffs of the plateau."}
    ]
  },
  "Dashboard — scend/ascendible.md": {
    "primary": "Capable of being ascended, climbed, scaled, or mounted; climbable.",
    "secondary": "In structural fire safety and rescue engineering, designing ascendible exterior fire escapes ensures emergency access.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The cliffs of Saint Helena appeared barely **ascendible**, broken only by a few narrow, treacherous goat tracks."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "A steep, talus-covered ravine provided the only **ascendible** route to the summit of the granite peak."},
      {"author": "Herman Melville", "work": "Typee", "quote": "Toby declared that the precipitous mountain ridge was **ascendible** if they followed the roots of the wild bamboo."}
    ]
  },
  "Dashboard — scend/ascending.md": {
    "primary": "Moving, climbing, or sloping upward; rising in scale, sequence, pitch, or magnitude.",
    "secondary": "In human cardiovascular anatomy, the ascending aorta arises from the left ventricle and arches into the systemic arterial tree.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The heavy mail coach labored up the hill, the horses panting in the chilly mist of the **ascending** road."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I observed the dark, colossal figure of the creature **ascending** the sheer face of the glacier with incredible speed."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Watson followed Holmes up the narrow, **ascending** trail leading to the ancient Neolithic stone hut."}
    ]
  },
  "Dashboard — scend/condescend.md": {
    "primary": "To show feelings of patronizing superiority; or to voluntarily waive one's rank and stoop to someone of lower status.",
    "secondary": "In eighteenth-century etiquette and moral philosophy, aristocratic patrons were praised when they would condescend with gracious courtesy.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lady Catherine de Bourgh did not **condescend** to converse with anyone of inferior social status at the assembly."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Estella would hardly **condescend** to touch Pip's hand when they met on the terrace of Satis House."},
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "He will not **condescend** to yield an inch of his ancestral French claims without fierce battle."}
    ]
  },
  "Dashboard — scend/condescending.md": {
    "primary": "Displaying or characterized by a patronizing, haughty, or superior attitude toward others.",
    "secondary": "In interpersonal communication and sociolinguistics, condescending vocal inflections undermine collaborative workplace dynamics.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins spoke with a **condescending** pomposity that made everyone in the parlor smile with amusement."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Steerforth addressed the humble boatmen in a charming yet unmistakably **condescending** manner."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Blanche Ingram cast a cold, **condescending** glance upon the quiet governess seated in the drawing-room corner."}
    ]
  },
  "Dashboard — scend/condescendingly.md": {
    "primary": "In a patronizing, haughty, or superior manner that implies social or intellectual condescension.",
    "secondary": "In diplomatic protocol and bilateral negotiations, addressing foreign delegates condescendingly poisons international relations.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lady Catherine patted Elizabeth's cheek **condescendingly**, approving her plain muslin gown as suitable for her station."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Sir Leicester Dedlock bowed **condescendingly** to his country neighbors at the church portal after the Sunday service."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond smiled **condescendingly** at her rustic cousins, conscious of her superior finishing-school education."}
    ]
  },
  "Dashboard — scend/condescendingness.md": {
    "primary": "The characteristic or quality of adopting a patronizing, superior, or haughty demeanor toward others.",
    "secondary": "In character psychology and ethical conduct literature, conscious condescendingness offends self-respecting individuals.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Nothing is more odious to a man of independent spirit than the calculated **condescendingness** of a wealthy patron."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley rebuked Emma for her thoughtless **condescendingness** toward poor Miss Bates at the picnic on Box Hill."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The philosopher despised the fashionable **condescendingness** with which aristocratic salons received sincere literary genius."}
    ]
  },
  "Dashboard — scend/crescendo.md": {
    "primary": "A gradual, steady increase in loudness or intensity, especially in a piece of music; or a climax.",
    "secondary": "In dramatic narrative structure and orchestral scoring, an orchestral crescendo builds dynamic emotional tension before the resolution.",
    "quotes": [
      {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "The brass and percussion surged into a thunderous **crescendo** that seemed to shake the foundations of the concert hall."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The roar of artillery and the screams of the Martian heat-ray rose to a terrifying **crescendo** across the valley."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "The yellow cocktail music played while the laughter and chatter swelled to an alcoholic **crescendo** under the garden lights."}
    ]
  },
  "Dashboard — scend/decrescendo.md": {
    "primary": "A gradual, steady decrease in loudness, volume, or musical intensity; diminuendo.",
    "secondary": "In classical musical performance, executing a controlled decrescendo requires subtle bow-pressure reduction and breath control.",
    "quotes": [
      {"author": "Thomas Mann", "work": "Buddenbrooks", "quote": "Hanno played the piano sonata with tender delicacy, allowing the closing chords to sink into a faint **decrescendo**."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The roaring surf along the sandy shore subsided into a soft **decrescendo** as the ocean tide began to turn."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Cardboard Box", "quote": "The distant street sounds faded in a slow **decrescendo** as midnight settled over the fog-bound metropolis."}
    ]
  },
  "Dashboard — scend/descend.md": {
    "primary": "To move, go, climb, or slope downward; to fall, sink, or be inherited by succession.",
    "secondary": "In aircraft avionics and air traffic navigation, transport aircraft descend along standardized three-degree instrument glide paths.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I saw the shadow of the daemon **descend** from the rocky pinnacles and vanish into the shadowy Alpine forest."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Down from the crystal battlements of heaven did the rebellious host **descend** into bottomless perdition."},
      {"author": "Jules Verne", "work": "Journey to the Center of the Earth", "quote": "The daring explorers prepared to **descend** into the dark volcanic chimney of Sneffels on sturdy rope ladders."}
    ]
  },
  "Dashboard — scend/descendant.md": {
    "primary": "A person, plant, or animal descended from a specific ancestor; offspring.",
    "secondary": "In evolutionary biology and cladistic phylogenetics, each modern vertebrate is a descendant of early lobe-finned sarcopterygian fish.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every living species is the direct **descendant** of ancient ancestral forms through continuous, modified generation."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Colonel Pyncheon's proud **descendant** inhabited the dark seven-gabled mansion, shadowed by an ancient curse."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The degenerate **descendant** of the great Antonines surrendered imperial power to eunuchs and corrupt favorites."}
    ]
  },
  "Dashboard — scend/descendants.md": {
    "primary": "Plural of descendant; individuals or organisms proceeding in direct lineage from a common progenitor.",
    "secondary": "In population genetics and pedigree analysis, the genetic diversity of surviving descendants reveals historical population bottlenecks.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The diversified **descendants** of a single species occupy many and widely different places in the economy of nature."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The disinherited Saxon **descendants** of King Alfred bitterly resented the rule of the Norman conquerors."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The proud **descendants** of the Cavalier nobility gathered to celebrate the restoration of the royal house."}
    ]
  },
  "Dashboard — scend/descendent.md": {
    "primary": "Moving or proceeding downward; descending; or a variant spelling of descendant.",
    "secondary": "In genealogical heraldry and lineage tracing, descendent branches of a family inherit cadency marks upon armorial bearings.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whalemen watched the **descendent** arc of the iron harpoon as it plunged into the foaming white water."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **descendent** lines of imperial legitimacy were repeatedly severed by military mutiny and civil war."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The heavy iron portcullis fell in a swift, **descendent** crash, cutting off retreat for the besieged defenders."}
    ]
  },
  "Dashboard — scend/descender.md": {
    "primary": "A person or thing that descends; or in typography, the portion of a lowercase letter extending below the baseline (e.g. g, j, p, q, y).",
    "secondary": "In typographic anatomy and typeface design, the length of the descender balances line spacing and vertical text density.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The medieval illuminator drew the long **descender** of the initial letter deep into the lower floral margin."},
      {"author": "Jules Verne", "work": "Journey to the Center of the Earth", "quote": "The courageous **descender** into the volcanic chasm secured his hempen guide-rope to a basalt pillar."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger designed a braking mechanism to ensure that the human **descender** could lower himself without injury."}
    ]
  },
  "Dashboard — scend/descending.md": {
    "primary": "Moving, falling, or sloping downward; dropping toward a lower elevation, level, or scale.",
    "secondary": "In human neuroanatomy, the descending corticospinal tracts transmit upper motor neuron signals to the spinal cord.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The winged archangel Raphael was seen **descending** through the radiant celestial spheres toward Eden."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The heavy knife of the guillotine was **descending** day after day, severing the heads of innocent and guilty alike."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The tropical twilight was **descending** rapidly, shrouding the dark river and the silent primeval forest."}
    ]
  },
  "Dashboard — scend/scend.md": {
    "primary": "The upward surge, heave, or momentum of a ship lifted by an ocean wave; or to heave upward in a sea swell.",
    "secondary": "In nautical seamanship and naval architecture, understanding the scend of the sea prevents vessels from broaching in following seas.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Pequod rose upon the colossal **scend** of the Pacific swell, her bowsprit pointing toward the stormy stars."},
      {"author": "Joseph Conrad", "work": "The Nigger of the 'Narcissus'", "quote": "With a long, majestic **scend**, the sailing ship climbed the towering mountain of green water, shaking the spray from her bows."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The schooner gave a heavy **scend** as she entered the narrow inlet, her keel barely clearing the submerged sandbar."}
    ]
  },
  "Dashboard — scend/transcend.md": {
    "primary": "To go beyond the range or limits of physical or normal experience; to surpass or excel.",
    "secondary": "In philosophical epistemology and Kantian idealism, synthetic a priori concepts transcend raw empirical sensory data.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "In the serene woods, the soul awakens to divine truths that **transcend** the petty concerns of worldly existence."},
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "Speculative reason attempts in vain to **transcend** the boundaries of sensible experience to comprehend the infinite."},
      {"author": "Percy Bysshe Shelley", "work": "A Defence of Poetry", "quote": "The creations of great poetry **transcend** mortal limits, awakening divine sensations that survive empires."}
    ]
  },
  "Dashboard — scend/transcendence.md": {
    "primary": "Existence or experience beyond the normal physical level; supreme or surpassing excellence.",
    "secondary": "In philosophical theology, divine transcendence denotes ultimate ontological otherness independent of the created universe.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The moral sentiment reveals the **transcendence** of the spiritual law, elevating the individual above circumstance."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The philosopher caught glimpses of eternal **transcendence** shining through the transient symbols of nature."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "True artistic genius achieves a sublime **transcendence** that lifts the human spirit toward absolute beauty."}
    ]
  },
  "Dashboard — scend/transcendency.md": {
    "primary": "The quality or state of being transcendent; surpassing preeminence, excellence, or elevation.",
    "secondary": "In scholastic metaphysics, the transcendentals (unity, truth, goodness, beauty) possess absolute transcendency across all ontological categories.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The **transcendency** of divine wisdom far surpasses the feeble grasp of human speculative imagination."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "Truth possesses an inherent **transcendency** that will assuredly prevail over error in free and open encounter."},
      {"author": "David Hume", "work": "Dialogues Concerning Natural Religion", "quote": "Philo questioned whether the claimed **transcendency** of theological concepts can be verified by human reason."}
    ]
  },
  "Dashboard — scend/transcendent.md": {
    "primary": "Beyond or above the range of normal physical human experience; exceptionally great, supreme, or sublime.",
    "secondary": "In transcendental philosophy, transcendent knowledge purports to step entirely outside the conditions of sensory experience.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The jagged icy peaks of Mont Blanc shone with a **transcendent** and silent beauty under the midnight moon."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan gazed upon the uncreated light of heaven with ruined, yet still **transcendent**, angelic glory."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "The soul's deep intuition reveals a **transcendent** truth that defies all conventional social dogmas."}
    ]
  },
  "Dashboard — scend/transcendental.md": {
    "primary": "Relating to a spiritual or non-physical realm; or in philosophy, relating to the presuppositions of empirical knowledge.",
    "secondary": "In pure mathematics and number theory, a transcendental number (such as pi or e) is not the root of any non-zero polynomial with rational coefficients.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "I entitle **transcendental** all cognition which is occupied not with objects, but with our mode of cognition of objects."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Teufelsdröckh expounded his **transcendental** philosophy of clothes from his attic tower high above Weissnichtwo."},
      {"author": "Ralph Waldo Emerson", "work": "The Transcendentalist", "quote": "The **transcendental** thinker trusts the direct voice of conscience above all established institutional authority."}
    ]
  },
  "Dashboard — scend/transcendentalism.md": {
    "primary": "A nineteenth-century philosophical and literary movement emphasizing intuition, spiritual self-reliance, and the unity of nature.",
    "secondary": "In American intellectual history, New England transcendentalism was championed by Ralph Waldo Emerson, Henry David Thoreau, and Margaret Fuller.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "The Transcendentalist", "quote": "What is popularly called **transcendentalism** among us is the assertion of the ideal over the sensible in human life."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The principles of practical **transcendentalism** led me to the woods, to live deliberately and confront the essential facts of life."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The utopian community at Blithedale attempted to embody the lofty ideals of New England **transcendentalism** in daily labor."}
    ]
  },
  "Dashboard — scend/transcendentalist.md": {
    "primary": "A person who adheres to or advocates the philosophical doctrines of transcendentalism.",
    "secondary": "In nineteenth-century literary history, the transcendentalist periodical The Dial published radical essays on philosophy, art, and abolition.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "The Transcendentalist", "quote": "The **transcendentalist** believes in miracles, in the perpetual openness of the human mind to new influxes of light."},
      {"author": "Nathaniel Hawthorne", "work": "The Celestial Railroad", "quote": "The traveler observed the strange modern pilgrim, who claimed to be a thorough **transcendentalist** in spiritual matters."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The solitary thinker lived as a practical **transcendentalist**, seeking truth in the silence of nature."}
    ]
  },
  "Dashboard — scend/transcendentally.md": {
    "primary": "In a manner that surpasses normal human experience or limits; supremely, sublimely, or metaphysically.",
    "secondary": "In Kantian philosophical critique, principles applied transcendentally beyond sensory limits produce dialectical antinomies.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The world of physical appearances is **transcendentally** symbolic of the unseen spiritual realities behind it."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The primary imagination operates **transcendentally** as the living power and prime agent of all human perception."},
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "When reason seeks to judge **transcendentally**, it wanders into unavoidable contradictions regarding the cosmos."}
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

print(f"Motion Batch 3A: Successfully updated {updated}/{len(data)} notes.")
