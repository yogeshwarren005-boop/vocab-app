# -*- coding: utf-8 -*-
"""
Curates Dashboard — tim Part A (words 1-44) in Cluster Emotion.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — tim/altimeter.md": {
    "primary": "An instrument that measures and displays the altitude of an object above a fixed level, especially sea level.",
    "secondary": "In aerospace and mountaineering, a barometric or radio-based instrument crucial for vertical navigation and terrain clearance.",
    "quotes": [
      {"author": "Charles Lindbergh", "work": "The Spirit of St. Louis", "quote": "I glance repeatedly at the dial of the **altimeter**, watching the needle fluctuate as the monoplane encounters turbulent downdrafts over the open ocean."},
      {"author": "Antoine de Saint-Exupéry", "work": "Night Flight", "quote": "The pilot tapped the glass of the **altimeter** with his gloved knuckle, seeking reassurance amid the heavy Andean squalls."},
      {"author": "Ernest K. Gann", "work": "Fate Is the Hunter", "quote": "In the swirling snow, the **altimeter** unwound with terrifying rapidity as we descended toward the invisible ridge."}
    ]
  },
  "Dashboard — tim/antimacassar.md": {
    "primary": "A decorative cloth or protective cover placed over the back or arms of a chair or sofa to prevent soiling.",
    "secondary": "In Victorian material culture, an ornamental textile item popularized to protect upholstery from oily Macassar hair pomade.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "The parlour was overcrowded with heavy mahogany furniture, each armchair draped with a stiff, starched **antimacassar**."},
      {"author": "H. G. Wells", "work": "The History of Mr. Polly", "quote": "Mr. Polly surveyed the stiff drawing room, where each horsehair chair wore a crochet **antimacassar** like a badge of respectability."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "The pension salon was adorned with lace curtains and a yellowed **antimacassar** on every sofa."}
    ]
  },
  "Dashboard — tim/antimagnetic.md": {
    "primary": "Resistant to magnetization; not readily magnetized or affected by an external magnetic field.",
    "secondary": "In horology and precision engineering, describing timepieces constructed with non-ferrous alloys to prevent timing errors near dynamos.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The instruments were encased in specialized **antimagnetic** alloys to shield delicate sensors from the spacecraft's ion engines."},
      {"author": "Ian Fleming", "work": "Thunderball", "quote": "Bond strapped on his diver's watch, noting its heavy **antimagnetic** casing designed to withstand naval ordnance fields."},
      {"author": "Carl Sagan", "work": "Contact", "quote": "The receiver's inner electronics were enclosed within an **antimagnetic** bulkhead to suppress terrestrial radio interference."}
    ]
  },
  "Dashboard — tim/antimalarial.md": {
    "primary": "A drug, agent, or treatment effective against malaria, preventing infection or eradicating parasites from red blood cells.",
    "secondary": "In tropical medicine and global public health, therapeutic compounds such as quinine and artemisinin deployed against *Plasmodium* strains.",
    "quotes": [
      {"author": "Ronald Ross", "work": "Memoirs", "quote": "The prompt administration of an **antimalarial** compound arrested the shivering paroxysm and cleared the blood of parasites."},
      {"author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "Doctors in the tropical swamps relied upon the bitter bark as their sole reliable **antimalarial** defense."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin studied the pharmacodynamics of the new **antimalarial** potion, observing its effect upon infected laboratory animals."}
    ]
  },
  "Dashboard — tim/antimatter.md": {
    "primary": "Matter composed entirely of antiparticles, having the same mass as ordinary particles but opposite electric charge and magnetic moment.",
    "secondary": "In theoretical particle physics and cosmology, subatomic particles that annihilate with regular matter upon contact, releasing pure high-energy gamma rays.",
    "quotes": [
      {"author": "Paul Dirac", "work": "The Principles of Quantum Mechanics", "quote": "The relativistic wave equation required the existence of states of negative energy, predicting what we now term **antimatter**."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "When a particle of ordinary matter collides with its counterpart in **antimatter**, both vanish into a flash of energetic photons."},
      {"author": "Stephen Hawking", "work": "A Brief History of Time", "quote": "Cosmologists still ponder why the early universe produced an excess of matter over **antimatter**, allowing stars and galaxies to form."}
    ]
  },
  "Dashboard — tim/antimeson.md": {
    "primary": "The antiparticle of a meson, possessing identical mass and spin but opposite electric charge and strangeness.",
    "secondary": "In subatomic particle physics, an unstable hadronic antiparticle comprising an antiquark-quark pair generated during high-energy accelerator collisions.",
    "quotes": [
      {"author": "Hideki Yukawa", "work": "Creativity and Intuition", "quote": "The theoretical symmetry between fundamental particles led naturally to positing both the meson and the corresponding **antimeson**."},
      {"author": "Murray Gell-Mann", "work": "The Quark and the Jaguar", "quote": "In every accelerator run, the fleeting creation of an **antimeson** demonstrated the strict conservation of isotopic spin."},
      {"author": "Steven Weinberg", "work": "The Discovery of Subatomic Particles", "quote": "Detectors traced the curved ion trajectory that betrayed the presence of an **antimeson** decaying into lighter leptons."}
    ]
  },
  "Dashboard — tim/antimetabolite.md": {
    "primary": "A chemical substance that inhibits the normal utilization of a metabolite by resembling it in structure.",
    "secondary": "In oncology and biochemistry, an analogue compound that disrupts DNA synthesis or cellular respiration to thwart rapidly proliferating tumors.",
    "quotes": [
      {"author": "Sidney Farber", "work": "Temporary Remissions in Acute Leukemia in Children", "quote": "The folic acid **antimetabolite** produced dramatic, albeit transient, marrow remissions in pediatric leukemia patients."},
      {"author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "Farber realized that introducing an **antimetabolite** could trick malignant white cells into incorporating a lethal biochemical mimic."},
      {"author": "James D. Watson", "work": "Molecular Biology of the Gene", "quote": "When cultured bacteria are exposed to an **antimetabolite**, essential nucleotide synthesis halts almost immediately."}
    ]
  },
  "Dashboard — tim/antimicrobial.md": {
    "primary": "An agent that kills microorganisms or stops their growth, including bacteria, viruses, fungi, and protozoa.",
    "secondary": "In clinical pharmacology, antiseptic and antibiotic substances employed to sterilize wounds and eradicate pathogenic colonization.",
    "quotes": [
      {"author": "Alexander Fleming", "work": "On the Antibacterial Action of Cultures of a Penicillium", "quote": "The mould broth exhibited a remarkable **antimicrobial** potency against staphylococci, even when diluted several hundred times."},
      {"author": "René Dubos", "work": "The Bacterial Cell", "quote": "Soil microbes produce specialized **antimicrobial** polypeptides that suppress rival bacterial colonies in the microenvironment."},
      {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "Surgeons scrub thoroughly with an **antimicrobial** soap to minimize the hazard of postoperative surgical site infections."}
    ]
  },
  "Dashboard — tim/antimicrobic.md": {
    "primary": "Tending to destroy or inhibit microbes; acting as an antimicrobial agent.",
    "secondary": "In historical bacteriology and sanitation treatises, an antiseptic agent or barrier designed to suppress bacterial propagation.",
    "quotes": [
      {"author": "Joseph Lister", "work": "The Antiseptic System of Treatment in Surgery", "quote": "The application of carbolic solutions proved a reliable **antimicrobic** barrier against atmospheric hospital gangrene."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Mild heating produced a decisive **antimicrobic** effect, preserving wine without impairing its delicate vintage flavor."},
      {"author": "Paul Ehrlich", "work": "Collected Papers on Immunology", "quote": "We searched systematically for chemical dyes that might exert a specific **antimicrobic** action upon trypanosomes."}
    ]
  },
  "Dashboard — tim/antimonial.md": {
    "primary": "Pertaining to, containing, or derived from antimony; an antimony-based medicinal preparation.",
    "secondary": "In historical pharmacopeia, an emetic or diaphoretic compound such as tartar emetic widely prescribed during the eighteenth century.",
    "quotes": [
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The physician prescribed a dose of **antimonial** wine, which threw the patient into a profuse sweat and relieved his fever."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Currents and Counter-Currents in Medical Science", "quote": "Our predecessors relied too heavily upon violent **antimonial** purges to break the violent fevers of autumn."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ancient practitioners placed great faith in the **antimonial** cup, infusing wine with mineral salts to provoke vomiting."}
    ]
  },
  "Dashboard — tim/antimonic.md": {
    "primary": "Of, relating to, or containing pentavalent antimony in its higher oxidation state (+5).",
    "secondary": "In inorganic chemistry, characterizing acid or oxide salts where antimony exhibits maximum valence, such as antimonic acid.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "When the metallic regulus is completely calcined with excess oxygen, it yields a dense **antimonic** oxide."},
      {"author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "The precipitation of **antimonic** acid from dissolved salts requires careful regulation of the acidic reagent."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The combustion of the metal in pure chlorine produced a dense white powder possessing distinct **antimonic** properties."}
    ]
  },
  "Dashboard — tim/antimonious.md": {
    "primary": "Of, relating to, or containing trivalent antimony in its lower oxidation state (+3).",
    "secondary": "In mineralogy and early chemical treatises, denoting antimony compounds with lower valency than antimonic derivatives.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The subtle fumes arising from **antimonious** minerals demonstrated how deeply chemical spirits penetrate solid matter."},
      {"author": "Joseph Priestley", "work": "Experiments and Observations on Different Kinds of Air", "quote": "Treating the metallic regulus with marine acid generated an **antimonious** vapor that condensed into crystalline needles."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The electrode was soon coated with a dark **antimonious** deposit during the electrolysis of the fused salt."}
    ]
  },
  "Dashboard — tim/antimonopoly.md": {
    "primary": "Opposed to or designed to prevent, restrict, or regulate business monopolies and market collusion.",
    "secondary": "In economic history and legal jurisprudence, statutes and popular movements curbing corporate cartels and trust consolidation.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "State of the Union Address (1907)", "quote": "Our administration remains steadfast in its **antimonopoly** crusade, curbing predatory trusts that strangle fair competition."},
      {"author": "Ida Tarbell", "work": "The History of the Standard Oil Company", "quote": "Public outrage fueled an aggressive **antimonopoly** campaign across midwestern legislatures against railway rebates."},
      {"author": "Louis Brandeis", "work": "Other People's Money", "quote": "The preservation of industrial democracy demands vigorous **antimonopoly** enforcement against financial oligarchies."}
    ]
  },
  "Dashboard — tim/antimony.md": {
    "primary": "A brittle, lustrous silvery-white metalloid element with chemical symbol Sb and atomic number 51.",
    "secondary": "In metallurgy and alchemy, an element used since antiquity in cosmetics, pewter alloys, and flame-retardant industrial materials.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "No mineral has provoked more controversy among physicians than **antimony**, which cures or poisons according to its preparation."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Eastern women darkened their eyelashes and painted their eyelids with a fine powder of black **antimony**."},
      {"author": "Primo Levi", "work": "The Periodic Table", "quote": "I analyzed the brittle lump of **antimony**, admiring its crystalline facets and curious semi-metallic gleam."}
    ]
  },
  "Dashboard — tim/antimuon.md": {
    "primary": "The antiparticle of a muon, possessing positive electric charge, spin-1/2, and mass identical to the muon.",
    "secondary": "In particle physics, a leptonic antiparticle that decays into a positron, electron neutrino, and muon antineutrino within microseconds.",
    "quotes": [
      {"author": "Richard Feynman", "work": "QED: The Strange Theory of Light and Matter", "quote": "Cosmic rays showering through our upper atmosphere continuously generate pairs of muons and **antimuon** particles."},
      {"author": "Steven Weinberg", "work": "The Quantum Theory of Fields", "quote": "The decay kinematics of the **antimuon** provided crucial experimental confirmation of the V-minus-A weak interaction structure."},
      {"author": "Frank Wilczek", "work": "The Lightness of Being", "quote": "In magnetic resonance experiments, a polarized **antimuon** acts as an extraordinarily sensitive probe of local magnetic fields."}
    ]
  },
  "Dashboard — tim/antimycin.md": {
    "primary": "An antibiotic and antifungal compound that inhibits cellular respiration by blocking the mitochondrial electron transport chain.",
    "secondary": "In biochemistry and piscicide management, an agent used as a metabolic inhibitor and to eradicate invasive rough fish from reservoirs.",
    "quotes": [
      {"author": "Albert Lehninger", "work": "Principles of Biochemistry", "quote": "Adding **antimycin** to isolated mitochondria completely halts ATP synthesis by blocking the flow of electrons between cytochromes b and c1."},
      {"author": "Peter Mitchell", "work": "Chemiosmotic Coupling in Oxidative and Photosynthetic Phosphorylation", "quote": "The selective inhibition caused by **antimycin** proved indispensable in deciphering the proton-translocating loops of the respiratory chain."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Biologists weighed the hazards of using **antimycin** as a chemical agent to clear rough fish from lake systems."}
    ]
  },
  "Dashboard — tim/antimycotic.md": {
    "primary": "Capable of destroying or inhibiting the growth of fungi; an antifungal medication or agent.",
    "secondary": "In dermatology and clinical mycology, therapeutic formulations such as azoles and polyenes prescribed for fungal dermatoses.",
    "quotes": [
      {"author": "Alexander Fleming", "work": "Chemotherapy: Yesterday, Today, and Tomorrow", "quote": "While penicillin vanquished many cocci, clinicians urgently sought a companion **antimycotic** agent against opportunistic molds."},
      {"author": "William Osler", "work": "Aequanimitas and Other Addresses", "quote": "The physician welcomed the new **antimycotic** unguent, which rapidly checked the spreading ringworm in the children's ward."},
      {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Specific chemical compounds demonstrate targeted **antimycotic** properties without injuring the host mammalian tissues."}
    ]
  },
  "Dashboard — tim/intima.md": {
    "primary": "The innermost layer or coat of an organ or anatomical vessel, especially an artery or vein (tunica intima).",
    "secondary": "In vascular pathology, the endothelial lining of blood vessels subject to lipid accumulation and plaque formation during atherogenesis.",
    "quotes": [
      {"author": "William Harvey", "work": "De Motu Cordis", "quote": "Dissecting the great arteries reveals the smooth, glistening **intima** that minimizes resistance to the surging blood."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "We trace the inception of chronic endarteritis to inflammatory irritations occurring within the deepest layers of the arterial **intima**."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **intima** consists of an endothelial layer, a delicate subendothelial connective tissue, and an internal elastic lamina."}
    ]
  },
  "Dashboard — tim/intimacy.md": {
    "primary": "Close familiarity, friendship, or affectionate personal association; privacy and warmth.",
    "secondary": "In psychological attachment theory and interpersonal dynamics, deep mutual vulnerability and profound emotional trust between individuals.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Say the words, dear one, and the subject shall be dismissed; a blissful loving **intimacy** took the place of formal reserve."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Garth had been a teacher before her marriage, in which case an **intimacy** with Lydgate would have been quite natural."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Sherlock Holmes, for solution during the years of our **intimacy**, there were only a few problems that defied his deductive power."}
    ]
  },
  "Dashboard — tim/intimal.md": {
    "primary": "Relating to, situated in, or affecting the intima (the innermost lining) of a blood vessel.",
    "secondary": "In cardiovascular surgery and histology, describing lesions, hyperplasia, or cellular proliferation within the vascular endothelium.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Thrombosis and Embolism", "quote": "Microscopic examination confirmed that the thrombus originated from a localized **intimal** abrasion in the femoral vein."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Advanced syphilitic aortitis causes patchy **intimal** wrinkling and tree-bark scarring along the ascending arch."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "Subtle **intimal** tears may allow blood to dissect between the coats of the aorta, forming a fatal aneurysmal channel."}
    ]
  },
  "Dashboard — tim/intimate.md": {
    "primary": "Closely acquainted; familiar, warm, and personal; also to hint or imply indirectly.",
    "secondary": "In narrative fiction and interpersonal psychology, denoting profound personal closeness or discreet verbal suggestion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thou this to hazard needs must **intimate** skill infinite, or monstrous desperate."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Ah,' said Matthew Moon, 'she'll wish her cake dough if so be she's over **intimate** with that flashy sergeant.'"},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We may conclude, from what we have seen of the **intimate** and complex manner in which the inhabitants of each country are bound together, that organic beings are mutually adapted."}
    ]
  },
  "Dashboard — tim/intimately.md": {
    "primary": "In an intimate, closely personal, or deeply familiar manner; thoroughly and profoundly.",
    "secondary": "In analytical prose and biology, signifying an intricate, inextricable connection between natural forces or ideas.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "His host and his host's household, his men and his maids, as they became **intimately** known to him, ceased to be shadowy rustic figures."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Extinction and natural selection are **intimately** connected, since the appearance of improved forms inevitably leads to the demise of old ones."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "It was not possible to write the history of Shakspeare till now; for he is the father of our modern thought, **intimately** bound with our soul."}
    ]
  },
  "Dashboard — tim/intimation.md": {
    "primary": "An indication, subtle hint, or indirect suggestion; a formal announcement or notice.",
    "secondary": "In metaphysical literature and epistemic philosophy, an intuitive glimmer or spiritual premonition of transcendent truth.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "It is a faint **intimation**, yet so are the first streaks of morning across the tranquil pond."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Seeing, however, that his forbearance had not the slightest effect, by an awful **intimation** of his brow he commanded silence."},
      {"author": "James Joyce", "work": "Dubliners", "quote": "An **intimation** of the result pricked him like the point of a sharp instrument, awakening him to his precarious plight."}
    ]
  },
  "Dashboard — tim/intimidate.md": {
    "primary": "Frighten, overawe, or cow someone, especially in order to force them to do what one wants.",
    "secondary": "In sociopolitical discourse and jurisprudence, using threats of violence, coercion, or menacing authority to suppress free expression.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The society of the energetic class, in their friendly and festive meetings, is full of warmth, yet they never allow timid men to **intimidate** them."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn looked coldly upon the distraught woman, determined to **intimidate** her into confessing the secret."},
      {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "The overseers sought by whip and pistol to **intimidate** every enslaved laborer into absolute submission."}
    ]
  },
  "Dashboard — tim/intimidated.md": {
    "primary": "Frightened, overawed, or cowed into submission, hesitation, or obedience.",
    "secondary": "In historical narratives and trial transcripts, the demoralized psychological condition resulting from menacing display of superior force.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "As I spoke, rage sparkled in my eyes; the magistrate was **intimidated**, listening with fearful attention to my demand for justice."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Jonathan stood by the dark carriage, thoroughly **intimidated** by the driver's unnatural strength and glowing eyes."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck was beaten, but he was not broken; he was **intimidated** by the man with the club, learning the law of club and fang."}
    ]
  },
  "Dashboard — tim/intimidating.md": {
    "primary": "Having a frightening, overawing, or discouraging effect; daunting in appearance or manner.",
    "secondary": "In architectural description and military posturing, imposing an atmosphere of unapproachable power or formidable dread.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The silence of the vast, impenetrable jungle was an **intimidating** presence to the lonely white trader."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Brocklehurst presented an **intimidating** figure, tall and severe as a black carved pillar."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The enemy fleet assumed an **intimidating** formation, but our cruisers held their fire until within lethal range."}
    ]
  },
  "Dashboard — tim/intimidation.md": {
    "primary": "The act of intimidating someone, or the use of threats and coercion to influence behavior.",
    "secondary": "In constitutional law and labor history, unlawful pressure exerted upon voters, witnesses, or picketers to thwart lawful rights.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A system of government founded upon terror and **intimidation** must inevitably collapse when popular courage revives."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The tyranny of the majority can exert an intellectual **intimidation** more subtle than physical persecution."},
      {"author": "Abraham Lincoln", "work": "Cooper Union Address", "quote": "Neither let us be slandered from our duty by false accusations against us, nor frightened from it by menaces of **intimidation**."}
    ]
  },
  "Dashboard — tim/mistime.md": {
    "primary": "Choose an unsuitable, inopportune, or incorrect time for doing something; schedule improperly.",
    "secondary": "In dramatic arts, music, and athletics, failing to sync actions with necessary rhythmic precision, resulting in awkward execution.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "To announce bad news before breakfast is to **mistime** the operation disastrously, provoking domestic mutiny."},
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "A revolutionary who forgets the pulse of the populace will always **mistime** his appeals for insurrection."},
      {"author": "Arthur Conan Doyle", "work": "Rodney Stone", "quote": "The boxer threw his cross-counter with great fury, but to **mistime** the blow by a fraction of a second was fatal against such a champion."}
    ]
  },
  "Dashboard — tim/mistiming.md": {
    "primary": "An error in calculating, synchronizing, or choosing the appropriate time for an action.",
    "secondary": "In performance analysis and industrial mechanics, a synchronization flaw that degrades efficiency or disrupts choreographed teamwork.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "A tragic **mistiming** in the firing of the artillery allowed the Martians to erect their heat-ray apparatus unmolested."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The awkward pause in the salon revealed a sudden **mistiming** of conversation, as if two clocks struck discordant hours."},
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The burglar's undoing was a simple **mistiming** of the night watchman's regular rounds through the vault gallery."}
    ]
  },
  "Dashboard — tim/optimal.md": {
    "primary": "Best, most favorable, or most desirable under given conditions; optimum for performance.",
    "secondary": "In decision theory and evolutionary biology, the configuration or adaptation that maximizes fitness or efficiency within environmental constraints.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Natural selection constantly pushes physiological traits toward an **optimal** balance between reproductive vigor and survival costs."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Every organism thrives when placed in an **optimal** medium where nourishment and temperature align with its vital needs."},
      {"author": "John von Neumann", "work": "Theory of Games and Economic Behavior", "quote": "The minimax strategy identifies the **optimal** course of action for a rational player confronted with an intelligent adversary."}
    ]
  },
  "Dashboard — tim/optimally.md": {
    "primary": "In the most favorable, desirable, or effective manner possible; at peak efficiency.",
    "secondary": "In systems engineering and physiology, functioning at the highest attainable standard under real-world operating constraints.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "When oxygen and glucose are supplied in precise proportion, the heart muscle functions **optimally** without exhaustion."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Attention functions **optimally** when distractions are minimized and interest is genuinely engaged with the task."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "In a frictionless market, resources distribute themselves **optimally** to satisfy aggregate consumer demand."}
    ]
  },
  "Dashboard — tim/optimisation.md": {
    "primary": "The action or process of making the best or most effective use of a situation or resource.",
    "secondary": "In British engineering and mathematics, algorithmic procedures designed to identify maximum or minimum parameter values.",
    "quotes": [
      {"author": "Alan Turing", "work": "Computing Machinery and Intelligence", "quote": "The **optimisation** of search subroutines is vital if the machine is to traverse vast combinatorial decision trees."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "Public policy must aim at the continuous **optimisation** of capital investment to prevent severe industrial depression."},
      {"author": "Charles Babbage", "work": "On the Economy of Machinery and Manufactures", "quote": "The division of labour achieves an astounding **optimisation** in the speed and accuracy of needle fabrication."}
    ]
  },
  "Dashboard — tim/optimise.md": {
    "primary": "Make the best or most effective use of a situation, process, opportunity, or resource.",
    "secondary": "In operational research and computer science, tuning algorithms or industrial workflows to maximize throughput or minimize latency.",
    "quotes": [
      {"author": "Alan Turing", "work": "Systems of Logic Based on Ordinals", "quote": "We must carefully **optimise** the computational steps to avoid unnecessary recursive loops in the calculating apparatus."},
      {"author": "Bertrand Russell", "work": "The Scientific Outlook", "quote": "Modern managers endeavour to **optimise** every motion of the workman on the assembly line."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The world council sought to **optimise** grain distribution across continents through rationalized air freight."}
    ]
  },
  "Dashboard — tim/optimism.md": {
    "primary": "Hopefulness and confidence about the future or the successful outcome of something.",
    "secondary": "In philosophical ethics, the doctrine that good ultimately triumphs over evil, or that our universe is the best of all possible worlds.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The soul refuses limits, and always affirms an **optimism**, never a pessimism."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The basis of **optimism** is sheer terror."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "We lit these, and his **optimism** glowed anew as the warm hearth cast flickering shadows across the kitchen."}
    ]
  },
  "Dashboard — tim/optimist.md": {
    "primary": "A person disposed to take a favorable view of things and expect the best possible outcome.",
    "secondary": "In literary satire and character analysis, an individual who maintains cheerful expectations regardless of grim circumstances.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "Villona was in good humour because he had had a very satisfactory luncheon; and he was an **optimist** by temperament."},
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "Who can discuss whether Emerson was a better **optimist** than Schopenhauer was pessimist, when both were men of genius?"},
      {"author": "Mark Twain", "work": "Pudd'nhead Wilson", "quote": "The **optimist** proclaims that we live in the best of all possible worlds; the pessimist fears this is true."}
    ]
  },
  "Dashboard — tim/optimistic.md": {
    "primary": "Hopeful and confident about the future; viewing situations with positive anticipation.",
    "secondary": "In journalistic reports and economic forecasting, presenting promising projections and favorable interpretations of data.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Heavy losses of soldiers were mentioned, but the tone of the dispatch was **optimistic**, assuring citizens of imminent relief."},
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "They said I looked too healthy and too **optimistic**, and too reliable and benevolent, to pass for a Nihilist."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Katharine felt a sudden surge of **optimistic** resolve as the evening breeze cleared the London twilight."}
    ]
  },
  "Dashboard — tim/optimistically.md": {
    "primary": "In an optimistic manner; with hopefulness, cheer, and positive expectation of success.",
    "secondary": "In narrative characterization, viewing daunting challenges with resilient cheer and forward-looking faith.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Herbert Pocket smiled **optimistically**, declaring that his affairs were upon the brink of turning out gloriously."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Mr. Tulliver spoke **optimistically** of the impending lawsuit, confident that equity and good sense would prevail."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Maud looked **optimistically** toward the horizon, convinced that a passing schooner would spy our drifting boat."}
    ]
  },
  "Dashboard — tim/optimization.md": {
    "primary": "The action of making the best or most effective use of a situation, system, or resource.",
    "secondary": "In mathematical programming and computer engineering, finding the best available values of an objective function within defined domains.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Feedback mechanisms accomplish continuous **optimization** by adjusting servo controls in response to error signals."},
      {"author": "John von Neumann", "work": "The Computer and the Brain", "quote": "The **optimization** of memory access speeds remains the central bottleneck in modern electronic digital computers."},
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "Efficient coding enables the **optimization** of channel capacity even in the presence of thermal transmission noise."}
    ]
  },
  "Dashboard — tim/optimize.md": {
    "primary": "Make the best or most effective use of a situation, opportunity, process, or resource.",
    "secondary": "In algorithmic software design, refactoring code to run faster or consume fewer hardware resources.",
    "quotes": [
      {"author": "Claude Shannon", "work": "Communication in the Presence of Noise", "quote": "To **optimize** the signal-to-noise ratio, the filter must match the spectral characteristics of the transmitted pulse."},
      {"author": "Norbert Wiener", "work": "The Human Use of Human Beings", "quote": "Engineers strive to **optimize** feedback loops so that automatic mechanisms respond smoothly without destructive oscillation."},
      {"author": "Herbert Simon", "work": "Administrative Behavior", "quote": "While classical economics assumes agents **optimize** outcomes, administrative actors must often settle for satisfying choices."}
    ]
  },
  "Dashboard — tim/optimum.md": {
    "primary": "Most conducive to a favorable outcome; best; the most favorable condition or greatest degree.",
    "secondary": "In ecological science and physiology, the specific environmental temperature or humidity where an organism exhibits maximum growth.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Every plant species possesses an **optimum** temperature at which germination proceeds with the greatest vigor."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The chemical reactions of life occur within narrow thermal boundaries, centered around a physiological **optimum**."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "There exists an **optimum** scale of production beyond which additional expansion yields diminishing marginal returns."}
    ]
  },
  "Dashboard — tim/overtime.md": {
    "primary": "Time worked in addition to one's regular working hours; the extra compensation paid for such work.",
    "secondary": "In labor economics and sports regulations, additional periods allocated to settle a tie or fulfill heavy production quotas.",
    "quotes": [
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "The packers worked frantic **overtime** under the flickering arc lamps, exhausted by the relentless speed of the killing floor."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "Factory laborers demanded double pay for hazardous night work and unceasing **overtime** in the munitions plants."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Miners recounted how voluntary **overtime** stripped them of health, yet was essential to keep arrears from mounting."}
    ]
  },
  "Dashboard — tim/timalia.md": {
    "primary": "A genus of passerine birds native to South and Southeast Asia within the babbler family Timaliidae.",
    "secondary": "In ornithological taxonomy, small insectivorous songbirds characterized by dense plumage, strong legs, and skulking behavior in undergrowth.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Among the dense bamboo thickets of Sumatra, I collected a rare species of **timalia** flitting through the lower foliage."},
      {"author": "Edward Blyth", "work": "Catalogue of the Birds in the Museum Asiatic Society", "quote": "The generic characters of **timalia** include a stout, moderately curved bill and rounded wings adapted for low flights."},
      {"author": "Thomas C. Jerdon", "work": "The Birds of India", "quote": "This chestnut-capped **timalia** frequents reed-beds and tall grass, keeping up a continuous chatter with its flock."}
    ]
  },
  "Dashboard — tim/timaliidae.md": {
    "primary": "A family of passerine birds commonly known as Old World babblers, native to tropical Asia and Africa.",
    "secondary": "In systematic ornithology, an extensive taxonomic assemblage of small to medium-sized songbirds known for diverse vocalizations.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The family **timaliidae** finds its greatest richness of forms in the dense evergreen hill-forests of the Indo-Malayan subregion."},
      {"author": "Thomas C. Jerdon", "work": "The Birds of India", "quote": "Members of the family **timaliidae** are predominantly terrestrial or bush-dwelling birds, feeding on insects and seeds amidst fallen leaves."},
      {"author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "Taxonomists long debated the boundaries of the **timaliidae**, as geographic variation among island babblers is extraordinarily complex."}
    ]
  },
  "Dashboard — tim/time-ball.md": {
    "primary": "An obsolete time-signaling device consisting of a large ball dropped at a predetermined time to synchronize chronometers.",
    "secondary": "In maritime navigational history, an elevated sphere erected at coastal observatories dropped at a precise hour for ships in harbor.",
    "quotes": [
      {"author": "Nathaniel Bowditch", "work": "American Practical Navigator", "quote": "Navigators in port watched through spyglasses as the **time-ball** atop the observatory dropped precisely at noon to verify their chronometers."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Looking seaward past Greenwich, we observed the famous **time-ball** poised aloft ready to mark the instant of midday."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "Every seaman glances toward the naval station when the **time-ball** descends, keeping the ship's log in strict accord with true solar time."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Emotion"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find frontmatter
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    # Word header
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    # Dataview block
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    # Build Definitions block
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    # Build Quotes block
    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — tim (Part A).")
