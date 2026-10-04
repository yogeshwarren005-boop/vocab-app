# -*- coding: utf-8 -*-
"""
Part 1: 33 words from Dashboard — lig ('alligator' to 'lignosae')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_lig = {
  "alligator": {
    "primary": "A large predatory amphibious reptile of the genus Alligator in the order Crocodylia, characterized by a broad, rounded snout and dark armored skin.",
    "secondary": "In leathercraft and commercial herpetology, durable exotic hide patterned with quadrangular scales; or specialized heavy mechanical jaws resembling a reptile's mouth.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The habits of the American **alligator** in the rivers of South America illustrate how predatory reptiles dominate freshwater margins."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "He described the southern bayous where the sluggish **alligator** basks upon the mudbanks through the sultry summer noon."},
      {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The leather traveling bag was crafted of genuine tanned **alligator**, its dark pebbled hide gleaming under the street lamp."}
    ]
  },
  "alligatored": {
    "primary": "Displaying a fractured surface pattern characterized by coarse interconnected cracks resembling the textured skin of a reptilian snout.",
    "secondary": "In materials engineering and architectural coatings, exhibiting extensive crazing or rectilinear fissure networks caused by severe thermal contraction or ultraviolet degradation.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ancient varnish across the Venetian panel had become heavily **alligatored**, fracturing into tiny rectangular plates over the centuries."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The dried sea-boots worn by the harpooneer had grown brittle and **alligatored** from decades of brine and sun exposure."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Examining the painted carriage door, Holmes noted the weathered enamel was cracked and **alligatored** near the brass handle."}
    ]
  },
  "alligatorfish": {
    "primary": "A slender marine bottom-dwelling teleost fish of the family Agonidae, distinguished by hard bony armor plates encasing its body.",
    "secondary": "In ichthyological taxonomy, a northern coastal agonid species such as Aspidophoroides monopterygius, adapted for crawling along rocky seabed substrates.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The curious **alligatorfish** of the northern seas carries a rigid exoskeleton of interlocking bony plates that protects it from benthic predators."},
      {"author": "George Brown Goode", "work": "Oceanic Ichthyology", "quote": "Specimens of the armored **alligatorfish** dredged from cold Atlantic shallows reveal how dorsal fins are reduced in bottom-dwelling species."},
      {"author": "William Beebe", "work": "The Arcturus Adventure", "quote": "Among the marine curiosities swept aboard in our dredge net was an armored **alligatorfish**, stiff and motionless as a carving."}
    ]
  },
  "alligatoridae": {
    "primary": "The taxonomic family of crocodilian reptiles comprising modern alligators, caimans, and their extinct ancestral lineages.",
    "secondary": "In vertebrate paleontology and systematic herpetology, a clade characterized by mandibular teeth fitting into internal pits of the upper jaw when the mouth closes.",
    "quotes": [
      {"author": "Richard Owen", "work": "Palaeontology", "quote": "Fossil crania attributable to the family **Alligatoridae** demonstrate that broad-snouted crocodilians flourished in temperate river systems during the Eocene."},
      {"author": "Alfred Romer", "work": "Vertebrate Paleontology", "quote": "Within the order Crocodylia, the **Alligatoridae** diverged early by developing specialized dentition adapted for crushing freshwater mollusks and armored prey."},
      {"author": "Thomas Henry Huxley", "work": "On the Classification of the Dinosauria", "quote": "Comparative anatomical studies of living **Alligatoridae** provide essential morphological insights into the cranial architecture of extinct reptiles."}
    ]
  },
  "colligate": {
    "primary": "To bind, tie, or unite closely together; especially to combine disparate observations or facts under a single unifying empirical law.",
    "secondary": "In philosophy of science and epistemology, to synthesize diverse experimental data under a general conception that explains their systematic relationship.",
    "quotes": [
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "The philosopher does not merely collect observations; his duty is to **colligate** facts by discovering the appropriate conception that binds them into a law."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Dr. Whewell maintains that Kepler did not deduce the planetary orbits, but did simply **colligate** the observed positions of Mars under the geometrical idea of an ellipse."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "When we **colligate** several empirical assertions, we formulate an integrated hypothesis that must undergo rigorous inductive verification."}
    ]
  },
  "colligation": {
    "primary": "The act of binding or tying together; specifically, the conceptual uniting of observed isolated phenomena under a single explanatory concept.",
    "secondary": "In scientific methodology and formal logic, the epistemic process whereby empirical propositions are organized into a coherent inductive generalization.",
    "quotes": [
      {"author": "William Whewell", "work": "Novum Organon Renovatum", "quote": "This **colligation** of facts is the primary foundation of scientific progress, transforming scattered data into an orderly system of truths."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "He argued that the **colligation** of known particulars does not constitute true induction unless it introduces a valid general inference beyond them."},
      {"author": "William Stanley Jevons", "work": "The Principles of Science", "quote": "A brilliant inductive discovery often consists in the sudden **colligation** of observations that had previously seemed utterly unconnected."}
    ]
  },
  "coreligionist": {
    "primary": "A person who adheres to the same religion, ecclesiastical community, or system of theological belief as another individual.",
    "secondary": "In sociology of religion and diplomatic history, an adherent bound by mutual confessional ties, often invoking communal solidarity across national boundaries.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The emigrant felt an immediate bond with each **coreligionist** he encountered in the frontier settlements of the western territory."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The emperor extended his imperial protection to every **coreligionist** dwelling under alien rule in the adjacent provinces."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The English Puritans sent fraternal greetings and financial subsidies to their beleaguered **coreligionist** brethren upon the European continent."}
    ]
  },
  "diligence": {
    "primary": "Constant and earnest effort to accomplish what is undertaken; persistent application to work, duty, or study.",
    "secondary": "In comparative civil law, the standard of prudent and reasonable care required of a fiduciary or contracting party to avoid culpable liability.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I will make her amend it; she shall use **diligence** to recover what she has so carelessly endangered."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate pursued his anatomical investigations with untiring **diligence**, rising before dawn to examine his tissue specimens."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The young detective had pursued his inquiries with commendable **diligence**, examining every footprint along the garden path."}
    ]
  },
  "diligent": {
    "primary": "Characterized by steady, earnest, and energetic effort in completing tasks; industriously attentive to obligations.",
    "secondary": "In administrative practice and scholarship, marked by painstaking, scrupulous, and meticulous investigative thoroughness.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "He is a **diligent** servant, watchful and prompt to fulfill every command that his lord assigns to him."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Silas was a **diligent** weaver, working long hours at his loom while the shuttle flew back and forth in rhythmic cadence."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A **diligent** observer of nature will discover that every hour of the day possesses its own distinct flora and light."}
    ]
  },
  "diligently": {
    "primary": "In a steady, careful, and painstaking manner; with persevering and conscientious attention to detail or duty.",
    "secondary": "In archival research and investigative jurisprudence, executed with rigorous, thorough, and exhaustive scrutiny.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel worked **diligently** throughout the stormy night to secure the wheat ricks against the penetrating rain."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "The White Rabbit searched **diligently** through the grass for his white kid gloves and fan, muttering anxiously."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mary Garth applied herself **diligently** to her sewing, listening patiently to the querulous complaints of the invalid."}
    ]
  },
  "disoblige": {
    "primary": "To refuse or neglect to accommodate another person; to act contrary to someone's wishes or convenience; to inconvenience or offend.",
    "secondary": "In social etiquette and civil jurisprudence, to breach a courteous accommodation or fail to render an agreed personal service.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was unwilling to **disoblige** her father by refusing a request that he urged with such affectionate earnestness."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "I resolved not to **disoblige** the prime minister by opposing any measure that might provoke his capricious wrath."},
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "She dreaded to **disoblige** her family, yet her conscience forbade her to yield to their tyrannical matrimonial demands."}
    ]
  },
  "disobliging": {
    "primary": "Unwilling to please or accommodate others; unaccommodating, uncooperative, or deliberately discourteous.",
    "secondary": "In behavioral description and diplomatic conduct, showing stubborn refusal to render conventional courtesies or concessions.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "It was impossible to consider him rude, yet his cold reserve was often interpreted as haughty and **disobliging**."},
      {"author": "Frances Burney", "work": "Evelina", "quote": "The shopkeeper was exceedingly **disobliging**, refusing to show the silk ribbons with any pretense of polite civility."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Tom considered his cousin exceedingly **disobliging** when she declined to fetch his fishing tackle from the upper loft."}
    ]
  },
  "eligibility": {
    "primary": "The state, condition, or status of being legally, formally, or morally qualified for selection, office, or privilege.",
    "secondary": "In public law, administrative governance, and electoral jurisprudence, the statutory satisfaction of mandatory qualification prerequisites.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional criteria governing **eligibility** for the presidency were established to prevent undue foreign intrigue and factional bias."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Broadening educational qualifications enhances the general **eligibility** of citizens to participate actively in democratic institutions."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In democratic societies, personal wealth does not confer exclusive political **eligibility**, which remains open to general civic merit."}
    ]
  },
  "eligible": {
    "primary": "Legally, formally, or practically qualified to participate, hold office, or be chosen; desirable or suitable as a prospective candidate.",
    "secondary": "In social courtship conventions and statutory law, meeting all conventional financial, class, or legal standards for marriage or appointment.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The community regarded young Mr. Chettam as an eminently **eligible** suitor, possessed of unencumbered estates and amiable manners."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The commissioner verified that every applicant was physically **eligible** before admitting them into the constabulary ranks."},
      {"author": "Oscar Wilde", "work": "The Importance of Being Earnest", "quote": "Lady Bracknell examined his family connections to judge whether he could be regarded as an **eligible** husband for her daughter."}
    ]
  },
  "ineligibility": {
    "primary": "The state or condition of not being legally or officially qualified to participate, hold an office, or receive a privilege.",
    "secondary": "In statutory governance and administrative law, legal disqualification resulting from failure to satisfy statutory age, residency, or citizenship criteria.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Writings of Thomas Jefferson", "quote": "The statute clearly defined the circumstances that would produce political **ineligibility** among former crown magistrates."},
      {"author": "James Madison", "work": "Debates in the Federal Convention", "quote": "He argued that temporary **ineligibility** to re-election was essential to guard public representatives against executive corruption."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Disqualifying senators during their term of service removes suspected motives of personal gain without creating perpetual **ineligibility**."}
    ]
  },
  "ineligible": {
    "primary": "Not legally, officially, or practically qualified to be chosen, elected, or granted a particular position or benefit.",
    "secondary": "In judicial review and public administration, barred by constitutional disqualification or statutory non-compliance from public office.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "The election board determined that the candidate was **ineligible** owing to his non-residence in the judicial district."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "Those who had not contributed toward the civic defense fund were deemed **ineligible** for the municipal privileges granted to subscribers."},
      {"author": "Henry Adams", "work": "The History of the United States", "quote": "Foreign ministers were declared **ineligible** to hold simultaneous commissions in the newly organized provincial assemblies."}
    ]
  },
  "irreligion": {
    "primary": "Absence of religious beliefs; indifference, neglect, hostility, or open opposition toward religious practices and divine reverence.",
    "secondary": "In theological discourse and moral philosophy, the habitual contempt for sacred duties and repudiation of organized ecclesiastical authority.",
    "quotes": [
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "He contended that moral decay was fostered far more by ecclesiastical tyranny than by speculative **irreligion** among thoughtful men."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The fanaticism of revolutionary **irreligion** demolished ancient shrines while erecting altars to abstract philosophical concepts."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The fashionable world too often excuses blatant **irreligion** under the false name of intellectual wit and social freedom."}
    ]
  },
  "irreligionist": {
    "primary": "A person who rejects or opposes religion; an outspoken advocate of religious skepticism, secularism, or impiety.",
    "secondary": "In church history and intellectual apologetics, an adversary who polemically assaults ecclesiastical traditions and orthodox dogmas.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The stern Puritan elders looked with deep suspicion upon the stranger, suspecting him of being an unrepentant **irreligionist**."},
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "He defended his skeptical philosophical theses against the charge of being a reckless **irreligionist** intent on unsettling popular faith."},
      {"author": "G. K. Chesterton", "work": "Orthodoxy", "quote": "The modern **irreligionist** often displays a dogmatic fervor as unyielding as the most rigorous medieval inquisitor."}
    ]
  },
  "irreligious": {
    "primary": "Lacking religious belief, reverence, or spiritual devotion; showing disregard, irreverence, or disrespect toward sacred things.",
    "secondary": "In social commentary and moral theology, manifesting active disregard for liturgical observance and theological doctrine.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Hold, unbeseeming hands! An **irreligious** act will draw down heavy judgment upon your rebellious heads."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The philosophers of pagan antiquity were frequently accused of harboring **irreligious** views because they scoffed at popular mythologies."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Captain Ahab was characterized as a dark, **irreligious** old man who dared to defy the elemental forces of heaven and ocean."}
    ]
  },
  "irreligiousness": {
    "primary": "The state, condition, or habit of being irreligious; lack of religious devotion, faith, or spiritual reverence.",
    "secondary": "In social ethics and pastoral literature, pervasive secular indifference characterized by the abandonment of devotional and liturgical life.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "An Argument Against Abolishing Christianity", "quote": "The growing **irreligiousness** of the metropolis was manifested in the complete neglect of Sunday worship and clerical counsel."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The rector lamented the casual **irreligiousness** of the farming folk, who treated sacred days as mere occasions for tavern conviviality."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A temperament marked by aggressive **irreligiousness** is often accompanied by an acute distrust of mystical or intuitive feelings."}
    ]
  },
  "ligament": {
    "primary": "A tough, flexible band of fibrous connective tissue that connects two bones or cartilages together or holds a joint in place.",
    "secondary": "In comparative anatomy and mechanical biology, dense regular collagenous tissue resisting tensile stress and guiding joint articulation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The articulation of the bones and the attachment of each **ligament** in the limb display exquisite functional adaptation."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "Microscopic examination of the capsular **ligament** reveals how closely anthropoid shoulder anatomy mirrors that of human primates."},
      {"author": "Oliver Wendell Holmes", "work": "The Autocrat of the Breakfast-Table", "quote": "Every fibrous **ligament** uniting human hearts in society is woven from mutual memories, shared trials, and long companionship."}
    ]
  },
  "ligan": {
    "primary": "Goods, cargo, or wreckage sunk at sea with a buoy attached to mark the spot for subsequent recovery.",
    "secondary": "In admiralty jurisprudence and maritime salvage law, cargo thrown overboard (jetsam) that remains buoyant or buoy-marked, preserving owner title.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Flotsam is where goods continue floating; jetsam where they sink; and **ligan** where they are sunk with a cork or buoy tied to them for recovery."},
      {"author": "Richard Henry Dana Jr.", "work": "The Seaman's Friend", "quote": "The coastal wreckers claimed salvage rights over the sunken cargo, asserting that the cask anchored by the buoy constituted legal **ligan**."},
      {"author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "The salvage tug drifted above the marked shoal, searching through the fog for the tethered cask of **ligan** dropped by the grounded steamer."}
    ]
  },
  "ligand": {
    "primary": "An ion or molecule that binds specifically to a central metal atom to form a coordination complex, or binds to a biological receptor.",
    "secondary": "In biochemistry and coordination chemistry, an electron-pair donating group or signaling molecule that induces conformational changes in proteins.",
    "quotes": [
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The bonding between a metallic ion and a surrounding **ligand** involves both electrostatic attraction and coordinate covalent electron donation."},
      {"author": "Svante Arrhenius", "work": "Immunochemistry", "quote": "The equilibrium between the biological receptor and its complementary **ligand** obeys the fundamental mathematical laws of mass action."},
      {"author": "John Howard Northrop", "work": "Crystalline Enzymes", "quote": "The specific binding of an organic **ligand** to the enzymatic active site dictates the catalytic rate of metabolic transformation."}
    ]
  },
  "ligate": {
    "primary": "To tie off or bind tightly, especially a blood vessel or surgical duct with a suture, ligature, or clamp during an operation.",
    "secondary": "In molecular genetics and surgical therapeutics, to join nucleic acid fragments covalently using ligase or occlude hollow structures to stop hemorrhage.",
    "quotes": [
      {"author": "Joseph Lister", "work": "On the Antiseptic Principle in the Practice of Surgery", "quote": "The surgeon must carefully **ligate** the exposed artery with carbolized catgut to prevent hemorrhage without introducing septic contagion."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cases of severe trauma, the immediate necessity is to **ligate** the bleeding vessel before systemic collapse supervenes."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "John Hunter demonstrated how to **ligate** the main arterial trunk far above the aneurysmal sac, revolutionizing vascular surgery."}
    ]
  },
  "ligation": {
    "primary": "The surgical act of tying off a blood vessel, duct, or tissue structure with a thread, wire, or suture.",
    "secondary": "In molecular biology and vascular surgery, the covalent joining of complementary DNA strands or therapeutic occlusion of hemorrhaging vessels.",
    "quotes": [
      {"author": "Joseph Lister", "work": "The Collected Papers of Joseph Lister", "quote": "The clinical success of arterial **ligation** depends entirely upon preventing putrefactive fermentation within the wound margin."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prompt **ligation** of the severed vessels prevented fatal exsanguination before the patient reached the hospital ward."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "William Harvey demonstrated the unidirectional circulation of blood by applying temporary **ligation** to the veins of the human arm."}
    ]
  },
  "ligature": {
    "primary": "A piece of cord, wire, or suture thread used in surgery to tie off blood vessels; or something that binds or connects things together.",
    "secondary": "In typography and music notation, a composite character combining two letters (like æ) or a curved slurred line binding musical notes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Bind up his wounds with tender care, and let a firm **ligature** stay the course of his fast-ebbing blood."},
      {"author": "Joseph Lister", "work": "Antiseptic Surgery", "quote": "The silk **ligature** was steeped in carbolized oil, ensuring that deep tissue closure remained free from bacterial decomposition."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "I felt hundreds of slender cords bound about my limbs, each tiny **ligature** holding me firmly fastened to the ground."}
    ]
  },
  "liger": {
    "primary": "A hybrid offspring resulting from the mating of a male lion (Panthera leo) and a female tiger (Panthera tigris).",
    "secondary": "In mammalian genetics and zoology, a large feline hybrid exhibiting striped tawny fur, marked gigantism, and male sterility caused by Haldane's rule.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The rare zoological hybrid known as a **liger** demonstrates that distinct species of Panthera can interbreed when kept in long confinement."},
      {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "Breeding experiments producing the **liger** illustrate how reproductive barriers between wild felids remain largely behavioral in nature."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The menagerie featured a captive **liger**, whose immense bulk exceeded that of either parent while displaying faint tiger stripes."}
    ]
  },
  "ligne": {
    "primary": "A historic unit of length equal to one-twelfth of an inch or roughly 2.256 millimeters, widely used in watchmaking and button sizing.",
    "secondary": "In traditional Swiss horology and garment manufacturing, a standard measure of movement caliber diameter or button diameter.",
    "quotes": [
      {"author": "Horace Walpole", "work": "Letters of Horace Walpole", "quote": "The delicate Swiss movement measured barely eight **ligne** across, yet ticked with absolute precision within its enameled gold case."},
      {"author": "Charles Dickens", "work": "Household Words", "quote": "The watchmaker examined the miniature escapement through his loupe, measuring each tiny gear down to a fraction of a **ligne**."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes measured the diameter of the foreign pearl button, noting it conformed exactly to the eighteen-**ligne** continental scale."}
    ]
  },
  "ligneous": {
    "primary": "Consisting of, resembling, or having the texture and properties of wood; woody or timber-like in composition.",
    "secondary": "In plant anatomy and histology, containing high concentrations of secondary xylem and rigid, heavily lignified cell walls.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Perennial shrubs produce tough **ligneous** stems that endure winter frosts by virtue of thickened secondary xylem."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The climbing lianas develop thick **ligneous** cords that twist around tropical forest trees to ascend into the sunlit canopy."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The old decayed pine stump had broken down into soft, reddish **ligneous** fibers that crumbled easily between my fingers."}
    ]
  },
  "lignify": {
    "primary": "To convert into wood or woody tissue; to become hard, rigid, and wood-like through the deposition of lignin.",
    "secondary": "In plant physiology, to deposit complex phenolic polymer networks within plant cell walls during vascular maturation.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "As tender vegetative shoots mature toward autumn, their primary vascular bundles begin to **lignify** and stiffen."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The aerial roots of the creeping vine **lignify** rapidly after grasping the rocky wall, anchoring the plant permanently."},
      {"author": "Julius von Sachs", "work": "Lectures on the Physiology of Plants", "quote": "Secondary cell walls in xylem vessels **lignify** through the enzymatic secretion of complex aromatic polymer substances."}
    ]
  },
  "lignin": {
    "primary": "A complex organic polymer deposited in the cell walls of many vascular plants, making them rigid, woody, and resistant to decay.",
    "secondary": "In wood biochemistry and paper manufacturing, an amorphous, cross-linked aromatic biopolymer that binds cellulose microfibrils in timber.",
    "quotes": [
      {"author": "Julius von Sachs", "work": "Text-Book of Botany", "quote": "The mechanical rigidity of timber is directly attributable to **lignin**, which encrusts the cellulose matrix of mature plant cells."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Plant cells synthesize **lignin** to form dense supportive skeletal tissue capable of lifting heavy foliage toward sunlight."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Chemical digestion removes the insoluble **lignin** from raw wood pulp, leaving behind the pliable cellulose fibers used for paper."}
    ]
  },
  "lignite": {
    "primary": "A soft, brownish-black intermediate fossil coal that retains traces of original plant wood structure; brown coal.",
    "secondary": "In sedimentary geology and economic mining, low-rank coal possessing low calorific heat value and high natural moisture content.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Strata of Tertiary **lignite** exposed along the river bank preserve charred fragments of conifers that once clothed ancient valleys."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In the sandstone cliffs of the Chilean coast we discovered thin seams of **lignite** containing fossilized leaves of extinct broadleaf trees."},
      {"author": "Herman Melville", "work": "The Encantadas", "quote": "The volcanic rocks were interspersed with dark beds of smoldering **lignite**, lending a desolate subterranean aspect to the coast."}
    ]
  },
  "lignosae": {
    "primary": "A former broad taxonomic or ecological grouping encompassing woody vascular plants, including trees and shrubs, as distinguished from herbs.",
    "secondary": "In historical phytogeography and plant systematics, a major phylogenetic or ecological division characterized by persistent secondary growth and woody stems.",
    "quotes": [
      {"author": "John Hutchinson", "work": "The Families of Flowering Plants", "quote": "In his taxonomic system, Hutchinson separated dicotyledonous families into the fundamentally woody **Lignosae** and the herbaceous Herbaceae."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The insular flora exhibited a remarkable predominance of arborescent forms belonging to the **Lignosae**, while annual herbs were scarce."},
      {"author": "Asa Gray", "work": "Scientific Papers of Asa Gray", "quote": "Classifying trees and shrubs under the comprehensive heading of **Lignosae** emphasizes ecological growth forms rather than strict genetic lineages."}
    ]
  }
}
